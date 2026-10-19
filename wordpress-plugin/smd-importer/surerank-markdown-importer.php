<?php
/**
 * Plugin Name: SureRank Markdown Blog Importer
 * Description: Import Markdown blog posts with front matter, formatting, taxonomy and SEO metadata. Creates drafts by default.
 * Version: 1.0.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Author: Site Admin
 * License: GPL-2.0-or-later
 */

if (!defined('ABSPATH')) exit;

class SMD_SureRank_Markdown_Importer {
    const VERSION = '1.0.0';
    const META_SEO_TITLE = 'smd_seo_title';
    const META_SEO_DESCRIPTION = 'smd_seo_description';
    const META_CANONICAL = 'smd_canonical_url';
    const META_ROBOTS = 'smd_robots';

    public function __construct() {
        add_action('admin_menu', [$this, 'menu']);
        add_action('admin_post_smd_import_markdown', [$this, 'handle_upload']);
        add_action('admin_notices', [$this, 'notice']);
        add_action('init', [$this, 'register_meta']);
    }

    public function menu() {
        add_management_page('Markdown Blog Importer', 'Markdown Blog Importer', 'edit_posts', 'smd-markdown-importer', [$this, 'render_page']);
    }

    public function register_meta() {
        $keys = [self::META_SEO_TITLE, self::META_SEO_DESCRIPTION, self::META_CANONICAL, self::META_ROBOTS];
        foreach ($keys as $key) {
            register_post_meta('post', $key, [
                'type' => 'string', 'single' => true, 'show_in_rest' => false,
                'auth_callback' => function() { return current_user_can('edit_posts'); },
                'sanitize_callback' => 'sanitize_text_field'
            ]);
        }
    }

    public function render_page() {
        if (!current_user_can('edit_posts')) return;
        $sure = defined('SURERANK_VERSION') || class_exists('SureRank') || function_exists('surerank_init');
        ?>
        <div class="wrap">
          <h1>Markdown Blog Importer</h1>
          <p>Upload one Markdown <code>.md</code> file. Posts are created as <strong>drafts</strong>; existing posts with the same slug are not overwritten.</p>
          <?php if (!$sure): ?><div class="notice notice-warning"><p>SureRank was not detected automatically. The importer will still create posts, but verify your SureRank integration before publishing.</p></div><?php else: ?><div class="notice notice-info"><p>SureRank appears to be active. This importer stores SEO title and description in its own custom fields; follow the one-time SureRank template setup in the included README to use them for search metadata.</p></div><?php endif; ?>
          <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>" enctype="multipart/form-data">
            <?php wp_nonce_field('smd_import_markdown'); ?>
            <input type="hidden" name="action" value="smd_import_markdown">
            <table class="form-table"><tr><th scope="row"><label for="smd_markdown_file">Markdown file</label></th><td><input type="file" id="smd_markdown_file" name="smd_markdown_file" accept=".md,.markdown,text/markdown,text/plain" required><p class="description">Maximum size: 2 MB. Use the provided template format.</p></td></tr>
            <tr><th scope="row">Import behavior</th><td><label><input type="checkbox" name="smd_allow_update" value="1"> Update an existing draft with the same slug (never updates published posts)</label></td></tr></table>
            <?php submit_button('Import as Draft'); ?>
          </form>
          <hr><h2>SEO custom fields</h2>
          <p>The importer stores SEO title and description in <code>smd_seo_title</code> and <code>smd_seo_description</code>. It also stores canonical and robots values for reference. SureRank's native per-post canonical/robots/schema fields are not written directly by this version, because their internal storage format is not a documented stable API.</p>
          <p><a href="<?php echo esc_url(plugins_url('README.txt', __FILE__)); ?>" target="_blank" rel="noopener">Read setup instructions and download the Markdown template</a></p>
        </div>
        <?php
    }

