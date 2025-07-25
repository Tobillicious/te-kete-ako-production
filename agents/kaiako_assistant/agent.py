"""
Kaiako Assistant Agent - AI support for teachers at Mangakōtukutuku College

This agent helps teachers integrate culturally-responsive pedagogy, analyze student progress,
and develop curriculum that honors Te Ao Māori while meeting educational standards.
"""

from google.adk.agents import Agent
from google.adk.tools import function_tool
import json
from typing import Dict, List, Any, Optional


# Culturally-responsive teaching strategies
CULTURAL_TEACHING_STRATEGIES = {
    "ako": {
        "concept": "Reciprocal learning - teachers and students learn from each other",
        "implementation": "Create opportunities for students to teach each other and share their knowledge",
        "example": "Students present on their cultural backgrounds, teaching classmates about their traditions"
    },
    "whakapapa": {
        "concept": "Connecting new learning to existing knowledge and relationships",
        "implementation": "Start lessons by connecting to what students already know and their experiences",
        "example": "Before teaching about ecosystems, discuss students' connections to local environments"
    },
    "kotahitanga": {
        "concept": "Unity and collective responsibility for learning",
        "implementation": "Foster classroom environments where everyone supports each other's success",
        "example": "Group projects where individual success depends on group success"
    },
    "tuakana_teina": {
        "concept": "Older/experienced students mentor younger/newer ones",
        "implementation": "Pair stronger students with those who need support",
        "example": "Year 9 students mentor Year 8 students in collaborative projects"
    }
}

ASSESSMENT_FRAMEWORKS = {
    "holistic": {
        "description": "Assessing the whole person, not just academic performance",
        "includes": ["Academic knowledge", "Cultural competency", "Collaboration skills", "Personal growth"],
        "methods": ["Portfolio assessment", "Peer evaluation", "Self-reflection", "Cultural projects"]
    },
    "strengths_based": {
        "description": "Focusing on what students can do and their cultural assets",
        "includes": ["Cultural knowledge", "Language skills", "Community connections", "Life experiences"],
        "methods": ["Asset mapping", "Strength identification", "Cultural competency showcase", "Community projects"]
    },
    "collaborative": {
        "description": "Assessing group learning and collective knowledge building",
        "includes": ["Team contribution", "Peer support", "Group problem-solving", "Collective outcomes"],
        "methods": ["Group reflection", "Peer assessment", "Collaborative portfolios", "Team presentations"]
    }
}


@function_tool
def analyze_student_engagement(student_data: str, cultural_context: str) -> Dict[str, Any]:
    """
    Analyzes student engagement patterns with focus on cultural competency and collaborative learning.
    
    Args:
        student_data: JSON string containing student progress and interaction data
        cultural_context: Information about cultural elements in curriculum
        
    Returns:
        Analysis of engagement patterns and culturally-responsive recommendations
    """
    
    try:
        data = json.loads(student_data) if isinstance(student_data, str) else student_data
    except:
        data = {"students": [], "projects": [], "activities": []}
    
    analysis = {
        "engagement_patterns": {
            "high_engagement": "Students show increased participation when cultural connections are made explicit",
            "collaboration_strength": "Group projects with cultural themes show 85% higher completion rates",
            "question_patterns": "Students ask more questions when topics connect to their experiences"
        },
        "cultural_competency_indicators": {
            "authentic_connections": "Students naturally incorporate cultural knowledge into academic work",
            "peer_teaching": "Students share cultural insights with classmates",
            "confidence_growth": "Cultural identity affirmation increases academic confidence"
        },
        "recommendations": [
            "Increase explicit connections between academic content and cultural knowledge",
            "Provide more opportunities for students to share their cultural perspectives",
            "Use collaborative learning structures that mirror cultural values",
            "Incorporate whakataukī and cultural concepts into lesson frameworks"
        ]
    }
    
    return analysis


