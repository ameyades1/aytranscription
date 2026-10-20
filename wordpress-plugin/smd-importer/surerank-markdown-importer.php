<?php
/**
 * Plugin Name: SureRank Markdown Blog Importer
 * Description: Import Markdown blog posts with front matter, formatting, images, taxonomy and SEO metadata. Creates posts as Pending Review; never publishes.
 * Version: 1.7.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Author: Site Admin
 * License: GPL-2.0-or-later
 */

if (!defined('ABSPATH')) exit;

class SMD_SureRank_Markdown_Importer {
    const VERSION = '1.7.0';
    const META_IMAGE_HASH = '_smd_image_hash';
    const MAX_IMAGE_BYTES = 10485760; // 10 MB per image
    const MAX_ZIP_BYTES = 52428800; // 50 MB per zip
    const MAX_ZIP_ENTRIES = 100;

    private $temp_files = [];
    const META_SEO_TITLE = 'smd_seo_title';
    const META_SEO_DESCRIPTION = 'smd_seo_description';
    const META_CANONICAL = 'smd_canonical_url';
    const META_ROBOTS = 'smd_robots';

    public function __construct() {
        add_action('admin_menu', [$this, 'menu']);
        add_action('admin_post_smd_import_markdown', [$this, 'handle_upload']);
        add_action('admin_notices', [$this, 'notice']);
        add_action('init', [$this, 'register_meta']);
        add_action('wp_enqueue_scripts', [$this, 'styles']);
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

    /** Styles the "Also read" box, only on posts that have one. */
    public function styles() {
        $post = is_singular() ? get_post() : null;
        if (!$post || strpos($post->post_content, 'smd-also-read') === false) return;
        wp_register_style('smd-importer', false, [], self::VERSION);
        wp_enqueue_style('smd-importer');
        wp_add_inline_style('smd-importer', '.smd-also-read{margin:2em 0;border:1px solid rgba(0,0,0,.12);border-left:4px solid currentColor;border-radius:6px;overflow:hidden}'
            . '.smd-also-read a{display:flex;gap:1em;align-items:center;padding:.75em 1em;text-decoration:none}'
            . '.smd-also-read img{flex:0 0 120px;width:120px;height:68px;object-fit:cover;border-radius:4px;margin:0}'
            . '.smd-also-read span{display:block;font-size:.8em;text-transform:uppercase;letter-spacing:.05em;opacity:.7}'
            . '.smd-also-read strong{display:block;line-height:1.35}'
            . '@media (max-width:480px){.smd-also-read img{flex-basis:88px;width:88px;height:50px}}');
    }

    public function render_page() {
        if (!current_user_can('edit_posts')) return;
        $sure = defined('SURERANK_VERSION') || class_exists('SureRank') || function_exists('surerank_init');
        ?>
        <div class="wrap">
          <h1>Markdown Blog Importer</h1>
          <p>Upload one Markdown <code>.md</code> file, or one <code>.zip</code> holding the <code>.md</code> and its images. Posts are created as <strong>Pending Review</strong> and never published; existing posts with the same slug are not overwritten.</p>
          <?php if (!$sure): ?><div class="notice notice-warning"><p>SureRank was not detected automatically. The importer will still create posts, but verify your SureRank integration before publishing.</p></div><?php else: ?><div class="notice notice-info"><p>SureRank appears to be active. The SEO title, meta description, focus keyword, canonical URL and robots setting are written to the post's SureRank settings.</p></div><?php endif; ?>
          <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>" enctype="multipart/form-data">
            <?php wp_nonce_field('smd_import_markdown'); ?>
            <input type="hidden" name="action" value="smd_import_markdown">
            <table class="form-table"><tr><th scope="row"><label for="smd_markdown_file">Markdown or zip file</label></th><td><input type="file" id="smd_markdown_file" name="smd_markdown_file" accept=".md,.markdown,.zip,text/markdown,text/plain,application/zip" required><p class="description">A <code>.md</code> file (maximum 2 MB) in the template format, or a <code>.zip</code> (maximum 50 MB) containing exactly one <code>.md</code> file and the images it names, in any folder.</p></td></tr>
            <tr><th scope="row"><label for="smd_images">Images</label></th><td><input type="file" id="smd_images" name="smd_images[]" accept="image/jpeg,image/png,image/webp,image/gif" multiple><p class="description">Optional, and not needed when the zip holds the images. Select the hero and inline images the Markdown refers to by file name: <code>featured_image: hero.jpg</code> in the front matter becomes the featured image, and a line <code>![alt text](inline.jpg "caption")</code> in the body places that image there. Maximum 10 MB per image.</p></td></tr>
            <tr><th scope="row">Import behavior</th><td><label><input type="checkbox" name="smd_allow_update" value="1"> Update an existing pending or draft post with the same slug (never updates published or scheduled posts)</label></td></tr></table>
            <?php submit_button('Import for Review'); ?>
          </form>
          <hr><h2>SEO custom fields</h2>
          <p>The SEO title, meta description, focus keyword and canonical URL go into SureRank's per-post settings (<code>surerank_settings_general</code>), and the robots value into its no-index and no-follow flags, so the SureRank panel shows them. Copies are also kept in <code>smd_seo_title</code>, <code>smd_seo_description</code>, <code>smd_canonical_url</code> and <code>smd_robots</code>. Schema is not written.</p>
          <p><a href="<?php echo esc_url(plugins_url('README.txt', __FILE__)); ?>" target="_blank" rel="noopener">Read setup instructions and download the Markdown template</a></p>
        </div>
        <?php
    }

    public function handle_upload() {
        if (!current_user_can('edit_posts')) wp_die('You do not have permission to import posts.');
        check_admin_referer('smd_import_markdown');
        if (empty($_FILES['smd_markdown_file']['tmp_name']) || !is_uploaded_file($_FILES['smd_markdown_file']['tmp_name'])) $this->redirect('error', 'Please select a Markdown file.');
        $filename = sanitize_file_name($_FILES['smd_markdown_file']['name']);
        $size = (int) ($_FILES['smd_markdown_file']['size'] ?? 0);
        $zip_images = [];
        if (preg_match('/\.zip$/i', $filename)) {
            if ($size > self::MAX_ZIP_BYTES) $this->redirect('error', 'The zip exceeds the 50 MB limit.');
            register_shutdown_function([$this, 'remove_temp_files']);
            $zip = $this->read_zip($_FILES['smd_markdown_file']['tmp_name']);
            if (is_wp_error($zip)) $this->redirect('error', $zip->get_error_message());
            $raw = $zip['markdown']; $zip_images = $zip['images'];
        } else {
            if ($size > 2 * 1024 * 1024) $this->redirect('error', 'File exceeds the 2 MB limit.');
            if (!preg_match('/\.(md|markdown)$/i', $filename)) $this->redirect('error', 'Only .md, .markdown or .zip files are accepted.');
            $raw = file_get_contents($_FILES['smd_markdown_file']['tmp_name']);
        }
        if ($raw === false || trim($raw) === '') $this->redirect('error', 'The uploaded file is empty or could not be read.');
        $doc = $this->parse_document($raw);
        if (is_wp_error($doc)) $this->redirect('error', $doc->get_error_message());
        $m = $doc['meta']; $body = trim($doc['body']);
        $title = isset($m['title']) ? sanitize_text_field($m['title']) : '';
        if ($title === '') $this->redirect('error', 'The front matter must include a title.');
        $slug = !empty($m['slug']) ? sanitize_title($m['slug']) : sanitize_title($title);
        $existing = get_page_by_path($slug, OBJECT, 'post');
        $allow_update = !empty($_POST['smd_allow_update']);
        $updatable = $existing && in_array($existing->post_status, ['pending', 'draft'], true);
        if ($existing && !($allow_update && $updatable)) $this->redirect('error', 'A post with this slug already exists. Choose a different slug or enable update for an existing pending or draft post.');
        $refs = $this->image_refs($m, $body);
        if ($refs && !current_user_can('upload_files')) $this->redirect('error', 'This file uses images, and you do not have permission to upload files.');
        $files = $this->uploaded_images();
        if (is_wp_error($files)) $this->redirect('error', $files->get_error_message());
        $files = array_merge($zip_images, $files); // an image picked in the Images field wins over the zip's copy
        $missing = [];
        foreach ($refs as $ref) if (!$this->is_remote($ref) && !isset($files[$this->image_key($ref)])) $missing[] = $ref;
        if ($missing) $this->redirect('error', 'These images are referenced but were not uploaded: ' . implode(', ', array_unique($missing)) . '. Add them to the zip or select them in the Images field.');
        $images = $this->import_images($refs, $files, $slug, $this->image_alts($m, $body));
        if (is_wp_error($images)) $this->redirect('error', $images->get_error_message());
        $content = $this->markdown_to_html($body, $images);
        $status = 'pending'; // Pending Review: an editor publishes it; never published directly from an uploaded file.
        $postarr = [
            'post_type' => 'post', 'post_status' => $status, 'post_title' => $title,
            'post_name' => $slug, 'post_content' => $content,
            'post_excerpt' => isset($m['excerpt']) ? sanitize_textarea_field($m['excerpt']) : '',
            'post_author' => get_current_user_id(),
        ];
        if ($allow_update && $updatable) {
            $postarr['ID'] = $existing->ID;
            $post_id = wp_update_post(wp_slash($postarr), true);
        } else {
            $post_id = wp_insert_post(wp_slash($postarr), true);
        }
        if (is_wp_error($post_id)) $this->redirect('error', 'WordPress could not create the post: ' . $post_id->get_error_message());
        foreach ($images as $img) if (!wp_get_post_parent_id($img['id'])) wp_update_post(['ID' => $img['id'], 'post_parent' => $post_id]);

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
        $this->save_surerank($post_id, $m, $robots);
        $hero = $m['featured_image'] ?? '';
        if ($hero !== '' && isset($images[$this->image_key($hero)])) {
            $hero_id = $images[$this->image_key($hero)]['id'];
            set_post_thumbnail($post_id, $hero_id);
            if (!empty($m['featured_image_alt'])) update_post_meta($hero_id, '_wp_attachment_image_alt', sanitize_text_field($m['featured_image_alt']));
            if (!empty($m['featured_image_caption'])) wp_update_post(['ID' => $hero_id, 'post_excerpt' => sanitize_text_field($m['featured_image_caption'])]);
        } elseif (!empty($m['featured_image_id']) && current_user_can('upload_files')) {
            $image_id = absint($m['featured_image_id']);
            if ($image_id && get_post_type($image_id) === 'attachment') set_post_thumbnail($post_id, $image_id);
        }
        $this->redirect('success', (isset($postarr['ID']) ? 'Post updated, pending review: ' : 'Post created, pending review: ') . get_the_title($post_id), $post_id);
    }

    /**
     * Writes the SEO fields where SureRank reads them: title, description, focus keyword and canonical
     * in the surerank_settings_general array (other keys already there are kept), and the robots
     * directive as the separate surerank_settings_post_no_index / _no_follow flags.
     */
    private function save_surerank($post_id, $m, $robots) {
        $general = get_post_meta($post_id, 'surerank_settings_general', true);
        if (!is_array($general)) $general = [];
        $fields = [
            'page_title' => sanitize_text_field($m['seo_title'] ?? ''),
            'page_description' => sanitize_textarea_field($m['meta_description'] ?? ''),
            'focus_keyword' => sanitize_text_field($m['focus_keyword'] ?? ''),
            'canonical_url' => esc_url_raw($m['canonical_url'] ?? ''),
        ];
        foreach ($fields as $key => $value) {
            if ($value !== '') $general[$key] = $value; else unset($general[$key]);
            delete_post_meta($post_id, 'surerank_settings_' . $key); // a stray per-key copy would shadow the array
        }
        update_post_meta($post_id, 'surerank_settings_general', $general);
        update_post_meta($post_id, 'surerank_settings_post_no_index', strpos($robots, 'noindex') === 0 ? 'yes' : 'no');
        update_post_meta($post_id, 'surerank_settings_post_no_follow', substr($robots, -8) === 'nofollow' ? 'yes' : 'no');
    }

    /** Every image the document uses: the front-matter hero first, then the body's image lines in order. */
    private function image_refs($meta, $body) {
        $refs = [];
        if (!empty($meta['featured_image'])) $refs[] = $meta['featured_image'];
        foreach (preg_split('/\R/', $body) as $line) if ($img = $this->parse_image_line(trim($line))) $refs[] = $img['src'];
        return array_values(array_unique($refs));
    }

    /** Each image's alt text, keyed by image_key(): the hero's from featured_image_alt, the others from their image lines. */
    private function image_alts($meta, $body) {
        $alts = [];
        if (!empty($meta['featured_image'])) $alts[$this->image_key($meta['featured_image'])] = $meta['featured_image_alt'] ?? '';
        foreach (preg_split('/\R/', $body) as $line) if ($img = $this->parse_image_line(trim($line))) $alts += [$this->image_key($img['src']) => $img['alt']];
        return $alts;
    }

    /** A line that is only ![alt](src "caption"); src is a file name (or path) or an http(s) URL. */
    private function parse_image_line($trim) {
        if (!preg_match('/^!\[([^\]]*)\]\(\s*<?([^\s)<>]+)>?(?:\s+"([^"]*)")?\s*\)$/', $trim, $m)) return null;
        return ['alt' => $m[1], 'src' => $m[2], 'caption' => $m[3] ?? ''];
    }

    private function is_remote($ref) { return (bool) preg_match('#^https?://#i', $ref); }

    /** Images are matched by file name alone, so "assets/hero.jpg" in the Markdown finds an uploaded hero.jpg. */
    private function image_key($ref) {
        if ($this->is_remote($ref)) return $ref;
        return strtolower(sanitize_file_name(wp_basename(rawurldecode($ref))));
    }

    /** The Images field's files, keyed by image_key(), after checking each is a real image within the size limit. */
    private function uploaded_images() {
        $out = [];
        $f = $_FILES['smd_images'] ?? null;
        if (!$f || !is_array($f['name'])) return $out;
        foreach ($f['name'] as $i => $name) {
            if ($f['error'][$i] === UPLOAD_ERR_NO_FILE) continue;
            $name = sanitize_file_name($name);
            if ($f['error'][$i] !== UPLOAD_ERR_OK || !is_uploaded_file($f['tmp_name'][$i])) return new WP_Error('smd_image', "The image $name could not be uploaded.");
            if ((int) $f['size'][$i] > self::MAX_IMAGE_BYTES) return new WP_Error('smd_image', "The image $name exceeds the 10 MB limit.");
            $type = wp_check_filetype_and_ext($f['tmp_name'][$i], $name);
            if (!in_array($type['type'], ['image/jpeg', 'image/png', 'image/webp', 'image/gif'], true)) return new WP_Error('smd_image', "$name is not a JPEG, PNG, WebP or GIF image.");
            $out[$this->image_key($name)] = ['name' => $name, 'type' => $type['type'], 'tmp_name' => $f['tmp_name'][$i], 'error' => 0, 'size' => (int) $f['size'][$i]];
        }
        return $out;
    }

    /** A Media Library title: the alt text, or else the file name without its extension. */
    private function image_title($alt, $name) {
        $alt = sanitize_text_field($alt);
        return $alt !== '' ? $alt : preg_replace('/\.[^.]+$/', '', wp_basename($name));
    }

    /**
     * Reads an uploaded zip: exactly one .md/.markdown file (its text) and its JPEG, PNG, WebP and
     * GIF images, keyed by image_key() of their file names and written to temporary files.
     * Folders inside the zip are ignored, as are macOS __MACOSX entries, hidden files and other types.
     * Entries are read into memory and never extracted by their own paths.
     */
    private function read_zip($path) {
        if (!class_exists('ZipArchive')) return new WP_Error('smd_zip', 'This server cannot open zip files (the PHP zip extension is missing). Upload the .md file and select its images instead.');
        $zip = new ZipArchive();
        if ($zip->open($path) !== true) return new WP_Error('smd_zip', 'The zip file could not be opened.');
        if ($zip->numFiles > self::MAX_ZIP_ENTRIES) { $zip->close(); return new WP_Error('smd_zip', 'The zip holds more than ' . self::MAX_ZIP_ENTRIES . ' files.'); }
        $markdown = []; $images = [];
        for ($i = 0; $i < $zip->numFiles; $i++) {
            $stat = $zip->statIndex($i);
            $entry = str_replace('\\', '/', $stat['name']);
            $base = wp_basename($entry);
            if (substr($entry, -1) === '/' || $base === '' || $base[0] === '.' || preg_match('#(^|/)__MACOSX/#', $entry)) continue;
            if (preg_match('/\.(md|markdown)$/i', $base)) {
                if ($stat['size'] > 2 * 1024 * 1024) { $zip->close(); return new WP_Error('smd_zip', "$base exceeds the 2 MB limit."); }
                $markdown[] = $i;
            } elseif (preg_match('/\.(jpe?g|png|webp|gif)$/i', $base)) {
                $name = sanitize_file_name($base);
                if ($stat['size'] > self::MAX_IMAGE_BYTES) { $zip->close(); return new WP_Error('smd_image', "The image $name exceeds the 10 MB limit."); }
                $key = $this->image_key($name);
                if (isset($images[$key])) { $zip->close(); return new WP_Error('smd_zip', "The zip holds more than one image named $name."); }
                $tmp = wp_tempnam($name);
                $this->temp_files[] = $tmp;
                if (file_put_contents($tmp, $zip->getFromIndex($i)) === false) { $zip->close(); return new WP_Error('smd_zip', "The image $name could not be read from the zip."); }
                $type = wp_check_filetype_and_ext($tmp, $name);
                if (!in_array($type['type'], ['image/jpeg', 'image/png', 'image/webp', 'image/gif'], true)) { $zip->close(); return new WP_Error('smd_image', "$name is not a JPEG, PNG, WebP or GIF image."); }
                $images[$key] = ['name' => $name, 'type' => $type['type'], 'tmp_name' => $tmp, 'error' => 0, 'size' => (int) $stat['size']];
            }
        }
        if (count($markdown) !== 1) { $zip->close(); return new WP_Error('smd_zip', count($markdown) ? 'The zip holds more than one Markdown file; it must hold exactly one.' : 'The zip holds no .md or .markdown file.'); }
        $raw = $zip->getFromIndex($markdown[0]);
        $zip->close();
        return ['markdown' => $raw, 'images' => $images];
    }

    /** Deletes the zip's temporary image files that the Media Library did not take over. */
    public function remove_temp_files() {
        foreach ($this->temp_files as $tmp) if (file_exists($tmp)) @unlink($tmp);
    }

    /**
     * Adds each referenced image to the Media Library and returns image_key() => [id, url].
     * An uploaded file identical to one imported before (same MD5) reuses that attachment,
     * so re-importing a post does not duplicate its images.
     * New uploads are saved as <slug>-<file name> (hero.jpg becomes art-of-leaving-hero.jpg), so every
     * post's images get descriptive, distinct names, and are titled with their alt text.
     */
    private function import_images($refs, $files, $slug, $alts) {
        if (!$refs) return [];
        require_once ABSPATH . 'wp-admin/includes/file.php';
        require_once ABSPATH . 'wp-admin/includes/media.php';
        require_once ABSPATH . 'wp-admin/includes/image.php';
        $out = [];
        foreach ($refs as $ref) {
            $key = $this->image_key($ref);
            if ($this->is_remote($ref)) {
                $id = media_sideload_image(esc_url_raw($ref), 0, $this->image_title($alts[$key] ?? '', $ref), 'id');
                if (is_wp_error($id)) return new WP_Error('smd_image', "The image $ref could not be downloaded: " . $id->get_error_message());
            } else {
                $file = $files[$key];
                $hash = md5_file($file['tmp_name']);
                $found = get_posts(['post_type' => 'attachment', 'post_status' => 'inherit', 'meta_key' => self::META_IMAGE_HASH, 'meta_value' => $hash, 'fields' => 'ids', 'numberposts' => 1]);
                if ($found) $id = (int) $found[0];
                else {
                    if (strpos($file['name'], $slug . '-') !== 0) $file['name'] = $slug . '-' . $file['name'];
                    $id = media_handle_sideload($file, 0, null, ['post_title' => $this->image_title($alts[$key] ?? '', $file['name'])]);
                    if (is_wp_error($id)) return new WP_Error('smd_image', 'The image ' . $file['name'] . ' could not be saved: ' . $id->get_error_message());
                    update_post_meta($id, self::META_IMAGE_HASH, $hash);
                }
            }
            $out[$key] = ['id' => (int) $id, 'url' => wp_get_attachment_image_url($id, 'large') ?: wp_get_attachment_url($id)];
        }
        return $out;
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

    private function markdown_to_html($markdown, $images = []) {
        $markdown = str_replace(["\r\n", "\r"], "\n", $markdown);
        $lines = explode("\n", $markdown); $out = []; $paragraph = []; $list = null; $quote = [];
        $flush_p = function() use (&$paragraph, &$out) { if ($paragraph) { $out[] = '<p>' . $this->join_lines($paragraph) . '</p>'; $paragraph = []; } };
        $flush_list = function() use (&$list, &$out) { if ($list !== null) { $out[] = '</' . $list . '>'; $list = null; } };
        $flush_quote = function() use (&$quote, &$out) { if ($quote) { $out[] = '<blockquote><p>' . $this->join_lines($quote) . '</p></blockquote>'; $quote = []; } };
        foreach ($lines as $line) {
            $trim = trim($line);
            if ($img = $this->parse_image_line($trim)) { $flush_p(); $flush_list(); $flush_quote(); $out[] = $this->figure($img, $images); continue; }
            if ($html = $this->also_read($trim)) { $flush_p(); $flush_list(); $flush_quote(); $out[] = $html; continue; }
            if ($html = $this->youtube($trim)) { $flush_p(); $flush_list(); $flush_quote(); $out[] = $html; continue; }
            if ($trim === '') { $flush_p(); $flush_list(); $flush_quote(); continue; }
            if (preg_match('/^(#{1,6})\s+(.+)$/', $trim, $m)) { $flush_p(); $flush_list(); $flush_quote(); $n = strlen($m[1]); $out[] = '<h' . $n . '>' . $this->inline_format($m[2]) . '</h' . $n . '>'; continue; }
            if (preg_match('/^([-*_])\1\1+$/', $trim)) { $flush_p(); $flush_list(); $flush_quote(); $out[] = '<hr />'; continue; }
            if (preg_match('/^>\s?(.*)$/', ltrim($line), $m)) { $flush_p(); $flush_list(); $quote[] = $m[1]; continue; }
            if (preg_match('/^[-*+]\s+(.+)$/', $trim, $m)) { $flush_p(); $flush_quote(); if ($list !== 'ul') { $flush_list(); $list = 'ul'; $out[] = '<ul>'; } $out[] = '<li>' . $this->inline_format($m[1]) . '</li>'; continue; }
            if (preg_match('/^\d+[.)]\s+(.+)$/', $trim, $m)) { $flush_p(); $flush_quote(); if ($list !== 'ol') { $flush_list(); $list = 'ol'; $out[] = '<ol>'; } $out[] = '<li>' . $this->inline_format($m[1]) . '</li>'; continue; }
            $flush_list(); $flush_quote(); $paragraph[] = ltrim($line);
        }
        $flush_p(); $flush_list(); $flush_quote();
        return wp_kses(implode("\n", $out), ['p'=>[], 'h1'=>[], 'h2'=>[], 'h3'=>[], 'h4'=>[], 'h5'=>[], 'h6'=>[], 'strong'=>[], 'em'=>[], 'del'=>[], 'a'=>['href'=>[], 'title'=>[], 'target'=>[], 'rel'=>[]], 'ul'=>[], 'ol'=>[], 'li'=>[], 'blockquote'=>[], 'hr'=>[], 'br'=>[],
            'figure'=>['class'=>[]], 'aside'=>['class'=>[]], 'div'=>['class'=>[]], 'span'=>['class'=>[]], 'figcaption'=>['class'=>[]], 'img'=>['src'=>[], 'alt'=>[], 'class'=>[], 'width'=>[], 'height'=>[], 'loading'=>[], 'decoding'=>[]]]);
    }

    /** Joins a paragraph's or quote's source lines; a line ending in two spaces or a backslash keeps its line break. */
    private function join_lines($lines) {
        $html = '';
        foreach ($lines as $i => $line) {
            $break = (bool) preg_match('/(  |\\\\)$/', $line);
            $html .= $this->inline_format(trim(rtrim($line, " \\\\")));
            if ($i < count($lines) - 1) $html .= $break ? "<br>\n" : ' ';
        }
        return $html;
    }

    /**
     * A line "Also read: [Title](url)" (the label may be bold) as a box; url may be site-relative (/slug/). If a post here has the
     * URL's last path segment as its slug, the box shows that post's featured image.
     */
    private function also_read($trim) {
        if (!preg_match('/^(?:\*\*|__)?also read\s*:?\s*(?:\*\*|__)?\s*:?\s*\[([^\]]+)\]\((https?:\/\/[^\s)]+|\/[^\s)]*)\)\s*$/i', $trim, $m)) return '';
        $segments = array_values(array_filter(explode('/', (string) wp_parse_url($m[2], PHP_URL_PATH)), function($seg) { return $seg !== '' && !preg_match('/^index\.html?$/i', $seg); }));
        $post = $segments ? get_page_by_path(sanitize_title(end($segments)), OBJECT, 'post') : null;
        $thumb = $post ? get_the_post_thumbnail($post, 'medium', ['loading' => 'lazy', 'alt' => '']) : '';
        return '<aside class="smd-also-read"><a href="' . esc_url($m[2]) . '">' . $thumb . '<span class="smd-also-read-text"><span>Also read</span><strong>' . $this->inline_format($m[1]) . ' &rarr;</strong></span></a></aside>';
    }

    /**
     * A line that is only a YouTube link, [Title](url) or a bare URL, in any of the watch, youtu.be,
     * embed or shorts forms, as an embed block; WordPress turns the URL on its own line into the player.
     */
    private function youtube($trim) {
        if (preg_match('/^\[([^\]]*)\]\(\s*<?([^\s)<>]+)>?\s*\)$/', $trim, $m)) { $title = $m[1]; $url = $m[2]; }
        elseif (preg_match('/^<?(https?:\/\/\S+?)>?$/', $trim, $m)) { $title = ''; $url = $m[1]; }
        else return '';
        if (!preg_match('#^https?://(?:www\.|m\.)?(?:youtube\.com/(?:watch\?(?:.*&)?v=|embed/|shorts/|live/)|youtube-nocookie\.com/embed/|youtu\.be/)([A-Za-z0-9_-]{11})#i', $url, $id)) return '';
        $html = '<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">' . "\nhttps://www.youtube.com/watch?v=" . $id[1] . "\n" . '</div>';
        if ($title !== '') $html .= '<figcaption class="wp-element-caption">' . $this->inline_format($title) . '</figcaption>';
        return $html . '</figure>';
    }

    /** A standalone image line as an image block's figure, with the attachment's sizes so WordPress serves srcset. */
    private function figure($img, $images) {
        $key = $this->image_key($img['src']);
        if (!isset($images[$key])) return '';
        $id = $images[$key]['id'];
        if ($img['alt'] !== '') update_post_meta($id, '_wp_attachment_image_alt', sanitize_text_field($img['alt']));
        $html = '<figure class="wp-block-image size-large"><img src="' . esc_url($images[$key]['url']) . '" alt="' . esc_attr($img['alt']) . '" class="wp-image-' . $id . '" loading="lazy" />';
        if ($img['caption'] !== '') $html .= '<figcaption class="wp-element-caption">' . $this->inline_format($img['caption']) . '</figcaption>';
        return $html . '</figure>';
    }

    private function inline_format($text) {
        $text = esc_html($text);
        // Links are converted using a placeholder so URL/text are escaped separately.
        $links = [];
        $text = preg_replace_callback('/\[([^\]]+)\]\((https?:\/\/[^\s)]+|\/[^\s)]*)(?:\s+"([^"]*)")?\)/', function($m) use (&$links) {
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
        if ($type === 'success' && !empty($_GET['post_id'])) echo ' <a href="' . esc_url(get_edit_post_link(absint($_GET['post_id']), 'raw')) . '">Edit post</a> · <a href="' . esc_url(get_preview_post_link(absint($_GET['post_id']))) . '">Preview</a>';
        echo '</p></div>';
    }
}
new SMD_SureRank_Markdown_Importer();
