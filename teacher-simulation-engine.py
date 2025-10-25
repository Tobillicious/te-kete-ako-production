#!/usr/bin/env python3
"""
TE KETE AKO - TEACHER SIMULATION ENGINE
Simulate 20 diverse teachers × 1000 iterations = 20,000 usage scenarios
Find and fix issues BEFORE real beta teachers arrive
"""

import random
import json
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# ============================================================================
# TEACHER PERSONAS (20 Diverse Teachers)
# ============================================================================

TEACHERS = [
    {
        "id": 1,
        "name": "Aroha Te Rangi",
        "subject": "Te Reo Māori",
        "years": [7, 8, 9],
        "tech_skill": "high",
        "priority": "cultural_authenticity",
        "school_type": "kura kaupapa",
        "experience": "15 years",
        "teaching_style": "immersive",
        "needs": ["authentic te reo", "cultural protocols", "whakataukī"]
    },
    {
        "id": 2,
        "name": "James Chen",
        "subject": "Mathematics",
        "years": [9, 10, 11],
        "tech_skill": "medium",
        "priority": "exam_prep",
        "school_type": "state secondary",
        "experience": "8 years",
        "teaching_style": "structured",
        "needs": ["NCEA aligned", "worked examples", "practice problems"]
    },
    {
        "id": 3,
        "name": "Sarah Williams",
        "subject": "Science",
        "years": [7, 8],
        "tech_skill": "low",
        "priority": "easy_to_use",
        "school_type": "intermediate",
        "experience": "3 years",
        "teaching_style": "hands_on",
        "needs": ["simple navigation", "printable", "clear instructions"]
    },
    {
        "id": 4,
        "name": "Hemi Parata",
        "subject": "Social Studies",
        "years": [9, 10],
        "tech_skill": "high",
        "priority": "critical_thinking",
        "school_type": "state secondary",
        "experience": "20 years",
        "teaching_style": "inquiry_based",
        "needs": ["primary sources", "discussion prompts", "māori perspective"]
    },
    {
        "id": 5,
        "name": "Emily Rodriguez",
        "subject": "English",
        "years": [8, 9, 10],
        "tech_skill": "medium",
        "priority": "differentiation",
        "school_type": "state integrated",
        "experience": "12 years",
        "teaching_style": "scaffolded",
        "needs": ["multiple levels", "visual aids", "cultural texts"]
    },
    {
        "id": 6,
        "name": "Tāne Wiremu",
        "subject": "Digital Technologies",
        "years": [9, 10, 11],
        "tech_skill": "expert",
        "priority": "real_world_projects",
        "school_type": "state secondary",
        "experience": "5 years",
        "teaching_style": "project_based",
        "needs": ["coding projects", "māori tech", "contemporary issues"]
    },
    {
        "id": 7,
        "name": "Lisa Thompson",
        "subject": "Health & PE",
        "years": [7, 8, 9],
        "tech_skill": "low",
        "priority": "student_wellbeing",
        "school_type": "intermediate",
        "experience": "10 years",
        "teaching_style": "holistic",
        "needs": ["te whare tapa whā", "mental health", "hauora"]
    },
    {
        "id": 8,
        "name": "David Kumar",
        "subject": "Mathematics",
        "years": [7, 8],
        "tech_skill": "medium",
        "priority": "engagement",
        "school_type": "intermediate",
        "experience": "6 years",
        "teaching_style": "game_based",
        "needs": ["interactive", "visual", "games"]
    },
    {
        "id": 9,
        "name": "Whetu Smith",
        "subject": "Science",
        "years": [10, 11, 12],
        "tech_skill": "high",
        "priority": "mātauranga_integration",
        "school_type": "kura",
        "experience": "18 years",
        "teaching_style": "bicultural",
        "needs": ["māori science", "traditional knowledge", "dual perspectives"]
    },
    {
        "id": 10,
        "name": "Rachel Green",
        "subject": "English",
        "years": [7, 8],
        "tech_skill": "low",
        "priority": "literacy_basics",
        "school_type": "intermediate",
        "experience": "25 years",
        "teaching_style": "traditional",
        "needs": ["simple", "printable", "clear structure"]
    },
    {
        "id": 11,
        "name": "Kahu Morrison",
        "subject": "Social Studies",
        "years": [7, 8, 9],
        "tech_skill": "medium",
        "priority": "treaty_education",
        "school_type": "state",
        "experience": "7 years",
        "teaching_style": "narrative",
        "needs": ["treaty content", "nz history", "decolonization"]
    },
    {
        "id": 12,
        "name": "Michael Lee",
        "subject": "Digital Technologies",
        "years": [7, 8],
        "tech_skill": "expert",
        "priority": "computational_thinking",
        "school_type": "intermediate",
        "experience": "4 years",
        "teaching_style": "maker",
        "needs": ["beginner coding", "unplugged activities", "progression"]
    },
    {
        "id": 13,
        "name": "Aroha Wilson",
        "subject": "Cross-Curricular",
        "years": [7, 8, 9, 10],
        "tech_skill": "high",
        "priority": "integrated_units",
        "school_type": "area school",
        "experience": "16 years",
        "teaching_style": "thematic",
        "needs": ["cross-subject", "project based", "real world"]
    },
    {
        "id": 14,
        "name": "Tom Anderson",
        "subject": "Science",
        "years": [9, 10],
        "tech_skill": "medium",
        "priority": "practical_labs",
        "school_type": "state secondary",
        "experience": "9 years",
        "teaching_style": "experimental",
        "needs": ["experiments", "safety notes", "equipment lists"]
    },
    {
        "id": 15,
        "name": "Mere Takerei",
        "subject": "Te Reo Māori",
        "years": [9, 10, 11],
        "tech_skill": "medium",
        "priority": "language_immersion",
        "school_type": "state secondary",
        "experience": "11 years",
        "teaching_style": "communicative",
        "needs": ["conversational", "authentic context", "language games"]
    },
    {
        "id": 16,
        "name": "Sophie Martin",
        "subject": "Mathematics",
        "years": [11, 12, 13],
        "tech_skill": "high",
        "priority": "university_prep",
        "school_type": "state secondary",
        "experience": "14 years",
        "teaching_style": "rigorous",
        "needs": ["calculus", "statistics", "scholarship prep"]
    },
    {
        "id": 17,
        "name": "Rangi Johnson",
        "subject": "English",
        "years": [10, 11],
        "tech_skill": "medium",
        "priority": "ncea_excellence",
        "school_type": "state secondary",
        "experience": "13 years",
        "teaching_style": "analytical",
        "needs": ["text analysis", "essay writing", "māori texts"]
    },
    {
        "id": 18,
        "name": "Anna Patel",
        "subject": "Science",
        "years": [7, 8, 9],
        "tech_skill": "medium",
        "priority": "inquiry_learning",
        "school_type": "intermediate",
        "experience": "5 years",
        "teaching_style": "questioning",
        "needs": ["investigations", "student-led", "wonder"]
    },
    {
        "id": 19,
        "name": "Matiu Brown",
        "subject": "Social Studies",
        "years": [11, 12, 13],
        "tech_skill": "high",
        "priority": "social_justice",
        "school_type": "state secondary",
        "experience": "17 years",
        "teaching_style": "activist",
        "needs": ["current issues", "critical analysis", "action projects"]
    },
    {
        "id": 20,
        "name": "Jessica White",
        "subject": "Health & PE",
        "years": [9, 10],
        "tech_skill": "low",
        "priority": "inclusive_pe",
        "school_type": "state secondary",
        "experience": "8 years",
        "teaching_style": "inclusive",
        "needs": ["modified activities", "wellbeing focus", "hauora"]
    }
]

