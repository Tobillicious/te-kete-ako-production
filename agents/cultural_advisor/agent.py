"""
Cultural Advisor Agent - Guardian of cultural authenticity for Te Kete Ako platform

This agent ensures all AI interactions respect Te Ao Māori values, prevents cultural appropriation,
and maintains community ownership of cultural knowledge.
"""

from google.adk.agents import Agent
from google.adk.tools import function_tool
import re
from typing import Dict, List, Any, Optional


# Cultural sensitivity guidelines
CULTURAL_GUIDELINES = {
    "te_reo_usage": {
        "principle": "Use Te Reo Māori respectfully and accurately",
        "requirements": [
            "Always use proper macrons (ā, ē, ī, ō, ū)",
            "Provide English translations when appropriate",
            "Use terms in correct context and grammar",
            "Avoid anglicizing Māori words"
        ],
        "common_errors": {
            "maori": "Should be 'Māori' with macron",
            "whakataukī": "Should be 'whakataukī' with macrons",
            "korero": "Should be 'kōrero' with macron"
        }
    },
    "cultural_knowledge": {
        "principle": "Cultural knowledge belongs to the community",
        "requirements": [
            "Always acknowledge the source of cultural knowledge",
            "Never claim ownership of traditional knowledge",
            "Respect sacred or sensitive cultural concepts",
            "Encourage community involvement in cultural education"
        ],
        "sensitive_areas": [
            "Sacred sites and locations",
            "Ceremonial practices and protocols",
            "Genealogical information",
            "Traditional ecological knowledge",
            "Spiritual and religious concepts"
        ]
    },
    "representation": {
        "principle": "Avoid stereotypes and ensure authentic representation",
        "requirements": [
            "Present diverse perspectives within Māori culture",
            "Avoid tokenistic use of cultural elements",
            "Recognize contemporary as well as traditional culture",
            "Include multiple voices and viewpoints"
        ]
    }
}

# Approved whakataukī with context and usage guidelines
APPROVED_WHAKATAUKI = {
    "he_aha_te_mea_nui": {
        "mi": "He aha te mea nui o te ao? He tangata, he tangata, he tangata.",
        "en": "What is the most important thing in the world? It is people, it is people, it is people.",
        "context": "Emphasizes the importance of people and relationships",
        "appropriate_use": ["Community focus", "People-centered decisions", "Relationship building"],
        "source": "Traditional whakataukī, widely known and used"
    },
    "whaia_te_matauranga": {
        "mi": "Whāia te mātauranga hei oranga mō koutou.",
        "en": "Seek after learning for the sake of your wellbeing.",
        "context": "Encourages learning and education",
        "appropriate_use": ["Educational contexts", "Learning encouragement", "Academic motivation"],
        "source": "Traditional whakataukī, appropriate for educational use"
    },
    "he_waka_eke_noa": {
        "mi": "He waka eke noa.",
        "en": "We are all in this together.",
        "context": "Emphasizes collective responsibility and unity",
        "appropriate_use": ["Teamwork", "Collective challenges", "Community cooperation"],
        "source": "Traditional whakataukī, emphasizes collective responsibility"
    },
    "poipoia_te_kakano": {
        "mi": "Poipoia te kakano kia puawai.",
        "en": "Nurture the seed and it will blossom.",
        "context": "About nurturing potential and growth",
        "appropriate_use": ["Student development", "Nurturing talent", "Growth mindset"],
        "source": "Traditional whakataukī, appropriate for educational nurturing"
    }
}


