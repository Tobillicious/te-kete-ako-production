# 📊 CURRICULUM V3 - DATA EXTRACTION NOTES

**Date:** October 29, 2025  
**Source:** English Phase 4 (Years 9-10) | Te Mātaiaho  
**URL:** https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---english-phase-4-years-9-10/5637291578.p

---

## 🏗️ **STRUCTURE DISCOVERED**

### Complete Hierarchy (Te Mātaiaho English Phase 4):

```
NZC English Phase 4 (Years 9-10)
│
├─ Text Studies (STRAND)
│   │
│   ├─ Textual and Critical Analysis (ELEMENT)
│   │   ├─ Features of text
│   │   │   ├─ Knowledge (bullets - same for Y9 & Y10)
│   │   │   ├─ Practices - Year 9 (bullets)
│   │   │   └─ Practices - Year 10 (bullets)
│   │   │
│   │   ├─ Context and purpose
│   │   │   ├─ Knowledge (bullets)
│   │   │   ├─ Practices - Year 9
│   │   │   └─ Practices - Year 10
│   │   │
│   │   ├─ Interpretations and connections
│   │   │   ├─ Knowledge
│   │   │   ├─ Practices - Year 9
│   │   │   └─ Practices - Year 10
│   │   │
│   │   └─ Response to texts
│   │       ├─ Knowledge
│   │       ├─ Practices - Year 9
│   │       └─ Practices - Year 10
│   │
│   └─ (More elements TBD)
│
├─ Language Studies (STRAND)
│   │
│   ├─ Crafting Texts (ELEMENT)
│   │   ├─ Audience and purpose
│   │   │   ├─ Knowledge
│   │   │   ├─ Practices - Year 9
│   │   │   └─ Practices - Year 10
│   │   │
│   │   ├─ Ideas and content
│   │   ├─ Structure
│   │   ├─ Language
│   │   └─ (More sub-elements)
│   │
│   └─ Oral Communication (ELEMENT)
│       └─ (Sub-elements TBD)
│
└─ Teaching Sequences
    ├─ Year 9 Sequence 1
    ├─ Year 9 Sequence 2
    ├─ Year 10 Sequence 1
    └─ Year 10 Sequence 2
```

---

## 📝 **CONTENT EXTRACTION EXAMPLES**

### Example 1: Knowledge Statement (Textual Analysis - Features of text)

**Verbatim from Tahurangi:**
- "Text forms and genres are selected and adapted by authors to achieve specific purposes."
- "Tropes are recurring features of text — such as storytelling patterns (e.g. the hero's journey, rags-to-riches), character types (e.g. the wise mentor, the chosen one), or plot devices (e.g. a mysterious prophecy, mistaken identity) — that authors use to shape meaning and guide audience expectations."
- "Characterisation, plot, setting, ideas, narrative perspective, trope, language, style, and structure are key tools authors use to shape meaning."
- "Features of text can be examined individually and together to support interpretation of meaning, reveal underlying themes, and allow connections with the text to emerge."
- "Media and digital media texts use deliberate language, structure, and multimodal features to establish credibility and influence how audiences respond to, interpret, and share information."

### Example 2: Practice Statement (Year 9 - Features of text)

**Verbatim:**
"Examining features of text across a range of forms, including:
- **in the novel**, explaining how features of text — such as characterisation, plot development, setting, trope, and narrative perspective — work together to shape meaning and create effects
- **in poetry**, explaining how features of text — such as rhythm, figurative language, lineation, sound devices, and imagery — work together to shape meaning and create effects
- **in the short story**, explaining how features of text — such as characterisation, pacing, setting, compressed plot structure, and narrative perspective — work together to shape meaning and create effects
- **in drama**, explaining how features of text — such as dialogue, stage directions, tension, dramatic irony, and conflict — work together to shape meaning and create effects
- **in film**, explaining how features of text — such as narrative progression, cinematography, lighting and sound design, dialogue, and visual storytelling — work together to shape meaning and create effects
- **in non-fiction**, explaining how features of text — such as perspective, tone and register, use of evidence, domain-specific vocabulary, and structure — work together to shape meaning and create effects
- **in oral presentations**, explaining how features of text — such as emotive or persuasive language, tone, structure, gesture, and diction — work together to shape meaning and create effects
- **in visual images**, explaining how features of text — such as composition, framing, colour, message, and symbolism — work together to shape meaning and create effects
- **in media and digital texts**, explaining how features — such as tone, visuals, structure, narrative framing, and clickbait — work together to shape meaning, influence perception, and position audiences

