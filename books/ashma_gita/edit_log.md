# Edit log: final editorial pass

Chapters before this pass are kept unchanged in `chapters_before_edit/`. Every change to `chapters/` is listed below with the exact old and new text, so any single change can be undone by putting the old text back. Chapter files not listed (1, 2, 4, 6, 8, 9, 13, 15, 17, 21, 23, 24, 27, 28, 29, 31, 34) were not changed.

## Summary

- 45 edits in 18 chapter files.
- Boundary duplicates removed: 1 (the Chitraketu preview at the end of ch. 18, kept in ch. 19). The other 34 joins were checked (last and first four paragraphs of every pair, plus an automatic paragraph-overlap check across the whole book) and needed no change.
- Repeated material reduced to a sentence or a pointer: Gita 4.34 in ch. 10; Gita 8.15, shloks 1 to 3, shlok 5 and the frame recap in ch. 12; a forward reference to the eye and stomach diseases in ch. 5. All other repeats in the plan's Repeated material table were already short (one or two sentences) or add a new example, and were left.
- Day and session markers turned into chapter references or removed: 15 places. Kept where the time carries meaning: "पहले दिन की सीख" and "शिविर के दूसरे दिन" (ch. 12), "दो दिन उसी में लगे" (ch. 18, plan section 5), "कल आप जगन्नाथ जी के दर्शन करने जाएँगे" (ch. 2, the pilgrimage), "यह सत्र रिकॉर्ड हो रहा है" (ch. 31).
- Chapter titles: ch. 12 and ch. 30 changed (Arabic and Persian words); book_plan.md updated. All other titles checked: Shuddh Hindi and distinct.
- Material for editorial review (plan section 5): nothing removed or changed. No decisions are marked in the plan.
- Takeaways per Part: not written. The recap rounds (ch. 12 "पहले दिन की सीख", ch. 19 Day 2 round) stay in the chapters, because they are the only place several answers appear; a takeaway list would repeat them.
- Register: chapters were spot-checked at their openings and endings and in the passages edited; two recorded stage directions were removed (ch. 7). No chapter stood out as more spoken or more ornate in the parts read; a full read for register was not done.
- Shared terms checked by search across all chapters: शिविर, ऋणानुबंध, दुःख, तत्त्व, अंतर योग, विश्वगुरु, साढ़ेसाती, गुरुकृपा, श्री विद्या, शान्तिपर्व, मार्कण्डेय and the names were already uniform except for the five spelling edits below. Verse reference lines use `चाणक्यनीति`, as verses_report.md set them; prose keeps चाणक्य नीति.
- Verse format: every `>` verse block now has Sanskrit (bold), meaning, and source line. The remaining one-line `>` blocks are quoted slide sayings, not verses, and are uniform among themselves.

## Changes by chapter

## Chapter 3 (`chapters/03_chapter.txt`)

**1. spelling.** Shared terms: श्री विद्या.

Old text:

```
तो कल श्रीविद्या फलीभूत होकर
```

New text:

```
तो कल श्री विद्या फलीभूत होकर
```

## Chapter 5 (`chapters/05_chapter.txt`)

