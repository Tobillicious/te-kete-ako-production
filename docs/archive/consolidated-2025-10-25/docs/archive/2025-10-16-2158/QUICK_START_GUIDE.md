# 🚀 Quick Start Guide - Te Kete Ako Content System

**Welcome to the Comprehensive Educational Content Generation System!**

This guide will help you get started in 5 minutes.

---

## 🎯 What Can This System Do?

This system generates **complete, print-ready educational units** with:
- ✅ Full lesson plans (minute-by-minute)
- ✅ Printable worksheets with answer keys
- ✅ Assessment rubrics
- ✅ Cultural integration (te reo Māori + tikanga)
- ✅ NZ Curriculum alignment
- ✅ Differentiation strategies

---

## 📖 For Teachers (Using Pre-Made Resources)

### Step 1: Browse Available Units

Open in your web browser:
```
/Users/admin/Documents/te-kete-ako-clean/public/units/subject-generation-roadmap.html
```

Or navigate to:
- **Year Level Progression:** `public/units/year-level-progression-generator.html`
- **Complete Example Unit:** `public/units/comprehensive-example-unit.html`

### Step 2: Access Printable Worksheets

Open the worksheet index:
```
/Users/admin/Documents/te-kete-ako-clean/public/handouts/printable-worksheets/index.html
```

**Available Worksheets:**
- 📐 Lesson 1: Star Compass Calculations
- 🌊 Lesson 2: Distance and Speed Calculations
- 📖 Navigation Vocabulary (Te Reo Māori & English)
- 📚 Traditional Navigation Reading Comprehension
- 📋 AsTTle-Style Template (customizable)

### Step 3: Print and Use

