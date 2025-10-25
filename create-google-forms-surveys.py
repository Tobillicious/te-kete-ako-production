#!/usr/bin/env python3
"""
CREATE GOOGLE FORMS FOR BETA SURVEYS
Generates shareable URLs for Week 1-4 feedback surveys
"""

import json
from pathlib import Path

# Survey templates for Google Forms
surveys = {
    "week_1": {
        "title": "Te Kete Ako - Week 1 Beta Feedback",
        "description": "Thank you for being a Founding Beta Teacher! Your Week 1 feedback helps us make Te Kete Ako exceptional. This takes 5 minutes.",
        "questions": [
            {
                "type": "multiple_choice",
                "question": "How easy was it to find what you needed?",
                "options": [
                    "Very easy (1-2 clicks, found immediately)",
                    "Easy (2-3 minutes of browsing)",
                    "Okay (5-10 minutes, found eventually)",
                    "Difficult (>10 minutes, still not sure)",
                    "Very difficult (couldn't find what I needed)"
                ],
                "required": True
            },
            {
                "type": "multiple_choice",
                "question": "Did you use any resources in your classroom this week?",
                "options": [
                    "Yes - used in class! 🎉",
                    "Yes - reviewed but haven't taught yet",
                    "No - still exploring",
                    "No - couldn't find what I needed"
                ],
                "required": True
            },
            {
                "type": "short_answer",
                "question": "If YES, which resource(s)? (Please list)",
                "required": False
            },
            {
                "type": "linear_scale",
                "question": "How was your first impression of the platform? (1-10)",
                "min": 1,
                "max": 10,
                "required": True
            },
            {
                "type": "long_answer",
                "question": "Why this rating? What made you feel this way?",
                "required": True
            },
            {
                "type": "long_answer",
                "question": "What worked brilliantly? ✨ (What made you go 'YES! This is exactly what I needed!')",
                "required": True
            },
            {
                "type": "long_answer",
                "question": "What was frustrating or confusing? 😕 (What made you go 'Ugh, why isn't this easier?')",
                "required": False
            },
            {
                "type": "multiple_choice",
                "question": "How much time did Te Kete Ako save you this week?",
                "options": [
                    "None yet - still exploring",
                    "30 minutes - 1 hour",
                    "1-2 hours",
                    "2-3 hours",
                    "3+ hours (I'm so grateful!)"
                ],
                "required": True
            },
            {
                "type": "multiple_choice",
                "question": "Would you use Te Kete Ako again next week?",
                "options": [
                    "Definitely yes!",
                    "Probably yes",
                    "Maybe",
                    "Probably not",
                    "Definitely not"
                ],
                "required": True
            },
            {
                "type": "short_answer",
                "question": "Why?",
                "required": False
            },
            {
                "type": "long_answer",
                "question": "Any features you wish existed?",
                "required": False
            },
            {
                "type": "multiple_choice",
                "question": "Is there anything we should fix URGENTLY?",
                "options": ["Yes (describe below)", "No, everything works fine"],
                "required": True
            },
            {
                "type": "long_answer",
                "question": "If yes, what's broken/urgent?",
                "required": False
            },
            {
                "type": "linear_scale",
                "question": "How likely are you to recommend Te Kete Ako to a colleague? (1-10)",
                "min": 1,
                "max": 10,
                "required": True
            },
            {
                "type": "long_answer",
                "question": "If you could only improve ONE thing this week, what would it be?",
                "required": True
            },
            {
                "type": "long_answer",
                "question": "OPTIONAL: Any success stories from using resources in class? (Student reactions, engagement, what worked well)",
                "required": False
            },
            {
                "type": "multiple_choice",
                "question": "Can we contact you for a quick 10-minute chat this week?",
                "options": [
                    "Yes - happy to chat!",
                    "Maybe later (after Week 2-3)",
                    "No thanks - surveys are fine"
                ],
                "required": True
            }
        ]
    },
    
    "week_2": {
        "title": "Te Kete Ako - Week 2 Beta Feedback",
        "description": "Week 2! Thanks for continuing. Your feedback helps us improve.",
        "questions": [
            {"type": "multiple_choice", "question": "How many resources have you used in class?", 
             "options": ["0", "1-2", "3-5", "6+"], "required": True},
            {"type": "long_answer", "question": "What worked brilliantly this week?", "required": True},
            {"type": "long_answer", "question": "What didn't work?", "required": False},
            {"type": "long_answer", "question": "Any features you wish existed?", "required": False},
            {"type": "short_answer", "question": "How much time did this save you?", "required": False},
            {"type": "linear_scale", "question": "Overall satisfaction (1-10)", "min": 1, "max": 10, "required": True}
        ]
    },
    
    "week_3": {
        "title": "Te Kete Ako - Week 3 Beta Feedback",
        "description": "Week 3! Getting into the rhythm. Your insights are gold!",
        "questions": [
            {"type": "multiple_choice", "question": "Has this become part of your routine?", 
             "options": ["Yes", "No"], "required": True},
            {"type": "multiple_choice", "question": "Have you recommended to colleagues?", 
             "options": ["Yes", "No"], "required": True},
            {"type": "long_answer", "question": "What would make you use it more?", "required": True},
            {"type": "long_answer", "question": "Any technical issues?", "required": False},
            {"type": "linear_scale", "question": "Overall satisfaction (1-10)", "min": 1, "max": 10, "required": True}
        ]
    },
    
    "week_4": {
        "title": "Te Kete Ako - Week 4 Final Beta Feedback",
        "description": "Final week! Thank you for your incredible contribution. This is the big one!",
        "questions": [
            {"type": "linear_scale", "question": "Overall rating for the entire beta experience (1-10)", 
             "min": 1, "max": 10, "required": True},
            {"type": "multiple_choice", "question": "Would you recommend to other teachers?", 
             "options": ["Yes", "No"], "required": True},
            {"type": "short_answer", "question": "Best resource you used:", "required": True},
            {"type": "long_answer", "question": "What should we prioritize next?", "required": True},
            {"type": "long_answer", "question": "Testimonial (optional): Would you share a quote about your experience?", "required": False},
            {"type": "multiple_choice", "question": "Can we feature you as a case study?", 
             "options": ["Yes", "No"], "required": True},
            {"type": "long_answer", "question": "Any final thoughts or suggestions?", "required": False}
        ]
    }
}