Comparing how features are used across different forms and genres to shape meaning and influence audience response

Evaluating how effectively features are used to communicate ideas, guide audience expectations, and create effects"

---

## 🎨 **FORMATTING OBSERVATIONS**

### What's Consistent:
- Knowledge = bullet lists (5-8 statements per sub-element)
- Practices = bullet lists (3-5 statements per year)
- Year 9 practices are foundation
- Year 10 practices build on Year 9
- Sub-elements have clear titles (e.g. "Features of text", "Context and purpose")

### Formatting to Preserve:
- Em dashes (—) not hyphens (-)
- Bold text for emphasis (**in the novel**)
- Parenthetical examples: (e.g. ...)
- Nested bullet structure
- Quote marks: "..." not '...'

### Special Characters Found:
- ā, ē, ī, ō, ū (macrons - CRITICAL)
- — (em dash)
- ' (apostrophe in "author's")
- " " (curly quotes)

---

## 💾 **PROPOSED JSON SCHEMA**

```json
{
  "metadata": {
    "curriculum": "te_mataiaho",
    "version": "2025_draft",
    "learning_area": "english",
    "phase": 4,
    "years": [9, 10],
    "effective_date": "2026-01-01",
    "status": "draft",
    "consultation_deadline": "2026-04-24",
    "source_url": "https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---english-phase-4-years-9-10/5637291578.p",
    "extracted_date": "2025-10-29",
    "extracted_by": "Te Kete Ako - Kaitiaki Aronui V3.0",
    "verification_status": "pending_user_review"
  },
  
  "strands": [
    {
      "id": "text-studies",
      "name": "Text Studies",
      "description": "Builds on Reading strand from Years 0-8",
      "sort_order": 1,
      
      "elements": [
        {
          "id": "textual-critical-analysis",
          "name": "Textual and Critical Analysis",
          "description": "Deepens skills developed in Reading",
          "sort_order": 1,
          
          "sub_elements": [
            {
              "id": "features-of-text",
              "name": "Features of text",
              "sort_order": 1,
              
              "knowledge": {
                "statements": [
                  "Text forms and genres are selected and adapted by authors to achieve specific purposes.",
                  "Tropes are recurring features of text — such as storytelling patterns (e.g. the hero's journey, rags-to-riches), character types (e.g. the wise mentor, the chosen one), or plot devices (e.g. a mysterious prophecy, mistaken identity) — that authors use to shape meaning and guide audience expectations.",
                  "Characterisation, plot, setting, ideas, narrative perspective, trope, language, style, and structure are key tools authors use to shape meaning.",
                  "Features of text can be examined individually and together to support interpretation of meaning, reveal underlying themes, and allow connections with the text to emerge.",
                  "Media and digital media texts use deliberate language, structure, and multimodal features to establish credibility and influence how audiences respond to, interpret, and share information."
                ]
              },
              
              "practices": {
                "year_9": [
                  {
                    "statement": "Examining features of text across a range of forms, including:",
                    "details": [
                      "**in the novel**, explaining how features of text — such as characterisation, plot development, setting, trope, and narrative perspective — work together to shape meaning and create effects",
                      "**in poetry**, explaining how features of text — such as rhythm, figurative language, lineation, sound devices, and imagery — work together to shape meaning and create effects",
                      "**in the short story**, explaining how features of text — such as characterisation, pacing, setting, compressed plot structure, and narrative perspective — work together to shape meaning and create effects",
                      "**in drama**, explaining how features of text — such as dialogue, stage directions, tension, dramatic irony, and conflict — work together to shape meaning and create effects",
                      "**in film**, explaining how features of text — such as narrative progression, cinematography, lighting and sound design, dialogue, and visual storytelling — work together to shape meaning and create effects",
                      "**in non-fiction**, explaining how features of text — such as perspective, tone and register, use of evidence, domain-specific vocabulary, and structure — work together to shape meaning and create effects",
                      "**in oral presentations**, explaining how features of text — such as emotive or persuasive language, tone, structure, gesture, and diction — work together to shape meaning and create effects",
                      "**in visual images**, explaining how features of text — such as composition, framing, colour, message, and symbolism — work together to shape meaning and create effects",
                      "**in media and digital texts**, explaining how features — such as tone, visuals, structure, narrative framing, and clickbait — work together to shape meaning, influence perception, and position audiences"
                    ]
                  },
                  "Comparing how features are used across different forms and genres to shape meaning and influence audience response",
                  "Evaluating how effectively features are used to communicate ideas, guide audience expectations, and create effects"
                ],
                "year_10": [
                  // Year 10 specific practices (to be extracted)
                ]
              }
            }
          ]
        }
      ]
    }
  ]
}
```

