<?php
/**
 * Plugin Name: Markdown Blog Importer
 * Description: Import Markdown blog posts with front matter, formatting, images, taxonomy and SEO metadata (written to SureRank, Yoast SEO, Rank Math or All in One SEO, whichever is active), one language or two at a time, linked as translations with Polylang. Creates posts as Pending Review; never publishes.
 * Version: 3.0.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Author: Site Admin
 * License: GPL-2.0-or-later
 */

if (!defined('ABSPATH')) exit;

class SMD_Markdown_Importer {
    const VERSION = '3.0.0';
    const META_LANG = 'smd_lang';
    const META_TRANSLATION_KEY = 'smd_translation_key';
    const TERM_META_CATEGORY_KEY = 'smd_category_key';
    const OPTION_SWITCH = 'smd_lang_switch';
    const MAX_DOCUMENTS = 2;
    const META_IMAGE_HASH = '_smd_image_hash';
    const MAX_IMAGE_BYTES = 10485760; // 10 MB per image
    const MAX_ZIP_BYTES = 52428800; // 50 MB per zip
    const MAX_ZIP_ENTRIES = 100;

    private $temp_files = [];
    private $link_lang = '';      // the language links are resolved for while a document is converted
    private $unresolved = [];     // site-relative links whose post is not on this site yet
    const META_SEO_TITLE = 'smd_seo_title';
    const META_SEO_DESCRIPTION = 'smd_seo_description';
    const META_CANONICAL = 'smd_canonical_url';
    const META_ROBOTS = 'smd_robots';

    public function __construct() {
        add_action('admin_menu', [$this, 'menu']);
        add_action('admin_post_smd_import_markdown', [$this, 'handle_upload']);
        add_action('admin_notices', [$this, 'notice']);
        add_action('init', [$this, 'register_meta']);
        add_action('admin_init', [$this, 'register_settings']);
        add_shortcode('smd_lang_switch', [$this, 'lang_switch']);
        add_filter('astra_single_post_meta', [$this, 'switch_after_byline']);
        add_filter('the_content', [$this, 'switch_at_top']);
        add_action('wp_head', [$this, 'head']);
    }

    public function menu() {
        add_management_page('Markdown Blog Importer', 'Markdown Blog Importer', 'edit_posts', 'smd-markdown-importer', [$this, 'render_page']);
    }

    public function register_meta() {
        $keys = [self::META_SEO_TITLE, self::META_SEO_DESCRIPTION, self::META_CANONICAL, self::META_ROBOTS, self::META_LANG, self::META_TRANSLATION_KEY];
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
        $seo = $this->active_seo_plugins();
        ?>
        <div class="wrap">
          <h1>Markdown Blog Importer</h1>
          <p>Upload one Markdown <code>.md</code> file, or one <code>.zip</code> holding the <code>.md</code> and its images. A zip may hold two <code>.md</code> files, one per language (for example <code>en.md</code> and <code>hi.md</code>), to import both and link them as translations. Posts are created as <strong>Pending Review</strong> and never published; existing posts with the same slug are not overwritten.</p>
          <?php if ($this->polylang()): ?><div class="notice notice-info"><p>Polylang is active (languages: <?php echo esc_html(implode(', ', pll_languages_list(['fields' => 'name']))); ?>). Each post gets the language in its <code>lang:</code> field, or <?php echo esc_html($this->language_label(pll_default_language())); ?> without one, and posts of one talk are linked as translations.</p></div><?php else: ?><div class="notice notice-warning"><p>Polylang is not active. Posts are imported, and their language and <code>translation_key</code> are saved, so the language switch and <code>hreflang</code> links work for posts; install Polylang for language URLs, per-language categories and menus.</p></div><?php endif; ?>
          <?php if (!$seo): ?><div class="notice notice-warning"><p>No supported SEO plugin (SureRank, Yoast SEO, Rank Math or All in One SEO) is active. Posts are still imported, and the SEO title, meta description, focus keyword, canonical URL and robots setting are kept in the importer's own fields, but no SEO plugin will use them.</p></div><?php else: ?><div class="notice notice-info"><p>The SEO title, meta description, focus keyword, canonical URL and robots setting will be written to <?php echo esc_html(implode(' and ', $seo)); ?>.</p></div><?php endif; ?>
          <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>" enctype="multipart/form-data">
            <?php wp_nonce_field('smd_import_markdown'); ?>
            <input type="hidden" name="action" value="smd_import_markdown">
            <table class="form-table"><tr><th scope="row"><label for="smd_markdown_file">Markdown or zip file</label></th><td><input type="file" id="smd_markdown_file" name="smd_markdown_file" accept=".md,.markdown,.zip,text/markdown,text/plain,application/zip" required><p class="description">A <code>.md</code> file (maximum 2 MB) in the template format, or a <code>.zip</code> (maximum 50 MB) containing exactly one <code>.md</code> file and the images it names, in any folder.</p></td></tr>
            <tr><th scope="row"><label for="smd_images">Images</label></th><td><input type="file" id="smd_images" name="smd_images[]" accept="image/jpeg,image/png,image/webp,image/gif" multiple><p class="description">Optional, and not needed when the zip holds the images. Select the hero and inline images the Markdown refers to by file name: <code>featured_image: hero.jpg</code> in the front matter becomes the featured image, and a line <code>![alt text](inline.jpg "caption")</code> in the body places that image there. Maximum 10 MB per image.</p></td></tr>
            <tr><th scope="row"><label for="smd_translation_of">Translation of</label></th><td><select id="smd_translation_of" name="smd_translation_of"><option value="0">— none, or found by translation_key —</option><?php foreach ($this->translation_choices() as $id => $label) echo '<option value="' . (int) $id . '">' . esc_html($label) . '</option>'; ?></select><p class="description">Optional, for uploading one language: the existing post in another language that this upload translates. The two are linked, and this choice wins over a <code>translation_key</code> match. Posts can also be linked later in the post editor's Languages panel (Polylang).</p></td></tr>
            <tr><th scope="row">Import behavior</th><td><label><input type="checkbox" name="smd_allow_update" value="1"> Update an existing pending or draft post with the same slug (never updates published or scheduled posts)</label></td></tr></table>
            <?php submit_button('Import for Review'); ?>
          </form>
          <?php if (current_user_can('manage_options')): $where = get_option(self::OPTION_SWITCH, 'byline'); ?>
          <hr><h2>Language switch</h2>
          <form method="post" action="options.php"><?php settings_fields('smd_importer'); ?>
            <p>A post with a published translation shows a switch with its languages (for example हिन्दी | English). Also available as the <code>[smd_lang_switch]</code> shortcode.</p>
            <p><?php foreach (['byline' => 'Below the byline (Astra; other themes: top of the post)', 'top' => 'Top of the post', 'off' => 'Off'] as $value => $label): ?><label style="margin-right:1.5em"><input type="radio" name="<?php echo esc_attr(self::OPTION_SWITCH); ?>" value="<?php echo esc_attr($value); ?>" <?php checked($where, $value); ?>> <?php echo esc_html($label); ?></label><?php endforeach; ?></p>
            <?php submit_button('Save switch setting', 'secondary'); ?>
          </form>
          <?php endif; ?>
          <hr><h2>SEO fields</h2>
          <p>The front matter's <code>seo_title</code>, <code>meta_description</code>, <code>focus_keyword</code>, <code>canonical_url</code> and <code>robots</code> are written to each active supported SEO plugin's own per-post settings, so its panel shows them. Copies are also kept in <code>smd_seo_title</code>, <code>smd_seo_description</code>, <code>smd_canonical_url</code> and <code>smd_robots</code>. Schema is not written.</p>
          <p><a href="<?php echo esc_url(plugins_url('README.txt', __FILE__)); ?>" target="_blank" rel="noopener">Read setup instructions and download the Markdown template</a></p>
        </div>
        <?php
    }

