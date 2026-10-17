# Blog categories: review and proposal

Prepared 2026-10-18 for review before running /seo_blog on all talks. Nothing has been changed yet: `gallery_topics.txt` and the live site are untouched.

## 1. What the live site has today

blogs.antaryogfoundation.in (WordPress REST API, 39 English posts, no Hindi posts, no translation plugin):

| Live category | Posts | Notes |
|---|---|---|
| Guru Gyan | 13 | Used as a catch-all for Acharya Ji's teachings: prayer, coincidence, suffering, Bharat's future, Yoga Day, plus real Guru topics |
| Women Empowerment | 8 | Marriage, boundaries, education, divine qualities in women |
| Idol Worship | 7 | Idol worship and multiple forms of God, including "Do Hindus really have 33 koti devatas?" |
| Diet | 5 | Food, veg vs non-veg, food and karma |
| Festivals and Observances | 5 | Navratri, Pitru Paksha, Ganesh Chaturthi, Jagran, Pitru Rin shibir |
| Daan (Donation) | 1 | One post |
| Ganesh Vidya | 0 | Empty; also exists as a tag |
| Uncategorized | 0 | WordPress default |

Tags: 14, mostly used once (Brahmacharya, Celibacy, Self Control, Sense Control…), with near-duplicates (Self Control / Sense Control / Control Senses).

Our blog index (`gallery_topics.txt`) has 10 topics, with 82 talks assigned and 64 under "Other".

## 2. Problems to solve

1. **Two lists that don't match.** The live site and our index use different categories. WordPress, the blog index and `seo.json` should share one list.
2. **"Guru Gyan" means two things.** On the live site it holds general teachings; in our index "Guru & Disciple" holds only Guru topics. A catch-all category tells Google nothing about the topic.
3. **Narrow categories.** "Idol Worship", "Diet" and "Daan" each describe one question rather than a theme, and "Daan" has one post.
4. **Missing themes.** Many of our talks have no home: Pitru Paksha and shraddha (6 talks), death and liberation (5), Bharat and society (6), and festivals.
5. **"Women & Society" mixes two themes**: talks for women, and talks about the nation and caste.
6. **Tags are scattered**: single-use tags and near-duplicates create empty, thin archive pages.
7. **Overlap with existing live posts.** Several of the 39 live posts cover the same topic as our talks; most clearly "Do Hindus really have 33 koti devatas?" vs our 33 crore gods blog. Publishing both would make them compete for the same search (keyword cannibalization). This needs a decision per pair when migrating (see section 6).

## 3. Proposed category list (14)

One list for WordPress, the blog index and `seo.json`. Each post gets **one** category; specifics go into tags.

| Key | English | Hindi | Slug | Replaces on live site | Talks |
|---|---|---|---|---|---|
| `guru` | Guru & Disciple | गुरु और शिष्य | guru-disciple | Guru Gyan (partly, see below) | 13 |
| `mind` | Mind & Self | मन और आत्मबोध | mind-self | – | 15 |
| `karma` | Karma & Destiny | कर्म और भाग्य | karma-destiny | – | 15 |
| `dharma` | Dharma & Scriptures | धर्म और शास्त्र | dharma-scriptures | – | 13 |
| `deities` | Deities & Worship | देवी-देवता और उपासना | deities-worship | Idol Worship (7), Ganesh Vidya (0) | 22 |
| `sadhana` | Sadhana, Mantra & Jyotish | साधना, मंत्र और ज्योतिष | sadhana-mantra-jyotish | – | 8 |
| `festivals` | Festivals & Observances | पर्व और व्रत | festivals-observances | Festivals and Observances (5) | 4 |
| `pitru` | Ancestors & Shraddha | पितृ और श्राद्ध | ancestors-shraddha | – | 6 |
| `moksha` | Death & Liberation | मृत्यु और मोक्ष | death-liberation | – | 5 |
| `love` | Love & Relationships | प्रेम और संबंध | love-relationships | – | 13 |
| `women` | Women & Spirituality | नारी और अध्यात्म | women-spirituality | Women Empowerment (8) | 5 |
| `food` | Food & Health | आहार और स्वास्थ्य | food-health | Diet (5) | 9 |
| `success` | Success & Prosperity | सफलता और समृद्धि | success-prosperity | Daan (1) | 12 |
| `nation` | Bharat & Society | भारत और समाज | bharat-society | – | 6 |

Total: 146 talks.

