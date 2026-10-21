<?php
/**
 * Plugin Name: FPJ SEO Sync
 * Description: Copies Free Press Journal SEO data and "Read Also" boxes onto the matching AY blog posts, from the fpj_to_ay.json file built by build_fpj_to_ay.py. Previews every change, saves the old values first, and can restore them.
 * Version: 1.0.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Author: Site Admin
 * License: GPL-2.0-or-later
 */

if (!defined('ABSPATH')) exit;

class FPJ_SEO_Sync {
    const VERSION = '1.0.0';
    const OPTION_DATA = 'fpjss_data';           // the uploaded records, keyed by AY slug
    const META_BACKUP = '_fpjss_backup';        // the post's values before the first apply
    const META_APPLIED = '_fpjss_applied';      // when and with which settings it was applied
    const MAX_JSON_BYTES = 5242880;             // 5 MB

    public function __construct() {
        add_action('admin_menu', [$this, 'menu']);
        add_action('admin_post_fpjss_upload', [$this, 'handle_upload']);
        add_action('admin_post_fpjss_apply', [$this, 'handle_apply']);
        add_action('admin_post_fpjss_restore', [$this, 'handle_restore']);
        add_action('admin_notices', [$this, 'notice']);
        add_action('wp_enqueue_scripts', [$this, 'box_style']);
    }

    public function menu() {
        add_management_page('FPJ SEO Sync', 'FPJ SEO Sync', 'edit_others_posts', 'fpj-seo-sync', [$this, 'render_page']);
    }

    /* ---------- page ---------- */

    public function render_page() {
        if (!current_user_can('edit_others_posts')) return;
        $data = get_option(self::OPTION_DATA, []);
        $seo = $this->active_seo_plugins();
        ?>
        <div class="wrap">
          <h1>FPJ SEO Sync</h1>
          <p>Copies the Free Press Journal SEO data and "Read Also" boxes onto the matching AY posts. Upload <code>fpj_to_ay.json</code>, check the preview, choose what to apply, then apply to the posts you tick. The old values are saved first, so each post can be restored.</p>
          <?php if (!$seo): ?>
            <div class="notice notice-warning inline"><p>No supported SEO plugin (Yoast SEO, SureRank or Rank Math) is active, so the SEO title, description and canonical cannot be written. The subheading, image alt text, tags and "Read Also" boxes still can.</p></div>
          <?php elseif (count($seo) > 1): ?>
            <div class="notice notice-error inline"><p><strong><?php echo esc_html(implode(' and ', $seo)); ?> are both active.</strong> Each adds its own canonical and social tags to every page, and they can contradict each other. This plugin writes to both, but deactivating one is strongly recommended.</p></div>
          <?php else: ?>
            <div class="notice notice-info inline"><p>SEO fields will be written to <?php echo esc_html(implode('', $seo)); ?>.</p></div>
          <?php endif; ?>

          <h2>1. Upload fpj_to_ay.json</h2>
          <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>" enctype="multipart/form-data">
            <?php wp_nonce_field('fpjss_upload'); ?>
            <input type="hidden" name="action" value="fpjss_upload">
            <input type="file" name="fpjss_file" accept=".json,application/json" required>
            <?php submit_button($data ? 'Replace the uploaded file' : 'Upload', 'secondary', 'submit', false); ?>
            <?php if ($data): ?><span class="description">&nbsp;Loaded: <?php echo count($data); ?> posts.</span><?php endif; ?>
          </form>

          <?php if ($data) $this->render_preview($data); ?>
        </div>
        <?php
    }

