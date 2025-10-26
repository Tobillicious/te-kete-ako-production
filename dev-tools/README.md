# 🔧 Dev Tools - Te Kete Ako

**Simple, practical scripts to make development easier.**

Based on actual working code, not AI-generated complexity.

---

## 📋 Available Tools

### 1. **validate-links.py**

Check all HTML files for broken links.

```bash
# From project root:
python3 dev-tools/validate-links.py
```

**What it does:**
- Finds all HTML files (excludes backups, node_modules)
- Extracts all local HTML links
- Checks if each link resolves to an existing file
- Reports broken links by file

**Output:**
```
🔍 Te Kete Ako Link Validator
📄 Found 993 HTML files
📊 RESULTS:
   Total links checked: 2,450
   Broken links: 2
   Files with broken links: 2

❌ BROKEN LINKS:
📄 index.html
   ❌ dist/lesson-plans/lesson-design-thinking.html
      → Resolved to: dist/lesson-plans/lesson-design-thinking.html
```

**Exit codes:**
- `0` - No broken links found
- `1` - Broken links found

---

### 2. **create-lesson.py**

Create a new lesson from template.

```bash
# Interactive mode:
python3 dev-tools/create-lesson.py

# Command line mode:
python3 dev-tools/create-lesson.py "Linear Equations" "Math" "8" "60"
```

**Arguments:**
1. Title (required)
2. Subject (optional)
3. Year level (optional)
4. Duration in minutes (optional, default: 60)

**What it does:**
- Copies `templates/lesson-template.html`
- Replaces title placeholders
- Creates file in `/lessons/` directory
- Generates filename from title (e.g., "Linear Equations" → `linear-equations.html`)

**Example:**
```bash
$ python3 dev-tools/create-lesson.py "Probability and Statistics" "Math" "8"

✅ Created: lessons/probability-and-statistics.html

✨ NEXT STEPS:
   1. Edit lessons/probability-and-statistics.html
   2. Replace [placeholders] with actual content
   3. Add whakataukī and cultural elements
   4. Test: http://localhost:8000/lessons/probability-and-statistics.html
```

---

## 🚀 Quick Start

### First Time Setup

```bash
# Make scripts executable
chmod +x dev-tools/*.py

# Optional: Add to PATH in your ~/.zshrc or ~/.bashrc
export PATH="$PATH:/Users/admin/Documents/te-kete-ako-clean/dev-tools"
```

### Daily Workflow

```bash
# 1. Create new lesson
python3 dev-tools/create-lesson.py "My Lesson Title"

# 2. Edit the file
open lessons/my-lesson-title.html

# 3. Test locally
open http://localhost:8000/lessons/my-lesson-title.html

# 4. Before committing, validate all links
python3 dev-tools/validate-links.py
```

---

## 🎯 Coming Soon

**Additional tools being considered:**

- `create-handout.py` - Create handout from template
- `create-unit.py` - Create unit plan from template
- `check-quality.py` - Run all quality checks (links, linter, etc.)
- `generate-sitemap.py` - Auto-generate sitemap.xml
- `update-nav.py` - Add new page to navigation
- `find-orphans.py` - Find HTML files not linked from anywhere

**Want one of these? Let us know which would be most helpful!**

---

## 💡 Tips

### Tip 1: Run link validation before deploying

```bash
# Add to your pre-commit hook or CI/CD:
python3 dev-tools/validate-links.py || exit 1
```

### Tip 2: Create multiple lessons quickly

```bash
# Batch create lessons from a list:
for lesson in "Intro to Algebra" "Solving Equations" "Graphing Lines"; do
    python3 dev-tools/create-lesson.py "$lesson" "Math" "8"
done
```

### Tip 3: Check links in specific directory

Modify `validate-links.py` to accept a directory argument if needed.

---

## 🐛 Troubleshooting

### "No such file or directory"

Make sure you're running scripts from the **project root**:

```bash
cd /Users/admin/Documents/te-kete-ako-clean
python3 dev-tools/validate-links.py
```

### "Template not found"

The script looks for `templates/lesson-template.html`. Make sure it exists:

```bash
ls templates/lesson-template.html
```

### "Permission denied"

Make scripts executable:

```bash
chmod +x dev-tools/*.py
```

---

## 📝 Adding New Tools

**Want to add a new dev tool?**

1. Create script in `/dev-tools/`
2. Follow existing patterns (simple, practical)
3. Add shebang: `#!/usr/bin/env python3`
4. Make executable: `chmod +x`
5. Document here
6. Test thoroughly

**Guidelines:**
- ✅ Simple and focused (one task per tool)
- ✅ Based on actual working patterns
- ✅ Clear error messages
- ✅ Exit codes (0 = success, 1 = error)
- ❌ Don't add complex dependencies
- ❌ Don't follow GraphRAG "ideal" systems
- ❌ Don't over-engineer

---

## 🎨 Philosophy

These tools are **boring and simple on purpose.**

- No fancy frameworks
- No AI-generated complexity
- No "ultimate" or "perfect" solutions
- Just practical scripts that save time

**Boring is reliable. Simple works. Users love what works.**

---

*Last updated: October 26, 2025*  
*Tools based on clean version (commit 7b1c43f90)*