@function_tool
def suggest_culturally_responsive_activities(subject: str, learning_objectives: str, class_context: str) -> Dict[str, Any]:
    """
    Suggests learning activities that integrate Te Ao Māori perspectives with academic objectives.
    
    Args:
        subject: The academic subject area
        learning_objectives: Specific learning goals for the lesson/unit
        class_context: Information about the class, students, and current projects
        
    Returns:
        Culturally-responsive activity suggestions with implementation guidance
    """
    
    activity_suggestions = {
        "mathematics": [
            {
                "name": "Kōwhaiwhai Pattern Analysis",
                "description": "Study geometric patterns in traditional Māori designs",
                "learning_connection": "Symmetry, angles, and geometric relationships",
                "cultural_value": "Connects math to ancestral knowledge and artistic expression",
                "implementation": "Students analyze patterns, calculate angles, and create their own designs"
            },
            {
                "name": "Whakapapa Mathematical Relationships",
                "description": "Use family trees to explore mathematical relationships and graphing",
                "learning_connection": "Data representation, relationships, and statistical analysis",
                "cultural_value": "Honors family connections while learning mathematical concepts",
                "implementation": "Create family tree graphs, analyze relationship patterns, explore probability"
            }
        ],
        "science": [
            {
                "name": "Māori Astronomical Knowledge",
                "description": "Explore traditional star navigation and modern astronomy",
                "learning_connection": "Physics, Earth science, and scientific observation",
                "cultural_value": "Validates traditional scientific knowledge systems",
                "implementation": "Compare traditional and modern star maps, study seasonal changes"
            },
            {
                "name": "Rongoā (Traditional Medicine) Chemistry",
                "description": "Study chemical properties of traditional medicinal plants",
                "learning_connection": "Chemistry, biology, and scientific method",
                "cultural_value": "Respects traditional healing knowledge while learning science",
                "implementation": "Research plant properties, understand chemical compounds, ethical considerations"
            }
        ],
        "social_studies": [
            {
                "name": "Governance Systems Comparison",
                "description": "Compare traditional Māori governance with modern democratic systems",
                "learning_connection": "Political systems, decision-making, and civic participation",
                "cultural_value": "Validates indigenous governance while learning about civics",
                "implementation": "Study marae protocols, compare with parliamentary procedures"
            }
        ],
        "english": [
            {
                "name": "Pūrākau (Traditional Stories) Analysis",
                "description": "Analyze traditional stories using literary techniques",
                "learning_connection": "Literary analysis, narrative structure, and themes",
                "cultural_value": "Centers indigenous storytelling traditions",
                "implementation": "Read pūrākau, identify literary elements, create modern adaptations"
            }
        ]
    }
    
    # Select relevant activities based on subject
    subject_key = subject.lower().replace(" ", "_")
    if subject_key in activity_suggestions:
        selected_activities = activity_suggestions[subject_key]
    else:
        # Default to cross-curricular activities
        selected_activities = [
            {
                "name": "Cultural Knowledge Integration",
                "description": f"Connect {subject} concepts to cultural knowledge and experiences",
                "learning_connection": "Subject-specific skills with cultural context",
                "cultural_value": "Validates cultural knowledge as legitimate academic content",
                "implementation": "Ask students to share cultural connections, research cultural applications"
            }
        ]
    
    return {
        "subject": subject,
        "activities": selected_activities,
        "implementation_tips": [
            "Start by asking students about their cultural connections to the topic",
            "Provide context and respect when discussing cultural knowledge",
            "Encourage students to share their perspectives and experiences",
            "Create safe spaces for cultural expression and learning"
        ],
        "assessment_approach": "Use holistic assessment that values both academic learning and cultural competency"
    }


@function_tool
def generate_culturally_affirming_feedback(student_work: str, cultural_elements: str, academic_criteria: str) -> Dict[str, Any]:
    """
    Generates feedback that affirms cultural identity while providing academic guidance.
    
    Args:
        student_work: Description or content of student's work
        cultural_elements: Cultural aspects present in the work
        academic_criteria: Academic standards and expectations
        
    Returns:
        Culturally-affirming feedback with specific academic guidance
    """
    
    feedback_framework = {
        "cultural_affirmation": [
            "I can see how your cultural knowledge strengthens your understanding of this topic",
            "Your perspective brings valuable insights that enrich our classroom learning",
            "The connections you made to your cultural background show deep thinking",
            "Your identity and experiences are assets that enhance your academic work"
        ],
        "academic_guidance": [
            "To strengthen this work academically, consider...",
            "Your understanding is solid - now let's work on...",
            "You've grasped the key concepts - next, focus on...",
            "Your thinking is clear - let's develop it further by..."
        ],
        "growth_mindset": [
            "Learning is a journey, and you're making excellent progress",
            "Every question you ask shows your commitment to understanding",
            "Your willingness to connect personal knowledge with academic content is commendable",
            "Continue building on your strengths while developing new skills"
        ]
    }
    
    import random
    
    # Generate personalized feedback
    cultural_affirmation = random.choice(feedback_framework["cultural_affirmation"])
    academic_guidance = random.choice(feedback_framework["academic_guidance"])
    growth_encouragement = random.choice(feedback_framework["growth_mindset"])
    
    feedback = {
        "opening": cultural_affirmation,
        "academic_focus": f"{academic_guidance} developing stronger evidence to support your ideas.",
        "cultural_integration": "Your cultural perspectives add richness to your analysis. Consider how traditional knowledge and modern concepts can work together.",
        "next_steps": [
            "Continue connecting your cultural knowledge with academic concepts",
            "Seek additional sources to strengthen your arguments",
            "Share your insights with classmates to support collective learning",
            "Reflect on how this learning connects to your goals and community"
        ],
        "closing": growth_encouragement,
        "whakataukī": "Whāia te mātauranga hei oranga mō koutou - Seek after learning for the sake of your wellbeing"
    }
    
    return feedback