    private function render_preview($data) {
        ?>
        <h2>2. Choose what to apply</h2>
        <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
          <?php wp_nonce_field('fpjss_apply'); ?>
          <input type="hidden" name="action" value="fpjss_apply">
          <table class="form-table">
            <tr><th scope="row">Canonical URL</th><td>
              <label><input type="radio" name="canonical" value="ay" checked> The AY post itself (recommended: lets the AY post rank)</label><br>
              <label><input type="radio" name="canonical" value="fpj"> The FPJ article (Google will credit FPJ; the AY post will not rank)</label><br>
              <label><input type="radio" name="canonical" value="keep"> Leave unchanged</label>
            </td></tr>
            <tr><th scope="row">Copy from FPJ</th><td>
              <label><input type="checkbox" name="parts[]" value="seo" checked> SEO title and meta description</label><br>
              <label><input type="checkbox" name="parts[]" value="social" checked> Facebook and Twitter title and description (Yoast SEO only)</label><br>
              <label><input type="checkbox" name="parts[]" value="subheading" checked> H2 subheading at the top of the post</label><br>
              <label><input type="checkbox" name="parts[]" value="alt" checked> Featured image alt text</label><br>
              <label><input type="checkbox" name="parts[]" value="tags"> Keywords, added as post tags</label><br>
              <label><input type="checkbox" name="parts[]" value="also_read" checked> "Read Also" boxes</label>
            </td></tr>
          </table>

          <h2>3. Preview and apply</h2>
          <p>Posts are found by slug. Posts already applied are skipped; restore one first to apply it again.</p>
          <table class="widefat striped">
            <thead><tr><th style="width:2em"><input type="checkbox" onclick="document.querySelectorAll('.fpjss-pick').forEach(c=>{if(!c.disabled)c.checked=this.checked})"></th>
              <th>AY post</th><th>SEO title: now → FPJ</th><th>Meta description: now → FPJ</th><th>Read Also</th><th>State</th></tr></thead>
            <tbody>
            <?php foreach ($data as $slug => $r):
                $post = $this->find_post($slug);
                $applied = $post ? get_post_meta($post->ID, self::META_APPLIED, true) : '';
                $now = $post ? $this->current_seo($post->ID) : ['title' => '', 'description' => ''];
                $boxes = count($r['also_read'] ?? []);
                $skipped = count($r['skipped_also_read'] ?? []);
                ?>
              <tr>
                <td><input type="checkbox" class="fpjss-pick" name="slugs[]" value="<?php echo esc_attr($slug); ?>" <?php disabled(!$post || $applied); ?>></td>
                <td><?php if ($post): ?><a href="<?php echo esc_url(get_edit_post_link($post->ID)); ?>"><?php echo esc_html(get_the_title($post)); ?></a><br><small><?php echo esc_html($post->post_status); ?></small><?php else: ?><?php echo esc_html($r['ay_title']); ?><br><small style="color:#b32d2e">No post with slug <code><?php echo esc_html($slug); ?></code></small><?php endif; ?></td>
                <td><small><?php echo esc_html($now['title'] ?: '(default)'); ?></small><br>→ <?php echo esc_html($r['seo']['seo_title'] ?? ''); ?></td>
                <td><small><?php echo esc_html($now['description'] ?: '(default)'); ?></small><br>→ <?php echo esc_html($r['seo']['meta_description'] ?? ''); ?></td>
                <td><?php echo (int) $boxes; ?><?php if ($skipped): ?><br><small><?php echo (int) $skipped; ?> left out (no AY copy)</small><?php endif; ?></td>
                <td><?php if ($applied): ?>Applied <?php echo esc_html($applied['time'] ?? ''); ?>
                      <br><a href="<?php echo esc_url(wp_nonce_url(admin_url('admin-post.php?action=fpjss_restore&post=' . $post->ID), 'fpjss_restore_' . $post->ID)); ?>" onclick="return confirm('Restore this post to its values before FPJ SEO Sync?')">Restore</a>
                    <?php elseif ($post): ?>Ready<?php else: ?>—<?php endif; ?></td>
              </tr>
            <?php endforeach; ?>
            </tbody>
          </table>
          <?php submit_button('Apply to the ticked posts'); ?>
        </form>
        <?php
    }