    public function handle_upload() {
        if (!current_user_can('edit_posts')) wp_die('You do not have permission to import posts.');
        check_admin_referer('smd_import_markdown');
        if (empty($_FILES['smd_markdown_file']['tmp_name']) || !is_uploaded_file($_FILES['smd_markdown_file']['tmp_name'])) $this->redirect('error', 'Please select a Markdown file.');
        if (!empty($_FILES['smd_markdown_file']['size']) && (int) $_FILES['smd_markdown_file']['size'] > 2 * 1024 * 1024) $this->redirect('error', 'File exceeds the 2 MB limit.');
        $filename = sanitize_file_name($_FILES['smd_markdown_file']['name']);
        if (!preg_match('/\.(md|markdown)$/i', $filename)) $this->redirect('error', 'Only .md or .markdown files are accepted.');
        $raw = file_get_contents($_FILES['smd_markdown_file']['tmp_name']);
        if ($raw === false || trim($raw) === '') $this->redirect('error', 'The uploaded file is empty or could not be read.');
        $doc = $this->parse_document($raw);
        if (is_wp_error($doc)) $this->redirect('error', $doc->get_error_message());
        $m = $doc['meta']; $body = trim($doc['body']);
        $title = isset($m['title']) ? sanitize_text_field($m['title']) : '';
        if ($title === '') $this->redirect('error', 'The front matter must include a title.');
        $slug = !empty($m['slug']) ? sanitize_title($m['slug']) : sanitize_title($title);
        $existing = get_page_by_path($slug, OBJECT, 'post');
        $allow_update = !empty($_POST['smd_allow_update']);
        if ($existing && !($allow_update && $existing->post_status === 'draft')) $this->redirect('error', 'A post with this slug already exists. Choose a different slug or enable update for an existing draft.');
        $content = $this->markdown_to_html($body);
        $status = 'draft'; // Safety default: never publish directly from an uploaded file.
        $postarr = [
            'post_type' => 'post', 'post_status' => $status, 'post_title' => $title,
            'post_name' => $slug, 'post_content' => $content,
            'post_excerpt' => isset($m['excerpt']) ? sanitize_textarea_field($m['excerpt']) : '',
            'post_author' => get_current_user_id(),
        ];
        if ($existing && $allow_update && $existing->post_status === 'draft') {
            $postarr['ID'] = $existing->ID;
            $post_id = wp_update_post(wp_slash($postarr), true);
        } else {
            $post_id = wp_insert_post(wp_slash($postarr), true);
        }
        if (is_wp_error($post_id)) $this->redirect('error', 'WordPress could not create the post: ' . $post_id->get_error_message());

        $cats = $this->csv_values($m['categories'] ?? '');
        $tags = $this->csv_values($m['tags'] ?? '');
        if ($cats) {
            $cat_ids = [];
            foreach ($cats as $cat) { $term = term_exists($cat, 'category'); if (!$term) $term = wp_insert_term($cat, 'category'); if (!is_wp_error($term)) $cat_ids[] = (int)(is_array($term) ? $term['term_id'] : $term); }
            if ($cat_ids) wp_set_post_categories($post_id, $cat_ids, false);
        }
        if ($tags) wp_set_post_tags($post_id, $tags, false);

        update_post_meta($post_id, self::META_SEO_TITLE, sanitize_text_field($m['seo_title'] ?? ''));
        update_post_meta($post_id, self::META_SEO_DESCRIPTION, sanitize_textarea_field($m['meta_description'] ?? ''));
        update_post_meta($post_id, self::META_CANONICAL, esc_url_raw($m['canonical_url'] ?? ''));
        $robots = sanitize_text_field($m['robots'] ?? 'index,follow');
        if (!in_array($robots, ['index,follow','noindex,follow','index,nofollow','noindex,nofollow'], true)) $robots = 'index,follow';
        update_post_meta($post_id, self::META_ROBOTS, $robots);
        if (!empty($m['featured_image_id']) && current_user_can('upload_files')) {
            $image_id = absint($m['featured_image_id']);
            if ($image_id && get_post_type($image_id) === 'attachment') set_post_thumbnail($post_id, $image_id);
        }
        $this->redirect('success', 'Draft created: ' . get_the_title($post_id), $post_id);
    }