**2. removal (sentence) + day marker.** In book order the eye and stomach diseases have not been told yet (they come in ch. 7), so the recap sentence pointed forward; "आज" is a session marker.
Kept in full in: Ch. 7, section "आँख का रोग और पेट का रोग" (full version, as the plan's Repeated material table puts it).

Old text:

```
आज थोड़ा अंधकार तो मिटा होगा। सिर्फ़ सहन ही नहीं करना है, इतना तो पहले समझ में आया। आँख की बीमारी और पेट की बीमारी की बात समझी। जीवन में कौन
```

New text:

```
अब तक थोड़ा अंधकार तो मिटा होगा। सिर्फ़ सहन ही नहीं करना है, इतना तो पहले समझ में आया। जीवन में कौन
```

## Chapter 7 (`chapters/07_chapter.txt`)

**3. format (stage direction).** Recording stage direction; no other chapter keeps laughter notes.

Old text:

```
(आचार्य जी हँसते हैं।) अब बताइए
```

New text:

```
अब बताइए
```

**4. format (stage direction).** Recording stage direction; no other chapter keeps laughter notes.

Old text:

```
"पापी पेट का सवाल है।" (आचार्य जी हँसते हैं।) तो पेट
```

New text:

```
"पापी पेट का सवाल है।" तो पेट
```

**5. verse format.** Verse block had only the meaning; every other Gita block in the book gives the Sanskrit first. Sanskrit as in Gita Press.

Old text:

```
> हजारों मनुष्यों में कोई एक
```

New text:

```
> **मनुष्याणां सहस्रेषु कश्चिद्यतति सिद्धये।**
> **यततामपि सिद्धानां कश्चिन्मां वेत्ति तत्त्वतः॥**
> हजारों मनुष्यों में कोई एक
```

## Chapter 10 (`chapters/10_chapter.txt`)

**6. verse reference format.** Only these three source lines carried the Mahabharata adhyaya.verse; all other Ashma Gita blocks give the slide number only. The Shanti Parva location is now stated once in the Note on the text (verses_report.md asks that slide = Gita Press numbering be confirmed before printing).

Old text:

```
(अश्मा गीता, श्लोक १; महाभारत, शान्तिपर्व २८.१)
```

New text:

```
(अश्मा गीता, श्लोक १)
```

**7. verse reference format.** Only these three source lines carried the Mahabharata adhyaya.verse; all other Ashma Gita blocks give the slide number only. The Shanti Parva location is now stated once in the Note on the text (verses_report.md asks that slide = Gita Press numbering be confirmed before printing).

Old text:

```
(अश्मा गीता, श्लोक २; महाभारत, शान्तिपर्व २८.२)
```

New text:

```
(अश्मा गीता, श्लोक २)
```

**8. verse reference format.** Only these three source lines carried the Mahabharata adhyaya.verse; all other Ashma Gita blocks give the slide number only. The Shanti Parva location is now stated once in the Note on the text (verses_report.md asks that slide = Gita Press numbering be confirmed before printing).

Old text:

```
(अश्मा गीता, श्लोक ३; महाभारत, शान्तिपर्व २८.३)
```

New text:

```
(अश्मा गीता, श्लोक ३)
```

**9. repeated material (verse block reduced).** Plan, Repeated material: Gita 4.34 in full in ch. 1; ch. 10 only applies it. The application paragraph that follows (दण्डवत् प्रणाम, सेवा, प्रश्न) is kept.
Kept in full in: Ch. 1, section "तत्त्वदर्शी के पास जाकर ज्ञान" (full verse block).

Old text:

```
प्रश्न कैसे पूछना है, यह भगवद्गीता के चौथे अध्याय के चौंतीसवें श्लोक में बताया गया है।

> **तद्विद्धि प्रणिपातेन परिप्रश्नेन सेवया।**
> **उपदेक्ष्यन्ति ते ज्ञानं ज्ञानिनस्तत्त्वदर्शिनः॥**
> उस ज्ञान को तू तत्त्वदर्शी ज्ञानियों के पास जाकर समझ। उनको भलीभाँति दण्डवत् प्रणाम करने से, उनकी सेवा करने से और कपट छोड़कर सरलतापूर्वक प्रश्न करने से वे परमात्म-तत्त्व को भलीभाँति जानने वाले ज्ञानी महात्मा तुझे उस तत्त्वज्ञान का उपदेश करेंगे।
> (श्रीमद्भगवद्गीता ४.३४)
```

New text:

```
प्रश्न कैसे पूछना है, यह भगवद्गीता के चौथे अध्याय के चौंतीसवें श्लोक (४.३४) में बताया गया है, जिसे अध्याय १ में देखा: तत्त्वदर्शी ज्ञानियों को भलीभाँति दण्डवत् प्रणाम करने से, उनकी सेवा करने से और कपट छोड़कर सरलतापूर्वक प्रश्न करने से वे तुझे तत्त्वज्ञान का उपदेश करेंगे।
```

## Chapter 11 (`chapters/11_chapter.txt`)

**10. verse format.** Shlok 5 is explained here, but its Sanskrit stood only in ch. 12 (the Day 2 re-reading). Moved the full block (Sanskrit and meaning exactly as in ch. 12) to the chapter that explains the shlok.
Kept in full in: The ch. 12 block is reduced to one sentence (see ch. 12).

Old text:

```
> राजन्! मनुष्य का यह शरीर जब जन्म लेता है, तब उसके साथ ही सुख और दुःख भी उसके पीछे लग जाते हैं।
> (अश्मा गीता, श्लोक ५)
```

New text:

```
> **उत्पन्नमिममात्मानं नरस्यानन्तरं ततः।**
> **तानि तान्यनुवर्तन्ते दुःखानि च सुखानि च॥**
> राजन्! मनुष्य का यह शरीर जब जन्म ग्रहण करता है, तब उसके साथ ही सुख और दुःख भी उसके पीछे लग जाते हैं।
> (अश्मा गीता, श्लोक ५)
```

**11. cross-reference added.** Plan: the four dukh are told in full in ch. 2; this section adds the slide commentary and new examples, so it stays, with a pointer back.
Kept in full in: Ch. 2, section "पतञ्जलि ऋषि के बताए चार दुःख".

Old text:

```
इसी सूत्र के चार प्रकार के दुःखों को ऋषि की व्याख्या के साथ संक्षेप में देखते हैं।
```

New text:

```
इसी सूत्र के चार प्रकार के दुःखों को, जिन्हें अध्याय २ में उदाहरणों से देखा, अब ऋषि की व्याख्या के साथ संक्षेप में देखते हैं।
```

## Chapter 12 (`chapters/12_chapter.txt`)

**12. title.** "हवा" is an Arabic loanword; title must be Shuddh Hindi. "पवन" keeps the image of shlok 6 (अनिल). book_plan.md updated.

Old text:

```
# अध्याय १२: हवा और बादल
```

New text:

```
# अध्याय १२: पवन और बादल
```

**13. spelling.** The book spells संबंध (51 times); only ch. 12 used सम्बन्ध. Verse meanings (Gita Press) left as they are.

Old text:

```
## सम्बन्धों की प्रकृति
```

New text:

```
## संबंधों की प्रकृति
```

**14. spelling.** The book spells संबंध (51 times); only ch. 12 used सम्बन्ध. Verse meanings (Gita Press) left as they are.

Old text:

```
हम अपने सम्बन्धों में देखते हैं
```

New text:

```
हम अपने संबंधों में देखते हैं
```

**15. spelling.** The book spells संबंध (51 times); only ch. 12 used सम्बन्ध. Verse meanings (Gita Press) left as they are.

Old text:

```
हर सम्बन्ध कभी
```

New text:

```
हर संबंध कभी
```

**16. spelling.** The book spells संबंध (51 times); only ch. 12 used सम्बन्ध. Verse meanings (Gita Press) left as they are.

Old text:

```
जिस सम्बन्ध से
```

New text:

```
जिस संबंध से
```

**17. spelling.** The book spells संबंध (51 times); only ch. 12 used सम्बन्ध. Verse meanings (Gita Press) left as they are.

Old text:

```
अब सम्बन्ध स्थायी
```

New text:

```
अब संबंध स्थायी
```

**18. repeated material (verse block reduced).** Shlok 5 is explained in ch. 11; the full block now stands there.
Kept in full in: Ch. 11, section "जनक का प्रश्न" (full block, moved there).

Old text:

```
छठा श्लोक समझने के लिए पहले यह याद कर लें कि पाँचवें श्लोक में क्या कहा गया था।

> **उत्पन्नमिममात्मानं नरस्यानन्तरं ततः।**
> **तानि तान्यनुवर्तन्ते दुःखानि च सुखानि च॥**
> अश्मा ने कहा: राजन्! मनुष्य का यह शरीर जब जन्म ग्रहण करता है, तब उसके साथ ही सुख और दुःख भी उसके पीछे लग जाते हैं।
> (अश्मा गीता, श्लोक ५)
```

New text:

```
छठा श्लोक समझने के लिए पहले यह याद कर लें कि पाँचवें श्लोक में क्या कहा गया था, जिसे पिछले अध्याय में देखा: मनुष्य का यह शरीर जब जन्म ग्रहण करता है, तब उसके साथ ही सुख और दुःख भी उसके पीछे लग जाते हैं।
```

**19. repeated material (verse block reduced).** Plan, Repeated material: Gita 8.15 in full in ch. 2.
Kept in full in: Ch. 2, section "संसार दुःखालय है" (full verse block).

Old text:

```
इसके बाद श्रीमद्भगवद्गीता का वह श्लोक आया, जिसे हम पहले देख चुके हैं:

> **मामुपेत्य पुनर्जन्म दुःखालयमशाश्वतम्।**
> **नाप्नुवन्ति महात्मानः संसिद्धिं परमां गताः॥**
> परम सिद्धि को प्राप्त महात्माजन मुझे प्राप्त होकर दुःखों के घर एवं क्षणभंगुर पुनर्जन्म को नहीं प्राप्त होते।
> (श्रीमद्भगवद्गीता ८.१५)
```

New text:

```
इसके बाद श्रीमद्भगवद्गीता का वह श्लोक (८.१५) आया, जिसे हम अध्याय २ में देख चुके हैं: परम सिद्धि को प्राप्त महात्माजन भगवान को प्राप्त होकर दुःखों के घर एवं क्षणभंगुर पुनर्जन्म को नहीं प्राप्त होते।
```

**20. day marker.** Greeting removed; the day is kept because it marks where the Shibir turns from the भूमिका to the re-reading (time reference carries meaning).

Old text:

```
दूसरे दिन "नमस्कार!" के साथ अश्मा गीता पर लौटते हुए
```

New text:

```
शिविर के दूसरे दिन अश्मा गीता पर लौटते हुए
```

**21. day marker.** "कल" made into a text reference.

Old text:

```
कल श्लोक में यह कहा गया था
```

New text:

```
छठे श्लोक में यह कहा गया था
```

**22. repeated material (reduced).** Plan, Repeated material: the frame is told in full in ch. 5; four sentences made one.
Kept in full in: Ch. 5, sections "वैशम्पायन और जनमेजय" to "युधिष्ठिर: धर्मयुद्ध में स्थिर".

Old text:

```
कथा का क्रम भी याद रखिए। सबसे पहले वैशम्पायन ऋषि जनमेजय को महाभारत सुना रहे थे। उसमें शान्तिपर्व का एक प्रसंग आया, जब युद्ध हो चुका है और युधिष्ठिर दुःख में हैं। उन्हें व्यास जी ने समझाया, और समझाते हुए वह कथा सुनाई जो अश्मा ऋषि ने राजा जनक से कही थी; उसमें "अश्मा उवाच" आता है।
```

New text:

```
कथा का क्रम भी याद रखिए, जिसे अध्याय ५ में विस्तार से देखा: वैशम्पायन ऋषि जनमेजय को महाभारत सुना रहे हैं, और उसके शान्तिपर्व में व्यास जी दुःखी युधिष्ठिर को वह कथा सुनाते हैं जो अश्मा ऋषि ने राजा जनक से कही थी; उसमें "अश्मा उवाच" आता है।
```

**23. day marker.** "कल" removed.

Old text:

```
क्योंकि यह एक ही अध्याय है और कल हम छठे श्लोक तक आए थे।
```

New text:

```
क्योंकि यह एक ही अध्याय है और अब तक हम छठे श्लोक तक आ चुके हैं।
```

**24. repeated material (verse blocks reduced).** Shloks 1 to 3 were printed in full a second time; they are explained in ch. 10. One linking sentence made from the ch. 10 meanings. The shlok 4 block is kept here: it is the only place its Sanskrit appears.
Kept in full in: Ch. 10, sections "व्यास जी: सामने बैठे जीवित गुरु" onward (full blocks of shloks 1, 2, 3).

Old text:

```
> **ज्ञातिशोकाभितप्तस्य प्राणानभ्युत्सिसृक्षतः।**
> **ज्येष्ठस्य पाण्डुपुत्रस्य व्यासः शोकमपानुदत्॥**
> वैशम्पायन जी कहते हैं: जनमेजय! भाई-बंधुओं के शोक से संतप्त हो अपने प्राणों को त्याग देने की इच्छा करने वाले ज्येष्ठ पाण्डव युधिष्ठिर के शोक को महर्षि व्यास ने इस प्रकार दूर किया।
> (अश्मा गीता, श्लोक १)

> **अत्राप्युदाहरन्तीममितिहासं पुरातनम्।**
> **अश्मगीतं नरव्याघ्र तन्निबोध युधिष्ठिर॥**
> व्यास जी बोले: पुरुषसिंह युधिष्ठिर! इस प्रसंग में जानकार लोग अश्मा ब्राह्मण के गीत सम्बन्धी इस प्राचीन इतिहास का उदाहरण दिया करते हैं, इसे सुनो।
> (अश्मा गीता, श्लोक २)

> **अश्मानं ब्राह्मणं प्राज्ञं वैदेहो जनको नृपः।**
> **संशयं परिपप्रच्छ दुःखशोकसमन्वितः॥**
> एक समय की बात है, दुःख-शोक में डूबे हुए विदेहराज जनक ने ज्ञानी ब्राह्मण अश्मा से अपने मन का संदेह इस प्रकार पूछा।
> (अश्मा गीता, श्लोक ३)
```

New text:

```
पहले तीन श्लोक कथा का ढाँचा बताते हैं, जिन्हें अध्याय १० में देखा: वैशम्पायन जी जनमेजय को बताते हैं कि व्यास जी ने युधिष्ठिर का शोक कैसे दूर किया; व्यास जी युधिष्ठिर को अश्मा ब्राह्मण के गीत का प्राचीन इतिहास सुनाते हैं; और दुःख-शोक में डूबे विदेहराज जनक अश्मा से अपना संदेह पूछते हैं। चौथे श्लोक में वह प्रश्न है:
```

## Chapter 14 (`chapters/14_chapter.txt`)

**25. spelling.** The book spells प्रायश्चित्त everywhere else.

Old text:

```
बाद में प्रायश्चित कर लूँगा
```

New text:

```
बाद में प्रायश्चित्त कर लूँगा
```

## Chapter 16 (`chapters/16_chapter.txt`)

**26. day marker.** "कल" removed.

Old text:

```
उसी आशीर्वाद का फल यह ज्ञानसत्र है, यह भी हमने कल सीखा था।
```

New text:

```
उसी आशीर्वाद का फल यह ज्ञानसत्र है, यह भी हमने पहले सीखा था।
```

**27. day marker.** "कल" made into a chapter reference (the story is in ch. 2).

Old text:

```
इन दोनों में यही अंतर है; यह हमने कल ही देखा था।
```

New text:

```
इन दोनों में यही अंतर है; यह हमने अध्याय २ में देखा था।
```

## Chapter 18 (`chapters/18_chapter.txt`)

**28. boundary duplicate (removed).** The Chitraketu preview is told again, in the same words, in the first two paragraphs of ch. 19, which the plan makes the Chitraketu chapter (ch. 18's source ends before «ये कथा भागवत महापुराण की»). No linking sentence needed: the next section starts with its own heading.
Kept in full in: Ch. 19, section "एक कथा में अनेक श्लोक", paragraphs 1 and 2 (every point: shloks up to 35/38, one story, Bhagavata, the child who dies at birth, joy and sorrow together, up to shlok 48 in fifteen minutes).

Old text:

```
कल के जो श्लोक हैं, पैंतीसवें या अड़तीसवें श्लोक तक, वे सब एक ही कथा पर आधारित हैं। यदि वह कथा समझ में आ गई, तो वे श्लोक जल्दी पूरे होंगे, अन्यथा पहले सिखाने में बहुत समय जाएगा। यह कथा भागवत महापुराण की है, चित्रकेतु की। उसमें बालक जन्म लेकर तुरंत मर जाता है, और माता-पिता को सुख और दुःख एक साथ आते हैं। उसे देख लेना; अड़तालीसवें श्लोक तक की सारी व्याख्या उन पंद्रह मिनटों में हो जाएगी।
```

New text:

```
(removed)
```

**29. session marker.** Session greeting.

Old text:

```
नमस्कार! अब फिर ज्ञानगंगा में डुबकी लगाते हैं।
```

New text:

```
अब फिर ज्ञानगंगा में डुबकी लगाते हैं।
```

**30. continuity.** In book order the film (the Chitraketu story) comes in the next chapter, so "we have already seen the film" read wrongly. Rewritten only from what ch. 19 says.

Old text:

```
क्योंकि हम चलचित्र भी देख चुके हैं और वे काफ़ी हद तक स्वयं स्पष्ट हैं।
```

New text:

```
क्योंकि उनमें से बहुत से श्लोक चित्रकेतु की कथा (अगला अध्याय) पर आधारित हैं और वे काफ़ी हद तक स्वयं स्पष्ट हैं।
```

**31. day marker.** "आज" removed. "दो दिन उसी में लगे" and "दो दिनों में मुख्य बातें सब सिखा दी गई हैं" kept: the plan lists the latter for editorial review.

Old text:

```
इसलिए आज ज़्यादा कुछ सिखाना नहीं है;
```

New text:

```
इसलिए अब ज़्यादा कुछ सिखाना नहीं है;
```

**32. day marker.** "कल" removed.

Old text:

```
यह हमने कल सुना था, क्योंकि
```

New text:

```
यह हमने पहले सुना था, क्योंकि
```

## Chapter 19 (`chapters/19_chapter.txt`)

**33. day marker.** Turned into a chapter reference (two logs, ch. 29).

Old text:

```
यह विस्तार से अगले दिन बताया जाएगा।
```

New text:

```
यह विस्तार से आगे अध्याय २९ में आएगा।
```

**34. day marker.** "अगले दिन" made a book reference.

Old text:

```
इसी कथा पर आधारित पंद्रह-बीस श्लोक अगले दिन तीव्र गति से पूरे किए जाएँगे।
```

New text:

```
इसी कथा पर आधारित पंद्रह-बीस श्लोक आगे के अध्यायों में तीव्र गति से पूरे होंगे।
```

**35. spelling.** Shared terms: दुःख always with visarga.

Old text:

```
अति दुखी को
```

New text:

```
अति दुःखी को
```

## Chapter 20 (`chapters/20_chapter.txt`)

**36. correction (frame).** Ashma speaks to Janaka; Yudhishthira hears it from Vyasa (book_plan.md header, ch. 5). Slip in the chapter text.

Old text:

```
अश्मा ऋषि सत्रहवें श्लोक में राजा युधिष्ठिर से कहते हैं कि हे नरेश्वर
```

New text:

```
अश्मा ऋषि सत्रहवें श्लोक में राजा जनक से कहते हैं कि हे नरेश्वर
```

## Chapter 22 (`chapters/22_chapter.txt`)

**37. spelling.** Ch. 28 spells पंचमहाभूत (twice); one form for the book.

Old text:

```
ये पंच महाभूत हैं
```

New text:

```
ये पंचमहाभूत हैं
```

## Chapter 25 (`chapters/25_chapter.txt`)

**38. session marker.** "एक सत्र में" removed; the shlok is explained earlier in the same chapter.

Old text:

```
पच्चीसवें श्लोक पर हमने एक सत्र में देखा कि
```

New text:

```
पच्चीसवें श्लोक पर हमने देखा कि
```

## Chapter 26 (`chapters/26_chapter.txt`)

**39. verse format.** Meaning-only block; Sanskrit supplied as in Gita Press, as for every other Gita block.

Old text:

```
> कर्म क्या है और अकर्म
```

New text:

```
> **किं कर्म किमकर्मेति कवयोऽप्यत्र मोहिताः।**
> **तत्ते कर्म प्रवक्ष्यामि यज्ज्ञात्वा मोक्ष्यसेऽशुभात्॥**
> कर्म क्या है और अकर्म
```

## Chapter 30 (`chapters/30_chapter.txt`)

**40. title.** "राहगीर" is Persian (राह + गीर); "पथिक" is the shlok's own image ("प्रारब्धजन्य पथिक"). book_plan.md updated. The speaker's "राहगीर" in the text is left as it is.

Old text:

```
# अध्याय ३०: काल की समदृष्टि और राहगीरों का साथ
```

New text:

```
# अध्याय ३०: काल की समदृष्टि और पथिकों का साथ
```

**41. day marker.** "कल" made into a chapter reference (Chitraketu, ch. 19).

Old text:

```
कल हमने मिश्रित सुख-दुःख की वह कथा सुनी थी
```

New text:

```
अध्याय १९ में हमने मिश्रित सुख-दुःख की वह कथा सुनी थी
```

**42. verse format.** Meaning-only block; Sanskrit supplied as in Gita Press.

Old text:

```
> श्रीभगवान बोले: हे अर्जुन! तू न शोक
```

New text:

```
> **अशोच्यानन्वशोचस्त्वं प्रज्ञावादांश्च भाषसे।**
> **गतासूनगतासूंश्च नानुशोचन्ति पण्डिताः॥**
> श्रीभगवान बोले: हे अर्जुन! तू न शोक
```

## Chapter 32 (`chapters/32_chapter.txt`)

**43. spelling.** One spelling of संबंध in prose.

Old text:

```
शरीर, नाते-सम्बन्ध, सुख-सम्पत्ति
```

New text:

```
शरीर, नाते-संबंध, सुख-सम्पत्ति
```

## Chapter 33 (`chapters/33_chapter.txt`)

**44. spelling.** Shared terms: गुरुकृपा is one word.

Old text:

```
गुरु कृपा इतनी बढ़ेगी
```

New text:

```
गुरुकृपा इतनी बढ़ेगी
```

## Chapter 35 (`chapters/35_chapter.txt`)

**45. day marker.** "पहले दिन" made into a chapter reference.

Old text:

```
कुरु का अर्थ है करना, यह पहले दिन बताया था।
```

New text:

```
कुरु का अर्थ है करना, यह अध्याय ३ में बताया था।
```

## Other files

- `book_plan.md`: chapter table titles for ch. 12 (हवा और बादल → पवन और बादल) and ch. 30 (काल की समदृष्टि और राहगीरों का साथ → काल की समदृष्टि और पथिकों का साथ). `reports/book_report.md` and `reports/chapters.json` still show the old titles until the report is regenerated.
- `front_matter.txt` (new): title and subtitle, placeholders `[समर्पण]`, `[आभार]`, `[लेखक परिचय]`, भूमिका (about 990 words), पाठ के विषय में (about 200 words), and the five Part title pages. Written only from the chapters and the plan header. The note does not give the Gita Press adhyaya number (28 in the plan) as fact; verses_report.md asks for the numbering to be checked against the printed edition first.
- `back_matter.txt` (new): शब्दावली (81 terms, Devanagari order, meaning as explained in the book, chapter numbers) and श्लोक-सूची (all 59 Ashma Gita shloks and the पुष्पिका in number order, then Bhagavad Gita, Chanakya Niti, Bhaj Govindam, Vivekachudamani, Brihadaranyaka and other sayings). For shloks the book gives only in meaning, the index gives the opening words of the meaning, marked "(अर्थ)".

## Left for the human editor

- The items in plan section 5 (none touched).
- verses_report.md "need a human check" items, including shloks 14, 15 and 23 (Sanskrit supplied, not recited), shlok 21 (fragments only) and the Chanakya Niti numbering.
- Ch. 18 keeps the Day 3 restart (plan: D3P05 late) after the shlok 16 material, so it now comes before the Chitraketu chapter it refers to; one sentence was adjusted (edit in ch. 18 above), but the order itself follows the plan.
- Ch. 12 sits in Part 2 but includes the opening of Day 2; the plan puts it there, and it was not moved.