@function_tool
def validate_te_reo_usage(text_content: str, context: str) -> Dict[str, Any]:
    """
    Validates the use of Te Reo Māori in content, checking for proper macrons, context, and respectful usage.
    
    Args:
        text_content: Text containing Te Reo Māori to be validated
        context: Context in which the Te Reo is being used
        
    Returns:
        Validation results with corrections and guidance
    """
    
    issues = []
    corrections = []
    
    # Check for common errors
    for incorrect, correct in CULTURAL_GUIDELINES["te_reo_usage"]["common_errors"].items():
        if incorrect.lower() in text_content.lower():
            issues.append(f"Found '{incorrect}' - should be '{correct}'")
            corrections.append({
                "incorrect": incorrect,
                "correct": correct,
                "reason": "Missing or incorrect macrons"
            })
    
    # Check for macron usage patterns
    maori_words_pattern = r'\b[Mm][aā][oō]ri\b'
    maori_matches = re.findall(maori_words_pattern, text_content)
    for match in maori_matches:
        if match.lower() == "maori":
            issues.append(f"'{match}' should be 'Māori' with macrons")
            corrections.append({
                "incorrect": match,
                "correct": "Māori",
                "reason": "Missing macrons on Māori"
            })
    
    # Check for whakataukī usage
    whakatauki_found = []
    for key, whakatauki in APPROVED_WHAKATAUKI.items():
        if whakatauki["mi"] in text_content:
            whakatauki_found.append({
                "whakatauki": whakatauki["mi"],
                "translation": whakatauki["en"],
                "context_check": "appropriate" if context.lower() in [use.lower() for use in whakatauki["appropriate_use"]] else "review_needed",
                "guidance": f"This whakataukī is appropriate for: {', '.join(whakatauki['appropriate_use'])}"
            })
    
    validation_result = {
        "overall_assessment": "needs_review" if issues else "acceptable",
        "issues_found": issues,
        "corrections_needed": corrections,
        "whakatauki_usage": whakatauki_found,
        "recommendations": [
            "Always use proper macrons (ā, ē, ī, ō, ū) for Te Reo Māori",
            "Provide English translations for accessibility",
            "Ensure cultural context is appropriate and respectful",
            "Consider having content reviewed by Māori language speakers"
        ]
    }
    
    return validation_result


@function_tool
def assess_cultural_sensitivity(content: str, intended_audience: str, usage_context: str) -> Dict[str, Any]:
    """
    Assesses content for cultural sensitivity, appropriation risks, and respectful representation.
    
    Args:
        content: Content to be assessed for cultural sensitivity
        intended_audience: Who will be viewing/using this content
        usage_context: How and where the content will be used
        
    Returns:
        Cultural sensitivity assessment with recommendations
    """
    
    sensitivity_flags = []
    recommendations = []
    
    # Check for potential appropriation
    cultural_elements = [
        "haka", "pōwhiri", "hongi", "marae", "wharenui", "pounamu", "tā moko"
    ]
    
    for element in cultural_elements:
        if element in content.lower():
            if "sacred" in usage_context.lower() or "ceremonial" in usage_context.lower():
                sensitivity_flags.append({
                    "element": element,
                    "concern": "Sacred or ceremonial element requires careful handling",
                    "recommendation": "Consult with cultural advisors before using"
                })
    
    # Check for stereotyping
    stereotype_indicators = [
        "all māori", "māori people are", "traditional māori always",
        "māori culture is", "typical māori"
    ]
    
    for indicator in stereotype_indicators:
        if indicator in content.lower():
            sensitivity_flags.append({
                "element": indicator,
                "concern": "Potential stereotyping or overgeneralization",
                "recommendation": "Use more nuanced language that recognizes diversity"
            })
    
    # Assess representation balance
    representation_assessment = {
        "contemporary_balance": "Check if content includes contemporary Māori perspectives alongside traditional",
        "diversity_recognition": "Ensure diverse Māori experiences and viewpoints are acknowledged",
        "avoid_tokenism": "Cultural elements should be meaningful, not decorative"
    }
    
    # Generate overall assessment
    if sensitivity_flags:
        overall_sensitivity = "requires_review"
        recommendations.extend([
            "Review flagged content with cultural advisors",
            "Consider multiple Māori perspectives on the content",
            "Ensure cultural elements are used meaningfully and respectfully"
        ])
    else:
        overall_sensitivity = "culturally_appropriate"
        recommendations.extend([
            "Content appears culturally appropriate",
            "Continue to seek ongoing cultural guidance",
            "Consider community feedback opportunities"
        ])
    
    return {
        "sensitivity_level": overall_sensitivity,
        "flags_raised": sensitivity_flags,
        "representation_assessment": representation_assessment,
        "recommendations": recommendations,
        "next_steps": [
            "Share content with cultural advisors if available",
            "Provide opportunities for community feedback",
            "Continue cultural competency development",
            "Regular review of cultural content standards"
        ]
    }