    private function parse_document($raw) {
        $raw = preg_replace('/^\xEF\xBB\xBF/', '', $raw);
        if (!preg_match('/\A---\s*\R(.*?)\R---\s*(?:\R|$)(.*)\z/s', $raw, $matches)) return new WP_Error('smd_front_matter', 'The file must begin with YAML-style front matter between --- lines.');
        $meta = []; $current = '';
        foreach (preg_split('/\R/', $matches[1]) as $line) {
            if (trim($line) === '' || preg_match('/^\s*#/', $line)) continue;
            if (preg_match('/^([a-zA-Z0-9_-]+):\s*(.*?)\s*$/', $line, $kv)) {
                $key = strtolower($kv[1]); $value = trim($kv[2]); $current = $key;
                if ($value === '') $meta[$key] = '';
                else $meta[$key] = $this->unquote($value);
            } elseif (preg_match('/^\s+-\s+(.*?)\s*$/', $line, $item) && $current && in_array($current, ['categories','tags'], true)) {
                if (!is_array($meta[$current] ?? null)) $meta[$current] = [];
                $meta[$current][] = $this->unquote(trim($item[1]));
            }
        }
        foreach (['categories','tags'] as $key) if (isset($meta[$key]) && !is_array($meta[$key])) $meta[$key] = $this->csv_values($meta[$key]);
        return ['meta' => $meta, 'body' => $matches[2]];
    }

    private function unquote($v) {
        if (strlen($v) >= 2 && (($v[0] === '"' && substr($v, -1) === '"') || ($v[0] === "'" && substr($v, -1) === "'"))) $v = substr($v, 1, -1);
        return trim(str_replace(['\\"', "\\'"], ['"', "'"], $v));
    }

    private function csv_values($value) {
        if (is_array($value)) $items = $value; else $items = explode(',', (string)$value);
        $out = []; foreach ($items as $item) { $item = sanitize_text_field(trim($item)); if ($item !== '') $out[] = $item; }
        return array_values(array_unique($out));
    }

    private function markdown_to_html($markdown) {
        $markdown = str_replace(["\r\n", "\r"], "\n", $markdown);
        $lines = explode("\n", $markdown); $out = []; $paragraph = []; $list = null; $quote = [];
        $flush_p = function() use (&$paragraph, &$out) { if ($paragraph) { $out[] = '<p>' . $this->inline_format(implode(' ', array_map('trim', $paragraph))) . '</p>'; $paragraph = []; } };
        $flush_list = function() use (&$list, &$out) { if ($list !== null) { $out[] = '</' . $list . '>'; $list = null; } };
        $flush_quote = function() use (&$quote, &$out) { if ($quote) { $out[] = '<blockquote><p>' . $this->inline_format(implode(' ', array_map('trim', $quote))) . '</p></blockquote>'; $quote = []; } };
        foreach ($lines as $line) {
            $trim = trim($line);
            if ($trim === '') { $flush_p(); $flush_list(); $flush_quote(); continue; }
            if (preg_match('/^(#{1,6})\s+(.+)$/', $trim, $m)) { $flush_p(); $flush_list(); $flush_quote(); $n = strlen($m[1]); $out[] = '<h' . $n . '>' . $this->inline_format($m[2]) . '</h' . $n . '>'; continue; }
            if (preg_match('/^([-*_])\1\1+$/', $trim)) { $flush_p(); $flush_list(); $flush_quote(); $out[] = '<hr />'; continue; }
            if (preg_match('/^>\s?(.*)$/', $trim, $m)) { $flush_p(); $flush_list(); $quote[] = $m[1]; continue; }
            if (preg_match('/^[-*+]\s+(.+)$/', $trim, $m)) { $flush_p(); $flush_quote(); if ($list !== 'ul') { $flush_list(); $list = 'ul'; $out[] = '<ul>'; } $out[] = '<li>' . $this->inline_format($m[1]) . '</li>'; continue; }
            if (preg_match('/^\d+[.)]\s+(.+)$/', $trim, $m)) { $flush_p(); $flush_quote(); if ($list !== 'ol') { $flush_list(); $list = 'ol'; $out[] = '<ol>'; } $out[] = '<li>' . $this->inline_format($m[1]) . '</li>'; continue; }
            $flush_list(); $flush_quote(); $paragraph[] = $trim;
        }
        $flush_p(); $flush_list(); $flush_quote();
        return wp_kses(implode("\n", $out), ['p'=>[], 'h1'=>[], 'h2'=>[], 'h3'=>[], 'h4'=>[], 'h5'=>[], 'h6'=>[], 'strong'=>[], 'em'=>[], 'del'=>[], 'a'=>['href'=>[], 'title'=>[], 'target'=>[], 'rel'=>[]], 'ul'=>[], 'ol'=>[], 'li'=>[], 'blockquote'=>[], 'hr'=>[]]);
    }

