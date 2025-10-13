#!/usr/bin/env python3
"""
Batch Content Integrator for Te Kete Ako
Integrates discovered resources into the site structure
"""

import json
import os
import sys
import shutil
from datetime import datetime
from pathlib import Path

class BatchContentIntegrator:
    def __init__(self):
        self.discovery_results = []
        self.integration_results = {
            "timestamp": datetime.now().isoformat(),
            "total_resources": 0,
            "integrated_resources": 0,
            "failed_integrations": [],
            "integration_log": []
        }
    
    def load_discovery_results(self):
        """Load the content discovery results"""
        try:
            with open('content-discovery-results.json', 'r') as f:
                self.discovery_results = json.load(f)
            self.integration_results["total_resources"] = len(self.discovery_results)
            print(f"📊 Loaded {len(self.discovery_results)} discovered resources")
            return True
        except FileNotFoundError:
            print("❌ Discovery results file not found")
            return False
    
    def categorize_resources(self):
        """Categorize resources by type and priority"""
        categories = {
            "high_priority": [],
            "medium_priority": [],
            "low_priority": []
        }
        
        for resource in self.discovery_results:
            # Skip archived/bloat content
            if "archived-bloat" in resource.get("path", ""):
                continue
            
            # High priority: High cultural level and good quality score
            if (resource.get("cultural_level") == "high" and 
                resource.get("quality_score", 0) >= 70):
                categories["high_priority"].append(resource)
            # Medium priority: Medium cultural level or good quality
            elif (resource.get("cultural_level") == "medium" or 
                  resource.get("quality_score", 0) >= 70):
                categories["medium_priority"].append(resource)
            # Low priority: Everything else
            else:
                categories["low_priority"].append(resource)
        
        return categories
    
    def integrate_lessons(self, lessons):
        """Integrate lesson resources"""
        print(f"📚 Integrating {len(lessons)} lesson resources...")
        
        # Create lessons directory structure if needed
        lessons_dir = Path("public/integrated-lessons")
        lessons_dir.mkdir(exist_ok=True)
        
        # Create subject-based subdirectories
        subjects = set()
        for lesson in lessons:
            subject = lesson.get("subject_area", "general")
            subjects.add(subject)
        
        for subject in subjects:
            (lessons_dir / subject).mkdir(exist_ok=True)
        
        integrated_count = 0
        for lesson in lessons:
            try:
                source_path = Path(lesson["path"])
                if not source_path.exists():
                    self.integration_results["failed_integrations"].append({
                        "resource": lesson,
                        "error": "Source file not found"
                    })
                    continue
                
                subject = lesson.get("subject_area", "general")
                dest_path = lessons_dir / subject / Path(lesson["path"]).name
                
                # Copy the file
                shutil.copy2(source_path, dest_path)
                
                # Create metadata file
                metadata = {
                    "original_path": lesson["path"],
                    "title": lesson["title"],
                    "description": lesson["description"],
                    "cultural_level": lesson.get("cultural_level"),
                    "subject_area": lesson.get("subject_area"),
                    "year_level": lesson.get("year_level"),
                    "quality_score": lesson.get("quality_score"),
                    "integrated_at": datetime.now().isoformat(),
                    "integrated_by": "agent-6"
                }
                
                metadata_path = dest_path.with_suffix('.metadata.json')
                with open(metadata_path, 'w') as f:
                    json.dump(metadata, f, indent=2)
                
                integrated_count += 1
                self.integration_results["integration_log"].append({
                    "resource": lesson["path"],
                    "status": "integrated",
                    "destination": str(dest_path)
                })
                
            except Exception as e:
                self.integration_results["failed_integrations"].append({
                    "resource": lesson,
                    "error": str(e)
                })
        
        print(f"✅ Integrated {integrated_count}/{len(lessons)} lessons")
        return integrated_count
    
    def integrate_handouts(self, handouts):
        """Integrate handout resources"""
        print(f"📄 Integrating {len(handouts)} handout resources...")
        
        # Create handouts directory structure
        handouts_dir = Path("public/integrated-handouts")
        handouts_dir.mkdir(exist_ok=True)
        
        # Create year-level based subdirectories
        year_levels = set()
        for handout in handouts:
            year_level = handout.get("year_level", "general")
            if year_level != "Not specified":
                year_levels.add(year_level)
        
        for year_level in year_levels:
            (handouts_dir / year_level).mkdir(exist_ok=True)
        
        integrated_count = 0
        for handout in handouts:
            try:
                source_path = Path(handout["path"])
                if not source_path.exists():
                    self.integration_results["failed_integrations"].append({
                        "resource": handout,
                        "error": "Source file not found"
                    })
                    continue
                
                year_level = handout.get("year_level", "general")
                if year_level == "Not specified":
                    dest_dir = handouts_dir / "general"
                else:
                    dest_dir = handouts_dir / year_level
                
                dest_path = dest_dir / Path(handout["path"]).name
                
                # Copy the file
                shutil.copy2(source_path, dest_path)
                
                # Create metadata file
                metadata = {
                    "original_path": handout["path"],
                    "title": handout["title"],
                    "description": handout["description"],
                    "cultural_level": handout.get("cultural_level"),
                    "subject_area": handout.get("subject_area"),
                    "year_level": handout.get("year_level"),
                    "quality_score": handout.get("quality_score"),
                    "integrated_at": datetime.now().isoformat(),
                    "integrated_by": "agent-4"
                }
                
                metadata_path = dest_path.with_suffix('.metadata.json')
                with open(metadata_path, 'w') as f:
                    json.dump(metadata, f, indent=2)
                
                integrated_count += 1
                self.integration_results["integration_log"].append({
                    "resource": handout["path"],
                    "status": "integrated",
                    "destination": str(dest_path)
                })
                
            except Exception as e:
                self.integration_results["failed_integrations"].append({
                    "resource": handout,
                    "error": str(e)
                })
        
        print(f"✅ Integrated {integrated_count}/{len(handouts)} handouts")
        return integrated_count
    
    def create_navigation_index(self, integrated_resources):
        """Create navigation index for integrated resources"""
        print("🗺️ Creating navigation index...")
        
        index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Integrated Resources | Te Kete Ako</title>
    <link rel="stylesheet" href="/css/te-kete-professional.css">