    public function notice() {
        if (empty($_GET['page']) || $_GET['page'] !== 'fpj-seo-sync' || empty($_GET['fpjss_msg'])) return;
        $type = (($_GET['fpjss_type'] ?? '') === 'error') ? 'error' : 'success';
        $lines = explode("\n", sanitize_textarea_field(wp_unslash($_GET['fpjss_msg'])));
        echo '<div class="notice notice-' . esc_attr($type) . ' is-dismissible"><p>' . implode('<br>', array_map('esc_html', $lines)) . '</p></div>';
    }

    private function redirect($type, $message) {
        wp_safe_redirect(add_query_arg(['page' => 'fpj-seo-sync', 'fpjss_type' => $type, 'fpjss_msg' => rawurlencode($message)], admin_url('tools.php')));
        exit;
    }

    /* ---------- actions ---------- */

    public function handle_upload() {
        if (!current_user_can('edit_others_posts')) wp_die('You do not have permission to do this.');
        check_admin_referer('fpjss_upload');
        $file = $_FILES['fpjss_file'] ?? null;
        if (!$file || empty($file['tmp_name']) || !is_uploaded_file($file['tmp_name'])) $this->redirect('error', 'Please choose fpj_to_ay.json.');
        if ((int) $file['size'] > self::MAX_JSON_BYTES) $this->redirect('error', 'The file exceeds 5 MB.');
        $records = json_decode(file_get_contents($file['tmp_name']), true);
        if (!is_array($records) || !$records) $this->redirect('error', 'The file is not valid JSON, or holds no records.');
        $data = [];
        foreach ($records as $r) {
            if (!is_array($r) || empty($r['ay_slug']) || !isset($r['seo']) || !is_array($r['seo'])) $this->redirect('error', 'This does not look like fpj_to_ay.json: each record needs ay_slug and seo.');
            $data[sanitize_title($r['ay_slug'])] = $r;
        }
        update_option(self::OPTION_DATA, $data, false);
        $this->redirect('success', 'Loaded ' . count($data) . ' posts. Check the preview below.');
    }

    public function handle_apply() {
        if (!current_user_can('edit_others_posts')) wp_die('You do not have permission to do this.');
        check_admin_referer('fpjss_apply');
        $data = get_option(self::OPTION_DATA, []);
        $slugs = array_map('sanitize_title', (array) ($_POST['slugs'] ?? []));
        $parts = array_intersect((array) ($_POST['parts'] ?? []), ['seo', 'social', 'subheading', 'alt', 'tags', 'also_read']);
        $canonical = in_array($_POST['canonical'] ?? '', ['ay', 'fpj', 'keep'], true) ? $_POST['canonical'] : 'ay';
        if (!$slugs) $this->redirect('error', 'Tick at least one post.');

        $report = [];
        foreach ($slugs as $slug) {
            $post = isset($data[$slug]) ? $this->find_post($slug) : null;
            if (!$post) { $report[] = "$slug: not found, skipped."; continue; }
            if (get_post_meta($post->ID, self::META_APPLIED, true)) { $report[] = "$slug: already applied, skipped."; continue; }
            $report[] = "$slug: " . $this->apply($post, $data[$slug], $parts, $canonical);
        }
        $this->redirect('success', implode("\n", $report));
    }

    public function handle_restore() {
        $id = (int) ($_GET['post'] ?? 0);
        if (!current_user_can('edit_post', $id)) wp_die('You do not have permission to do this.');
        check_admin_referer('fpjss_restore_' . $id);
        $b = get_post_meta($id, self::META_BACKUP, true);
        if (!is_array($b)) $this->redirect('error', 'No saved values for this post.');

        wp_update_post(['ID' => $id, 'post_content' => wp_slash($b['content'])]);
        foreach ($b['meta'] as $key => $value) {
            if ($value === null) delete_post_meta($id, $key); else update_post_meta($id, $key, $value);
        }
        if (!empty($b['thumb_id'])) {
            if ($b['thumb_alt'] === null) delete_post_meta($b['thumb_id'], '_wp_attachment_image_alt');
            else update_post_meta($b['thumb_id'], '_wp_attachment_image_alt', $b['thumb_alt']);
        }
        wp_set_post_tags($id, $b['tags'], false);
        delete_post_meta($id, self::META_BACKUP);
        delete_post_meta($id, self::META_APPLIED);
        $this->redirect('success', get_the_title($id) . ': restored.');
    }

