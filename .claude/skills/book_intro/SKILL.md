---
name: book_intro
description: Make the designed opening pages of a Hindi book in books/<book>/intro/ (title page with the Antar Yog logo, imprint, photo pages of Acharya Ji, Guruma Neeta Tai and Roopa Tai, their profiles, and the Antar Yog Foundation page), modelled on the Foundation's printed Gita booklets. The /book pdf step then puts them in front of the book, in the PDF and the EPUB.
argument-hint: <book> [reference pages folder] [cover image]
---

# Book intro pages

Book: the first word of `$ARGUMENTS` (`books/<book>/`). The rest, if given: a folder of photos of
the opening pages of an earlier Foundation book (the model), and the book's cover image.

Output, all in `books/<book>/intro/`:
- `intro_pages.html`: the pages, one `<section class="page">` each, with their CSS in one `<style>`.
- the images it uses, next to it, referred to by bare file name (`logo.png`, `acharya_ji.jpg`, ...).
- `intro_pages.pdf`: a preview, printed from the HTML.

`tools/book/build_pdf.py` picks up `intro/intro_pages.html` by itself: its pages replace the plain
cover, keep their own styles and margins (its `@page` rules become a named page), and its images go
into the PDF and the EPUB. Do not edit `build_pdf.py` or the `/book` skill for this.

## Pages (in this order)

1. **Title page**, inside one thin border: `॥ ॐ श्री गुरवे नमः ॥`, the Antar Yog logo, the book title,
   the subtitle, then a verse between two short rules with its source line.
   - Title and subtitle: from the cover. Add the Shibir line from `book.json` if there is one.
   - Leave out "(हिंदी अनुवाद सहित)" if the book is Acharya Ji's discourses rather than a translation.
   - The verse: a short, central shlok of the book's main text, taken from the book's own verse
     blocks (which follow Gita Press), never from memory.
2. **Imprint:** "अंतर योग <book title>", "(आचार्य उपेंद्र जी के प्रवचन)", "सभी अधिकार अंतर योग फाउंडेशन®
   के स्वाधीन", मूल्य (left blank), the publisher block, and "प्रथम संस्करण : [माह वर्ष]". Copy the
   publisher block (address, helpline, email, website) exactly from the model book's imprint.
3. **Acharya Ji's photo page:** the portrait, then his name and the caption from the model.
4. **Guruma Neeta Tai and Roopa Tai:** the heading, two portraits side by side, names and captions.
5. **Profiles:** Acharya Ji, then Guruma Neeta Tai, then Roopa Tai, each starting on a new page.
6. **Antar Yog Foundation:** the motto, the two short paragraphs, the four-yogas image, the closing line.

## Texts

- The captions, profiles and Foundation page are the Foundation's own standard texts. Transcribe
  them from the model book word for word. Change nothing else, and add nothing, apart from these
  approved corrections of the booklet's slips: सद्गुरू → सद्गुरु, स्त्रोत → स्रोत, निभाति → निभाती,
  तरंगे → तरंगें; the nukta in हज़ारों, ज़िम्मेदारी, मज़बूत; "कहा है वहीं आचार्य उपेंद्र जी का भी उपदेश" →
  वही; "रुचि दिखाई हैं" → है; the dash after "नीता ताई" → a comma; "बन गया है··· बन रहा है" (an edit
  left half done) → "बन रहा है". Keep "कहा हैं कि" and "उपाधियां" as printed. No em dashes.
- The one adaptation: the last sentence of Acharya Ji's profile names the model book's Gita ("गुरु
  गीता भी इन्हीं गीताओं में से एक है"); put this book's Gita there.
- Where a photo cuts off a line end, complete the word from context and list it in your report, so
  someone can check it against the printed booklet.
- Do not check or soften the claims in these texts; they are the Foundation's. Do not invent a
  समर्पण, आभार or any other text.
- **Check the transcription** before reporting: cut each photo into a top and a bottom half at full
  resolution, read them again and compare word by word with the HTML, punctuation included. Write
  every difference from the booklet (the adaptations, the corrections above, anything else) to
  `intro/text_differences.md` as a table, booklet next to intro, for the Foundation's approval.

## Images

- **Model pages from an iPhone (`.heic`):** convert them to JPEG first (Pillow with `pillow-heif`,
  installed into the session scratchpad), then read each page.
- **Logo:** use the original Hindi logo file if the user has one. Otherwise crop it from the cover and
  blend the cover's background colour to white. Report that this copy is too low-resolution for print.
- **Photos:** look on https://antaryogfoundation.in/ first. The founder portrait is in the home page's
  founder section (`images/Home/02-founder/..._Acharya+Ji-s+Photo.jpg`, about 3000 px, print quality).
  Keep a copy scaled to about 1600 px wide. Download into a new folder in the scratchpad and copy into
  `intro/` only the images used.
- **Rupa Tai:** https://vasturupantaran.antaryogfoundation.in/ has her portrait
  (`logo/..._Rupa+tai.png`, "Rupa Tai CEO | Lead Interior Designer"); it is only 331 × 397 px, so
  report that it is too small for print.
- **Neeta Tai** and the **four-yogas image** are on no website (antaryogfoundation.in has only
  activity photos of her). Ask the user for photos of them from the printed booklet:
  - a photographed portrait: crop away the paper border, scale to about 1000 px wide;
  - the four-yogas line drawing: crop it, convert to grey, divide by a heavy blur (radius about 35)
    to even out the lighting, then stretch the levels (ratio 0.55 → black, 0.95 → white, gamma about
    1.8) and apply a 3 px median filter. That turns the paper white and drops the print showing through
    from the reverse page, while keeping the thin outlines.
- Until an image is there, use a dashed placeholder box with a label (`[ गुरुमाँ नीता ताई का चित्र ]`).
  Do not crop people out of crowd photos. Ask the Foundation for the original files before print.

## Layout

- A5, `@page { size: A5; margin: 16mm 14mm 18mm 14mm; @bottom-center { content: counter(page); } }`,
  no number on the first page; the same font as the book (Noto Serif Devanagari), 11 pt, line height
  about 1.6. Use the book's page-number digits (`counter(page)`), so the numbering matches.
- Give every page `padding-top: 3mm`: Devanagari vowel signs rise above the first line, and without
  it Chrome draws them at the foot of the previous page.
- Keep each closing ornament with the paragraph before it (`break-before: avoid`); keep the title
  page's bordered box short enough for the page (about 168 mm high), with a single thin border.
- Size photos with `img.photo-... { display: block; object-fit: cover; }` on the `img` only, so the
  placeholder boxes keep their centred labels.
- Print the preview with headless Chrome, as `build_pdf.py` does, then render every page to an image
  and look at it: no blank page, no ornament alone on a page, nothing spilling into the next page, the
  border whole.

## Then

Run `tools/book/book.sh <book> pdf` and check the book's first pages the same way: the intro, then the
contents (विषय-सूची). If the front matter has its own title section or an empty लेखक परिचय, the intro
replaces them: say so and offer to remove them (keep a backup of `front_matter.txt`).

## Report

The pages made, what each image is and where it came from (and which are too low-resolution for
print), the placeholders still waiting for images, the completed line ends to check, the differences
file, and the open items: edition date, price, and the Foundation's approval of the texts.