**Changes from our current 10 topics:** "Mind" → "Mind & Self"; "Mantra & Planets" → "Sadhana, Mantra & Jyotish" (adds sadhana, brahmacharya, Vastu); "Women & Society" split into "Women & Spirituality" and "Bharat & Society"; new: Festivals & Observances, Ancestors & Shraddha, Death & Liberation.

**Live categories:** Guru Gyan → split between Guru & Disciple and the topic each post is really about; Idol Worship and Ganesh Vidya → Deities & Worship; Diet → Food & Health; Women Empowerment → Women & Spirituality; Daan → Success & Prosperity; Festivals and Observances kept.

## 4. Rules for choosing a category

- **One category per post**, the main thing the post is about. Use tags for everything else.
- **Festivals:** use Festivals & Observances only when the post is about the festival itself (how and why it is observed). When a festival is just the occasion, use the topic's category and add the festival as a tag. Example: "Why Ganesha loves red flowers" → Deities & Worship, tag "Ganesh Chaturthi".
- **Pitru Paksha** posts go to Ancestors & Shraddha, not Festivals, because people search them by topic year-round, not only during the festival.
- **Series** (Ganesh Vidya, the Ganesh Series on YouTube) are tags, not categories.
- **Tags:** 3–6 per post, naming concepts, deities, festivals or texts (Ganesh, Pitru Paksha, Bhagavad Gita, Advaita Vedanta). Reuse existing tags; never create near-duplicates. A tag should be expected to collect at least 3 posts.

## 5. Proposed category for every talk

"Change" marks talks that move from their current topic (or from "Other").

### Guru & Disciple (13)

| Talk | Title | Change |
|---|---|---|
| `true_disciple_change_your_life` | A True Disciple Turns Knowledge into Action |  |
| `being_presence_guru_changes_way_think` | How the Guru's Presence Changes the Way You Think | new (was Other) |
| `when_disciple_become_truly_powerful` | I Have a Guru, So Is My Work Done? | new (was Other) |
| `every_moment_enlightened_master_new_birth` | In the Guru's Presence, Every Moment Is a New Birth | new (was Other) |
| `competent_guru_activate_chakras_kundalini` | The Competent Guru and Kundalini: Many Lifetimes of Progress in One Sadhana |  |
| `guru_and_disciple_highest_form_love` | The Guru and the Disciple: The Highest Form of Love |  |
| `real_meaning_guru` | The Secret of Guru Purnima and the Real Meaning of Vyasa | new (was Other) |
| `what_is_a_guru` | What Is a Guru, and Why We Must Understand It Before Becoming a Vishwaguru | new (was Other) |
| `know_kind_student_shishya` | What Kind of Disciple Are You? Three Ways to Approach the Guru | new (was Other) |
| `guru_bridging_science_spirituality` | When the Questions Come from Science, Let the Answers Come from the Self |  |
| `why_satsang_does_not_change_your_life` | Why Satsang Does Not Change Your Life |  |
| `surrendering_to_guru` | Why Set Aside Every Dharma and Take Refuge in the Guru |  |
| `without_guru_scriptures_can_mislead` | Without the Guru, Scriptures Can Lead You Astray |  |

### Mind & Self (15)

| Talk | Title | Change |
|---|---|---|
| `joy_sorrow_transformation` | A Horse in the Dung, Tears Among the Toys: The Secret of Dharana Shakti |  |
| `stop_mind_controlling_unlock_true_focus` | A Mind That Chases Every New Thing: Vritti, Pravritti and the Yoga of Steadiness |  |
| `rigid_mind_vs_flexible_mind_destiny` | A Stubborn Mind or a Flexible Intellect: Who Holds Your Destiny? |  |
| `truly_independent` | Are We Really Free? | new (was Other) |
| `control_your_mind_before_it_controls_you` | Control Your Mind Before It Controls You |  |
| `hidden_power_of_positivity` | Hear What Is Auspicious, See What Is Auspicious: The Hidden Power of Positivity |  |
| `spiritual_age_matters_physical_age` | How Old Are You Really? Not Your Body, Your Soul | new (was Other) |
| `worldly_maya_makes_forget_true_self` | How the Maya of the World Makes Us Forget Who We Are | new (was Other) |
| `one_realisation_free_from_all_suffering` | One Realisation That Frees You from Suffering: Finding the Unchanging in a Changing World | new (was Other) |
| `secrets_mastering_your_mind_technique` | The Atharva Mind: Becoming the Ganadhipati of Your Own Life |  |
| `mind_or_body_more_powerful` | The Pen or the Sword: Which Comes First? |  |
| `secret_ultimate_happiness` | The Secret of Supreme Bliss: Which Knowledge Sets You Free | new (was Other) |
| `trapped_illusory_happiness` | The Trap of Fleeting Happiness and the Truth About Physical Bliss |  |
| `what_changed_within_you_this_year` | What Changed Within You This Year? | new (was Other) |
| `artificial_intelligence_getting_smarter_but_humans` | Your Phone Is Getting Smarter. Are You? | new (was Other) |

