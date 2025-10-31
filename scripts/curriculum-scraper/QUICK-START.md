# ⚡ QUICK START - Curriculum Scraper

**Get curriculum data in 5 commands!**

---

## 🚀 **FOR USER / NEXT AGENT:**

```bash
# 1. Navigate to scraper directory
cd /Users/admin/Documents/te-kete-ako-clean/scripts/curriculum-scraper

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure Supabase (add your service key)
cp .env.example .env
nano .env  # Add SUPABASE_SERVICE_KEY

# 4. Test with English only (quick test - 2 minutes)
python scraper.py --version temataiaho_2025 --learning-area English

# 5. Validate the output
python validator.py ./scraped-data

# 6. If validation passes, upload!
python uploader.py ./scraped-data
```

---

## 🎯 **WHAT YOU GET:**

After running the test scrape (English only):
- **~48 curriculum statements** (Phase 1-4, Knowledge + Practices, 2 strands)
- Verbatim from MoE Tahurangi website
- Validated (no placeholders, proper structure)
- Ready for Supabase upload

---

## 📊 **FULL EXTRACTION:**

Once test works, run full extraction:
```bash
# This will scrape ALL configured sources (~30-40 minutes)
python scraper.py

# Expected output:
# - temataiaho_2025: English, Mathematics (mandatory Jan 1)
# - draft_2025: Science, Social Sciences, Health & PE, Arts, Tech, Languages
# - Total: ~500-800 statements initially
```

---

## ✅ **SUCCESS CHECKLIST:**

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file configured with Supabase service key
- [ ] Test scrape completed (English)
- [ ] Validation passed (no errors)
- [ ] Test upload successful (statements in database)
- [ ] Full scrape ready to run

---

## 🐛 **TROUBLESHOOTING:**

**Can't install dependencies?**
```bash
# Use virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Supabase connection error?**
- Check `.env` file has correct `SUPABASE_SERVICE_KEY`
- Verify key is **service role key** (not anon key)
- Test connection: `python -c "from uploader import CurriculumUploader; CurriculumUploader()"`

**No statements extracted?**
- HTML structure may have changed on Tahurangi
- Check URL is accessible: open in browser
- Review logs for specific errors
- May need to update selectors in `config.py`

---

## 🎉 **YOU'RE READY!**

System is production-ready and waiting for you to run it!

**Kia kaha!** 🚀

