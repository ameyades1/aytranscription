# FPJ SEO Sync: plan for two fixes

## 1. Alt text on the "Read Also" box images

**Now:** each box image has `alt=""`, so the image is treated as decorative.

**Data available:** all 36 box targets are themselves records in `fpj_to_ay.json`, and every record
has FPJ's `featured_image_alt`. The AY site's own alt texts are only the slug in words (for example
"navratri how to celebrate this festival in its true sense"), so FPJ's are better.

**What FPJ does (checked on 4 live FPJ articles, 11 boxes, 2026-11-25):** the box image's alt is
the linked article's headline, for example alt="Her right education is our bright future".

**Plan (follows FPJ):**
- Plugin `box_html()`: alt = the box's `target_title` (the AY title of the linked post), escaped
  with `esc_attr()`. No JSON change is needed for this.
- Posts already applied with 1.1.0: Restore, then apply again, so the boxes are remade with alt.

## 2. Meta descriptions over 160 characters

**Now:** 14 of 37 records have a `meta_description` over 160 characters (longest 264). The same
14 have the same overlong `og_description` and `twitter_description`.

**Plan:**
- Hand-write a description of 150 to 160 characters for each of the 14, keeping FPJ's wording
  and keywords as far as possible and ending on a complete sentence. No mechanical cutting: a cut
  at 160 often ends in the middle of a question.
- Keep them in a new `description_overrides.json` (slug to description), which
  `build_fpj_to_ay.py` applies to `meta_description`, `og_description` and `twitter_description`.
  That way a rebuild of the JSON keeps them. The build fails if any description is still over 160.
- Plugin, as a safety net:
  - the preview shows each description's length and marks any over 160 in red;
  - on apply, a description over 160 is cut at the last whole word within 157 characters
    and "..." is added, and the report says so.
- Version 1.2.0; rebuild the zip and copy the new `fpj_to_ay.json` to Downloads.

## Order

1. Write the 14 descriptions in `description_overrides.json` (for your review before going on).
2. Update `build_fpj_to_ay.py`, rebuild `fpj_to_ay.json`, check: 0 descriptions over 160.
3. Update the plugin, lint it, and test on the local site with a few posts.
4. Rebuild the zip, copy both files to Downloads, and commit.

## Shortened descriptions

