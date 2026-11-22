# British English fixes (scan of 2026-11-22)

Scanned every `output/*/*_blog_en.txt`, `*_blog_seo_en.txt` and `blog/seo.json` for American
spellings. Everything else already uses British spelling (colour, honour, centre, realise,
practise and so on). 23 talks need fixes; "computer program" is correct and is not listed.

## Spelling fixes (must fix)

| Talk | Change | Where |
|---|---|---|
| know_your_first_duty_in_life | realized → realised | blog_en ×2, blog_seo_en ×3, seo.json (meta_description, secondary keyword) |
| competent_guru_activate_chakras_kundalini | judgment → judgement | blog_en ×1, blog_seo_en ×1 |

## toward → towards (British style)

| Talk | blog_en | blog_seo_en | seo.json |
|---|---|---|---|
| shreya_vs_preya_vedantic_wisdom | 10 (headings too) | 10 | links[0], also_read |
| one_realisation_free_from_all_suffering | 4 | 4 | |
| gita_warning_worship_without_understanding | 2 | 3 | links[0], links[1] |
| become_billionaire_shree_vidya_secrets | 2 | 2 | |
| love_respect_friendship_connection | 2 | 2 | |
| true_power_of_scriptures_decoded | 2 | 2 | |
| mahalay_shraddha_matters_truth_about_pitru | 1 | 2 | |
| need_murtis_symbols_understand_god | 1 | 1 | hero caption |
| not_wait_until_retirement_transform_life | 1 | 1 | inline alt |
| dharma_teaches_us | 1 | 1 | |
| future_country_bharat_know | 1 | 1 | |
| knowledge_work_for_you | 1 | 1 | |
| physical_mental_strength_spiritual_path | 1 | 1 | |
| stop_asking_god_fix_your_life | 1 | 1 | |
| unveiling_truth_karma_ultimate_goal_or | | 1 | |
| competent_guru_activate_chakras_kundalini | | | inline alt |
| every_ganesh_idol_look_different | | | inline alt, inline caption |
| missing_step_blocking_spiritual_success | | | hero alt |
| sacred_guru_jupiter_chanting | | | inline alt |
| spiritual_science_om_aum | | | hero alt |
| stop_tolerating_toxic_love | | | hero alt |
| why_blind_love_is_dangerous | | | hero alt |

No slug contains any of these words, so no URL changes.

## Where to update after the fixes

1. Edit the text files and seo.json (keep `links[].en` anchors matching the text).
2. `tools/check_seo.py` and `tools/verify_seo_fix.py` for each talk.
3. `tools/rebuild_blogs.sh <talk>` for each talk (GitHub Pages copies).
4. Local WordPress: `./publish_wordpress.sh <talk>`. Only need_murtis_symbols_understand_god has
   been imported locally.
5. Live WordPress: rebuild zips with `tools/make_post_zip.py <talk>` and re-upload any talk
   already on the live site.
6. Commit and push `output/` to deploy GitHub Pages.