    /* ---------- applying one post ---------- */

    private function apply($post, $r, $parts, $canonical) {
        $id = $post->ID;
        $seo = $r['seo'];
        $thumb = (int) get_post_thumbnail_id($id);
        $done = [];

        // save everything this could change, before changing it
        $meta = [];
        foreach ($this->meta_keys() as $key) $meta[$key] = metadata_exists('post', $id, $key) ? get_post_meta($id, $key, true) : null;
        update_post_meta($id, self::META_BACKUP, [
            'content' => $post->post_content,
            'meta' => $meta,
            'thumb_id' => $thumb,
            'thumb_alt' => $thumb && metadata_exists('post', $thumb, '_wp_attachment_image_alt') ? get_post_meta($thumb, '_wp_attachment_image_alt', true) : null,
            'tags' => wp_get_post_tags($id, ['fields' => 'names']),
        ]);

        $fields = [];
        if (in_array('seo', $parts, true)) { $fields['title'] = $seo['seo_title'] ?? ''; $fields['description'] = $seo['meta_description'] ?? ''; }
        if ($canonical !== 'keep') $fields['canonical'] = $r['canonical_options'][$canonical] ?? '';
        if (in_array('social', $parts, true)) {
            $fields['og_title'] = $seo['og_title'] ?? ''; $fields['og_description'] = $seo['og_description'] ?? '';
            $fields['twitter_title'] = $seo['twitter_title'] ?? ''; $fields['twitter_description'] = $seo['twitter_description'] ?? '';
        }
        if ($fields && $this->active_seo_plugins()) { $this->save_seo($id, $fields); $done[] = 'SEO fields'; }

        if (in_array('alt', $parts, true) && $thumb && !empty($seo['featured_image_alt'])) {
            update_post_meta($thumb, '_wp_attachment_image_alt', sanitize_text_field($seo['featured_image_alt']));
            $done[] = 'alt text';
        }
        if (in_array('tags', $parts, true) && !empty($seo['keywords'])) {
            $tags = array_values(array_unique(array_filter(array_map('trim', explode(',', $seo['keywords'])))));
            wp_set_post_tags($id, $tags, true);
            $done[] = count($tags) . ' tags';
        }

        $content = $post->post_content;
        $notes = [];
        if (in_array('also_read', $parts, true) && !empty($r['also_read'])) {
            [$content, $placed, $missed] = $this->insert_boxes($content, $r['also_read']);
            $done[] = "$placed Read Also boxes";
            if ($missed) $notes[] = count($missed) . ' box(es) not placed: ' . implode('; ', $missed);
        }
        if (in_array('subheading', $parts, true) && !empty($seo['subheading'])) {
            $content = "<!-- wp:heading {\"className\":\"fpjss-subheading\"} -->\n<h2 class=\"wp-block-heading fpjss-subheading\">"
                . esc_html($seo['subheading']) . "</h2>\n<!-- /wp:heading -->\n\n" . $content;
            $done[] = 'subheading';
        }
        if ($content !== $post->post_content) wp_update_post(['ID' => $id, 'post_content' => wp_slash($content)]); // makes a revision

        update_post_meta($id, self::META_APPLIED, ['time' => current_time('Y-m-d H:i'), 'parts' => array_values($parts), 'canonical' => $canonical]);
        return ($done ? implode(', ', $done) : 'nothing to change') . '.' . ($notes ? ' ' . implode(' ', $notes) : '');
    }