| Post | FPJ description | Used instead |
|---|---|---|
| Navratri: How To Celebrate This Festival In Its True Sense | Have you ever wondered why it is celebrated only for nine nights? Is the Navratri celebration only limited to bringing Durga idols, doing Durga pooja, fasting, playing garba, offering prasad, immersion, etc? (207) | Why is Navratri celebrated for nine nights? Is it only about Durga idols, Durga pooja, fasting, garba and prasad? Learn how to celebrate it in its true sense. (158) |
| Pitru Paksha: Real Secret To Liberate Ancestors & Solve Problems | As per our Vedic scriptures like Garud Puran, Bramha Puran, etc rituals of pind daan, shraddha, tarpan, donation, etc. should be performed to help the souls of your ancestors to attain peace, liberate or move on to their next births (232) | Vedic scriptures like Garud Puran advise pind daan, shraddha, tarpan and donation in Pitru Paksha, to help your ancestors' souls find peace and liberation. (155) |
| Do you know the true purpose of prayer? Understanding the art and science of prayer | Prayer is a ray of hope for people in times of hardship. Regardless of which religion you belong to, prayer is an integral part of your life. When situations seem to go beyond your control, most of you start praying to God. (223) | Prayer is a ray of hope in hard times, whatever your religion. When things seem beyond your control, you pray to God. Learn the art and science of prayer. (154) |
| Bharat’s future and your big role in it | What is the real meaning of spirituality? Is being religious and spiritual the same? Religion i.e. Dharma is any action done repeatedly with a sense of responsibility whereas spirituality is knowing the spirit, the life force, which keeps us alive. (248) | What is the real meaning of spirituality? Are religion and spirituality the same? Dharma is duty done repeatedly; spirituality is knowing the spirit within you. (160) |
| Guru Purnima special: Why do you need a Guru? | It is said that life is a beautiful journey. But many seem to loose the path and do not find the right way. Do you know where you have come from and where you have to go? (170) | Life is a beautiful journey, yet many lose the path and never find the right way. Do you know where you have come from and where you have to go? A Guru does. (157) |
| Key role of parents in the successful marriage of a woman | In ancient times, when a child was born, the parents would first show the child’s kundali (birth chart) to their Guru, who could identify the yog (opportunities), dosh (sins), rin (pending karmic debts), etc (207) | In ancient times, parents first showed a newborn's kundali to their Guru, who could see its yog, dosh and rin. Learn the role of parents in a woman's marriage. (159) |
| Do saints commit sin if they consume meat? | In this series of articles on diet, you must have realised true purpose of your diet and how rajasik/ tamasik foods like meat, deep-fried, junk food, alcohol, etc. not only harm your health but can also hinder your moksha (221) | Rajasik and tamasik foods like meat, junk food and alcohol not only harm your health but can also hinder your moksha. So do saints commit sin if they eat meat? (159) |
| Guru Gyan: Who is a real Guru? | What is your idea of a Guru? Is Guru someone with just a huge number of devotees? Or one who performs miracles? Is he someone wearing coloured robes who gives you a mantra or a gemstone to ease your sufferings in a minute? (222) | What is your idea of a Guru? Someone with huge numbers of devotees, who performs miracles, or gives you a mantra or gemstone to end your suffering? Who is real? (160) |
| Guru Gyan: Do you really love others? Or only your own self? | You all have someone or something in your life that you dearly love. Am I right? It could be your partner, children, parents, car or pet, and the list could be endless. (168) | You all have someone or something you dearly love: a partner, children, parents, a car or a pet. But do you really love others, or only your own self? (150) |
| Guru Gyan: You must read this if you love anyone | Love, the most important virtue in life, is also the most misunderstood one! This is the root cause of problems in most of the relationships today. An entire life passes by without realising the true meaning of love. (216) | Love, the most important virtue in life, is also the most misunderstood. It is the root cause of problems in most relationships today. Learn what love truly is. (160) |
| Guru Gyan: Awaken the giant within you… life lessons from Bhagavad Gita | Bharat is always referred to as the ‘land of Avatars’. Time and again great Avatars have taken birth to uplift the mankind and free it from evil. Even in times ahead, it is popularly believed that in Kaliyug, Kalki, will be born to save humanity and dharma. (257) | Bharat is called the land of Avatars, where Avatars take birth to uplift mankind and free it from evil. Awaken the giant within you with the Bhagavad Gita. (155) |
| Do Hindus really have 33 koti devatas? Here’s the truth behind the belief | Our journey in this series has come to an important turn. In the previous article, we understood the thought process of our saints behind designing the system of many forms of one God, each representing a particular quality or energy of the ultimate formless God. (263) | Our saints designed many forms of one God, each showing a quality or energy of the formless God. So do Hindus really have 33 koti devatas? Here is the truth. (157) |
| Settling the debate: Veg v/s Non-Veg | In this article, I will not tell you what you should or should not eat, but I will definitely reveal the karma rahasya (secrets) and the subtle effects of consuming meat which deeply affect your life (199) | This article does not tell you what to eat, but reveals the karma rahasya (secrets) and the subtle effects of eating meat that deeply affect your life. (151) |
| Guru Gyan: What is the Antar Yog way of life? Here’s all you need to know | What is God? Does God really exist? If there is God, where we can find Him? Does God reside in the temples and the deities that we worship? If such questions have ever crossed your mind, here are some answers for you. (217) | What is God? Does God really exist? If so, where can we find Him: in temples, in the deities we worship? If such questions have crossed your mind, read on. (155) |