### Karma & Destiny (15)

| Talk | Title | Change |
|---|---|---|
| `three_gunas_karma` | Are You the One Acting, or Is Nature Acting Through You? | new (was Other) |
| `life_boomerang_before_react` | As You Come to Me, So I Come to You | new (was Other) |
| `burn_your_karma_before_it_burns_you` | Burn Your Karma Before It Burns You |  |
| `stop_asking_god_fix_your_life` | Don't Ask God to Remove Your Problems; Ask for the Strength to Solve Them |  |
| `take_so_long_fulfil_desires` | The Fear of Sin, the Knot in the Heart and the Path Beyond Ritual Worship | new (was Other) |
| `reveals_4_life_changing_components` | To Change Your Destiny, You Need These Four Things | new (was Other) |
| `overcome_struggles_of_life` | Whatever Comes Must Also Go: Overcoming Life's Struggles with the Gita |  |
| `unveiling_truth_karma_ultimate_goal_or` | When Should You Let Go of the Pole of Action? | new (was Other) |
| `who_real_doer_karma_ego_bhagavad` | Who Is the Doer When Nature Does Everything? | new (was Other) |
| `two_causes_create_your_life` | Who Makes the Pot? The Secret of the Material and Efficient Causes |  |
| `decides_destiny` | Who Writes Your Destiny? Not Your Actions, but Your Samskaras | new (was Other) |
| `legends_keep_working` | Why Do Those Who Need Nothing Still Act? | new (was Other) |
| `struggling_despite_trying_best` | Why Do We Struggle Despite Our Best Efforts? The Secret of Acting with Understanding |  |
| `punya_vs_paap` | Why the Same Action Can Be a Virtue or a Sin | new (was Other) |
| `destiny_awaits_obstacle_in_way` | Your Destiny Is Already Flowing: Just Clear the Obstacle |  |

### Dharma & Scriptures (13)

| Talk | Title | Change |
|---|---|---|
| `ultimate_source_learn_about_every_religion` | All Religions Spring from One Source | new (was Other) |
| `every_human_inherently_spiritual` | Are Spiritual and Worldly Life Really Separate? |  |
| `know_your_first_duty_in_life` | Do You Remember Your First Duty? |  |
| `evolution_of_dharma_sanatan_dharma` | From Praise to Self-Knowledge: How Sanatan Dharma Evolved |  |
| `see_god_even_enemy` | How to See God Even in Your Enemy | new (was Other) |
| `satyug_rules_kaliyug_different_path` | Satyuga's Rules, Kaliyuga's Path: Bhairava Shakti and India as Vishwaguru |  |
| `see_lord_everyone_but_treat_merit` | See God in Everyone, but Treat Each on Merit | new (was Other) |
| `shreya_vs_preya_vedantic_wisdom` | Shreya or Preya: Where Are Your Actions Taking You? |  |
| `true_power_of_scriptures_decoded` | The Real Meaning of Shastra: A Rulebook or a Map for Life |  |
| `dharma_teaches_us` | The True Essence of Dharma: How the Word of Saints Differs from the Word of God | new (was Other) |
| `attain_divine_qualities_empower_spiritual` | The True Lakshmi Puja: The Art of Awakening Divine Wealth |  |
| `difference_ved_vedant` | The Veda Is Not a Book to Read but a Journey of Knowing |  |
| `when_kalki_avatar_come` | When Will the Kalki Avatar Come? | new (was Other) |

### Deities & Worship (22)

