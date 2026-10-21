power_of_collectivity: SEO fix

`check_seo.py` failed before this fix: neither meta description contained the focus keyword ("समाज की शक्ति" / "power of community"). Both blog bodies also lacked it: the original texts use it only in the H1, which does not count. The report had no section 12 checklist, so one was added. Each language gets a short direct answer at the end of the first section, which puts the focus keyword in the first 100 words. Each also gets one H2 rephrased as the question readers search. The focus keywords, titles and slugs stay the same. Only the meta descriptions changed in seo.json.

## Hindi (`power_of_collectivity_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| "जीवन में सबसे पहले क्या आता है?", new third paragraph (after "…अपने आप खुलने लगते हैं।") | (none) | संक्षेप में, समाज की शक्ति यही है: आचार्य उपेंद्र जी के अनुसार जीवन की सभी संपदाओं में समाज सबसे पहले आता है, और धन बाद में अपने आप आता है। समाज वाणी से जुड़ता है, और दैवी संपत्ति विवादों को बातचीत में सुलझाकर सबसे कीमती धन, समय, बचाती है। | The focus keyword was missing from the body, and the post had no early direct answer. This direct answer (about 50 words) is built only from the blog's own sections and the report's section 5. It puts "समाज की शक्ति" in the first 100 words. It repeats no link phrase. |
| Second H2 | ## वाणी: समाज से जुड़ने का पुल | ## समाज से कैसे जुड़ें? वाणी है पुल | Rephrased as the question readers ask (report FAQ 2). The section answers it. The number and order of headings are unchanged. |

## English (`power_of_collectivity_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| "What Comes First in Life?", new third paragraph (after "…open on its own.") | (none) | In short, the power of community works like this: according to Acharya Upendra Ji, community comes first among all of life's riches, and money follows on its own. Speech connects you to people, and daivi sampatti settles disputes in conversation, saving the most precious wealth of all: time. | The focus keyword was missing from the body, and the post had no early direct answer. This direct answer (about 50 words, from the report's section 5) puts "power of community" in the first 100 words. It repeats no link phrase. |
| Second H2 | ## Speech: Your Bridge to Others | ## How Do You Connect with People? Speech Is the Bridge | Rephrased as the question readers ask (report FAQ 2). The section answers it. The number and order of headings are unchanged. |

No teaching, example, H1 or order of ideas changed, and the Markdown is kept. The blog quotes no verses. A check confirms that all four `links` phrases in each language are still in the texts, once each. So is the `also_read` heading ("क्या मेरा विश्व छोटा है या बड़ा?" / "Is My World Small or Large?").

## Checklist

- Now met:
  - Focus keyword in the body text and within the first 100 words, in both languages.
  - Focus keyword in the meta description, in both languages.
- `check_seo.py` now passes; it failed before.
- The report had no section 12. The checklist was added from `tools/prompts/seo_checklist.md` and marked.
- Still unmet (1):
  - Each tag can be shared by at least 3 posts. "Daivi Sampatti" / "दैवी संपत्ति" is not yet a tag in any other post. Tags are outside this fix, so this is left for the editor.
- Left alone on purpose:
  - Report section 4 suggests turning the H2 "दैवी संपत्ति: विवाद जो बातचीत में सुलझ जाएँ" / "Divine Wealth: Disputes That End in Conversation" into "What Is Daivi Sampatti…?". That was not done. The Hindi heading is where `images.txt` places the inline image, so renaming it would break the image's placement. "What is daivi sampatti" is also better left to attain_divine_qualities_empower_spiritual (section 7, cannibalization). The second H2 was rephrased instead.
  - Report section 4 still calls the keyword use and the direct answer optional. This fix may edit only sections 2, 3, 8, 11 and 12.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | जीवन की सब संपदाओं में समाज पहले क्यों आता है? आचार्य उपेंद्र जी बताते हैं कि वाणी समाज को जोड़ती है और दैवी संपत्ति विवादों को बातचीत में सुलझाकर समय बचाती है। | समाज की शक्ति क्या है? आचार्य उपेंद्र जी बताते हैं कि जीवन की संपदाओं में समाज पहले क्यों आता है, वाणी उसे कैसे जोड़ती है और दैवी संपत्ति कैसे समय बचाती है। (156) |
| wordpress.en.meta_description | Why does community come before money? Acharya Upendra Ji explains how speech connects people and how divine wealth settles disputes and saves your time. | What is the power of community? Acharya Upendra Ji explains why community comes before money, how speech connects people and how divine wealth saves time. (154) |
| wordpress.hi.slug | samaj-ki-shakti-daivi-sampatti | samaj-ki-shakti-daivi-sampatti (unchanged; already fits the keyword) |
| wordpress.en.slug | power-of-community-divine-wealth | power-of-community-divine-wealth (unchanged; 32 characters, contains the keyword) |

These fields are unchanged: `focus_keyword` and `secondary_keywords` (the focus keywords were already the searched wording), `title` (both already contain the keyword), `links`, `also_read`, `alt`, `caption`, `related`, category and tags. The report's section 11 holds the same JSON. Section 2 (keyword note), section 3 (metas and slugs marked recommended) and section 8 (schema descriptions, and the suggested slugs added to its placeholder note) were updated to match, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | samaj-ki-shakti-daivi-sampatti | power-of-community-divine-wealth |
| focus_keyword | समाज की शक्ति | power of community |
| title | समाज की शक्ति: दैवी संपत्ति से खुलते हैं सारे रास्ते | The Power of Community: Why Divine Wealth Comes First |
| meta_description | समाज की शक्ति क्या है? आचार्य उपेंद्र जी बताते हैं कि जीवन की संपदाओं में समाज पहले क्यों आता है, वाणी उसे कैसे जोड़ती है और दैवी संपत्ति कैसे समय बचाती है। | What is the power of community? Acharya Upendra Ji explains why community comes before money, how speech connects people and how divine wealth saves time. |