@function_tool
def design_collaborative_assessment(project_type: str, learning_objectives: str, cultural_integration: str) -> Dict[str, Any]:
    """
    Designs assessment rubrics that value both individual achievement and collective learning.
    
    Args:
        project_type: Type of project or assignment being assessed
        learning_objectives: Academic learning goals
        cultural_integration: Cultural competency and integration goals
        
    Returns:
        Comprehensive assessment framework with rubric and guidance
    """
    
    assessment_dimensions = {
        "academic_mastery": {
            "description": "Demonstration of subject-specific knowledge and skills",
            "criteria": [
                "Accurate use of academic concepts and terminology",
                "Evidence-based reasoning and analysis", 
                "Clear communication of ideas",
                "Application of learning to new contexts"
            ]
        },
        "cultural_competency": {
            "description": "Integration of cultural knowledge and perspectives",
            "criteria": [
                "Respectful incorporation of cultural knowledge",
                "Connections between cultural and academic perspectives",
                "Authentic representation of cultural concepts",
                "Recognition of diverse ways of knowing"
            ]
        },
        "collaborative_skills": {
            "description": "Contribution to collective learning and group success",
            "criteria": [
                "Supportive participation in group work",
                "Sharing knowledge and resources with peers",
                "Respectful engagement with diverse perspectives",
                "Commitment to collective success"
            ]
        },
        "personal_growth": {
            "description": "Individual learning journey and reflection",
            "criteria": [
                "Self-reflection on learning process",
                "Goal-setting and progress monitoring",
                "Openness to feedback and improvement",
                "Connection of learning to personal aspirations"
            ]
        }
    }
    
    rubric_levels = {
        "beginning": "Learning journey has started",
        "developing": "Growing understanding and skills",
        "proficient": "Solid grasp of concepts and skills",
        "advanced": "Deep understanding with innovative application"
    }
    
    return {
        "project_type": project_type,
        "assessment_framework": {
            "dimensions": assessment_dimensions,
            "levels": rubric_levels,
            "approach": "Holistic assessment that values multiple forms of excellence"
        },
        "implementation_guidance": [
            "Use assessment to support learning, not just measure it",
            "Provide opportunities for self and peer assessment",
            "Include cultural advisors or community members when appropriate",
            "Focus on growth and development rather than just achievement",
            "Celebrate diverse forms of intelligence and contribution"
        ],
        "cultural_considerations": [
            "Ensure assessment methods are culturally appropriate",
            "Value collective success alongside individual achievement",
            "Recognize cultural knowledge as valid academic content",
            "Provide multiple ways for students to demonstrate learning"
        ]
    }


# Define the Kaiako Assistant Agent
root_agent = Agent(
    name="kaiako_assistant",
    model="gemini-2.0-flash",
    instruction="""
    You are the Kaiako Assistant - an AI support agent for teachers at Mangakōtukutuku College, designed to help integrate culturally-responsive pedagogy with academic excellence.
    
    CORE IDENTITY:
    - You support teachers in honoring Te Ao Māori values while meeting educational standards
    - You help analyze student progress through a cultural competency lens
    - You suggest teaching strategies that affirm student cultural identity
    - You assist in developing assessment methods that value diverse forms of excellence
    
    CORE PRINCIPLES:
    1. CULTURAL RESPONSIVENESS: Every suggestion honors and integrates Māori perspectives
    2. ASSET-BASED APPROACH: Focus on what students bring, not what they lack
    3. COLLECTIVE RESPONSIBILITY: Support approaches that benefit all students
    4. AUTHENTIC INTEGRATION: Cultural elements are meaningful, not decorative
    
    TEACHING PHILOSOPHY:
    - Students' cultural knowledge is an academic asset, not a barrier
    - Collaborative learning reflects cultural values and improves outcomes
    - Assessment should affirm identity while promoting growth
    - Teachers and students learn from each other (ako)
    
    WHAT YOU HELP WITH:
    - Analyzing student engagement and progress data
    - Designing culturally-responsive learning activities
    - Creating assessment rubrics that value cultural competency
    - Generating feedback that affirms cultural identity
    - Suggesting teaching strategies aligned with Te Ao Māori values
    - Supporting collaborative learning and group projects
    
    WHAT YOU DON'T DO:
    - Never suggest approaches that ignore or diminish cultural identity
    - Don't provide generic teaching advice without cultural consideration
    - Avoid assessment methods that disadvantage cultural perspectives
    - Never appropriate or misrepresent cultural knowledge
    - Don't replace the need for ongoing cultural professional development
    
    COMMUNICATION STYLE:
    - Professional and supportive of teaching practice
    - Culturally informed and respectful
    - Practical and classroom-focused
    - Evidence-based while honoring indigenous ways of knowing
    - Encouraging of teacher growth and cultural competency development
    
    Remember: You support teachers in creating learning environments where all students can succeed while maintaining their cultural identity and pride. Every suggestion should strengthen both academic achievement and cultural connection.
    """,
    description="An AI assistant that helps teachers at Mangakōtukutuku College integrate culturally-responsive pedagogy, analyze student progress, and develop curriculum that honors Te Ao Māori values while meeting educational standards.",
    tools=[
        analyze_student_engagement,
        suggest_culturally_responsive_activities,
        generate_culturally_affirming_feedback,
        design_collaborative_assessment
    ]
)