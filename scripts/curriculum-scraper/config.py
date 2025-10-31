"""
Curriculum Scraper Configuration
Defines all curriculum sources and their structures
"""

# Tahurangi Base URLs
TAHURANGI_BASE = "https://newzealandcurriculum.tahurangi.education.govt.nz"

# Curriculum Versions
CURRICULUM_VERSIONS = {
    "temataiaho_2025": {
        "name": "Te Mātaiaho 2025",
        "status": "mandatory",  # For English & Math
        "effective_date": "2025-01-01",
        "learning_areas": [
            {
                "name": "English",
                "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/new-zealand-curriculum/learning-areas/english-curriculum/5637165583.c",
                "phases": [
                    {"phase": "Phase 1", "year_levels": [0, 1, 2, 3], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---english-phase-1-years-0-3/5637288579.p"},
                    {"phase": "Phase 2", "year_levels": [4, 5, 6], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---english-phase-2-years-4-6/5637289329.p"},
                    {"phase": "Phase 3", "year_levels": [7, 8], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---english-phase-3-years-7-8/5637290836.p"},
                    {"phase": "Phase 4", "year_levels": [9, 10], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---english-phase-4-years-9-10/5637291578.p"},
                ],
                "strands": ["Text Studies", "Language Studies"],
                "elements": ["Knowledge", "Practices"]
            },
            {
                "name": "Mathematics",
                "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/new-zealand-curriculum/learning-areas/mathematics-and-statistics-curriculum/5637165587.c",
                "phases": [
                    {"phase": "Phase 1", "year_levels": [0, 1, 2, 3], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---mathematics-and-statistics-phase-1-years-0-3/5637289331.p"},
                    {"phase": "Phase 2", "year_levels": [4, 5, 6], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---mathematics-and-statistics-phase-2-years-4-6/5637289332.p"},
                    {"phase": "Phase 3", "year_levels": [7, 8], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---mathematics-and-statistics-phase-3-years-7-8/5637289333.p"},
                    {"phase": "Phase 4", "year_levels": [9, 10], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---mathematics-and-statistics-phase-4-years-9-10/5637291579.p"},
                ],
                "strands": ["Number", "Measurement", "Statistics", "Algebra", "Geometry"],  # Will extract actual strands
                "elements": ["Knowledge", "Practices"]
            }
        ]
    },
    
    "draft_2025": {
        "name": "Draft 2025 Learning Areas",
        "status": "consultation",
        "consultation_end": "2026-04-30",
        "learning_areas": [
            {
                "name": "Science",
                "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/new-zealand-curriculum/learning-areas/science-curriculum/5637165588.c",
                "phases": [
                    {"phase": "Phase 1", "year_levels": [0, 1, 2, 3], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---science-phase-1-years-0-3/5637292339.p"},
                    {"phase": "Phase 2", "year_levels": [4, 5, 6], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---science-phase-2-years-4-6/5637292340.p"},
                    {"phase": "Phase 3", "year_levels": [7, 8], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---science-phase-3-years-7-8/5637290856.p"},
                    {"phase": "Phase 4", "year_levels": [9, 10], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---science-phase-4-years-9-10/5637290857.p"},
                ],
                "strands": ["Nature of Science", "Physical World", "Living World", "Material World", "Planet Earth and Beyond"],
                "elements": ["Knowledge", "Practices"]
            },
            {
                "name": "Social Sciences",
                "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/new-zealand-curriculum/learning-areas/social-sciences-curriculum/5637165589.c",
                "phases": [
                    {"phase": "Phase 1", "year_levels": [0, 1, 2, 3], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---social-sciences-years-0---3/5637292338.p"},
                    {"phase": "Phase 2", "year_levels": [4, 5, 6], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---social-sciences-years-4---6/5637290852.p"},
                    {"phase": "Phase 3", "year_levels": [7, 8], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---social-sciences-years-7---8/5637290853.p"},
                    {"phase": "Phase 4", "year_levels": [9, 10], "url": f"{TAHURANGI_BASE}/new-zealand-curriculum-online/nzc---social-sciences-years-9---10/5637290854.p"},
                ],
                "strands": ["History", "Civics and Society", "Geography", "Economic Activity"],
                "elements": ["Knowledge", "Practices"]
            },
            # Add other draft subjects: Health & PE, The Arts, Technology, Learning Languages
        ]
    },
    
    "2007_nzc": {
        "name": "The New Zealand Curriculum 2007",
        "status": "active",  # Still valid
        "effective_date": "2007-01-01",
        "learning_areas": [
            # Will extract from legacy NZC pages
            # Different structure: Levels 1-8 instead of Phases
        ]
    }
}

# Statement extraction patterns
STATEMENT_PATTERNS = {
    "temataiaho_2025": {
        # Te Mātaiaho uses tables with "Knowledge" and "Practices" columns
        "container_selector": "table",
        "row_selector": "tr",
        "knowledge_selector": "td:nth-child(2)",  # Column 2
        "practices_selector": "td:nth-child(3)",  # Column 3
        "year_header_pattern": r"During Year (\d+)",
    },
    "2007_nzc": {
        # 2007 NZC uses different HTML structure
        "container_selector": ".achievement-objectives",
        "statement_selector": "li",
    }
}

# Validation rules
VALIDATION_RULES = {
    "min_statement_length": 10,
    "max_statement_length": 5000,
    "required_fields": ["curriculum_version", "learning_area", "statement_text"],
    "invalid_phrases": ["lorem ipsum", "placeholder", "TODO", "TBD", "[INSERT", "DRAFT ONLY"]
}

