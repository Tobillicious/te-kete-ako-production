#!/usr/bin/env python3
"""
Content Treasure Hunter for Te Kete Ako
Discovers, categorizes, and integrates thousands of HTML files into the site
"""

import json
import os
import re
import sys
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from pathlib import Path

class ContentTreasureHunter:
    def __init__(self):
        self.project_root = Path("/Users/admin/Documents/te-kete-ako-clean")
        self.discovered_content = []
        self.categories = {
            "lessons": [],
            "handouts": [],
            "units": [],
            "activities": [],
            "assessments": [],
            "games": [],
            "resources": [],
            "teacher_guides": [],
            "cultural_content": [],
            "other": []
        }
        
        # Patterns to identify content types
        self.patterns = {
            "lessons": [
                r"lesson",
                r"teaching",
                r"plan",
                r"objective",
                r"walt",
                r"success.criteria"
            ],
            "handouts": [
                r"handout",
                r"worksheet",
                r"printable",
                r"student",
                r"activity.sheet"
            ],
            "units": [
                r"unit",
                r"topic",
                r"theme",
                r"module",
                r"subject"
            ],
            "activities": [
                r"activity",
                r"exercise",
                r"task",
                r"practice",
                r"interactive"
            ],
            "assessments": [
                r"assessment",
                r"test",
                r"quiz",
                r"evaluation",
                r"rubric"
            ],
            "games": [
                r"game",
                r"puzzle",
                r"wordle",
                r"challenge",
                r"play"
            ],
            "resources": [
                r"resource",
                r"material",
                r"tool",
                r"guide",
                r"reference"
            ],
            "teacher_guides": [
                r"teacher",
                r"guide",
                r"instruction",
                r"facilitator",
                r"educator"
            ],
            "cultural_content": [
                r"māori",
                r"maori",
                r"tikanga",
                r"te.reo",
                r"whakatauki",
                r"karakia",
                r"pūrākau",
                r"matauranga"
            ]
        }
    
    def discover_all_html_files(self) -> List[Dict]:
        """Discover all HTML files in the project"""
        print("🔍 Discovering HTML files...")
        
        html_files = list(self.project_root.glob("**/*.html"))
        print(f"Found {len(html_files)} HTML files")
        
        for html_file in html_files:
            # Skip certain directories
            if any(skip in str(html_file) for skip in ["node_modules", ".git", "dist"]):
                continue
            
            file_info = self.analyze_html_file(html_file)
            if file_info:
                self.discovered_content.append(file_info)
        
        print(f"✅ Analyzed {len(self.discovered_content)} HTML files")
        return self.discovered_content
    
    def analyze_html_file(self, file_path: Path) -> Optional[Dict]:
        """Analyze an HTML file to determine its type and content"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Skip if too small or empty
            if len(content) < 100:
                return None
            
            # Extract key information
            title = self.extract_title(content)
            description = self.extract_description(content)
            content_type = self.categorize_content(content, file_path)
            cultural_level = self.assess_cultural_level(content)
            subject_area = self.identify_subject_area(content)
            year_level = self.identify_year_level(content)
            
            return {
                "path": str(file_path.relative_to(self.project_root)),
                "title": title,
                "description": description,
                "type": content_type,
                "cultural_level": cultural_level,
                "subject_area": subject_area,
                "year_level": year_level,
                "file_size": len(content),
                "last_modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                "quality_score": self.assess_quality(content)
            }
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return None
    
    def extract_title(self, content: str) -> str:
        """Extract title from HTML content"""
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
        if title_match:
            return title_match.group(1).strip()
        
        # Try h1 tag
        h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content, re.IGNORECASE)
        if h1_match:
            return h1_match.group(1).strip()
        
        return "Untitled"
    
    def extract_description(self, content: str) -> str:
        """Extract description from HTML content"""
        # Try meta description
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', content, re.IGNORECASE)
        if desc_match:
            return desc_match.group(1).strip()
        
        # Try first paragraph
        p_match = re.search(r'<p[^>]*>([^<]+)</p>', content, re.IGNORECASE)
        if p_match:
            return p_match.group(1).strip()[:200] + "..." if len(p_match.group(1)) > 200 else p_match.group(1).strip()
        
        return "No description available"
    
    def categorize_content(self, content: str, file_path: Path) -> str:
        """Categorize content based on patterns and file path"""
        content_lower = content.lower()
        path_lower = str(file_path).lower()
        
        # Check file path first
        if "lesson" in path_lower:
            return "lessons"
        elif "handout" in path_lower or "worksheet" in path_lower:
            return "handouts"
        elif "unit" in path_lower:
            return "units"
        elif "game" in path_lower:
            return "games"
        elif "assessment" in path_lower or "test" in path_lower:
            return "assessments"
        
        # Check content patterns
        for category, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, content_lower):
                    return category
        
        return "other"
    
    def assess_cultural_level(self, content: str) -> str:
        """Assess the cultural level of content"""
        content_lower = content.lower()
        
        # Count cultural indicators
        cultural_indicators = [
            "māori", "maori", "tikanga", "te reo", "whakatauki", 
            "karakia", "pūrākau", "matauranga", "iwi", "hapū",
            "marae", "tangata whenua", "kaitiaki", "kaitiakitanga"
        ]
        
        count = sum(1 for indicator in cultural_indicators if indicator in content_lower)
        
        if count >= 5:
            return "high"
        elif count >= 2:
            return "medium"
        elif count >= 1:
            return "low"
        else:
            return "none"
    
    def identify_subject_area(self, content: str) -> str:
        """Identify the subject area of content"""
        content_lower = content.lower()
        
        subjects = {
            "mathematics": ["math", "algebra", "geometry", "statistics", "number", "measurement"],
            "science": ["science", "biology", "chemistry", "physics", "experiment", "investigation"],
            "english": ["english", "writing", "reading", "literature", "grammar", "comprehension"],
            "social studies": ["social studies", "history", "geography", "society", "culture", "treaty"],
            "te reo māori": ["te reo", "māori language", "reo māori", "māori", "language"],
            "technology": ["technology", "digital", "computing", "coding", "design"],
            "arts": ["art", "music", "drama", "dance", "visual", "creative"],
            "health": ["health", "pe", "physical education", "wellbeing", "hauora"],
            "general": []
        }
        
        for subject, keywords in subjects.items():
            if any(keyword in content_lower for keyword in keywords):
                return subject
        
        return "general"
    
    def identify_year_level(self, content: str) -> str:
        """Identify the year level of content"""
        content_lower = content.lower()
        
        year_patterns = [
            (r"year\s*([0-9]+)", lambda m: f"Year {m.group(1)}"),
            (r"level\s*([0-9]+)", lambda m: f"Level {m.group(1)}"),
            (r"grade\s*([0-9]+)", lambda m: f"Grade {m.group(1)}"),
            (r"y([0-9]+)", lambda m: f"Year {m.group(1)}"),
            (r"nz\s*curriculum\s*level\s*([0-9]+)", lambda m: f"NZC Level {m.group(1)}")
        ]
        
        for pattern, formatter in year_patterns:
            match = re.search(pattern, content_lower)
            if match:
                return formatter(match)
        
        return "Not specified"
    
    def assess_quality(self, content: str) -> int:
        """Assess the quality of content on a scale of 1-100"""
        score = 50  # Base score
        
        # Add points for quality indicators
        if re.search(r'<title[^>]*>[^<]+</title>', content):
            score += 10
        
        if re.search(r'<meta[^>]*name=["\']description["\']', content):
            score += 5
        
        if re.search(r'<h1[^>]*>[^<]+</h1>', content):
            score += 5
        
        if re.search(r'<nav[^>]*>', content):
            score += 5
        
        if re.search(r'<footer[^>]*>', content):
            score += 5
        
        # Check for structured content
        if re.search(r'<(ul|ol)[^>]*>.*</\1>', content, re.DOTALL):
            score += 5
        
        if re.search(r'<table[^>]*>', content):
            score += 5
        
        # Check for accessibility
        if re.search(r'alt=["\'][^"\']*["\']', content):
            score += 5
        
        # Check for CSS styling
        if re.search(r'<link[^>]*stylesheet[^>]*>', content):
            score += 5
        
        # Check for educational structure
        if re.search(r'(objective|goal|outcome|learning|intention)', content, re.IGNORECASE):
            score += 5
        
        # Deduct for quality issues
        if len(content) < 500:
            score -= 10
        
        if content.count('<script') > 10:
            score -= 5
        
        return max(0, min(100, score))
    
    def categorize_all_content(self):
        """Categorize all discovered content"""
        print("📂 Categorizing content...")
        
        for item in self.discovered_content:
            content_type = item["type"]
            if content_type in self.categories:
                self.categories[content_type].append(item)
        
        # Print summary
        print("\n📊 Content Summary:")
        for category, items in self.categories.items():
            print(f"  {category}: {len(items)} files")
    
    def generate_integration_plan(self) -> Dict:
        """Generate a plan for integrating content into the site"""
        plan = {
            "generated_at": datetime.now().isoformat(),
            "total_files": len(self.discovered_content),
            "categories": {},
            "integration_priorities": [],
            "quality_improvements": []
        }
        
        # Analyze each category
        for category, items in self.categories.items():
            if not items:
                continue
                
            # Calculate quality metrics
            quality_scores = [item["quality_score"] for item in items]
            avg_quality = sum(quality_scores) / len(quality_scores)
            high_quality = [item for item in items if item["quality_score"] >= 70]
            
            plan["categories"][category] = {
                "count": len(items),
                "average_quality": avg_quality,
                "high_quality_count": len(high_quality),
                "needs_improvement": len(items) - len(high_quality)
            }
            
            # Add to integration priorities
            if category in ["lessons", "handouts", "units"] and len(high_quality) > 0:
                plan["integration_priorities"].append({
                    "category": category,
                    "priority": "high" if avg_quality >= 70 else "medium",
                    "files_to_integrate": len(high_quality),
                    "example_files": high_quality[:3]
                })
        
        # Sort priorities by count
        plan["integration_priorities"].sort(key=lambda x: x["files_to_integrate"], reverse=True)
        
        return plan
    
    def save_discovery_results(self, plan: Dict):
        """Save discovery results to files"""
        # Save full content list
        with open("content-discovery-results.json", "w") as f:
            json.dump(self.discovered_content, f, indent=2)
        
        # Save integration plan
        with open("content-integration-plan.json", "w") as f:
            json.dump(plan, f, indent=2)
        
        # Save categorized content
        with open("categorized-content.json", "w") as f:
            json.dump(self.categories, f, indent=2)
        
        print("\n💾 Results saved:")
        print("  - content-discovery-results.json")
        print("  - content-integration-plan.json")
        print("  - categorized-content.json")
    
    def create_integration_tasks(self) -> List[Dict]:
        """Create specific tasks for content integration"""
        tasks = []
        
        # High priority: Integrate high-quality lessons
        high_quality_lessons = [item for item in self.categories["lessons"] if item["quality_score"] >= 70]
        if high_quality_lessons:
            tasks.append({
                "type": "content-integration",
                "description": f"Integrate {len(high_quality_lessons)} high-quality lessons",
                "category": "lessons",
                "files": high_quality_lessons[:10],  # Limit to first 10
                "priority": "critical",
                "estimated_time": "3 hours",
                "agent": "agent-6"
            })
        
        # High priority: Integrate high-quality handouts
        high_quality_handouts = [item for item in self.categories["handouts"] if item["quality_score"] >= 70]
        if high_quality_handouts:
            tasks.append({
                "type": "content-integration",
                "description": f"Integrate {len(high_quality_handouts)} high-quality handouts",
                "category": "handouts",
                "files": high_quality_handouts[:10],  # Limit to first 10
                "priority": "critical",
                "estimated_time": "2 hours",
                "agent": "agent-4"
            })
        
        # Medium priority: Cultural content integration
        high_cultural = [item for item in self.discovered_content if item["cultural_level"] == "high"]
        if high_cultural:
            tasks.append({
                "type": "cultural-integration",
                "description": f"Integrate {len(high_cultural)} high cultural value resources",
                "category": "cultural_content",
                "files": high_cultural[:10],  # Limit to first 10
                "priority": "high",
                "estimated_time": "2 hours",
                "agent": "agent-7"
            })
        
        return tasks

if __name__ == "__main__":
    hunter = ContentTreasureHunter()
    
    if len(sys.argv) < 2:
        print("Usage: python content-treasure-hunter.py <command>")
        print("Commands:")
        print("  discover - Discover and analyze all HTML files")
        print("  plan - Generate integration plan")
        print("  tasks - Create integration tasks")
        print("  full - Run complete discovery and planning")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "discover":
        hunter.discover_all_html_files()
        hunter.categorize_all_content()
        
    elif command == "plan":
        if not hunter.discovered_content:
            hunter.discover_all_html_files()
            hunter.categorize_all_content()
        
        plan = hunter.generate_integration_plan()
        hunter.save_discovery_results(plan)
        
        print("\n📋 Integration Plan:")
        print(f"Total files: {plan['total_files']}")
        print("\nIntegration Priorities:")
        for priority in plan["integration_priorities"]:
            print(f"  {priority['category']}: {priority['files_to_integrate']} files ({priority['priority']} priority)")
        
    elif command == "tasks":
        if not hunter.discovered_content:
            hunter.discover_all_html_files()
            hunter.categorize_all_content()
        
        tasks = hunter.create_integration_tasks()
        
        print("\n🎯 Integration Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['description']}")
            print(f"   Priority: {task['priority']}")
            print(f"   Agent: {task['agent']}")
            print(f"   Estimated time: {task['estimated_time']}")
        
        # Save tasks
        with open("content-integration-tasks.json", "w") as f:
            json.dump(tasks, f, indent=2)
        
    elif command == "full":
        print("🚀 Running complete content discovery and planning...")
        hunter.discover_all_html_files()
        hunter.categorize_all_content()
        plan = hunter.generate_integration_plan()
        hunter.save_discovery_results(plan)
        tasks = hunter.create_integration_tasks()
        
        with open("content-integration-tasks.json", "w") as f:
            json.dump(tasks, f, indent=2)
        
        print("\n✅ Complete! Results saved to:")
        print("  - content-discovery-results.json")
        print("  - content-integration-plan.json")
        print("  - categorized-content.json")
        print("  - content-integration-tasks.json")
        
    else:
        print(f"Unknown command: {command}")