    /**
     * Imports one or two Markdown documents (one per language). Every document is checked first, its images,
     * slug, language and translation partner, so a problem in either stops the import before anything is
     * created. Then each post is written, and the posts are linked as translations: with each other, with the
     * post chosen in "Translation of", or with posts already here that share their translation_key.
     */
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
            $raws = $zip['markdown']; $zip_images = $zip['images'];
        } else {
            if ($size > 2 * 1024 * 1024) $this->redirect('error', 'File exceeds the 2 MB limit.');
            if (!preg_match('/\.(md|markdown)$/i', $filename)) $this->redirect('error', 'Only .md, .markdown or .zip files are accepted.');
            $raws = [$filename => file_get_contents($_FILES['smd_markdown_file']['tmp_name'])];
        }
        $files = $this->uploaded_images();
        if (is_wp_error($files)) $this->redirect('error', $files->get_error_message());
        $files = array_merge($zip_images, $files); // an image picked in the Images field wins over the zip's copy
        $result = $this->run_import($raws, $files, !empty($_POST['smd_allow_update']), absint($_POST['smd_translation_of'] ?? 0));
        $this->redirect($result['ok'] ? 'success' : 'error', $result['message'], $result['ids']);
    }

    /**
     * The import itself, shared by the upload page and `wp smd import`: Markdown texts by file name and image
     * files by image_key(). Returns ['ok' => bool, 'message' => text, 'ids' => saved post IDs].
     */
    public function run_import($raws, $files, $allow_update, $translation_of = 0) {
        $this->unresolved = [];
        $docs = [];
        foreach ($raws as $name => $raw) {
            $doc = $this->prepare_document($name, $raw, $files, $allow_update);
            if (is_wp_error($doc)) return ['ok' => false, 'message' => $doc->get_error_message(), 'ids' => []];
            $docs[] = $doc;
        }
        $group = $this->plan_translations($docs, $translation_of);
        if (is_wp_error($group)) return ['ok' => false, 'message' => $group->get_error_message(), 'ids' => []];

        $done = [];
        foreach ($docs as $doc) {
            $post_id = $this->write_post($doc, $files);
            if (is_wp_error($post_id)) {
                $saved = $done ? ' The ' . implode(' and ', array_column($done, 'lang_label')) . ' post was saved; fix the problem and import again with update ticked.' : '';
                return ['ok' => false, 'message' => $post_id->get_error_message() . $saved, 'ids' => array_column($done, 'id')];
            }
            $done[] = ['id' => $post_id, 'lang' => $doc['lang'], 'lang_label' => $doc['lang_label'], 'updated' => (bool) $doc['existing']];
        }
        foreach ($done as $d) if ($d['lang'] !== '') $group['posts'][$d['lang']] = $d['id'];
        $linked = $this->save_translations($group);

        $parts = [];
        foreach ($done as $d) $parts[] = ($d['lang_label'] !== '' ? $d['lang_label'] . ': ' : '') . ($d['updated'] ? 'updated' : 'created') . ', pending review: ' . get_the_title($d['id']);
        $message = implode('. ', $parts) . '.';
        if ($linked) $message .= ' Linked as translations: ' . implode(', ', $linked) . '.';
        if ($this->unresolved) $message .= ' Not on this site yet, so linked by slug: ' . implode(', ', array_unique($this->unresolved)) . '.';
        return ['ok' => true, 'message' => $message, 'ids' => array_column($done, 'id')];
    }

    /**
     * `wp smd import <file> [--update] [--translation-of=<id>]`: imports a .md file or a zip, as the upload
     * page does (Pending Review, never published). Run it as a user who may upload files, e.g. --user=admin.
     * Prints one line per saved post, "<ID> <lang> <slug>", after the result message.
     */
    public function cli_import($args, $assoc) {
        $path = $args[0];
        if (!is_readable($path)) WP_CLI::error("Cannot read $path.");
        if (!current_user_can('edit_posts') || !current_user_can('upload_files')) WP_CLI::error('Run this as a user who can edit posts and upload files, for example with --user=admin.');
        $images = [];
        if (preg_match('/\.zip$/i', $path)) {
            register_shutdown_function([$this, 'remove_temp_files']);
            $zip = $this->read_zip($path);
            if (is_wp_error($zip)) WP_CLI::error($zip->get_error_message());
            $raws = $zip['markdown']; $images = $zip['images'];
        } elseif (preg_match('/\.(md|markdown)$/i', $path)) {
            $raws = [wp_basename($path) => file_get_contents($path)];
        } else {
            WP_CLI::error('Only .md, .markdown or .zip files are accepted.');
        }
        $result = $this->run_import($raws, $images, !empty($assoc['update']), absint($assoc['translation-of'] ?? 0));
        if (!$result['ok']) WP_CLI::error($result['message']);
        WP_CLI::success($result['message']);
        foreach ($result['ids'] as $id) WP_CLI::line($id . ' ' . ($this->post_language($id) ?: '-') . ' ' . get_post_field('post_name', $id));
    }

    /** Posts for the "Translation of" list: every post that has a language, newest first, labelled with it. */
    private function translation_choices() {
        $out = [];
        foreach (get_posts(['post_type' => 'post', 'post_status' => ['publish', 'pending', 'draft', 'future', 'private'], 'numberposts' => 500, 'orderby' => 'date', 'order' => 'DESC', 'lang' => '', 'suppress_filters' => false]) as $p) {
            $lang = $this->post_language($p->ID);
            if ($lang !== '') $out[$p->ID] = $this->language_label($lang) . ': ' . get_the_title($p) . ($p->post_status !== 'publish' ? ' (' . $p->post_status . ')' : '');
        }
        return $out;
    }

    /** Parses and checks one document: front matter, language, slug, update permission and images. */
    private function prepare_document($name, $raw, $files, $allow_update) {
        $where = $name !== '' ? " ($name)" : '';
        if ($raw === false || trim($raw) === '') return new WP_Error('smd_empty', "The Markdown file$where is empty or could not be read.");
        $doc = $this->parse_document($raw);
        if (is_wp_error($doc)) return new WP_Error('smd_front_matter', $doc->get_error_message() . $where);
        $m = $doc['meta']; $body = trim($doc['body']);
        $title = isset($m['title']) ? sanitize_text_field($m['title']) : '';
        if ($title === '') return new WP_Error('smd_title', "The front matter must include a title$where.");
        $lang = $this->document_language($m);
        if (is_wp_error($lang)) return new WP_Error('smd_lang', $lang->get_error_message() . $where);
        $slug = !empty($m['slug']) ? sanitize_title($m['slug']) : sanitize_title($title);
        $existing = get_page_by_path($slug, OBJECT, 'post');
        $updatable = $existing && in_array($existing->post_status, ['pending', 'draft'], true);
        if ($existing && !($allow_update && $updatable)) return new WP_Error('smd_exists', "A post with the slug \"$slug\" already exists$where. Choose a different slug or enable update for an existing pending or draft post.");
        if ($existing && $lang !== '' && ($have = $this->post_language($existing->ID)) !== '' && $have !== $lang) return new WP_Error('smd_exists', "The post with the slug \"$slug\" is in " . $this->language_label($have) . ", not " . $this->language_label($lang) . "$where.");
        $refs = $this->image_refs($m, $body);
        if ($refs && !current_user_can('upload_files')) return new WP_Error('smd_upload', 'This file uses images, and you do not have permission to upload files.');
        $missing = [];
        foreach ($refs as $ref) if (!$this->is_remote($ref) && !isset($files[$this->image_key($ref)])) $missing[] = $ref;
        if ($missing) return new WP_Error('smd_missing', 'These images are referenced but were not uploaded' . $where . ': ' . implode(', ', array_unique($missing)) . '. Add them to the zip or select them in the Images field.');
        return [
            'meta' => $m, 'body' => $body, 'title' => $title, 'slug' => $slug, 'lang' => $lang,
            'lang_label' => $lang !== '' ? $this->language_label($lang) : '',
            'key' => sanitize_key($m['translation_key'] ?? ''), 'category_key' => sanitize_key($m['category_key'] ?? ''),
            'existing' => $existing && $allow_update && $updatable ? $existing : null, 'refs' => $refs, 'name' => $name,
        ];
    }

    /**
     * Works out which posts the imported ones will be linked with, before anything is written: the other
     * document, the "Translation of" post, and posts here with the same translation_key. Returns
     * ['posts' => lang => post ID already here, 'key' => translation key] or an error when the documents or
     * the existing links disagree, so a post is never silently re-linked to a different translation.
     */
    private function plan_translations($docs, $translation_of) {
        $langs = array_column($docs, 'lang');
        if (count($docs) > 1) {
            if (in_array('', $langs, true)) return new WP_Error('smd_lang', 'With two Markdown files, each must name its language with lang: in the front matter (for example lang: en and lang: hi).');
            if (count(array_unique($langs)) < count($langs)) return new WP_Error('smd_lang', 'The two Markdown files have the same language; they must be one per language.');
            if (count(array_unique(array_column($docs, 'slug'))) < count($docs)) return new WP_Error('smd_slug', 'The two Markdown files have the same slug; each language needs its own slug.');
            $keys = array_values(array_filter(array_unique(array_column($docs, 'key'))));
            if (count($keys) > 1) return new WP_Error('smd_key', 'The two Markdown files have different translation_key values: ' . implode(' and ', $keys) . '.');
            if ($translation_of) return new WP_Error('smd_translation_of', '"Translation of" is for uploading one language; with two files, the two posts are linked to each other.');
        }
        $key = '';
        foreach ($docs as $d) if ($d['key'] !== '') $key = $d['key'];
        $posts = [];
        if ($translation_of) {
            $post = get_post($translation_of);
            if (!$post || $post->post_type !== 'post' || $post->post_status === 'trash') return new WP_Error('smd_translation_of', 'The post chosen in "Translation of" was not found.');
            $other = $this->post_language($post->ID);
            if ($other === '') return new WP_Error('smd_translation_of', 'The post chosen in "Translation of" has no language set, so it cannot be linked.');
            if ($docs[0]['lang'] === '') return new WP_Error('smd_lang', 'Name the uploaded post\'s language with lang: in the front matter to link it with "Translation of".');
            if ($other === $docs[0]['lang']) return new WP_Error('smd_translation_of', 'The post chosen in "Translation of" is in the same language as the upload (' . $docs[0]['lang_label'] . ').');
            $posts = $this->translations($post->ID) + [$other => $post->ID];
            if ($key === '') $key = (string) get_post_meta($post->ID, self::META_TRANSLATION_KEY, true);
        }
        if ($key !== '') $posts += $this->posts_with_key($key);
        foreach ($docs as $d) {
            if ($d['existing']) $posts += $this->translations($d['existing']->ID);
        }
        // every language the upload brings must be free, or held by the very post being updated
        foreach ($docs as $d) {
            if ($d['lang'] === '' || empty($posts[$d['lang']])) continue;
            if (!$d['existing'] || (int) $posts[$d['lang']] !== (int) $d['existing']->ID) {
                return new WP_Error('smd_conflict', 'The ' . $d['lang_label'] . ' translation is already "' . get_the_title($posts[$d['lang']]) . '" (slug ' . get_post_field('post_name', $posts[$d['lang']]) . '), not the post with the slug "' . $d['slug'] . '". Unlink it first, or upload with that post\'s slug and update ticked.');
            }
        }
        return ['posts' => $posts, 'key' => $key, 'docs' => $docs];
    }

    /** Creates or updates one document's post, with its language, terms, SEO and images; returns its ID. */
    private function write_post($doc, $files) {
        $m = $doc['meta']; $existing = $doc['existing'];
        $images = $this->import_images($doc['refs'], $files, $doc['slug'], $this->image_alts($m, $doc['body']), $existing ? $existing->ID : 0);
        if (is_wp_error($images)) return $images;
        $this->link_lang = $doc['lang'];
        $content = $this->markdown_to_blocks($doc['body'], $images);
        $this->link_lang = '';
        if (!$this->blocks_round_trip($content)) return new WP_Error('smd_blocks', 'The converted post did not parse back into the same blocks, so nothing was saved. Please report the Markdown that caused this.');
        $postarr = [
            'post_type' => 'post', 'post_status' => 'pending', // Pending Review: an editor publishes it; never published directly from an uploaded file.
            'post_title' => $doc['title'], 'post_name' => $doc['slug'], 'post_content' => $content,
            'post_excerpt' => isset($m['excerpt']) ? sanitize_textarea_field($m['excerpt']) : '',
            'post_author' => get_current_user_id(),
        ];
        if ($existing) {
            $postarr['ID'] = $existing->ID;
            unset($postarr['post_author']); // an update keeps the post's author
            // WordPress caches each embed's result on the post, including a failed "{{unknown}}"; clear them so
            // a re-import tries every video again.
            foreach (array_keys(get_post_meta($existing->ID)) as $key) if (strpos($key, '_oembed_') === 0) delete_post_meta($existing->ID, $key);
            $post_id = wp_update_post(wp_slash($postarr), true);
        } else {
            $post_id = wp_insert_post(wp_slash($postarr), true);
        }
        if (is_wp_error($post_id)) return new WP_Error('smd_post', 'WordPress could not save the post: ' . $post_id->get_error_message());
        foreach ($images as $img) if (!wp_get_post_parent_id($img['id'])) wp_update_post(['ID' => $img['id'], 'post_parent' => $post_id]);

        // the language first, so the post's categories and tags are found or created in that language
        if ($doc['lang'] !== '') {
            update_post_meta($post_id, self::META_LANG, $doc['lang']);
            if ($this->polylang()) pll_set_post_language($post_id, $doc['lang']);
        }
        $cat_ids = [];
        foreach ($this->csv_values($m['categories'] ?? '') as $cat) if ($id = $this->term_id($cat, 'category', $doc['lang'])) $cat_ids[] = $id;
        if ($cat_ids) wp_set_post_categories($post_id, $cat_ids, false);
        if ($cat_ids && $doc['category_key'] !== '') $this->link_category($cat_ids[0], $doc['category_key']);
        $tag_ids = [];
        foreach ($this->csv_values($m['tags'] ?? '') as $tag) if ($id = $this->term_id($tag, 'post_tag', $doc['lang'])) $tag_ids[] = $id;
        if ($tag_ids) wp_set_post_terms($post_id, $tag_ids, 'post_tag', false);

        update_post_meta($post_id, self::META_SEO_TITLE, sanitize_text_field($m['seo_title'] ?? ''));
        update_post_meta($post_id, self::META_SEO_DESCRIPTION, sanitize_textarea_field($m['meta_description'] ?? ''));
        update_post_meta($post_id, self::META_CANONICAL, esc_url_raw($m['canonical_url'] ?? ''));
        $robots = sanitize_text_field($m['robots'] ?? 'index,follow');
        if (!in_array($robots, ['index,follow','noindex,follow','index,nofollow','noindex,nofollow'], true)) $robots = 'index,follow';
        update_post_meta($post_id, self::META_ROBOTS, $robots);
        $this->save_seo($post_id, $m, $robots);
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
        return (int) $post_id;
    }

    /**
     * Links the planned posts as translations: in Polylang when it is active, and always through a shared
     * smd_translation_key, which the language switch uses when there is no Polylang. Returns the linked
     * posts' titles with their languages, or [] when there is nothing to link.
     */
    private function save_translations($group) {
        $posts = array_map('intval', array_filter($group['posts']));
        if (count($posts) < 2) {
            foreach ($posts as $id) if ($group['key'] !== '') update_post_meta($id, self::META_TRANSLATION_KEY, $group['key']);
            return [];
        }
        $key = $group['key'];
        if ($key === '') foreach ($posts as $id) if ($key === '' && ($k = (string) get_post_meta($id, self::META_TRANSLATION_KEY, true)) !== '') $key = $k;
        if ($key === '') $key = 'post-' . min($posts);
        foreach ($posts as $lang => $id) {
            update_post_meta($id, self::META_TRANSLATION_KEY, $key);
            if (get_post_meta($id, self::META_LANG, true) === '') update_post_meta($id, self::META_LANG, $lang);
        }
        if ($this->polylang()) pll_save_post_translations($posts);
        $out = [];
        foreach ($posts as $lang => $id) $out[] = $this->language_label($lang) . ' "' . get_the_title($id) . '"';
        return $out;
    }

    // ---- languages -------------------------------------------------------------------------------------------

    /** True when Polylang's functions are available. */
    private function polylang() {
        return function_exists('pll_set_post_language') && function_exists('pll_languages_list');
    }

    /** The document's language: its lang: field, else Polylang's default language, else '' (no language). */
    private function document_language($m) {
        $lang = sanitize_key($m['lang'] ?? '');
        if (!$this->polylang()) return $lang;
        $known = pll_languages_list(['fields' => 'slug']);
        if ($lang === '') return (string) pll_default_language();
        if (!in_array($lang, $known, true)) return new WP_Error('smd_lang', "The language \"$lang\" is not set up in Polylang (Languages > Languages); it has: " . implode(', ', $known) . '.');
        return $lang;
    }

    /** A post's language: Polylang's when it is active, else the importer's smd_lang field. */
    private function post_language($post_id) {
        if ($this->polylang() && ($lang = pll_get_post_language($post_id))) return $lang;
        return (string) get_post_meta($post_id, self::META_LANG, true);
    }

    /** A post's translations, lang => post ID, including itself. */
    private function translations($post_id) {
        if ($this->polylang()) return array_map('intval', pll_get_post_translations($post_id));
        $key = (string) get_post_meta($post_id, self::META_TRANSLATION_KEY, true);
        $out = $key !== '' ? $this->posts_with_key($key) : [];
        if (($lang = $this->post_language($post_id)) !== '') $out[$lang] = (int) $post_id;
        return $out;
    }

    /** Posts with this translation_key, lang => post ID (any status but trash, every language). */
    private function posts_with_key($key) {
        $ids = get_posts(['post_type' => 'post', 'post_status' => ['publish', 'pending', 'draft', 'future', 'private'], 'meta_key' => self::META_TRANSLATION_KEY, 'meta_value' => $key, 'fields' => 'ids', 'numberposts' => 20, 'lang' => '', 'suppress_filters' => false]);
        $out = [];
        foreach ($ids as $id) if (($lang = $this->post_language($id)) !== '' && !isset($out[$lang])) $out[$lang] = (int) $id;
        return $out;
    }

    /** A language's name: Polylang's, else English / हिन्दी for en / hi, else the code. */
    private function language_label($lang) {
        if ($this->polylang()) {
            $names = array_combine(pll_languages_list(['fields' => 'slug']), pll_languages_list(['fields' => 'name']));
            if (!empty($names[$lang])) return $names[$lang];
        }
        return ['en' => 'English', 'hi' => 'हिन्दी'][$lang] ?? strtoupper($lang);
    }

    /**
     * A category or tag's ID by name, created if missing. With Polylang the term is looked up and created in the
     * post's language, so an English and a Hindi post never share one; a new term's slug gets "-<lang>" when its
     * plain slug is taken by another language.
     */
    private function term_id($name, $taxonomy, $lang) {
        if (!$this->polylang() || $lang === '') {
            $term = term_exists($name, $taxonomy);
            if (!$term) $term = wp_insert_term($name, $taxonomy);
            return is_wp_error($term) ? 0 : (int) (is_array($term) ? $term['term_id'] : $term);
        }
        $untranslated = 0;
        foreach (get_terms(['taxonomy' => $taxonomy, 'name' => $name, 'hide_empty' => false, 'lang' => '']) as $t) {
            $have = pll_get_term_language($t->term_id);
            if ($have === $lang) return (int) $t->term_id;
            if (!$have) $untranslated = (int) $t->term_id;
        }
        if ($untranslated) { pll_set_term_language($untranslated, $lang); return $untranslated; }
        $slug = sanitize_title($name);
        if (term_exists($slug, $taxonomy)) $slug .= '-' . $lang;
        $term = wp_insert_term($name, $taxonomy, ['slug' => $slug]);
        if (is_wp_error($term)) return 0;
        pll_set_term_language($term['term_id'], $lang);
        return (int) $term['term_id'];
    }

    /** Tags a category with its category_key and, with Polylang, links the categories sharing that key as translations. */
    private function link_category($term_id, $category_key) {
        update_term_meta($term_id, self::TERM_META_CATEGORY_KEY, $category_key);
        if (!$this->polylang()) return;
        $group = [];
        foreach (get_terms(['taxonomy' => 'category', 'hide_empty' => false, 'lang' => '', 'meta_key' => self::TERM_META_CATEGORY_KEY, 'meta_value' => $category_key]) as $t) {
            $lang = pll_get_term_language($t->term_id);
            if ($lang && !isset($group[$lang])) $group[$lang] = (int) $t->term_id;
        }
        if (count($group) > 1) pll_save_term_translations($group);
    }

    /**
     * A site-relative post link ("/slug/", optionally "/<lang>/slug/") pointed at the post in the language being
     * imported: its translation when it has one, else the post itself. A slug not on this site yet keeps its
     * slug, under the language's URL (e.g. /hi/slug/ with Polylang), and is reported after the import.
     * Other links are returned unchanged.
     */
    private function resolve_link($url) {
        if ($this->link_lang === '' || !preg_match('#^(/[^?\#]*)([?\#].*)?$#', $url, $m)) return $url;
        $segments = array_values(array_filter(explode('/', $m[1]), 'strlen'));
        if ($this->polylang() && count($segments) === 2 && in_array($segments[0], pll_languages_list(['fields' => 'slug']), true)) array_shift($segments);
        if (count($segments) !== 1 || preg_match('/\.[a-z0-9]+$/i', $segments[0])) return $url;
        $slug = sanitize_title($segments[0]);
        $post = get_page_by_path($slug, OBJECT, 'post');
        $lang = $this->link_lang;
        if ($post) {
            $translations = $this->translations($post->ID);
            $target = $translations[$lang] ?? $post->ID;
            $lang = $this->post_language($target) ?: $lang;
            $slug = get_post_field('post_name', $target);
        } else {
            $this->unresolved[] = $m[1];
        }
        return $this->post_path($slug, $lang) . ($m[2] ?? '');
    }

    /** The site-relative URL of a post slug in a language, as Polylang builds it (no prefix without Polylang). */
    private function post_path($slug, $lang) {
        $url = home_url(user_trailingslashit($slug));
        if ($this->polylang() && function_exists('PLL') && ($language = PLL()->model->get_language($lang))) $url = PLL()->links_model->add_language_to_link($url, $language);
        return wp_make_link_relative($url);
    }

    // ---- language switch -------------------------------------------------------------------------------------

    public function register_settings() {
        register_setting('smd_importer', self::OPTION_SWITCH, ['type' => 'string', 'default' => 'byline', 'sanitize_callback' => function($v) { return in_array($v, ['byline', 'top', 'off'], true) ? $v : 'byline'; }]);
    }

    /** The current post's published translations, lang => post ID, in the site's language order; [] for none. */
    private function switch_targets($post_id) {
        $all = $this->translations($post_id);
        if (count($all) < 2) return [];
        $order = $this->polylang() ? pll_languages_list(['fields' => 'slug']) : array_keys($all);
        $out = [];
        foreach ($order as $lang) if (isset($all[$lang]) && ((int) $all[$lang] === (int) $post_id || get_post_status($all[$lang]) === 'publish')) $out[$lang] = (int) $all[$lang];
        return count($out) > 1 ? $out : [];
    }

    /** [smd_lang_switch]: links to the post in each of its languages; the current one is marked, not linked. */
    public function lang_switch() {
        $post_id = get_the_ID();
        if (!$post_id || !($targets = $this->switch_targets($post_id))) return '';
        $out = '';
        foreach ($targets as $lang => $id) {
            $label = esc_html($this->language_label($lang));
            $out .= $id === (int) $post_id
                ? '<span class="smd-lang-current" lang="' . esc_attr($lang) . '" aria-current="true">' . $label . '</span>'
                : '<a href="' . esc_url(get_permalink($id)) . '" lang="' . esc_attr($lang) . '" hreflang="' . esc_attr($lang) . '">' . $label . '</a>';
        }
        return '<nav class="smd-lang-switch" aria-label="Language">' . $out . '</nav>';
    }

    private function switch_here() {
        return is_singular('post') && in_the_loop() && is_main_query();
    }

    /** "Below the byline" in Astra, whose byline has a filter; other themes get it at the top of the content. */
    public function switch_after_byline($meta) {
        if (get_option(self::OPTION_SWITCH, 'byline') === 'byline' && $this->switch_here() && ($html = $this->lang_switch())) $meta .= '<div class="smd-lang-switch-wrap">' . $html . '</div>';
        return $meta;
    }

    public function switch_at_top($content) {
        $where = get_option(self::OPTION_SWITCH, 'byline');
        if (($where === 'top' || ($where === 'byline' && !defined('ASTRA_THEME_VERSION'))) && $this->switch_here() && ($html = $this->lang_switch())) $content = '<div class="smd-lang-switch-wrap">' . $html . '</div>' . $content;
        return $content;
    }

    /** The switch's styles, and without Polylang (which prints its own) the hreflang links of a translated post. */
    public function head() {
        if (!is_singular('post')) return;
        $post_id = get_queried_object_id();
        $targets = $this->switch_targets($post_id);
        if (!$targets) return;
        if (!$this->polylang()) foreach ($targets as $lang => $id) echo '<link rel="alternate" hreflang="' . esc_attr($lang) . '" href="' . esc_url(get_permalink($id)) . '" />' . "\n";
        if (get_option(self::OPTION_SWITCH, 'byline') === 'off') return;
        ?>
<style id="smd-lang-switch">
.smd-lang-switch { display: inline-flex; border: 1px solid currentColor; border-radius: 999px; overflow: hidden; font-size: 14px; line-height: 1; white-space: nowrap; }
.smd-lang-switch a, .smd-lang-switch span { padding: 7px 12px; text-decoration: none; }
.smd-lang-switch a { color: inherit; }
.smd-lang-switch a:hover, .smd-lang-switch a:focus-visible { background: rgba(0, 0, 0, .06); }
.smd-lang-switch .smd-lang-current { background: var(--ast-global-color-0, #1e73be); color: #fff; }
.smd-lang-switch-wrap { margin: 1em 0; }
</style>
        <?php
    }

    /** The supported SEO plugins that are active, by name. */
    private function active_seo_plugins() {
        $found = [];
        if (defined('SURERANK_VERSION')) $found['surerank'] = 'SureRank';
        if (defined('WPSEO_VERSION')) $found['yoast'] = 'Yoast SEO';
        if (defined('RANK_MATH_VERSION')) $found['rankmath'] = 'Rank Math';
        if (function_exists('aioseo') && class_exists('\AIOSEO\Plugin\Common\Models\Post')) $found['aioseo'] = 'All in One SEO';
        return $found;
    }

    /**
     * Writes the SEO title, description, focus keyword, canonical URL and robots directive into each active
     * supported SEO plugin's own per-post settings. An empty value clears that plugin's override, so it falls back
     * to its default. With none active, only the importer's own smd_* fields hold them.
     */
    private function save_seo($post_id, $m, $robots) {
        $title = sanitize_text_field($m['seo_title'] ?? '');
        $description = sanitize_textarea_field($m['meta_description'] ?? '');
        $keyword = sanitize_text_field($m['focus_keyword'] ?? '');
        $canonical = esc_url_raw($m['canonical_url'] ?? '');
        $noindex = strpos($robots, 'noindex') === 0;
        $nofollow = substr($robots, -8) === 'nofollow';
        $set = function($key, $value) use ($post_id) { if ($value !== '') update_post_meta($post_id, $key, $value); else delete_post_meta($post_id, $key); };
        $active = $this->active_seo_plugins();

        if (isset($active['surerank'])) { // title, description, keyword and canonical share one array; robots are flags
            $general = get_post_meta($post_id, 'surerank_settings_general', true);
            if (!is_array($general)) $general = [];
            foreach (['page_title' => $title, 'page_description' => $description, 'focus_keyword' => $keyword, 'canonical_url' => $canonical] as $key => $value) {
                if ($value !== '') $general[$key] = $value; else unset($general[$key]);
                delete_post_meta($post_id, 'surerank_settings_' . $key); // a stray per-key copy would shadow the array
            }
            update_post_meta($post_id, 'surerank_settings_general', $general);
            update_post_meta($post_id, 'surerank_settings_post_no_index', $noindex ? 'yes' : 'no');
            update_post_meta($post_id, 'surerank_settings_post_no_follow', $nofollow ? 'yes' : 'no');
        }
        if (isset($active['yoast'])) { // robots: "1" sets noindex / nofollow, no value keeps the default
            $set('_yoast_wpseo_title', $title);
            $set('_yoast_wpseo_metadesc', $description);
            $set('_yoast_wpseo_focuskw', $keyword);
            $set('_yoast_wpseo_canonical', $canonical);
            $set('_yoast_wpseo_meta-robots-noindex', $noindex ? '1' : '');
            $set('_yoast_wpseo_meta-robots-nofollow', $nofollow ? '1' : '');
        }
        if (isset($active['rankmath'])) { // robots: a list of directives
            $set('rank_math_title', $title);
            $set('rank_math_description', $description);
            $set('rank_math_focus_keyword', $keyword);
            $set('rank_math_canonical_url', $canonical);
            update_post_meta($post_id, 'rank_math_robots', array_values(array_filter([$noindex ? 'noindex' : 'index', $nofollow ? 'nofollow' : ''])));
        }
        if (isset($active['aioseo'])) { // its own table, written through its public model
            \AIOSEO\Plugin\Common\Models\Post::savePost($post_id, [
                'title' => $title !== '' ? $title : null,
                'description' => $description !== '' ? $description : null,
                'focus_keyword' => $keyword !== '' ? $keyword : null,
                'keyphrases' => $keyword !== '' ? ['focus' => ['keyphrase' => $keyword], 'additional' => []] : null,
                'canonical_url' => $canonical !== '' ? $canonical : null,
                'default' => !$noindex && !$nofollow,
                'noindex' => $noindex,
                'nofollow' => $nofollow,
            ]);
        }
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
     * Reads an uploaded zip: one .md/.markdown file per language, at most two (their texts by file name), and its JPEG, PNG, WebP and
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
        if (!$markdown || count($markdown) > self::MAX_DOCUMENTS) { $zip->close(); return new WP_Error('smd_zip', $markdown ? 'The zip holds more than ' . self::MAX_DOCUMENTS . ' Markdown files; it may hold one per language.' : 'The zip holds no .md or .markdown file.'); }
        $raws = [];
        foreach ($markdown as $i) $raws[wp_basename(str_replace('\\', '/', $zip->getNameIndex($i)))] = $zip->getFromIndex($i);
        $zip->close();
        return ['markdown' => $raws, 'images' => $images];
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
                    // saving moves the file into the Media Library, and the other language's post needs it too
                    $copy = wp_tempnam($file['name']);
                    if (!copy($file['tmp_name'], $copy)) return new WP_Error('smd_image', 'The image ' . $file['name'] . ' could not be copied for saving.');
                    $this->temp_files[] = $copy;
                    $file['tmp_name'] = $copy;
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
        $also['url'] = $this->resolve_link($also['url']);
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
            $links[$key] = '<a href="' . esc_url($this->resolve_link($m[2])) . '"' . (isset($m[3]) ? ' title="' . esc_attr($m[3]) . '"' : '') . '>' . $m[1] . '</a>';
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

    private function redirect($type, $message, $post_ids = []) {
        $args = ['page' => 'smd-markdown-importer', 'smd_result' => $type, 'smd_message' => rawurlencode(wp_strip_all_tags($message))];
        if ($post_ids) $args['post_id'] = implode(',', array_map('intval', (array) $post_ids));
        wp_safe_redirect(add_query_arg($args, admin_url('tools.php'))); exit;
    }

    public function notice() {
        if (empty($_GET['page']) || $_GET['page'] !== 'smd-markdown-importer' || empty($_GET['smd_result'])) return;
        $type = $_GET['smd_result'] === 'success' ? 'success' : 'error';
        $message = isset($_GET['smd_message']) ? sanitize_text_field(rawurldecode(wp_unslash($_GET['smd_message']))) : 'Import finished.';
        echo '<div class="notice notice-' . esc_attr($type) . ' is-dismissible"><p>' . esc_html($message);
        echo '</p>';
        foreach (array_filter(array_map('absint', explode(',', (string) ($_GET['post_id'] ?? '')))) as $id) {
            if (!get_post($id)) continue;
            $lang = $this->post_language($id);
            echo '<p>' . ($lang !== '' ? esc_html($this->language_label($lang)) . ': ' : '') . esc_html(get_the_title($id))
                . ' — <a href="' . esc_url(get_edit_post_link($id, 'raw')) . '">Edit post</a> · <a href="' . esc_url(get_preview_post_link($id)) . '">Preview</a></p>';
        }
        echo '</div>';
    }
}
$smd_markdown_importer = new SMD_Markdown_Importer();
if (defined('WP_CLI') && WP_CLI) WP_CLI::add_command('smd import', [$smd_markdown_importer, 'cli_import']);
