# 🏔️ Curriculum Scraper - Phase 2

**Purpose:** Extract verbatim NZ Curriculum statements from Tahurangi website

---

## 📋 **QUICK START**

### **1. Install Dependencies**
```bash
cd scripts/curriculum-scraper
pip install -r requirements.txt
```

### **2. Configure Environment**
```bash
# Copy example and fill in your Supabase service key
cp .env.example .env
nano .env  # Add your SUPABASE_SERVICE_KEY
```

### **3. Scrape Curriculum**
```bash
# Scrape everything (all versions, all learning areas)
python scraper.py

# OR scrape specific version/area for testing
python scraper.py --version temataiaho_2025 --learning-area English
```

### **4. Validate Data**
```bash
python validator.py ./scraped-data
```

### **5. Upload to Supabase**
```bash
python uploader.py ./scraped-data
```

---

## 📂 **FILE STRUCTURE**

```
curriculum-scraper/
├── README.md          # This file
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
├── config.py          # Curriculum sources & structures
├── scraper.py         # Main scraping logic
├── validator.py       # Data validation
├── uploader.py        # Supabase upload
└── scraped-data/      # Output directory (gitignored)
    ├── temataiaho_2025_english.json
    ├── temataiaho_2025_mathematics.json
    ├── draft_2025_science.json
    ├── draft_2025_social_sciences.json
    ├── scraping_summary.json
    └── validation_report.json
```

---

## 🎯 **SCRAPER FEATURES**

### **Respectful Scraping:**
- 1-second delay between requests (configurable)
- Proper User-Agent header
- Retry logic with exponential backoff
- Handles rate limiting gracefully

### **Smart Extraction:**
- Parses Te Mātaiaho 2025 table format
- Extracts Knowledge vs Practices separately
- Identifies year-specific vs phase-wide statements
- Extracts examples (if present)
- Cleans text (removes weird Unicode, extra spaces)

### **Verbatim Content:**
- No paraphrasing - exact text from MoE
- Preserves formatting
- Captures complete statements

### **Structured Output:**
- JSON format per learning area
- Metadata included (extracted_at, statement_count)
- Summary file for all extractions

---

## 🧪 **VALIDATOR FEATURES**

### **Checks:**
- ✅ Required fields present
- ✅ Statement text length (10-5000 chars)
- ✅ No placeholder text (TODO, TBD, lorem ipsum, etc.)
- ✅ Valid curriculum_version
- ✅ Valid year_levels (0-13)
- ✅ Phase OR level present (not both)
- ✅ Valid element (Knowledge/Practices for Te Mātaiaho)

### **Reporting:**
- Per-file validation results
- Overall statistics
- Strand/element distribution
- Detailed error messages
- Saves validation_report.json

---

##  **UPLOADER FEATURES**

### **Safe Upload:**
- Batch inserts (50 statements at a time)
- Transaction support (all or nothing)
- Duplicate detection (by statement text + version + learning area)
- Progress tracking with tqdm
- Rollback on error

### **Quality Assurance:**
- Pre-upload validation
- Post-upload verification
- Detailed logging
- Upload summary report

---

## 📊 **EXPECTED OUTPUT**

### **Te Mātaiaho 2025 - English (Example)**
```json
{
  "curriculum_version": "temataiaho_2025",
  "learning_area": "English",
  "statement_count": 48,
  "extracted_at": "2025-10-29 10:30:00",
  "statements": [
    {
      "curriculum_version": "temataiaho_2025",
      "learning_area": "English",
      "phase": "Phase 4",
      "strand": "Text Studies",
      "element": "Knowledge",
      "statement_text": "Students understand how texts are shaped by purpose, audience, and context...",
      "year_levels": [9, 10],
      "context": null,
      "examples": ["Analyzing persuasive techniques in speeches", "..."]
    },
    // ... 47 more statements
  ]
}
```

---

## 🚀 **USAGE EXAMPLES**

### **Test Scraping (Single Area)**
```bash
# Just scrape English to test
python scraper.py --version temataiaho_2025 --learning-area English --delay 2.0

# Check output
cat scraped-data/temataiaho_2025_english.json | jq '.statement_count'
```

### **Full Extraction**
```bash
# Scrape everything (will take ~30 minutes with delays)
python scraper.py --output ./curriculum-data

# Validate all
python validator.py ./curriculum-data

# If validation passes, upload
python uploader.py ./curriculum-data
```

### **Re-scrape After Updates**
```bash
# When MoE updates curriculum, re-scrape specific area
python scraper.py --version temataiaho_2025 --learning-area English

# Validate just that file
python validator.py ./scraped-data/temataiaho_2025_english.json

# Upload updates (will detect duplicates)
python uploader.py ./scraped-data --file temataiaho_2025_english.json
```

---

## ⚠️ **IMPORTANT NOTES**

### **Legal:**
- NZ Curriculum is Crown Copyright
- Direct copying is legally required for educational use
- Must be verbatim (no paraphrasing)

### **Technical:**
- Be respectful: 1-second delay minimum
- Check `robots.txt` before mass scraping
- If Tahurangi blocks you, increase delay
- Consider scraping during off-peak hours (NZ time)

### **Data Quality:**
- Always validate before uploading
- Check for placeholder text
- Verify statement counts match expectations
- Compare with source website manually for first extraction

---

## 🐛 **TROUBLESHOOTING**

### **"Failed to fetch" errors:**
- Check internet connection
- Increase delay: `--delay 2.0`
- Check if URL changed on Tahurangi
- Try with VPN (if geo-blocked)

### **"No statements extracted":**
- HTML structure may have changed
- Check `config.py` selectors
- Manually inspect page source
- Update extraction logic in `scraper.py`

### **Validation errors:**
- Check `validation_report.json` for details
- Most common: placeholder text, missing fields
- Fix data in JSON files before uploading
- OR fix scraper and re-scrape

### **Upload errors:**
- Check Supabase connection (`.env` file)
- Verify service key has write permissions
- Check database schema matches (run migration first)
- Review upload logs for specific SQL errors

---

## 📈 **PROGRESS TRACKING**

Track completion in `CURRICULUM-V3-README.md`:

- [ ] English Phase 1-4 (Te Mātaiaho 2025)
- [ ] Mathematics Phase 1-4 (Te Mātaiaho 2025)
- [ ] Science Phase 1-4 (Draft 2025)
- [ ] Social Sciences Phase 1-4 (Draft 2025)
- [ ] Health & PE Phase 1-4 (Draft 2025)
- [ ] The Arts Phase 1-4 (Draft 2025)
- [ ] Technology Phase 1-4 (Draft 2025)
- [ ] Learning Languages Phase 1-4 (Draft 2025)
- [ ] 2007 NZC - All subjects (Levels 1-8)

**Estimated:** ~136 documents → ~2,500-3,500 statements

---

## 🎉 **SUCCESS CRITERIA**

- ✅ All statements verbatim from MoE
- ✅ Zero placeholder text
- ✅ 100% validation pass rate
- ✅ Complete coverage (no missing strands/phases)
- ✅ Proper attribution (Tahurangi URLs stored)
- ✅ Ready for UI consumption

---

**He mahi nui tēnei! Kia kaha!**  
(This is big work! Stay strong!)

🧺 ✨ 📚 🗺️ 🚀