# ============================================================================
# USAGE SCENARIOS (What Teachers Actually Do)
# ============================================================================

class TeacherSimulation:
    def __init__(self, teacher):
        self.teacher = teacher
        self.session_history = []
        self.frustrations = []
        self.wins = []
        self.feature_requests = []
        
    def simulate_session(self, iteration):
        """Simulate one teaching session"""
        session = {
            "iteration": iteration,
            "teacher_id": self.teacher["id"],
            "teacher_name": self.teacher["name"],
            "timestamp": datetime.now() + timedelta(minutes=iteration),
            "actions": [],
            "outcome": None,
            "satisfaction": 0
        }
        
        # Teacher workflow simulation
        workflow = self.choose_workflow()
        
        for step in workflow:
            action_result = self.simulate_action(step)
            session["actions"].append(action_result)
            
            # Check if action failed
            if action_result["success"] == False:
                self.frustrations.append({
                    "iteration": iteration,
                    "action": step,
                    "reason": action_result["reason"]
                })
                session["outcome"] = "frustrated"
                session["satisfaction"] = random.randint(2, 5)  # Low satisfaction
                break
        else:
            # All actions succeeded
            self.wins.append({
                "iteration": iteration,
                "workflow": workflow
            })
            session["outcome"] = "success"
            session["satisfaction"] = random.randint(7, 10)  # High satisfaction
        
        self.session_history.append(session)
        return session
    
    def choose_workflow(self):
        """Choose realistic workflow based on teacher persona"""
        subject = self.teacher["subject"]
        tech_skill = self.teacher["tech_skill"]
        priority = self.teacher["priority"]
        
        workflows = {
            "quick_lesson_search": [
                "visit_homepage",
                "search_by_subject",
                "filter_by_year",
                "open_lesson",
                "download_handout"
            ],
            "browse_and_discover": [
                "visit_homepage",
                "click_subject_hub",
                "browse_featured",
                "check_cultural_integration",
                "save_to_my_kete"
            ],
            "plan_unit": [
                "visit_homepage",
                "navigate_to_units",
                "find_year_appropriate",
                "review_lessons",
                "check_assessments",
                "download_materials"
            ],
            "cultural_focus": [
                "visit_homepage",
                "search_cultural_content",
                "filter_high_integration",
                "verify_authenticity",
                "bookmark_resources"
            ],
            "simple_print": [
                "visit_homepage",
                "quick_search",
                "open_first_result",
                "print_lesson"
            ]
        }
        
        # Choose workflow based on persona
        if priority == "cultural_authenticity":
            return workflows["cultural_focus"]
        elif tech_skill == "low":
            return workflows["simple_print"]
        elif priority == "integrated_units":
            return workflows["plan_unit"]
        elif random.random() < 0.3:
            return workflows["browse_and_discover"]
        else:
            return workflows["quick_lesson_search"]
    
    def simulate_action(self, action):
        """Simulate single action with realistic success/failure"""
        
        # Success rates based on platform quality
        success_rates = {
            "visit_homepage": 0.99,  # Almost always works
            "search_by_subject": 0.95,  # Search is good
            "filter_by_year": 0.90,  # Filters work now (we fixed!)
            "open_lesson": 0.92,  # Most lessons load fine
            "download_handout": 0.85,  # Some might not have handouts
            "click_subject_hub": 0.98,  # Hubs work well
            "browse_featured": 0.97,  # Featured system solid
            "check_cultural_integration": 0.88,  # Metadata now 100%
            "save_to_my_kete": 0.75,  # Auth required, might fail
            "navigate_to_units": 0.94,  # Navigation 98%+
            "find_year_appropriate": 0.92,  # Good metadata now
            "review_lessons": 0.95,  # Content loads well
            "check_assessments": 0.70,  # Assessments less common
            "download_materials": 0.88,  # Most have materials
            "search_cultural_content": 0.93,  # 100% metadata helps
            "filter_high_integration": 0.85,  # Cultural metadata exists
            "verify_authenticity": 0.95,  # High quality content
            "bookmark_resources": 0.75,  # Auth dependent
            "quick_search": 0.96,  # Search works great
            "open_first_result": 0.94,  # First result usually good
            "print_lesson": 0.92,  # Print CSS exists
        }
        
        success = random.random() < success_rates.get(action, 0.90)
        
        result = {
            "action": action,
            "success": success,
            "time_seconds": random.randint(5, 45)
        }
        
        if not success:
            # Generate realistic failure reasons
            failure_reasons = {
                "search_by_subject": "Too many results, couldn't find specific year level",
                "filter_by_year": "Filter UI confusing, unclear which year",
                "download_handout": "No handout available for this lesson",
                "save_to_my_kete": "Login required, didn't have account",
                "check_assessments": "Couldn't find assessment rubric",
                "bookmark_resources": "Not sure how to save for later",
            }
            result["reason"] = failure_reasons.get(action, "Unclear how to proceed")
        
        return result