# Generate instructions for creating forms
instructions = """
# 📋 GOOGLE FORMS CREATION GUIDE

## Quick Setup (15 minutes total)

### WEEK 1 SURVEY:
1. Go to: https://forms.google.com
2. Click "+ Blank" to create new form
3. Title: "Te Kete Ako - Week 1 Beta Feedback"
4. Description: "Thank you for being a Founding Beta Teacher! Your Week 1 feedback helps us make Te Kete Ako exceptional. This takes 5 minutes."

5. Add these questions (copy from BETA-WEEK-1-SURVEY.md):
   - How easy was it to find what you needed? (Multiple choice)
   - Did you use any resources in class? (Multiple choice)
   - Which resources? (Short answer)
   - First impression rating (Linear scale 1-10)
   - Why this rating? (Paragraph)
   - What worked brilliantly? (Paragraph)
   - What was frustrating? (Paragraph)
   - Time saved? (Multiple choice)
   - Would you use again? (Multiple choice)
   - Any features you wish existed? (Paragraph)
   - Anything urgent to fix? (Multiple choice + paragraph)
   - Recommend to colleague? (Linear scale 1-10)
   - One thing to improve? (Paragraph)
   - Success stories? (Paragraph - optional)
   - Can we chat? (Multiple choice)

6. Settings:
   ✅ Collect email addresses
   ✅ Limit to 1 response
   ✅ Send copy of responses to respondent
   
7. Click "Send" → Get shareable link
8. Add link to beta tracker spreadsheet

### WEEK 2 SURVEY:
Same process, 6 questions (quicker!)

### WEEK 3 SURVEY:
Same process, 5 questions

### WEEK 4 SURVEY:
Same process, 7 questions (final comprehensive)

---

## Alternative: Use This JSON

Copy the survey_templates.json file and use Google Forms API or import tool to create forms automatically.

---

## Quick Links After Creation:

Add these to your beta-teacher-tracker.csv:
- Week 1: [YOUR_FORM_LINK_HERE]
- Week 2: [YOUR_FORM_LINK_HERE]
- Week 3: [YOUR_FORM_LINK_HERE]
- Week 4: [YOUR_FORM_LINK_HERE]

---

## Email Templates with Links:

Week 1 Email:
"Hi [Name], how was your first week? Please share 5 minutes of feedback: [WEEK_1_LINK]"

Week 2 Email:
"Week 2 check-in! Quick 3-minute survey: [WEEK_2_LINK]"

Week 3 Email:
"Week 3! Getting into the groove? 2-minute survey: [WEEK_3_LINK]"

Week 4 Email:
"Final feedback! Help shape the future: [WEEK_4_LINK]"

---

Kia kaha! 🌿
"""

# Save templates
templates_path = Path("survey-templates.json")
with open(templates_path, 'w') as f:
    json.dump(surveys, f, indent=2)

instructions_path = Path("GOOGLE-FORMS-SETUP-GUIDE.md")
with open(instructions_path, 'w') as f:
    f.write(instructions)

print("✅ Survey templates created!")
print(f"   - {templates_path}")
print(f"   - {instructions_path}")
print()
print("📋 Next: Create forms at https://forms.google.com")
print("   Follow the guide in GOOGLE-FORMS-SETUP-GUIDE.md")
print()
print("⏱️  Time: 15 minutes to create all 4 surveys")
print("🎯 Then: Add links to beta-teacher-tracker.csv")

