<?php
/**
 * Plugin Name: SureRank Markdown Blog Importer
 * Description: Import Markdown blog posts with front matter, formatting, images, taxonomy and SEO metadata. Creates posts as Pending Review; never publishes.
 * Version: 2.0.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Author: Site Admin
 * License: GPL-2.0-or-later
 */

if (!defined('ABSPATH')) exit;

class SMD_SureRank_Markdown_Importer {
    const VERSION = '2.0.0';
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
        $images = $this->import_images($refs, $files, $slug, $this->image_alts($m, $body), ($allow_update && $updatable) ? $existing->ID : 0);
        if (is_wp_error($images)) $this->redirect('error', $images->get_error_message());
        $content = $this->markdown_to_blocks($body, $images);
        if (!$this->blocks_round_trip($content)) $this->redirect('error', 'The converted post did not parse back into the same blocks, so nothing was saved. Please report the Markdown that caused this.');
        $status = 'pending'; // Pending Review: an editor publishes it; never published directly from an uploaded file.
        $postarr = [
            'post_type' => 'post', 'post_status' => $status, 'post_title' => $title,
            'post_name' => $slug, 'post_content' => $content,
            'post_excerpt' => isset($m['excerpt']) ? sanitize_textarea_field($m['excerpt']) : '',
            'post_author' => get_current_user_id(),
        ];
        if ($allow_update && $updatable) {
            $postarr['ID'] = $existing->ID;
            // WordPress caches each embed's result on the post, including a failed "{{unknown}}"; clear them so
            // a re-import tries every video again.
            foreach (array_keys(get_post_meta($existing->ID)) as $key) if (strpos($key, '_oembed_') === 0) delete_post_meta($existing->ID, $key);
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
        foreach (explode("\n", $body) as $line) {
            $trim = trim($line);
            if ($img = $this->parse_image_line($trim)) $refs[] = $img['src'];
            elseif (($also = $this->parse_also_read($trim)) && $also['img'] !== '') $refs[] = $also['img'];
        }
        return array_values(array_unique($refs));
    }