    /**
     * Inserts each box after the paragraph whose text ends with the box's ay_paragraph_end (or, at 0, before the
     * first paragraph). Returns [content, number placed, list of boxes not placed].
     */
    private function insert_boxes($content, $boxes) {
        preg_match_all('#(?:<!-- wp:paragraph[^>]*-->\s*)?<p[\s>].*?</p>(?:\s*<!-- /wp:paragraph -->)?#s', $content, $m, PREG_OFFSET_CAPTURE);
        $paras = [];
        foreach ($m[0] as [$html, $offset]) {
            $text = $this->norm(wp_strip_all_tags($html));
            if ($text !== '') $paras[] = ['text' => $text, 'start' => $offset, 'end' => $offset + strlen($html)];
        }
        $inserts = []; $missed = []; $from = 0;
        foreach ($boxes as $box) {
            $after = (int) $box['after_ay_paragraph'];
            if ($after === 0 && $paras) { $inserts[] = [$paras[0]['start'], $box]; continue; }
            $want = $this->norm($box['ay_paragraph_end'] ?? '');
            $at = null;
            for ($i = $from; $i < count($paras) && $want !== ''; $i++) {
                if (substr($paras[$i]['text'], -strlen($want)) === $want || strpos($paras[$i]['text'], $want) !== false) { $at = $i; break; }
            }
            if ($at === null) { $missed[] = $box['target_title']; continue; }
            $inserts[] = [$paras[$at]['end'], $box];
            $from = $at;
        }
        usort($inserts, function($a, $b) { return $b[0] <=> $a[0]; }); // from the end, so offsets stay valid
        foreach ($inserts as [$offset, $box]) $content = substr($content, 0, $offset) . "\n\n" . $this->box_html($box) . "\n\n" . substr($content, $offset);
        return [$content, count($inserts), $missed];
    }

    /** A "Read Also" box, linking to the target post on this site when it exists, else to its AY address. */
    private function box_html($box) {
        $target = $this->find_post($box['target_slug'] ?? '');
        $url = $target ? get_permalink($target) : ($box['target_link'] ?? '');
        $title = $target ? get_the_title($target) : ($box['target_title'] ?? '');
        $img = $target ? get_the_post_thumbnail_url($target, 'thumbnail') : ($box['target_featured_image'] ?? '');
        $html = '<div class="fpjss-also-read"><span class="fpjss-label">' . esc_html($box['label'] ?? 'Read Also') . '</span>'
            . '<a href="' . esc_url($url) . '">' . ($img ? '<img src="' . esc_url($img) . '" alt="" loading="lazy" width="96" height="64">' : '')
            . '<span class="fpjss-title">' . esc_html($title) . '</span></a></div>';
        return "<!-- wp:html -->\n$html\n<!-- /wp:html -->";
    }

    public function box_style() {
        if (!is_singular('post')) return;
        wp_register_style('fpjss', false, [], self::VERSION);
        wp_enqueue_style('fpjss');
        wp_add_inline_style('fpjss', '.fpjss-also-read{border-left:4px solid #c0392b;background:#faf6f2;padding:12px 16px;margin:1.5em 0}'
            . '.fpjss-also-read .fpjss-label{display:block;font-size:.8em;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#c0392b;margin-bottom:6px}'
            . '.fpjss-also-read a{display:flex;gap:12px;align-items:center;text-decoration:none;font-weight:600}'
            . '.fpjss-also-read img{width:96px;height:64px;object-fit:cover;border-radius:4px;flex:none}');
    }

    /* ---------- helpers ---------- */

    /** The same text normalisation as build_fpj_to_ay.py's norm(). */
    private function norm($text) {
        $text = html_entity_decode($text, ENT_QUOTES | ENT_HTML5, 'UTF-8');
        $text = str_replace(["\u{2019}", "\u{2018}", "\u{201C}", "\u{201D}"], ["'", "'", '"', '"'], $text);
        $text = preg_replace('/[*_#>]/u', '', $text);
        $text = preg_replace('/[\x{2013}\x{2014}-]/u', '-', $text);
        return strtolower(trim(preg_replace('/\s+/u', ' ', $text)));
    }

