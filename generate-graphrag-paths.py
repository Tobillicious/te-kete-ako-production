#!/usr/bin/env python3
"""
GENERATE GRAPHRAG PATH LOOKUP TABLE
Query Supabase database to get all actual resource paths
Creates comprehensive lookup table for intelligent-link-fixer.py
"""

import json

# This script would query the Supabase database via MCP
# For now, I'll create the lookup table manually from our GraphRAG queries

def generate_lookup_table():
    """Generate comprehensive path lookup from GraphRAG"""
    
    lookup = {
        # REAL PATHS FROM GRAPHRAG (from our queries above)
        
        # Mathematics
        "y7-algebra": "/units/y7-maths-algebra/lessons/lesson-1-patterns-and-sequences.html",
        "y7-maths-algebra": "/units/y7-maths-algebra/index.html",
        "patterns-sequences": "/units/y7-maths-algebra/lessons/lesson-1-patterns-and-sequences.html",
        "algebra-lesson-3": "/units/y7-maths-algebra/lessons/lesson-3-building-with-algebra.html",
        "algebra-lesson-4": "/units/y7-maths-algebra/lessons/lesson-4-balancing-act.html",
        "algebra-lesson-5": "/units/y7-maths-algebra/lessons/lesson-5-the-two-step-shuffle.html",
        
        "y8-statistics": "/units/y8-statistics/index.html",
        "statistics-intro": "/units/y8-statistics/lesson-1-introduction-statistical-investigations.html",
        "statistics-lesson-2": "/units/y8-statistics/lesson-2-analysing-nz-sports-data.html",
        "census-data": "/units/y8-statistics/lesson-3-census-population-trends.html",
        "probability": "/units/y8-statistics/lesson-4-probability-real-world-predictions.html",
        
        "y9-statistics": "/units/y9-statistics-chain/lesson-1-introduction-statistical-thinking.html",
        "y9-statistics-chain": "/units/y9-statistics-chain/index.html",
        "statistical-thinking": "/units/y9-statistics-chain/lesson-1-introduction-statistical-thinking.html",
        "ppdac-cycle": "/units/y9-statistics-chain/lesson-2-ppdac-cycle.html",
        "nz-census-data": "/units/y9-statistics-chain/lesson-3-nz-census-data.html",
        "charts-graphs": "/units/y9-statistics-chain/lesson-4-charts-and-graphs.html",
        "statistical-investigation": "/units/y9-statistics-chain/lesson-5-statistical-investigation.html",
        
        "whakapapa-mathematics": "/integrated-lessons/mathematics/whakapapa-mathematics.html",
        "algebraic-thinking": "/integrated-lessons/mathematics/algebraic-thinking-in-traditional-māori-games.html",
        "geometric-patterns": "/integrated-lessons/mathematics/geometric-patterns-in-māori-art-and-architecture.html",
        
        # Science  
        "y7-science": "/units/y7-science-ecosystems/lessons/lesson-1-kaitiakitanga-intro.html",
        "ecosystems": "/units/y7-science-ecosystems/lessons/lesson-1-kaitiakitanga-intro.html",
        "kaitiakitanga-intro": "/units/y7-science-ecosystems/lessons/lesson-1-kaitiakitanga-intro.html",
        
        "y9-ecology": "/units/y9-science-ecology/lessons/lesson-5-restoration-kaitiakitanga.html",
        "ecology-lesson-2": "/units/y9-science-ecology/lessons/lesson-2-biodiversity-endemism.html",
        "restoration-kaitiakitanga": "/units/y9-science-ecology/lessons/lesson-5-restoration-kaitiakitanga.html",
        "guardians-future": "/units/y9-science-ecology/lessons/lesson-6-guardians-future.html",
        
        "genetics-whakapapa": "/generated-resources-alpha/lessons/genetics-and-whakapapa-scientific-and-cultural-perspectives.html",
        "climate-change": "/integrated-lessons/science/climate-emergency-aotearoa-handout.html",
        
        # English
        "creative-writing": "/integrated-lessons/english/creative-writing-inspired-by-whakataukī.html",
        "whakataukī-writing": "/integrated-lessons/english/creative-writing-inspired-by-whakataukī.html",
        "storytelling": "/integrated-lessons/english/creative-writing-inspired-by-whakataukī.html",
        
        "writers-toolkit": "/public/writers-toolkit/index.html",
        "hook-lesson": "/lessons/writers-toolkit/hook-lesson-plan.html",
        "peel-lesson": "/lessons/writers-toolkit/peel-lesson-plan.html",
        "show-dont-tell": "/lessons/writers-toolkit/show-dont-tell-lesson-plan.html",
        "conclusion-lesson": "/lessons/writers-toolkit/conclusion-lesson-plan.html",
        "rhetorical-devices": "/lessons/writers-toolkit/rhetorical-devices-lesson-plan.html",
        
        "critical-thinking": "/units/y8-critical-thinking/index.html",
        "critical-thinking-intro": "/units/y8-critical-thinking/lesson-1-introduction.html",
        "bias-sources": "/units/y8-critical-thinking/lesson-2-bias-and-sources.html",
        "logical-fallacies": "/units/y8-critical-thinking/lesson-3-logical-fallacies.html",
        "ethics-decision": "/units/y8-critical-thinking/lesson-4-ethics-decision-making.html",
        "asking-questions": "/units/y8-critical-thinking/lesson-5-asking-right-questions.html",
        "evaluating-arguments": "/units/y8-critical-thinking/lesson-6-evaluating-arguments.html",
        "group-decision": "/units/y8-critical-thinking/lesson-7-group-decision-making.html",
        "critical-challenge": "/units/y8-critical-thinking/lesson-8-critical-thinking-challenge.html",
        
        # Social Studies
        "te-ao-maori": "/units/unit-1-te-ao-maori.html",
        "te-ao-maori-intro": "/units/unit-1-te-ao-maori/lessons/lesson-1-intro-te-ao-maori.html",
        "whakapapa-identity": "/units/unit-1-te-ao-maori/lessons/lesson-2-whakapapa-identity.html",
        "tikanga-protocols": "/units/unit-1-te-ao-maori/lessons/lesson-3-tikanga-protocols.html",
        "kaitiakitanga": "/units/unit-1-te-ao-maori/lessons/lesson-5-kaitiakitanga.html",
        "treaty-of-waitangi": "/units/unit-1-te-ao-maori/lessons/lesson-2-whakapapa-identity.html",
        
        # Te Reo Māori
        "te-reo-basics": "/units/unit-1-te-ao-maori/lessons/lesson-6-te-reo-basics.html",
        "te-reo-greetings": "/units/unit-1-te-ao-maori/lessons/lesson-6-te-reo-basics.html",
        "te-reo-wordle": "games/te-reo-wordle.html",
        
        # Digital Technologies
        "digital-kaitiakitanga": "/units/y8-digital-kaitiakitanga/index.html",
        "digital-whenua": "/units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html",
        "digital-kaitiakitanga-l1": "/units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html",
        "four-walls": "/units/y8-digital-kaitiakitanga/lessons/lesson-2-four-walls.html",
        "ai-ethics": "/units/unit-1-te-ao-maori/lessons/ai-ethics-through-māori-data-sovereignty.html",
        "ai-ethics-fixed": "/units/unit-1-te-ao-maori/lessons/ai-ethics-through-māori-data-sovereignty.html",
        "game-development": "/units/unit-1-te-ao-maori/lessons/game-development-with-cultural-themes.html",
        
        # Health & PE
        "hauora": "/generated-resources-alpha/lessons/health-and-wellbeing-te-whare-tapa-whā-model.html",
        "te-whare-tapa-wha": "/generated-resources-alpha/lessons/health-and-wellbeing-te-whare-tapa-whā-model.html",
        "hauora-wellbeing": "/generated-resources-alpha/lessons/health-and-wellbeing-te-whare-tapa-whā-model.html",
        "health-wellbeing": "/generated-resources-alpha/lessons/health-and-wellbeing-te-whare-tapa-whā-model.html",
        
        # Emergency/Special
        "emergency-lessons": "/emergency-lessons.html",
        "cultural-excellence": "/cultural-excellence-hub.html",
        "collections": "/collections.html",
    }
    
    # Save to JSON
    with open('graphrag-path-lookup.json', 'w') as f:
        json.dump(lookup, f, indent=2)
    
    print(f"✅ Generated lookup table with {len(lookup)} path mappings")
    print(f"💾 Saved to: graphrag-path-lookup.json")
    
    return lookup

if __name__ == "__main__":
    generate_lookup_table()