| Talk | Title | Change |
|---|---|---|
| `goddess_lakshmi_lord_vishnu_stories` | Creation Takes a Moment, Sustaining Takes a Lifetime |  |
| `ganesh_have_elephant_head_mouse` | How Did Ganapati Get an Elephant's Head, and How Does He Ride a Mouse? | new (was Other) |
| `power_of_deities_in_your_life` | How the Three Gods and Three Goddesses Work in Your Life |  |
| `awaken_divine_shakti_kali_lakshmi_saraswati` | Kali, Lakshmi, Saraswati: Awaken the Three Powers Within |  |
| `know_your_lord_before_worship` | Know Before You Worship: Do You Really Know Your God? |  |
| `know_your_god_transformative_path` | Know God, Don't Just Believe |  |
| `only_way_know_god` | Loving a Picture, or Meeting God? | new (was Other) |
| `gita_warning_worship_without_understanding` | Marrying a Photograph, or Meeting God | new (was Other) |
| `unlock_divine_energy_durga_saptashati_mantra` | Six Hours of Sadhana in Ten Minutes Through Bija Mantras |  |
| `hidden_meaning_spiritual_symbols` | The Hidden Meaning Behind Symbols |  |
| `radha_krishna_divine_secret` | The Secret of Gopika Vallabha: When Radha and Krishna Traded Places |  |
| `hidden_truth_rudra_rudraksha` | The True Meaning of Rudraksha: The Tears of the Guru |  |
| `33_crore_gods_truth_about_hinduism` | Thirty-Three Crore Gods, or One God? |  |
| `awaken_inner_shiv_shakti_maha_shivratri` | This Maha Shivratri, Discover the True Secret of the Shivling |  |
| `three_types_obstacle_removers_harta` | Three Kinds of Harta: What Are You Taking Away, and for Whom? |  |
| `understand_spiritual_science_behind_different_offerings` | Tulsi, Bilva Leaves and Durva Grass: The Science Behind Our Offerings | new (was Other) |
| `worship_ganesh_every_year_but_understand` | We Worship Lord Ganesha Every Year, but Have We Understood Him? | new (was Other) |
| `animal_sacrifice` | What Animal Sacrifice Truly Means: Offering Up the Beast Within | new (was Other) |
| `truth_about_lord_ganesh` | Who Is the Real Lord Ganesha? |  |
| `durva_red_flowers_lord_ganesh_worship` | Why Lord Ganesha Loves Red Flowers and Durva Grass |  |
| `real_role_maha_kali` | Why Mahakali Comes First: The Power That Guards Every Auspicious Beginning | new (was Other) |
| `need_murtis_symbols_understand_god` | Why Worship a Murti If God Has No Form? | new (was Other) |

### Sadhana, Mantra & Jyotish (8)

| Talk | Title | Change |
|---|---|---|
| `chant_thousand_names_god` | A Thousand Names of the One God | new (was Other) |
| `sacred_guru_jupiter_chanting` | The Guru Is Shiva: The Secret of Devguru Brihaspati's Grace |  |
| `missing_step_blocking_spiritual_success` | The Missing Step That Is Holding Back Your Sadhana | new (was Other) |
| `saturn_mars_succeed_shani_mangal` | The Real Secret of Brakes: What Saturn and Mars Teach Us About Success |  |
| `truth_about_brahmacharya_exposed_video` | The Truth About Brahmacharya That No One Tells You | new (was Other) |
| `spiritual_science_om_aum` | The Whole Universe Hidden in A, U and M |  |
| `vastu_positive_energy_in_your_space` | Vastu and the Energy of Your Home | new (was Other) |
| `shukra_graha_chanting_wealth_relationships` | When Venus Awakens, Love, Wealth and Radiance Flow Naturally |  |

### Festivals & Observances (4)

| Talk | Title | Change |
|---|---|---|
| `hidden_meaning_behind_10_days_ganesh` | The Hidden Meaning of Ganesh Chaturthi: Turiya and the Birth of Discernment | new (was Other) |
| `ganesh_chaturthi_pitru_paksha_navratri_diwali` | The Hidden Spiritual Sequence of Festivals from Ganapati to Diwali | new (was Other) |
| `ganpati_visarjan_tradition` | What the Handful of Clay Returned After Visarjan Tells Us | new (was Other) |
| `every_ganesh_idol_look_different` | Whose Choice Decides How Ganpati Comes Home? | new (was Other) |

### Ancestors & Shraddha (6)