    private function inline_format($text) {
        $text = esc_html($text);
        // Links are converted using a placeholder so URL/text are escaped separately.
        $links = [];
        $text = preg_replace_callback('/\[([^\]]+)\]\((https?:\/\/[^\s)]+)(?:\s+"([^"]*)")?\)/', function($m) use (&$links) {
            $key = 'SMDLINK' . count($links) . 'TOKEN';
            $links[$key] = '<a href="' . esc_url($m[2]) . '"' . (isset($m[3]) ? ' title="' . esc_attr($m[3]) . '"' : '') . '>' . $m[1] . '</a>';
            return $key;
        }, $text);
        $text = preg_replace('/\*\*(.+?)\*\*/s', '<strong>$1</strong>', $text);
        $text = preg_replace('/__(.+?)__/s', '<strong>$1</strong>', $text);
        $text = preg_replace('/(?<!\*)\*([^*]+)\*(?!\*)/s', '<em>$1</em>', $text);
        $text = preg_replace('/(?<!_)_([^_]+)_(?!_)/s', '<em>$1</em>', $text);
        $text = preg_replace('/~~(.+?)~~/s', '<del>$1</del>', $text);
        if ($links) $text = strtr($text, $links);
        return $text;
    }

    private function redirect($type, $message, $post_id = 0) {
        $args = ['page' => 'smd-markdown-importer', 'smd_result' => $type, 'smd_message' => rawurlencode(wp_strip_all_tags($message))];
        if ($post_id) $args['post_id'] = (int)$post_id;
        wp_safe_redirect(add_query_arg($args, admin_url('tools.php'))); exit;
    }

    public function notice() {
        if (empty($_GET['page']) || $_GET['page'] !== 'smd-markdown-importer' || empty($_GET['smd_result'])) return;
        $type = $_GET['smd_result'] === 'success' ? 'success' : 'error';
        $message = isset($_GET['smd_message']) ? sanitize_text_field(rawurldecode(wp_unslash($_GET['smd_message']))) : 'Import finished.';
        echo '<div class="notice notice-' . esc_attr($type) . ' is-dismissible"><p>' . esc_html($message);
        if ($type === 'success' && !empty($_GET['post_id'])) echo ' <a href="' . esc_url(get_edit_post_link(absint($_GET['post_id']), 'raw')) . '">Edit draft</a> · <a href="' . esc_url(get_preview_post_link(absint($_GET['post_id']))) . '">Preview</a>';
        echo '</p></div>';
    }
}
new SMD_SureRank_Markdown_Importer();