1. Click "Open Worksheet" on any resource
2. Review the teacher notes at the bottom (won't print)
3. Click "Print" button or use Ctrl/Cmd+P
4. Distribute to students!

### Step 4: Use Assessment Rubric

Open the master rubric:
```
/Users/admin/Documents/te-kete-ako-clean/public/units/master-assessment-rubric.html
```

Print and share with students before beginning assessments.

---

## 🛠️ For Content Developers (Generating New Units)

### Prerequisites

Ensure you have Python 3 installed:
```bash
python3 --version
```

### Generate a New Unit

1. **Navigate to the project:**
   ```bash
   cd /Users/admin/Documents/te-kete-ako-clean
   ```

2. **Run the unit generator:**
   ```bash
   python3 scripts/comprehensive-unit-generator.py
   ```

3. **View generated content:**
   ```bash
   ls -la output/comprehensive-units/
   ```

### Customize Unit Generation

Edit the unit specification in `scripts/comprehensive-unit-generator.py`:

```python
spec = UnitSpecification(
    title="Your Unit Title Here",
    year_level="Year 8",
    subject="Mathematics",  # or Science, English, etc.
    duration_weeks=5,
    lessons_per_week=2,
    lesson_duration_minutes=60,
    cultural_context="Your cultural context",
    curriculum_objectives=[
        "NZ Curriculum objectives here"
    ],
    learning_outcomes=[
        "Your learning outcomes"
    ]
)
```

Then run the generator again.

---

## 🤖 Using the Multi-Agent System

The multi-agent system uses 6 specialized AI agents to create content:

1. **Kaitiaki Aronui** - Cultural knowledge keeper
2. **Kaiako Mātauranga** - Curriculum specialist
3. **Kaiako Whakamātau** - Assessment specialist
4. **Kaiako Pūtaiao** - STEM specialist
5. **Kaiako Whakaaro** - Critical thinking specialist
6. **Kaiako Rauemi** - Resource creation specialist

### Run Multi-Agent Generation:

```bash
cd /Users/admin/Documents/te-kete-ako-clean
python3 scripts/multi-agent-content-creation.py
```

**Note:** This creates a comprehensive content package with all agent contributions integrated.

---

## 📁 Project Structure

```
te-kete-ako-clean/
│
├── public/                          # Web-accessible resources
│   ├── units/                       # Unit planning interfaces
│   │   ├── year-level-progression-generator.html
│   │   ├── subject-generation-roadmap.html
│   │   ├── comprehensive-assessment-generator.html
│   │   ├── comprehensive-example-unit.html
│   │   ├── ultra-comprehensive-navigation-unit.html
│   │   └── master-assessment-rubric.html
│   │
│   └── handouts/                    # Printable resources
│       └── printable-worksheets/
│           ├── index.html           # ← START HERE FOR WORKSHEETS
│           ├── lesson-1-star-compass-calculations.html
│           ├── lesson-2-distance-speed-calculations.html
│           ├── navigation-vocabulary-te-reo-maori.html
│           ├── navigation-reading-comprehension.html
│           ├── asttle-comprehension-template.html
│           └── traditional-navigation-mathematics-worksheet.html
│
├── scripts/                         # Content generation scripts
│   ├── comprehensive-unit-generator.py
│   ├── multi-agent-content-creation.py
│   └── example-multi-agent-unit-creation.py
│
├── output/                          # Generated content storage
│   └── comprehensive-units/
│       ├── units/                   # Complete unit JSON files
│       ├── lessons/                 # Individual lesson plans
│       ├── teacher-resources/       # Assessment frameworks & inventories
│       ├── handouts/               # Student handouts
│       └── student-materials/      # Student resources
│
└── Documentation/
    ├── COMPREHENSIVE_CONTENT_SYSTEM_STATUS.md  # ← Full system documentation
    ├── COMPREHENSIVE_NESTED_EDUCATION_SYSTEM.md
    ├── MULTI_AGENT_KAIKO_SYSTEM_DESIGN.md
    ├── ULTRA_COMPREHENSIVE_NESTED_SYSTEM.md
    └── QUICK_START_GUIDE.md                    # ← You are here
```

---

## 🎓 Example: Traditional Māori Navigation Mathematics Unit

### What's Included:

✅ **10 Complete Lesson Plans** (60 min each)
- Lesson 1: Introduction to Traditional Navigation
- Lesson 2: Star Compass Mathematics
- Lesson 3: Distance and Speed Calculations
- Lesson 4: Wave Pattern Analysis
- Lesson 5: Traditional Measurement Methods
- Lessons 6-10: Advanced topics and assessment

✅ **6 Printable Worksheets**
- Star Compass Calculations
- Distance & Speed Problems
- Te Reo Māori Vocabulary
- Reading Comprehension Assessment
- And more...

✅ **Complete Assessment Framework**
- Formative assessment checkpoints
- Summative project-based assessment
- Cultural competency evaluation
- Self-assessment tools

✅ **Teacher Resources**
- Minute-by-minute lesson guides
- Word-for-word teaching scripts
- Complete answer keys
- Differentiation strategies
- Cultural protocols
- Emergency procedures

---

## 🏛️ Cultural Protocols

### Before Using Any Content:

1. ✅ **Review with Cultural Advisors**
   - Consult with local iwi education liaisons
   - Ensure cultural appropriateness for your context
   - Get approval for use of cultural content

2. ✅ **Practice Te Reo Māori**
   - Learn correct pronunciation before teaching
   - Use audio resources when available
   - Respect the language by using it correctly

3. ✅ **Community Consultation**
   - Follow the consultation protocols in each unit
   - Engage with community before and during implementation
   - Seek feedback and adjust as needed

4. ✅ **Ongoing Cultural Sensitivity**
   - Treat traditional knowledge with respect
   - Acknowledge knowledge sources
   - Support students' cultural learning journey

---

## ⚡ Quick Links

### For Teachers:
- [📚 Browse All Units](public/units/subject-generation-roadmap.html)
- [📝 Printable Worksheets](public/handouts/printable-worksheets/index.html)
- [📊 Assessment Rubric](public/units/master-assessment-rubric.html)
- [🎯 Example Complete Unit](public/units/comprehensive-example-unit.html)

### For Developers:
- [🤖 Multi-Agent System Design](MULTI_AGENT_KAIKO_SYSTEM_DESIGN.md)
- [📖 Complete System Documentation](COMPREHENSIVE_CONTENT_SYSTEM_STATUS.md)
- [🔧 Unit Generator Script](scripts/comprehensive-unit-generator.py)
- [🧪 Generated Content](output/comprehensive-units/)

---

## 🆘 Troubleshooting

### Problem: Python script won't run

**Solution:**
```bash
# Check Python version (needs 3.x)
python3 --version

# If missing, install Python 3
# Then try again
```

### Problem: HTML files won't open properly

**Solution:**
- Use a modern web browser (Chrome, Firefox, Safari, Edge)
- Open files directly from file system, or
- Run a local web server:
  ```bash
  cd /Users/admin/Documents/te-kete-ako-clean
  python3 -m http.server 8000
  # Then visit http://localhost:8000 in your browser
  ```

### Problem: Print formatting looks wrong

**Solution:**
- Use the "Print" button on the worksheet page
- Check your print preview before printing
- Adjust margins in print dialog if needed
- Ensure "Print background graphics" is enabled

---

## 📞 Getting Help

### Documentation:
1. [Complete System Status](COMPREHENSIVE_CONTENT_SYSTEM_STATUS.md) - Full documentation
2. [Multi-Agent System Design](MULTI_AGENT_KAIKO_SYSTEM_DESIGN.md) - Technical details
3. [Nested System Spec](ULTRA_COMPREHENSIVE_NESTED_SYSTEM.md) - Content structure

### Support:
- **Technical Issues:** Check script documentation in Python files
- **Content Questions:** Review generated JSON files in `output/`
- **Cultural Guidance:** Consult with local iwi education liaisons
- **Implementation:** See complete example unit

---

## 🎉 Success! You're Ready to Go

### Next Steps:

**For Teachers:**
1. ✅ Open `public/handouts/printable-worksheets/index.html`
2. ✅ Browse available worksheets
3. ✅ Print what you need
4. ✅ Implement in your classroom!

**For Developers:**
1. ✅ Review `COMPREHENSIVE_CONTENT_SYSTEM_STATUS.md`
2. ✅ Run `python3 scripts/comprehensive-unit-generator.py`
3. ✅ Check generated output in `output/comprehensive-units/`
4. ✅ Customize and generate more content!

---

## 💡 Pro Tips

1. **Start with the Example:** Review the complete Navigation Mathematics unit to see the full system in action

2. **Use the Templates:** The AsTTle template can be customized for any reading passage

3. **Cultural First:** Always review cultural content with advisors before implementation

4. **Differentiate:** Every worksheet includes support and extension activities - use them!

5. **Print in Batches:** Print worksheets for the whole week at once to save time

6. **Share Success:** When you create great content, share it back with the community

---

*Ko te pae tawhiti whāia kia tata, ko te pae tata whakamaua kia tīna*  
*Seek the distant horizons, hold fast to those close at hand*

**🌟 Happy Teaching & Creating! 🌟**