    private function find_post($slug) {
        if ($slug === '') return null;
        $posts = get_posts(['name' => $slug, 'post_type' => 'post', 'post_status' => ['publish', 'pending', 'draft', 'future', 'private'], 'numberposts' => 1]);
        return $posts ? $posts[0] : null;
    }

    private function active_seo_plugins() {
        $found = [];
        if (defined('WPSEO_VERSION')) $found['yoast'] = 'Yoast SEO';
        if (defined('SURERANK_VERSION')) $found['surerank'] = 'SureRank';
        if (defined('RANK_MATH_VERSION')) $found['rankmath'] = 'Rank Math';
        return $found;
    }

    /** Every post meta key this plugin may change, so the backup can put each back. */
    private function meta_keys() {
        return ['_yoast_wpseo_title', '_yoast_wpseo_metadesc', '_yoast_wpseo_canonical',
                '_yoast_wpseo_opengraph-title', '_yoast_wpseo_opengraph-description',
                '_yoast_wpseo_twitter-title', '_yoast_wpseo_twitter-description',
                'surerank_settings_general', 'rank_math_title', 'rank_math_description', 'rank_math_canonical_url'];
    }

    private function current_seo($id) {
        $active = $this->active_seo_plugins();
        if (isset($active['yoast'])) return ['title' => get_post_meta($id, '_yoast_wpseo_title', true), 'description' => get_post_meta($id, '_yoast_wpseo_metadesc', true)];
        if (isset($active['surerank'])) { $g = get_post_meta($id, 'surerank_settings_general', true); return ['title' => $g['page_title'] ?? '', 'description' => $g['page_description'] ?? '']; }
        if (isset($active['rankmath'])) return ['title' => get_post_meta($id, 'rank_math_title', true), 'description' => get_post_meta($id, 'rank_math_description', true)];
        return ['title' => '', 'description' => ''];
    }

    /** Writes the given fields (title, description, canonical, og_*, twitter_*) to each active SEO plugin. */
    private function save_seo($id, $f) {
        $active = $this->active_seo_plugins();
        $set = function($key, $value) use ($id) { if ($value !== '') update_post_meta($id, $key, $value); else delete_post_meta($id, $key); };
        $text = function($k) use ($f) { return array_key_exists($k, $f) ? sanitize_text_field($f[$k]) : null; };
        $url = array_key_exists('canonical', $f) ? esc_url_raw($f['canonical']) : null;

        if (isset($active['yoast'])) {
            foreach (['title' => '_yoast_wpseo_title', 'description' => '_yoast_wpseo_metadesc',
                      'og_title' => '_yoast_wpseo_opengraph-title', 'og_description' => '_yoast_wpseo_opengraph-description',
                      'twitter_title' => '_yoast_wpseo_twitter-title', 'twitter_description' => '_yoast_wpseo_twitter-description'] as $k => $key) {
                if ($text($k) !== null) $set($key, $text($k));
            }
            if ($url !== null) $set('_yoast_wpseo_canonical', $url);
        }
        if (isset($active['surerank'])) { // title, description and canonical share one array
            $general = get_post_meta($id, 'surerank_settings_general', true);
            if (!is_array($general)) $general = [];
            foreach (['page_title' => $text('title'), 'page_description' => $text('description'), 'canonical_url' => $url] as $key => $value) {
                if ($value === null) continue;
                if ($value !== '') $general[$key] = $value; else unset($general[$key]);
            }
            update_post_meta($id, 'surerank_settings_general', $general);
        }
        if (isset($active['rankmath'])) {
            if ($text('title') !== null) $set('rank_math_title', $text('title'));
            if ($text('description') !== null) $set('rank_math_description', $text('description'));
            if ($url !== null) $set('rank_math_canonical_url', $url);
        }
    }
}

new FPJ_SEO_Sync();