| Talk | Title | Change |
|---|---|---|
| `women_have_right_perform_shraddha_pind` | Can Women Perform Shraddha and Pind Daan? | new (was Other) |
| `mrityu_versus_moksha` | Death Is Not Liberation: The True Meaning of Pitru Paksha | new (was Other) |
| `big_pitru_dosh_understanding_pitru_rin` | How Deep Pitru Dosh Runs When Your Ancestors Span Seven Lifetimes | new (was Other) |
| `true_meaning_pitru_rin` | The True Meaning of Pitru Rin: Service Before Shraddha | new (was Other) |
| `mahalay_shraddha_matters_truth_about_pitru` | Why Mahalaya Shraddha Matters: The Truth About Our Ancestors | new (was Other) |
| `pind_daan` | Why the Crow Eats the Pind, and Why It Sometimes Will Not | new (was Other) |

### Death & Liberation (5)

| Talk | Title | Change |
|---|---|---|
| `art_living_life` | Beyond the Art of Living: The Art of Leaving This World | new (was Other) |
| `anyone_grant_liberation_living_or_dead` | Liberation After Death, or Freedom While Alive? | new (was Other) |
| `biggest_spiritual_misconception_about_death` | Liberation Does Not Come After Death | new (was Other) |
| `chanting_om_final_breath_liberation` | Om with Your Last Breath: Can You Find Liberation at the Moment of Death? | from Mantra & Planets |
| `gita_escape_cycle_of_rebirth` | The Real Bondage Is an Old Mind, Not an Old Body | new (was Other) |

### Love & Relationships (13)

| Talk | Title | Change |
|---|---|---|
| `too_bad_to_be_too_good_valentines` | Can Being Too Good Also Be a Mistake? |  |
| `love_respect_friendship_connection` | Four Forms of Love, and the Oneness We Learn from the Guru |  |
| `loving_in_the_right_way_valentines` | Love That Shows in Action |  |
| `marriage_giving_not_taking_relationships` | Marriage Is About Giving, Not Taking |  |
| `stop_tolerating_toxic_love` | Putting Up with Abuse Is Not a Virtue |  |
| `love_burden_for_child_parenting` | The Burden of Dreams and Rajasic Parenting |  |
| `company_you_keep_shapes_destiny` | The Company You Keep Shapes Your Destiny |  |
| `married_or_not_insights` | The True Meaning of Pativrata: Living with Radiance, Not in Submission |  |
| `truly_desire_or_infatuation` | True Kama or Mere Attraction? |  |
| `true_meaning_of_love_valentines` | What Love Is, and What It Is Not |  |
| `why_blind_love_is_dangerous` | Why Blind Love Is Dangerous |  |
| `twin_flames_soulmates_karmic_bonds` | Why Do You Keep Meeting the Same Person? |  |
| `when_love_turns_into_control` | Why a Mother's Bill Always Comes to Zero | new (was Other) |

### Women & Spirituality (5)

| Talk | Title | Change |
|---|---|---|
| `gyan_sarovar_mount_abu_women_address` | A Woman Is Not Man's Equal: She Is a Thousand Times Stronger | from Women & Society |
| `divine_power_every_woman_holds` | The Divine Power Hidden Within Every Woman | from Women & Society |
| `future_lies_in_hands_message_to_women` | The Future Lies in the Hands of Women | from Women & Society |
| `spiritual_power_women_kali_yug` | The Power of Speech and the Mahakali Asleep Within Every Woman | new (was Other) |
| `women_continue_sadhana_during_their_monthly` | Why Your Sadhana Need Not Stop During Your Monthly Cycle | new (was Other) |

### Food & Health (9)

| Talk | Title | Change |
|---|---|---|
| `hardcore_non_vegetarian_awakening` | Eat Yourself First |  |
| `eat_shapes_how_you_think` | Eat the Food of the Land You Were Born In |  |
| `eat_to_heal_not_to_harm_spiritual` | Eat to Heal, Not to Harm |  |
| `physical_mental_strength_spiritual_path` | From Illness to Liberation: The Four Steps of the Spiritual Journey |  |
| `ghee_more_than_food` | Ghee Is More Than Food | new (was Other) |
| `power_of_healing_antar_yog_science` | The Medicine of Faith: When Trust Itself Becomes the Cure |  |
| `water_is_your_first_medicine` | Water Is Your First Medicine |  |
| `non_veg_food_remains_body_truths` | What Is Your Body Built to Eat? |  |
| `diet_hindering_success_link_prosperity` | Your Plate Also Serves Up How You Earned It |  |

### Success & Prosperity (12)