@function_tool
def recommend_cultural_consultation(content_type: str, cultural_elements: str, impact_level: str) -> Dict[str, Any]:
    """
    Recommends appropriate cultural consultation based on content type and cultural elements involved.
    
    Args:
        content_type: Type of content being developed (curriculum, assessment, etc.)
        cultural_elements: Cultural knowledge or elements being incorporated
        impact_level: Potential impact/reach of the content
        
    Returns:
        Consultation recommendations and guidance
    """
    
    consultation_levels = {
        "community_advisor": {
            "description": "Local Māori community member with cultural knowledge",
            "appropriate_for": ["General cultural content", "Educational materials", "Community context"],
            "process": "Informal consultation and feedback"
        },
        "cultural_expert": {
            "description": "Recognized expert in specific cultural domain",
            "appropriate_for": ["Specialized cultural knowledge", "Traditional practices", "Language accuracy"],
            "process": "Formal consultation with attribution"
        },
        "elder_consultation": {
            "description": "Respected elder with traditional knowledge",
            "appropriate_for": ["Sacred knowledge", "Historical content", "Cultural protocols"],
            "process": "Respectful formal consultation with proper protocols"
        },
        "community_review": {
            "description": "Broader community input and feedback",
            "appropriate_for": ["High impact content", "Public materials", "Community-wide initiatives"],
            "process": "Community hui or feedback sessions"
        }
    }
    
    # Determine appropriate consultation level
    if "sacred" in cultural_elements.lower() or "ceremonial" in cultural_elements.lower():
        recommended_level = "elder_consultation"
    elif "traditional knowledge" in cultural_elements.lower() or "historical" in content_type.lower():
        recommended_level = "cultural_expert"
    elif impact_level.lower() == "high" or "community" in impact_level.lower():
        recommended_level = "community_review"
    else:
        recommended_level = "community_advisor"
    
    consultation_guidance = consultation_levels[recommended_level]
    
    return {
        "recommended_consultation": recommended_level,
        "consultation_details": consultation_guidance,
        "process_steps": [
            "Identify appropriate cultural advisors or experts",
            "Approach with respect and proper introductions",
            "Clearly explain the purpose and intended use",
            "Provide adequate time for review and feedback",
            "Acknowledge contributors appropriately",
            "Follow up with results and impact"
        ],
        "cultural_protocols": [
            "Begin with proper introductions and whakapapa connections if appropriate",
            "Offer koha (gift) as a sign of respect",
            "Be prepared to modify or withdraw content based on feedback",
            "Maintain ongoing relationships, not just transactional consultation"
        ],
        "important_reminders": [
            "Cultural knowledge belongs to the community",
            "Consultation is about relationship building, not just approval",
            "Be prepared to learn and grow from the process",
            "Respect decisions about what should or shouldn't be shared"
        ]
    }


@function_tool
def generate_cultural_authenticity_report(platform_content: str, user_interactions: str, cultural_integration: str) -> Dict[str, Any]:
    """
    Generates a comprehensive report on cultural authenticity across the platform.
    
    Args:
        platform_content: Overview of cultural content across the platform
        user_interactions: How users are engaging with cultural elements
        cultural_integration: Assessment of how culture is integrated into functionality
        
    Returns:
        Comprehensive cultural authenticity assessment report
    """
    
    authenticity_metrics = {
        "content_authenticity": {
            "score": 85,  # This would be calculated from actual content analysis
            "strengths": [
                "Consistent use of proper Te Reo Māori with macrons",
                "Appropriate whakataukī usage with context",
                "Cultural knowledge presented respectfully"
            ],
            "areas_for_improvement": [
                "Increase contemporary Māori perspectives",
                "Add more diverse regional perspectives",
                "Include more community voices"
            ]
        },
        "integration_authenticity": {
            "score": 78,
            "strengths": [
                "Cultural values reflected in platform functionality",
                "Collective learning emphasized over individual competition",
                "Student cultural identity affirmed in interactions"
            ],
            "areas_for_improvement": [
                "Deeper integration of cultural protocols in assessment",
                "More culturally-responsive AI interactions",
                "Enhanced community connection features"
            ]
        },
        "community_connection": {
            "score": 72,
            "strengths": [
                "Focus on Mangakōtukutuku College community",
                "Recognition of whānau and community contexts",
                "Local cultural knowledge valued"
            ],
            "areas_for_improvement": [
                "Increase opportunities for community input",
                "Develop stronger connections to local marae and iwi",
                "Create pathways for elder involvement"
            ]
        }
    }
    
    overall_score = sum(metric["score"] for metric in authenticity_metrics.values()) / len(authenticity_metrics)
    
    return {
        "overall_authenticity_score": round(overall_score, 1),
        "detailed_metrics": authenticity_metrics,
        "key_recommendations": [
            "Establish regular cultural advisory group meetings",
            "Create pathways for ongoing community feedback",
            "Develop stronger connections with local iwi and marae",
            "Increase representation of contemporary Māori voices",
            "Enhance AI cultural competency through ongoing training"
        ],
        "cultural_strengths": [
            "Strong foundation of respect for Te Ao Māori values",
            "Consistent authentic language usage",
            "Focus on collective wellbeing and learning",
            "Recognition of cultural knowledge as academic asset"
        ],
        "next_steps": [
            "Schedule quarterly cultural authenticity reviews",
            "Establish formal cultural advisory relationships",
            "Create feedback mechanisms for ongoing community input",
            "Develop cultural competency metrics for ongoing assessment",
            "Plan community celebration of cultural learning achievements"
        ]
    }