    /** Each image's alt text, keyed by image_key(): the hero's from featured_image_alt, the others from their image lines. */
    private function image_alts($meta, $body) {
        $alts = [];
        if (!empty($meta['featured_image'])) $alts[$this->image_key($meta['featured_image'])] = $meta['featured_image_alt'] ?? '';
        foreach (explode("\n", $body) as $line) {
            $trim = trim($line);
            if ($img = $this->parse_image_line($trim)) $alts += [$this->image_key($img['src']) => $img['alt']];
            elseif (($also = $this->parse_also_read($trim)) && $also['img'] !== '') $alts += [$this->image_key($also['img']) => $also['alt'] !== '' ? $also['alt'] : $also['title']];
        }
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
     * An uploaded file identical to one this post already has (same MD5) reuses that attachment,
     * so re-importing a post does not duplicate its images. Other posts' copies are not reused:
     * the Hindi and English posts of one talk share image files but need their own alt text.
     * New uploads are saved as <slug>-<file name> (hero.jpg becomes art-of-leaving-hero.jpg), so every
     * post's images get descriptive, distinct names, and are titled with their alt text.
     */
    private function import_images($refs, $files, $slug, $alts, $post_id = 0) {
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
                $found = $post_id ? get_posts(['post_type' => 'attachment', 'post_status' => 'inherit', 'post_parent' => $post_id, 'meta_key' => self::META_IMAGE_HASH, 'meta_value' => $hash, 'fields' => 'ids', 'numberposts' => 1]) : [];
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
        // Line breaks are normalised here and split on "\n": PCRE's \R would also break on the byte 0x85, which
        // is inside many Devanagari letters (अ is E0 A4 85), cutting Hindi lines in two.
        $raw = str_replace(["\r\n", "\r"], "\n", $raw);
        if (!preg_match('/\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)(.*)\z/s', $raw, $matches)) return new WP_Error('smd_front_matter', 'The file must begin with YAML-style front matter between --- lines.');
        $meta = []; $current = '';
        foreach (explode("\n", $matches[1]) as $line) {
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

    /**
     * Converts the Markdown body to the post's content as core blocks (paragraph, heading, list, quote, separator,
     * image, embed, group, columns), in the markup the block editor itself saves, so any theme renders it and the
     * editor opens it as ordinary blocks. Lines ":::" or "::: name" open a bordered group (class name), ":::" closes it.
     */
    private function markdown_to_blocks($markdown, $images = []) {
        $lines = explode("\n", str_replace(["\r\n", "\r"], "\n", $markdown));
        $stack = [[]]; $groups = []; $paragraph = []; $list = null; $items = []; $quote = [];
        $add = function($block) use (&$stack) { $stack[count($stack) - 1][] = $block; };
        $flush = function() use (&$paragraph, &$list, &$items, &$quote, $add) {
            if ($paragraph) { $add($this->block('paragraph', [], '<p>' . $this->join_lines($paragraph) . '</p>')); $paragraph = []; }
            if ($list !== null) {
                $inner = '';
                foreach ($items as $item) $inner .= $this->block('list-item', [], '<li>' . $item . '</li>');
                $tag = $list === 'ol' ? 'ol' : 'ul';
                $add($this->block('list', $list === 'ol' ? ['ordered' => true] : [], '<' . $tag . ' class="wp-block-list">' . $inner . '</' . $tag . '>'));
                $list = null; $items = [];
            }
            if ($quote) {
                $add($this->block('quote', [], '<blockquote class="wp-block-quote">' . $this->block('paragraph', [], '<p>' . $this->join_lines($quote) . '</p>') . '</blockquote>'));
                $quote = [];
            }
        };
        foreach ($lines as $line) {
            $trim = trim($line);
            if (preg_match('/^:::\s*([A-Za-z0-9_-]*)$/', $trim, $m)) {
                $flush();
                if ($m[1] === '' && count($stack) > 1) { $add_to = array_pop($stack); $stack[count($stack) - 1][] = $this->group(array_pop($groups), $add_to); }
                else { $stack[] = []; $groups[] = $m[1]; }
                continue;
            }
            if ($img = $this->parse_image_line($trim)) { $flush(); $add($this->image_block($img, $images)); continue; }
            if ($also = $this->parse_also_read($trim)) { $flush(); $add($this->also_read_block($also, $images)); continue; }
            if ($html = $this->youtube_block($trim)) { $flush(); $add($html); continue; }
            if ($trim === '') { $flush(); continue; }
            if (preg_match('/^(#{1,6})\s+(.+)$/', $trim, $m)) {
                $flush();
                $level = max(2, strlen($m[1])); // the post title is the page's only H1
                $add($this->block('heading', $level === 2 ? [] : ['level' => $level], '<h' . $level . ' class="wp-block-heading">' . $this->inline_format($m[2]) . '</h' . $level . '>'));
                continue;
            }
            if (preg_match('/^([-*_])\1\1+$/', $trim)) { $flush(); $add($this->block('separator', [], '<hr class="wp-block-separator has-alpha-channel-opacity"/>')); continue; }
            if (preg_match('/^>\s?(.*)$/', ltrim($line), $m)) { if ($paragraph || $list !== null) $flush(); $quote[] = $m[1]; continue; }
            if (preg_match('/^([-*+]|\d+[.)])\s+(.+)$/', $trim, $m)) {
                $type = ctype_digit($m[1][0]) ? 'ol' : 'ul';
                if ($paragraph || $quote || ($list !== null && $list !== $type)) $flush();
                $list = $type; $items[] = $this->inline_format($m[2]);
                continue;
            }
            if ($list !== null || $quote) $flush();
            $paragraph[] = ltrim($line);
        }
        $flush();
        while (count($stack) > 1) { $inner = array_pop($stack); $stack[count($stack) - 1][] = $this->group(array_pop($groups), $inner); }
        return implode("\n\n", $stack[0]);
    }

    /** One block: its comment delimiters around its saved markup; attributes as the editor serialises them. */
    private function block($name, $attrs, $html) {
        $json = $attrs ? ' ' . serialize_block_attributes($attrs) : '';
        return "<!-- wp:$name$json -->\n$html\n<!-- /wp:$name -->";
    }

    /** A group with a 1px border, rounded corners and padding, all saved on the block, so it is boxed in any theme. */
    private function group($class, $blocks, $extra = []) {
        $attrs = ($class !== '' ? ['className' => $class] : []) + [
            'style' => ['border' => ['width' => '1px', 'radius' => '8px'], 'spacing' => ['padding' => ['top' => '1rem', 'right' => '1.5rem', 'bottom' => '1rem', 'left' => '1.5rem']]],
            'layout' => ['type' => 'constrained'],
        ] + $extra;
        $html = '<div class="wp-block-group' . ($class !== '' ? ' ' . esc_attr($class) : '') . '" style="border-width:1px;border-radius:8px;padding-top:1rem;padding-right:1.5rem;padding-bottom:1rem;padding-left:1.5rem">'
            . implode("\n\n", $blocks) . '</div>';
        return $this->block('group', $attrs, $html);
    }

    /** Joins a paragraph's or quote's source lines; a line ending in two spaces or a backslash keeps its line break. */
    private function join_lines($lines) {
        $html = '';
        foreach ($lines as $i => $line) {
            $break = (bool) preg_match('/(  |\\\\)$/', $line);
            $html .= $this->inline_format(trim(rtrim($line, " \\\\")));
            if ($i < count($lines) - 1) $html .= $break ? '<br>' : ' ';
        }
        return $html;
    }

    /** A standalone image line as an image block, centred (which centres its caption in every theme). */
    private function image_block($img, $images) {
        $key = $this->image_key($img['src']);
        if (!isset($images[$key])) return '';
        $id = $images[$key]['id'];
        if ($img['alt'] !== '') update_post_meta($id, '_wp_attachment_image_alt', sanitize_text_field($img['alt']));
        $html = '<figure class="wp-block-image aligncenter size-large"><img src="' . esc_url($images[$key]['url']) . '" alt="' . esc_attr($img['alt']) . '" class="wp-image-' . $id . '"/>';
        if ($img['caption'] !== '') $html .= '<figcaption class="wp-element-caption">' . $this->inline_format($img['caption']) . '</figcaption>';
        return $this->block('image', ['id' => $id, 'sizeSlug' => 'large', 'linkDestination' => 'none', 'align' => 'center'], $html . '</figure>');
    }

    /**
     * A line "Also read: [Title](url)" or "यह भी पढ़ें: [Title](url)" (the label may be bold), optionally with a
     * thumbnail image before the link: "Also read: ![alt](also-read.jpg) [Title](url)". url may be site-relative.
     */
    private function parse_also_read($trim) {
        if (!preg_match('/^(?:\*\*|__)?(also read|यह भी पढ़ें)\s*:?\s*(?:\*\*|__)?\s*:?\s*(?:!\[([^\]]*)\]\(\s*([^\s)]+)\s*\)\s*)?\[([^\]]+)\]\((https?:\/\/[^\s)]+|\/[^\s)]*)\)\s*$/iu', $trim, $m)) return null;
        return ['label' => strtolower($m[1]) === 'also read' ? 'Also read' : $m[1], 'alt' => $m[2], 'img' => $m[3], 'title' => $m[4], 'url' => $m[5]];
    }

    /**
     * The Also read box: a bordered group holding two columns, a small linked thumbnail and the label over the
     * linked title. The thumbnail is the line's own image, else the featured image of the post here whose slug is
     * the URL's last path segment, else there is none and the box holds only the text.
     */
    private function also_read_block($also, $images) {
        $id = 0;
        if ($also['img'] !== '' && isset($images[$this->image_key($also['img'])])) $id = $images[$this->image_key($also['img'])]['id'];
        else {
            $segments = array_values(array_filter(explode('/', (string) wp_parse_url($also['url'], PHP_URL_PATH)), function($seg) { return $seg !== '' && !preg_match('/^index\.html?$/i', $seg); }));
            $post = $segments ? get_page_by_path(sanitize_title(end($segments)), OBJECT, 'post') : null;
            if ($post) $id = (int) get_post_thumbnail_id($post);
        }
        $url = esc_url($also['url']);
        $text = $this->block('paragraph', [], '<p><em>' . esc_html($also['label']) . '</em><br><strong><a href="' . $url . '">' . $this->inline_format($also['title']) . '</a></strong></p>');
        if (!$id) return $this->group('also-read', [$text]);
        $src = wp_get_attachment_image_url($id, 'thumbnail');
        $alt = (string) get_post_meta($id, '_wp_attachment_image_alt', true);
        $thumb = $this->block('image', ['id' => $id, 'sizeSlug' => 'thumbnail', 'linkDestination' => 'custom'],
            '<figure class="wp-block-image size-thumbnail"><a href="' . $url . '"><img src="' . esc_url($src) . '" alt="' . esc_attr($alt) . '" class="wp-image-' . $id . '"/></a></figure>');
        $columns = $this->block('columns', ['verticalAlignment' => 'center', 'isStackedOnMobile' => false],
            '<div class="wp-block-columns are-vertically-aligned-center is-not-stacked-on-mobile">'
            . $this->block('column', ['width' => '6rem'], '<div class="wp-block-column" style="flex-basis:6rem">' . $thumb . '</div>')
            . "\n\n" . $this->block('column', ['verticalAlignment' => 'center'], '<div class="wp-block-column is-vertically-aligned-center">' . $text . '</div>')
            . '</div>');
        return $this->group('also-read', [$columns]);
    }

    /**
     * A line that is only a YouTube link, [Title](url) or a bare URL (watch, youtu.be, embed, shorts or live), as an
     * embed block with the link text as caption. If YouTube refuses to embed the video (its owner turned embedding
     * off), it becomes the video's thumbnail linking to it on YouTube instead, so the reader still gets a picture.
     */
    private function youtube_block($trim) {
        if (preg_match('/^\[([^\]]*)\]\(\s*<?([^\s)<>]+)>?\s*\)$/', $trim, $m)) { $title = $m[1]; $url = $m[2]; }
        elseif (preg_match('/^<?(https?:\/\/\S+?)>?$/', $trim, $m)) { $title = ''; $url = $m[1]; }
        else return '';
        if (!preg_match('#^https?://(?:www\.|m\.)?(?:youtube\.com/(?:watch\?(?:.*&)?v=|embed/|shorts/|live/)|youtube-nocookie\.com/embed/|youtu\.be/)([A-Za-z0-9_-]{11})#i', $url, $id)) return '';
        $watch = 'https://www.youtube.com/watch?v=' . $id[1];
        $caption = $title !== '' ? '<figcaption class="wp-element-caption">' . $this->inline_format($title) . '</figcaption>' : '';
        if (wp_oembed_get($watch)) {
            return $this->block('embed', ['url' => $watch, 'type' => 'video', 'providerNameSlug' => 'youtube', 'responsive' => true, 'className' => 'wp-embed-aspect-16-9 wp-has-aspect-ratio'],
                '<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">' . "\n" . $watch . "\n" . '</div>' . $caption . '</figure>');
        }
        $alt = 'Video: ' . ($title !== '' ? $title : 'watch on YouTube');
        // the full-width thumbnail when the video has one (HD uploads), else the standard one, which every video has
        $thumb = 'https://i.ytimg.com/vi/' . $id[1] . '/maxresdefault.jpg';
        if (wp_remote_retrieve_response_code(wp_remote_head($thumb)) !== 200) $thumb = 'https://i.ytimg.com/vi/' . $id[1] . '/hqdefault.jpg';
        return $this->block('image', ['sizeSlug' => 'large', 'linkDestination' => 'custom', 'align' => 'center'],
            '<figure class="wp-block-image aligncenter size-large"><a href="' . esc_url($watch) . '"><img src="' . esc_url($thumb) . '" alt="' . esc_attr($alt) . '"/></a>' . $caption . '</figure>');
    }

    /** True when the content parses back into blocks and serialises to exactly the same text (balanced, well-formed). */
    private function blocks_round_trip($content) {
        return serialize_blocks(parse_blocks($content)) === $content;
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
