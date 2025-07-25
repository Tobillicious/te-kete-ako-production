"""
Ākonga Companion Agent - Culturally-aware learning support for students at Mangakōtukutuku College

This agent provides personalized learning guidance while honoring Te Ao Māori values and fostering
both individual growth and collective knowledge building.
"""

from google.adk.agents import Agent
from google.adk.tools import function_tool
import json
import os
from typing import Dict, List, Any


# Cultural knowledge base - Te Ao Māori concepts and connections
CULTURAL_KNOWLEDGE = {
    "whakapapa": {
        "concept": "Genealogical connections and relationships",
        "learning_connection": "Everything is connected - academic subjects relate to each other and to your identity",
        "example": "Mathematics patterns reflect natural relationships, just like whakapapa shows family connections"
    },
    "manaakitanga": {
        "concept": "Hospitality, care, and support for others", 
        "learning_connection": "Learning together strengthens everyone - support your classmates",
        "example": "When you help a friend understand a concept, you both learn more deeply"
    },
    "kaitiakitanga": {
        "concept": "Guardianship and responsibility for the environment",
        "learning_connection": "Take care of your learning environment and resources",
        "example": "Protecting our school's computers helps everyone learn better"
    },
    "whakatōhia": {
        "concept": "Collective decision-making and consensus",
        "learning_connection": "Group projects work best when everyone contributes their knowledge",
        "example": "In society design projects, combine everyone's ideas for the strongest outcome"
    }
}

WHAKATAUKI = [
    {
        "mi": "He aha te mea nui o te ao? He tangata, he tangata, he tangata.",
        "en": "What is the most important thing in the world? It is people, it is people, it is people.",
        "learning_context": "Your learning is not just for you - it serves your whānau and community"
    },
    {
        "mi": "Whāia te mātauranga hei oranga mō koutou.",
        "en": "Seek after learning for the sake of your wellbeing.",
        "learning_context": "Education is a pathway to wellness for yourself and others"
    },
    {
        "mi": "He waka eke noa.",
        "en": "We are all in this together.",
        "learning_context": "Your classmates are your learning whānau - support each other"
    },
    {
        "mi": "Mā te kōrero, ka mōhio; mā te mōhio, ka mārama; mā te mārama, ka mātau; mā te mātau, ka ora.",
        "en": "Through discussion comes awareness; through awareness comes understanding; through understanding comes knowledge; through knowledge comes life.",
        "learning_context": "Talk about your learning - share ideas and ask questions to deepen understanding"
    }
]


@function_tool
def get_cultural_guidance(topic: str, learning_context: str) -> Dict[str, Any]:
    """
    Provides culturally-relevant guidance for academic topics by connecting them to Te Ao Māori concepts.
    
    Args:
        topic: The academic subject or topic being studied
        learning_context: Current learning situation or challenge
        
    Returns:
        Cultural wisdom and connections to support learning
    """
    
    # Find relevant cultural concepts
    relevant_concepts = []
    for concept, details in CULTURAL_KNOWLEDGE.items():
        if any(keyword in topic.lower() for keyword in ['group', 'team', 'together']):
            if concept in ['manaakitanga', 'whakatōhia']:
                relevant_concepts.append({
                    'concept': concept,
                    'guidance': details['learning_connection'],
                    'example': details['example']
                })
        elif any(keyword in topic.lower() for keyword in ['environment', 'care', 'responsibility']):
            if concept == 'kaitiakitanga':
                relevant_concepts.append({
                    'concept': concept,
                    'guidance': details['learning_connection'],
                    'example': details['example']
                })
        elif any(keyword in topic.lower() for keyword in ['connection', 'relationship', 'pattern']):
            if concept == 'whakapapa':
                relevant_concepts.append({
                    'concept': concept,
                    'guidance': details['learning_connection'],
                    'example': details['example']
                })
    
    # Default to manaakitanga if no specific match
    if not relevant_concepts:
        relevant_concepts.append({
            'concept': 'manaakitanga',
            'guidance': CULTURAL_KNOWLEDGE['manaakitanga']['learning_connection'],
            'example': CULTURAL_KNOWLEDGE['manaakitanga']['example']
        })
    
    return {
        'cultural_concepts': relevant_concepts,
        'topic': topic,
        'context': learning_context
    }


@function_tool  
def select_appropriate_whakatauki(situation: str, emotional_context: str) -> Dict[str, Any]:
    """
    Selects an appropriate whakataukī (proverb) to provide wisdom and encouragement for the learning situation.
    
    Args:
        situation: Description of the current learning situation
        emotional_context: Student's emotional state or challenge
        
    Returns:
        An appropriate whakataukī with explanation and application
    """
    
    # Match situation to appropriate whakataukī
    if any(keyword in situation.lower() for keyword in ['difficult', 'hard', 'struggling', 'challenge']):
        selected = WHAKATAUKI[1]  # Seek learning for wellbeing
    elif any(keyword in situation.lower() for keyword in ['group', 'team', 'together', 'collaboration']):
        selected = WHAKATAUKI[2]  # We are all in this together
    elif any(keyword in situation.lower() for keyword in ['discussion', 'question', 'talk', 'share']):
        selected = WHAKATAUKI[3]  # Through discussion comes knowledge
    else:
        selected = WHAKATAUKI[0]  # People are most important
    
    return {
        'whakatauki': {
            'te_reo': selected['mi'],
            'english': selected['en'],
            'learning_application': selected['learning_context']
        },
        'situation': situation,
        'guidance': f"This whakataukī reminds us that {selected['learning_context'].lower()}"
    }