</head>
<body>
    <div id="header-component"></div>
    
    <main class="container" style="padding: 2rem;">
        <h1>📚 Integrated Resources</h1>
        <p>Resources integrated from discovery process</p>
        
        <div class="resource-grid">
            <div class="resource-category">
                <h2>📚 Lessons ({len([r for r in integrated_resources if r['type'] == 'lessons'])})</h2>
                <a href="/integrated-lessons/" class="btn btn-primary">Browse Lessons</a>
            </div>
            
            <div class="resource-category">
                <h2>📄 Handouts ({len([r for r in integrated_resources if r['type'] == 'handouts'])})</h2>
                <a href="/integrated-handouts/" class="btn btn-primary">Browse Handouts</a>
            </div>
        </div>
    </main>
</body>
</html>"""
        
        with open('public/integrated-resources-index.html', 'w') as f:
            f.write(index_content)
        
        print("✅ Navigation index created")
    
    def run_batch_integration(self):
        """Run the complete batch integration process"""
        print("🔄 Starting Batch Content Integration...")
        print("=" * 50)
        
        # Load discovery results
        if not self.load_discovery_results():
            return False
        
        # Categorize resources
        categories = self.categorize_resources()
        
        # Get resources by type
        lessons = [r for r in self.discovery_results if r["type"] == "lessons"]
        handouts = [r for r in self.discovery_results if r["type"] == "handouts"]
        
        # Integrate high and medium priority resources first
        priority_lessons = [l for l in lessons if l in categories["high_priority"] + categories["medium_priority"]]
        priority_handouts = [h for h in handouts if h in categories["high_priority"] + categories["medium_priority"]]
        
        # Integrate lessons
        lessons_integrated = self.integrate_lessons(priority_lessons)
        
        # Integrate handouts
        handouts_integrated = self.integrate_handouts(priority_handouts)
        
        # Update results
        self.integration_results["integrated_resources"] = lessons_integrated + handouts_integrated
        
        # Create navigation index
        self.create_navigation_index(self.discovery_results)
        
        # Save integration results
        with open('batch-integration-results.json', 'w') as f:
            json.dump(self.integration_results, f, indent=2)
        
        # Print summary
        print("\n" + "=" * 50)
        print("📊 BATCH INTEGRATION SUMMARY")
        print("=" * 50)
        print(f"Total Resources: {self.integration_results['total_resources']}")
        print(f"Integrated Resources: {self.integration_results['integrated_resources']}")
        print(f"Failed Integrations: {len(self.integration_results['failed_integrations'])}")
        print(f"Success Rate: {(self.integration_results['integrated_resources'] / self.integration_results['total_resources'] * 100):.1f}%")
        
        return True

if __name__ == "__main__":
    integrator = BatchContentIntegrator()
    success = integrator.run_batch_integration()
    
    if not success:
        sys.exit(1)
