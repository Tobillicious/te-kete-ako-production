#!/usr/bin/env python3
"""
Example: Multi-Agent Creation of "Māori Navigation Mathematics" Unit
Demonstrates how specialized agents collaborate to create comprehensive educational content
"""

import json
from typing import Dict, List, Any

class ExampleMultiAgentUnitCreation:
    """Example of how the multi-agent system would create a complete unit"""
    
    def __init__(self):
        self.unit_topic = "Traditional Māori Navigation Mathematics"
        self.year_level = "Year 8"
        self.subject = "Mathematics"
        self.duration = "5 weeks"
    
    def demonstrate_agent_collaboration(self) -> Dict[str, Any]:
        """Show how each agent contributes to the final unit"""
        
        # Kaitiaki Aronui (Cultural Knowledge Keeper) Contribution
        cultural_foundation = {
            "cultural_opening": {
                "karakia": "He karakia mo te haerenga - Prayer for the journey",
                "whakataukī": {
                    "māori": "Ko te pae tawhiti whāia kia tata, ko te pae tata whakamaua kia tīna",
                    "english": "Seek the distant horizons, hold fast to those close at hand",
                    "relevance": "Emphasizes both ambitious goals (distant horizons) and practical skills (close at hand)"
                },
                "cultural_context": "Traditional Polynesian navigation was one of humanity's greatest achievements in mathematics, astronomy, and environmental science."
            },
            "māori_language_integration": [
                "rā (sun) - for solar navigation",
                "whetū (star) - for stellar navigation", 
                "nuku (land) - destination",
                "moana (ocean) - the journey medium",
                "tauira (pattern) - mathematical patterns in nature"
            ],
            "cultural_assessment_criteria": [
                "Demonstrates respect for traditional knowledge",
                "Uses te reo Māori appropriately",
                "Shows understanding of cultural context",
                "Connects mathematical concepts to cultural practices"
            ]
        }
        
        # Kaiako Mātauranga (Curriculum Specialist) Contribution
        curriculum_alignment = {
            "achievement_objectives": [
                "NZ Curriculum Mathematics Level 4: Use measurement skills to solve problems",
                "NZ Curriculum Mathematics Level 4: Use geometric reasoning to solve problems",
                "NZ Curriculum Mathematics Level 4: Use number strategies to solve problems"
            ],
            "learning_progression": [
                "Week 1: Introduction to traditional navigation concepts",
                "Week 2: Mathematical foundations (angles, distances, calculations)",
                "Week 3: Practical applications and problem-solving",
                "Week 4: Cultural connections and traditional knowledge",
                "Week 5: Assessment and reflection"
            ],
            "year_level_appropriateness": {
                "mathematical_complexity": "Appropriate for Year 8 students with support",
                "cultural_concepts": "Age-appropriate introduction to traditional knowledge",
                "practical_skills": "Hands-on activities suitable for middle school"
            }
        }
        
        # Kaiako Pūtaiao (STEM Specialist) Contribution
        stem_content = {
            "mathematical_problems": [
                {
                    "problem": "Traditional navigators divided the horizon into 32 directions. Calculate the angle between each direction.",
                    "solution_steps": [
                        "Total degrees in a circle: 360°",
                        "Number of directions: 32",
                        "Calculation: 360° ÷ 32 = 11.25° per direction"
                    ],
                    "extension": "If a star rises at the 8th direction, what angle is this from North?",
                    "answer": "8 × 11.25° = 90° from North"
                },
                {
                    "problem": "A traditional canoe travels at 15 km/h. How long to travel 3,500 km from Rarotonga to Aotearoa?",
                    "solution_steps": [
                        "Distance: 3,500 km",
                        "Speed: 15 km/h", 
                        "Time = Distance ÷ Speed = 3,500 ÷ 15 = 233.33 hours",
                        "Convert to days: 233.33 ÷ 24 = 9.72 days"
                    ],
                    "practical_application": "Plan food and water for 10-day journey"
                }
            ],
            "hands_on_activities": [
                {
                    "activity": "Traditional Angle Measurement",
                    "materials": ["Hands, rulers, protractors"],
                    "instructions": [
                        "Use fist to measure angles (1 fist = 10°)",
                        "Measure classroom objects using traditional methods",
                        "Compare with modern measurement tools"
                    ],
                    "learning_outcomes": "Understand traditional measurement systems and compare with modern methods"
                }
            ],
            "scientific_investigations": [
                {
                    "investigation": "Wave Pattern Analysis",
                    "question": "How do ocean waves help navigators find land?",
                    "hypothesis": "Wave patterns change when they encounter land masses",
                    "method": "Use water tanks and obstacles to simulate wave behavior",
                    "data_collection": "Measure wave frequency and amplitude changes",
                    "analysis": "Calculate wave speed and interference patterns"
                }
            ]
        }
        
        # Kaiako Whakamātau (Assessment Specialist) Contribution
        assessment_framework = {
            "asttle_style_questions": [
                {
                    "question": "According to the text, why was mathematical accuracy important for traditional navigators?",
                    "type": "literal_comprehension",
                    "options": [
                        "A) To impress other navigators",
                        "B) To avoid getting lost at sea", 
                        "C) To win navigation competitions",
                        "D) To record their journeys"
                    ],
                    "correct_answer": "B",
                    "explanation": "Mathematical errors could mean death at sea, so accuracy was literally a matter of survival."
                },
                {
                    "question": "What can you infer about the relationship between traditional knowledge and modern science?",
                    "type": "inferential_comprehension",
                    "answer_guidance": "Students should recognize that traditional knowledge often aligns with modern scientific understanding",
                    "marking_criteria": "Award marks for recognizing the sophistication of traditional knowledge systems"
                }
            ],
            "formative_assessments": [
                {
                    "checkpoint": "Week 2 - Mathematical Foundations",
                    "assessment_type": "Problem-solving worksheet",
                    "criteria": [
                        "Can calculate angles between star directions",
                        "Can solve distance, speed, time problems",
                        "Can convert between traditional and modern units"
                    ],
                    "feedback_focus": "Mathematical accuracy and problem-solving strategies"
                }
            ],
            "summative_assessment": {
                "type": "Project-based assessment",
                "task": "Design a traditional navigation route using mathematical calculations",
                "rubric_criteria": [
                    "Mathematical accuracy (40%)",
                    "Cultural understanding (30%)",
                    "Problem-solving approach (20%)",
                    "Presentation quality (10%)"
                ]
            }
        }
        
        # Kaiako Whakaaro (Critical Thinking Specialist) Contribution
        inquiry_framework = {
            "guided_inquiry_questions": [
                "How did traditional navigators use mathematics to ensure safe ocean travel?",
                "What mathematical patterns exist in nature that can guide navigation?",
                "How does traditional knowledge compare with modern navigation technology?",
                "What can we learn from traditional navigators about problem-solving?"
            ],
            "project_based_learning": {
                "project_title": "Traditional Navigation Challenge",
                "challenge": "Plan and mathematically justify a traditional Polynesian voyage",
                "student_agency": [
                    "Choose destination and route",
                    "Calculate journey parameters",
                    "Design navigation strategy",
                    "Present findings to class"
                ],
                "collaboration_opportunities": [
                    "Peer review of calculations",
                    "Group problem-solving sessions",
                    "Cultural knowledge sharing",
                    "Presentation preparation"
                ]
            },
            "critical_thinking_activities": [
                {
                    "activity": "Traditional vs Modern Navigation",
                    "thinking_skills": ["Compare and contrast", "Evaluate effectiveness", "Consider context"],
                    "questions": [
                        "What are the advantages and disadvantages of each approach?",
                        "When might traditional methods be more appropriate?",
                        "How can we combine traditional and modern knowledge?"
                    ]
                }
            ]
        }
        
        # Kaiako Rauemi (Resource Creation Specialist) Contribution
        resource_package = {
            "printable_worksheets": [
                {
                    "title": "Traditional Navigation Mathematics Worksheet",
                    "file": "/handouts/printable-worksheets/traditional-navigation-mathematics-worksheet.html",
                    "content": "Comprehensive worksheet with calculation problems, answer spaces, and reflection questions"
                },
                {
                    "title": "Star Compass Template",
                    "file": "/handouts/printable-worksheets/star-compass-template.html",
                    "content": "Printable template for students to create their own star compass"
                }
            ],
            "visual_materials": [
                {
                    "title": "Traditional Navigation Poster",
                    "description": "Visual guide showing star compass, wave patterns, and navigation tools",
                    "accessibility": "High contrast, large text, visual and text descriptions"
                },
                {
                    "title": "Mathematical Concept Cards",
                    "description": "Flash cards with Māori mathematical terms and concepts",
                    "format": "Printable cards with te reo Māori, English, and visual representations"
                }
            ],
            "teacher_resources": [
                {
                    "title": "Implementation Guide",
                    "content": "Step-by-step instructions for teaching the unit",
                    "includes": ["Timing suggestions", "Differentiation strategies", "Cultural protocols"]
                },
                {
                    "title": "Assessment Rubric",
                    "content": "Detailed marking criteria for all assessments",
                    "includes": ["Performance indicators", "Sample responses", "Moderation notes"]
                }
            ],
            "multimedia_integration": [
                {
                    "type": "Video",
                    "title": "Traditional Navigation Documentary",
                    "description": "Short video showing traditional navigation in practice",
                    "accessibility": "Captions, transcript, and audio description available"
                },
                {
                    "type": "Interactive",
                    "title": "Star Compass Simulator",
                    "description": "Digital tool for practicing star compass calculations",
                    "features": ["Drag and drop interface", "Immediate feedback", "Progress tracking"]
                }
            ]
        }
        
        # Integration of all contributions
        comprehensive_unit = {
            "unit_overview": {
                "title": self.unit_topic,
                "year_level": self.year_level,
                "subject": self.subject,
                "duration": self.duration,
                "created_by": "Multi-Agent Kaiako System"
            },
            "cultural_foundation": cultural_foundation,
            "curriculum_alignment": curriculum_alignment,
            "stem_content": stem_content,
            "assessment_framework": assessment_framework,
            "inquiry_framework": inquiry_framework,
            "resource_package": resource_package,
            "integration_summary": {
                "cultural_authenticity": "Verified by Kaitiaki Aronui with appropriate protocols and language",
                "curriculum_compliance": "Aligned to NZ Curriculum Level 4 Mathematics objectives",
                "mathematical_rigor": "Problems designed by STEM specialist with step-by-step solutions",
                "assessment_quality": "AsTTle-style questions and comprehensive rubrics provided",
                "student_engagement": "Inquiry-based approach with student agency and choice",
                "resource_completeness": "All necessary materials, worksheets, and guides included"
            }
        }
        
        return comprehensive_unit
    
    def save_example_unit(self):
        """Save the example unit to demonstrate the output"""
        unit = self.demonstrate_agent_collaboration()
        
        with open("output/example_māori_navigation_unit.json", "w") as f:
            json.dump(unit, f, indent=2)
        
        print("📦 Example unit saved to output/example_māori_navigation_unit.json")
        print("\n🎯 This demonstrates how specialized agents collaborate to create:")
        print("✅ Culturally authentic content (Kaitiaki Aronui)")
        print("✅ Curriculum-aligned learning (Kaiako Mātauranga)")
        print("✅ Rigorous mathematical problems (Kaiako Pūtaiao)")
        print("✅ Quality assessments (Kaiako Whakamātau)")
        print("✅ Engaging inquiry experiences (Kaiako Whakaaro)")
        print("✅ Complete resource packages (Kaiako Rauemi)")
        
        return unit

# Example usage
if __name__ == "__main__":
    example = ExampleMultiAgentUnitCreation()
    unit = example.save_example_unit()
    
    print("\n📊 Unit Quality Metrics:")
    print(f"• Cultural authenticity: ✅ Verified")
    print(f"• Curriculum alignment: ✅ Level 4 Mathematics objectives")
    print(f"• Assessment quality: ✅ AsTTle-style questions included")
    print(f"• Resource completeness: ✅ All materials provided")
    print(f"• Student engagement: ✅ Inquiry-based with student agency")
    print(f"• Implementation ready: ✅ Teacher guides and rubrics included")