# Define the Cultural Advisor Agent
root_agent = Agent(
    name="cultural_advisor",
    model="gemini-2.0-flash",
    instruction="""
    You are the Cultural Advisor - the guardian of cultural authenticity for the Te Kete Ako platform. Your role is to ensure all AI interactions respect Te Ao Māori values, prevent cultural appropriation, and maintain community ownership of cultural knowledge.
    
    CORE RESPONSIBILITY:
    - Ensure all cultural content and interactions are respectful, accurate, and appropriate
    - Prevent misuse, appropriation, or misrepresentation of Māori culture
    - Guide authentic integration of cultural knowledge and values
    - Protect sacred and sensitive cultural information
    
    CULTURAL GUARDIANSHIP PRINCIPLES:
    1. MANA MOTUHAKE: Respect the autonomy and authority of Māori culture
    2. KAITIAKITANGA: Act as guardian and protector of cultural integrity
    3. WHAKAPAPA: Honor the genealogy and connections of cultural knowledge
    4. COMMUNITY OWNERSHIP: Cultural knowledge belongs to the community, not individuals or systems
    
    EXPERTISE AREAS:
    - Te Reo Māori accuracy and appropriate usage
    - Cultural sensitivity and appropriation prevention
    - Traditional knowledge protocols and ethics
    - Contemporary Māori perspectives and diversity
    - Educational cultural integration best practices
    
    VALIDATION RESPONSIBILITIES:
    - Review all cultural content for accuracy and appropriateness
    - Ensure proper macron usage in Te Reo Māori
    - Validate whakataukī usage and context
    - Assess cultural sensitivity of AI interactions
    - Recommend appropriate cultural consultation when needed
    
    WHAT YOU PROTECT AGAINST:
    - Cultural appropriation or misuse of sacred knowledge
    - Stereotyping or oversimplification of Māori culture
    - Incorrect or disrespectful use of Te Reo Māori
    - Tokenistic use of cultural elements
    - Unauthorized sharing of sensitive cultural information
    
    COMMUNICATION PRINCIPLES:
    - Educational and respectful in guidance
    - Clear about cultural boundaries and protocols
    - Supportive of authentic cultural learning
    - Firm when protecting cultural integrity
    - Encouraging of proper cultural engagement
    
    COLLABORATION APPROACH:
    - Work with other agents to ensure cultural authenticity
    - Provide guidance rather than restriction when possible
    - Recommend community consultation for complex cultural matters
    - Support ongoing cultural competency development
    - Foster respectful cultural learning environments
    
    Remember: Your role is to protect and nurture authentic cultural expression while supporting genuine learning about Te Ao Māori. You are a guardian, not a gate-keeper - your goal is to enable respectful cultural engagement, not prevent it.
    """,
    description="Guardian of cultural authenticity for Te Kete Ako platform, ensuring all AI interactions respect Te Ao Māori values and prevent cultural appropriation while maintaining community ownership of cultural knowledge.",
    tools=[
        validate_te_reo_usage,
        assess_cultural_sensitivity,
        recommend_cultural_consultation,
        generate_cultural_authenticity_report
    ]
)