---

## 🔍 **EXTRACTION CHECKLIST**

### For Each Sub-Element:

- [ ] **Sub-element name** (e.g. "Features of text")
- [ ] **Knowledge statements** (5-8 bullets)
- [ ] **Year 9 Practices** (3-10 bullets, may have nested lists)
- [ ] **Year 10 Practices** (usually builds on Year 9)
- [ ] **Preserve formatting** (bold, italics, em dashes, macrons)
- [ ] **Capture examples** in parentheses (e.g. ...)
- [ ] **Note any footnotes** or references

### Text Studies - Complete List:

**Textual and Critical Analysis:**
- [ ] Features of text
- [ ] Context and purpose
- [ ] Interpretations and connections
- [ ] Response to texts

**Language Studies - Complete List:**

**Crafting Texts:**
- [ ] Audience and purpose
- [ ] Ideas and content
- [ ] Structure
- [ ] Language
- [ ] Transcription (spelling, punctuation, grammar)
- [ ] Revision and editing

**Oral Communication:**
- [ ] (To be mapped from full page)

---

## ⚠️ **CHALLENGES IDENTIFIED**

### 1. Nested Lists
Some practices have sub-bullets (see "Examining features of text across a range of forms")
**Solution:** Use nested array structure in JSON

### 2. Bold/Italic Preservation
Text uses **bold** for emphasis (e.g. "**in the novel**")
**Solution:** Use markdown notation in JSON strings

### 3. Special Punctuation
- Em dashes (—) not regular dashes (-)
- Curly quotes (" ") not straight quotes (" ")
**Solution:** Copy-paste directly preserves these

### 4. Length Variation
- Some Knowledge statements: 1 line
- Some Practices: Multiple paragraphs with 9 sub-bullets
**Solution:** Flexible JSON schema (string OR array of strings)

---

## 📋 **NEXT STEPS**

### Immediate (This Session):
1. [ ] Read full snapshot file (all 865 lines)
2. [ ] Extract ALL Text Studies content
3. [ ] Extract ALL Language Studies content  
4. [ ] Create complete te-mataiaho-english-phase4.json
5. [ ] Validate verbatim accuracy

### Tomorrow:
1. [ ] User spot-checks 10 statements
2. [ ] Build curriculum-v3.html UI
3. [ ] Wire up interactivity
4. [ ] Test & ship

---

**Status:** Data structure mapped, ready for extraction  
**Next:** Read full source, build complete JSON  
**Owner:** Kaitiaki Aronui V3.0