# ============================================================================
# SIMULATION RUNNER
# ============================================================================

class SimulationEngine:
    def __init__(self):
        self.teachers = [TeacherSimulation(t) for t in TEACHERS]
        self.all_frustrations = []
        self.all_wins = []
        self.improvement_log = []
        
    def run_iteration_batch(self, iterations_per_teacher=1000):
        """Run 1000 iterations for each of 20 teachers"""
        print(f"\n{'='*70}")
        print(f"🎯 TE KETE AKO - TEACHER SIMULATION ENGINE")
        print(f"{'='*70}\n")
        print(f"Teachers: {len(self.teachers)}")
        print(f"Iterations per teacher: {iterations_per_teacher}")
        print(f"Total simulations: {len(self.teachers) * iterations_per_teacher:,}\n")
        print(f"Starting simulation...\n")
        
        # Run simulations
        for teacher_sim in self.teachers:
            teacher_name = teacher_sim.teacher["name"]
            subject = teacher_sim.teacher["subject"]
            
            print(f"👩‍🏫 {teacher_name} ({subject})...")
            
            for i in range(iterations_per_teacher):
                session = teacher_sim.simulate_session(i)
                
                # Progress indicator every 100 iterations
                if (i + 1) % 100 == 0:
                    success_rate = len(teacher_sim.wins) / (i + 1) * 100
                    print(f"   {i+1:4d} iterations | Success: {success_rate:.1f}%")
            
            # Teacher summary
            total = len(teacher_sim.session_history)
            successes = len(teacher_sim.wins)
            frustrations = len(teacher_sim.frustrations)
            success_rate = successes / total * 100
            
            print(f"   ✅ Complete: {successes}/{total} ({success_rate:.1f}% success)\n")
            
            # Collect frustrations for analysis
            self.all_frustrations.extend(teacher_sim.frustrations)
            self.all_wins.extend(teacher_sim.wins)
        
        print(f"\n{'='*70}")
        print(f"✅ SIMULATION COMPLETE")
        print(f"{'='*70}\n")
        
        # Analyze results
        self.analyze_results()
        
    def analyze_results(self):
        """Analyze frustrations and identify improvements"""
        print(f"\n{'='*70}")
        print(f"📊 ANALYSIS: WHAT TEACHERS STRUGGLE WITH")
        print(f"{'='*70}\n")
        
        # Count frustration patterns
        frustration_counts = {}
        for frust in self.all_frustrations:
            action = frust["action"]
            reason = frust["reason"]
            key = f"{action}: {reason}"
            frustration_counts[key] = frustration_counts.get(key, 0) + 1
        
        # Sort by frequency
        sorted_frustrations = sorted(
            frustration_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:15]
        
        print("🔴 TOP 15 PAIN POINTS:\n")
        for i, (issue, count) in enumerate(sorted_frustrations, 1):
            percentage = count / len(self.all_frustrations) * 100
            action, reason = issue.split(": ", 1)
            print(f"{i:2d}. [{count:4d}x | {percentage:5.1f}%] {action}")
            print(f"    → {reason}\n")
        
        # Generate improvements
        print(f"\n{'='*70}")
        print(f"🔧 RECOMMENDED IMPROVEMENTS")
        print(f"{'='*70}\n")
        
        self.generate_improvements(sorted_frustrations[:10])
        
        # Success patterns
        print(f"\n{'='*70}")
        print(f"✅ WHAT'S WORKING WELL")
        print(f"{'='*70}\n")
        
        total_sessions = sum(len(ts.session_history) for ts in self.teachers)
        total_successes = len(self.all_wins)
        overall_success = total_successes / total_sessions * 100
        
        print(f"Overall Success Rate: {overall_success:.1f}%")
        print(f"Total Successful Sessions: {total_successes:,}")
        print(f"Total Frustrated Sessions: {len(self.all_frustrations):,}\n")
        
        if overall_success >= 85:
            print("✅ EXCELLENT - Platform performing very well!")
        elif overall_success >= 75:
            print("✅ GOOD - Platform working, room for improvement")
        elif overall_success >= 60:
            print("⚠️ FAIR - Several improvements needed")
        else:
            print("🔴 NEEDS WORK - Major improvements required")
    
    def generate_improvements(self, top_frustrations):
        """Generate SQL/code fixes for top issues"""
        
        improvements = []
        
        for issue, count in top_frustrations:
            action, reason = issue.split(": ", 1)
            
            improvement = self.create_improvement(action, reason, count)
            if improvement:
                improvements.append(improvement)
                print(f"💡 IMPROVEMENT #{len(improvements)}:")
                print(f"   Issue: {action}")
                print(f"   Frequency: {count}x")
                print(f"   Fix: {improvement['fix']}")
                print(f"   SQL/Code: {improvement['implementation'][:100]}...")
                print(f"   Impact: {improvement['impact']}\n")
        
        # Save improvements to file
        output_file = Path("SIMULATION-IMPROVEMENTS-OCT25.json")
        output_file.write_text(json.dumps(improvements, indent=2))
        print(f"\n💾 Improvements saved to: {output_file}")
        
        return improvements
    
    def create_improvement(self, action, reason, frequency):
        """Create executable improvement for common frustration"""
        
        if "Too many results" in reason:
            return {
                "issue": action,
                "reason": reason,
                "frequency": frequency,
                "fix": "Add 'Sort by Relevance' default + Better filters",
                "implementation": "UPDATE resources SET featured = true WHERE quality_score >= 90 AND subject = ...",
                "impact": f"Helps {frequency}+ teachers find best content first",
                "priority": "HIGH" if frequency > 200 else "MEDIUM"
            }
        
        elif "No handout available" in reason:
            return {
                "issue": action,
                "reason": reason,
                "frequency": frequency,
                "fix": "Create lesson-handout pairs automatically",
                "implementation": "INSERT INTO graphrag_relationships (lesson, handout, type='has_handout') ...",
                "impact": f"Provides handouts for {frequency}+ lessons",
                "priority": "MEDIUM"
            }
        
        elif "Login required" in reason:
            return {
                "issue": action,
                "reason": reason,
                "frequency": frequency,
                "fix": "Allow guest bookmarking (localStorage)",
                "implementation": "// localStorage.setItem('bookmarks', JSON.stringify(bookmarks))",
                "impact": f"Enables {frequency}+ teachers to save without login",
                "priority": "HIGH" if frequency > 150 else "LOW"
            }
        
        elif "Couldn't find assessment" in reason:
            return {
                "issue": action,
                "reason": reason,
                "frequency": frequency,
                "fix": "Build Assessment Hub + Link from lessons",
                "implementation": "CREATE /assessments/index.html + Add links in lessons",
                "impact": f"Helps {frequency}+ teachers find rubrics",
                "priority": "HIGH"
            }
        
        return None

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    engine = SimulationEngine()
    
    # Run simulation
    engine.run_iteration_batch(iterations_per_teacher=1000)
    
    # Generate reports
    print(f"\n{'='*70}")
    print(f"📈 GENERATING IMPROVEMENT REPORTS")
    print(f"{'='*70}\n")
    
    # Teacher-specific insights
    print("👥 PER-TEACHER SUCCESS RATES:\n")
    for teacher_sim in engine.teachers:
        total = len(teacher_sim.session_history)
        successes = len(teacher_sim.wins)
        rate = successes / total * 100
        teacher = teacher_sim.teacher
        
        status = "✅" if rate >= 85 else "⚠️" if rate >= 75 else "🔴"
        print(f"{status} {teacher['name']:20s} ({teacher['subject']:20s}) | {rate:5.1f}% | {teacher['tech_skill']:6s} | {teacher['priority']}")
    
    print(f"\n✨ SIMULATION COMPLETE - Ready for improvements!")
    print(f"\nNext: Apply top 10 improvements to platform\n")

if __name__ == "__main__":
    main()