@function_tool
def provide_learning_encouragement(progress_data: str, cultural_identity: str) -> Dict[str, Any]:
    """
    Provides personalized encouragement that honors the student's cultural identity and learning progress.
    
    Args:
        progress_data: Information about student's academic progress and achievements
        cultural_identity: Student's cultural background and identity information
        
    Returns:
        Culturally-affirming encouragement and next steps
    """
    
    # Parse progress data (in a real system, this would come from Supabase)
    try:
        progress = json.loads(progress_data) if isinstance(progress_data, str) else progress_data
    except:
        progress = {"general": "continuing to learn"}
    
    encouragements = [
        f"Your ancestors would be proud of your commitment to learning, e hoa. Every step forward honors their wisdom.",
        f"You carry the strength of your tipuna (ancestors) in your learning journey. Kia kaha!",
        f"Your questions show deep thinking - this is the Māori way of seeking understanding through inquiry.",
        f"Each project you complete adds to the collective knowledge of our learning whānau.",
        f"Your cultural perspective brings unique value to every discussion and project."
    ]
    
    import random
    selected_encouragement = random.choice(encouragements)
    
    next_steps = [
        "Continue connecting your cultural knowledge with academic learning",
        "Share your insights with classmates - your perspective strengthens everyone",
        "Ask questions fearlessly - curiosity is a gift to be celebrated",
        "Remember that learning is a collective journey, not a competition"
    ]
    
    return {
        'encouragement': selected_encouragement,
        'cultural_affirmation': "Your identity and heritage are strengths that enhance your learning",
        'next_steps': next_steps,
        'reminder': "He tangata, he tangata, he tangata - you are part of something greater"
    }


@function_tool
def suggest_learning_connections(current_topic: str, student_interests: str) -> Dict[str, Any]:
    """
    Suggests connections between current academic topics and student interests, including cultural knowledge.
    
    Args:
        current_topic: The academic subject or topic being studied
        student_interests: Student's personal interests and cultural connections
        
    Returns:
        Relevant connections and learning pathways
    """
    
    connections = {
        'mathematics': {
            'cultural': 'Traditional Māori patterns (kōwhaiwhai) use mathematical principles',
            'modern': 'Math helps understand science, technology, and even social patterns',
            'practical': 'Budgeting for whānau, calculating materials for projects'
        },
        'science': {
            'cultural': 'Traditional Māori knowledge of stars, plants, and seasons',
            'modern': 'Environmental science connects to kaitiakitanga values',
            'practical': 'Understanding how things work helps you take care of them'
        },
        'english': {
            'cultural': 'Storytelling is central to Māori culture - pūrākau carry wisdom',
            'modern': 'Communication skills help you share your voice with the world',
            'practical': 'Writing helps you express ideas and advocate for your community'
        },
        'social_studies': {
            'cultural': 'Understanding history helps you know where you come from',
            'modern': 'Current events affect your whānau and community',
            'practical': 'Knowing your rights and civic duties empowers you'
        }
    }
    
    # Find relevant connection
    topic_key = None
    for key in connections.keys():
        if key in current_topic.lower():
            topic_key = key
            break
    
    if not topic_key:
        topic_key = 'english'  # Default
    
    connection_set = connections[topic_key]
    
    return {
        'topic': current_topic,
        'cultural_connection': connection_set['cultural'],  
        'modern_relevance': connection_set['modern'],
        'practical_application': connection_set['practical'],
        'encouragement': f"Your learning in {current_topic} connects to both your cultural heritage and your future goals"
    }


# Define the Ākonga Companion Agent
root_agent = Agent(
    name="akonga_companion",
    model="gemini-2.0-flash",
    instruction="""
    You are the Ākonga Companion - a culturally-aware AI learning support agent for students at Mangakōtukutuku College.
    
    CORE IDENTITY:
    - You understand and honor Te Ao Māori values in all interactions
    - You support both individual learning and collective knowledge building
    - You help students see connections between their cultural identity and academic learning
    - You encourage questions, collaboration, and cultural pride
    
    CORE PRINCIPLES:
    1. MANAAKITANGA: Show care and support for every student
    2. WHAKATŌHIA: Encourage collaborative learning and group wisdom
    3. KAITIAKITANGA: Help students take responsibility for their learning
    4. WHAKAPAPA: Connect all learning to relationships and identity
    
    COMMUNICATION STYLE:
    - Warm, encouraging, and culturally affirming
    - Use appropriate Te Reo Māori terms with respect
    - Connect academic concepts to cultural knowledge when relevant
    - Acknowledge student strengths and cultural perspectives
    - Encourage questions and collaborative learning
    
    WHAT YOU DO:
    - Provide learning guidance that honors cultural identity
    - Help students connect academic topics to their interests and heritage
    - Offer encouragement during challenging learning moments
    - Suggest study strategies that align with cultural values
    - Support collaborative project work with cultural wisdom
    
    WHAT YOU DON'T DO:
    - Never appropriate or misuse cultural knowledge
    - Don't make assumptions about student cultural backgrounds
    - Avoid giving direct answers - guide students to discover
    - Don't replace teacher authority or cultural experts
    - Never discourage cultural identity or perspectives
    
    Remember: You are a learning companion, not a replacement for teachers, whānau, or cultural advisors. Your role is to support and encourage learning while honoring the cultural richness students bring to their education.
    """,
    description="A culturally-aware learning companion that supports students at Mangakōtukutuku College by connecting academic learning with Te Ao Māori values and cultural identity.",
    tools=[
        get_cultural_guidance,
        select_appropriate_whakatauki, 
        provide_learning_encouragement,
        suggest_learning_connections
    ]
)