| Talk | Title | Change |
|---|---|---|
| `do_this_one_thing_achieve_successful_life` | Act from Happiness, Not in Search of It |  |
| `secrets_of_becoming_billionaire_marathi` | From Shri Vidya to Prosperity: The Forgotten Secret of Becoming a Billionaire | new (was Other) |
| `gau_seva_antar_yog_purity_prosperity` | Gau Seva: Turning Gratitude into Prosperity |  |
| `sattva_rajas_tamas_balance_success_liberation` | Sattva, Rajas and Tamas: Three Cords That Bind Us and Also Move Us |  |
| `become_billionaire_shree_vidya_secrets` | Shri Vidya: The Ancient Secret of Wealth, Dharma and Liberation |  |
| `manifesting_goals_correctly` | Strong Willpower, Not Mere Wishing, Shapes Your Life |  |
| `true_wealth_money_health_respect_or` | What Is True Wealth? | new (was Other) |
| `knowledge_work_for_you` | Why Can't We Do What Is Right, Even When We Know It? |  |
| `lakshmi_come_some_people_not_others` | Why Does Lakshmi Come to Some People and Not Others? | new (was Other) |
| `struggling_laziness_lack_drive_spiritual` | Why Laziness Won't Leave, and How to Break Free |  |
| `not_wait_until_retirement_transform_life` | Why Wait Until Retirement to Turn Inward? | new (was Other) |
| `unlock_full_potential_in_life` | Why Wait Until Sixty for Spirituality? |  |

### Bharat & Society (6)

| Talk | Title | Change |
|---|---|---|
| `ideal_king_sanatan_rashtra_interview` | A Good King Stops You, and Shows You the Way | from Women & Society |
| `why_society_remains_divided_interview` | One Answer from Hanuman That Could End Casteism | from Women & Society |
| `power_of_collectivity` | The Power of Community and Divine Wealth | from Women & Society |
| `spiritual_meaning_secularism_independence_day_special` | The Spiritual Meaning of Secularism: Show the Fruits of Your Faith | new (was Other) |
| `was_ram_rajya_like_federal_or` | Was Ram Rajya Federal or Unitary? | new (was Other) |
| `future_country_bharat_know` | Who Holds the Future of Bharat? | new (was Other) |

## 6. Live posts that overlap with our talks

When migrating, each pair needs one decision: **keep the live post and redirect ours to it**, **replace the live post with ours and redirect the old URL** (301 redirect, so its search ranking carries over), or **keep both** if they truly answer different questions.

| Live post | Our talk |
|---|---|
| Do Hindus really have 33 koti devatas? Here's the truth behind… | 33_crore_gods_truth_about_hinduism |
| Why multiple forms of God were designed and their deep significance… | power_of_deities_in_your_life, know_your_lord_before_worship |
| Why do people worship symbols or photos? Tracing the origin of idol worship | need_murtis_symbols_understand_god, hidden_meaning_spiritual_symbols |
| Pitru Paksha: Real Secret To Liberate Ancestors & Solve Problems | mrityu_versus_moksha, mahalay_shraddha_matters_truth_about_pitru |
| Ganesh Chaturthi: Celebrate The Festival In The Right Way | hidden_meaning_behind_10_days_ganesh, worship_ganesh_every_year_but_understand |
| Guru Purnima special: Why do you need a Guru? | real_meaning_guru |
| Guru Gyan: Who is a real Guru? | what_is_a_guru, real_meaning_guru |
| Bharat's future and your big role in it | future_country_bharat_know |
| Do saints commit sin if they consume meat? / Settling the debate: Veg v/s Non-Veg | non_veg_food_remains_body_truths, hardcore_non_vegetarian_awakening |
| Did you know that there is a connection between food and your karma? | diet_hindering_success_link_prosperity |
| I Thought I Had Control Over Myself… (Brahmacharya) | truth_about_brahmacharya_exposed_video |
| What Mahakali Taught Me About Bhakti, Fear… | real_role_maha_kali |

This list comes from titles only; a closer check of each pair is needed before migration.

## 7. Decisions needed

1. Approve the 14 categories, or rename, merge or drop some. The smallest are Festivals (4), Death & Liberation (5) and Women & Spirituality (5); these could merge, for example Death & Liberation with Ancestors & Shraddha.
2. Approve the festival rule (section 4), or put every festival-related post under Festivals.
3. Review the per-talk assignments in section 5.
4. Keep "Guru Gyan" as a name on the live site (familiar to readers), or rename it to "Guru & Disciple".
5. Live site: re-categorise the 39 existing posts to the new list now, or at migration time.
6. The overlapping posts in section 6: decide at migration time, but before publishing our versions.
