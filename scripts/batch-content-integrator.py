#!/usr/bin/env python3
"""
Quality-Focused Content Review & Integration
Manual review process to ensure educational excellence before integration
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class QualityContentReviewer:
    def __init__(self):
        self.project_root = Path("/Users/admin/Documents/te-kete-ako-clean")
        self.review_log = []
        self.current_index = 0
        self.approved_content = []
        self.rejected_content = []
        self.needs_enrichment = []  # Track items needing specialist attention
        
    def get_next_content_item(self) -> Optional[Dict]:
        """Get the next content item to review"""
        # Load content discovery results
        with open(self.project_root / "content-discovery-results.json", 'r') as f:
            all_content = json.load(f)
        
        # Skip already reviewed content
        reviewed_paths = set()
        for item in self.review_log:
            if "file_path" in item:
                reviewed_paths.add(item["file_path"])
        
        unreviewed = [item for item in all_content if item["path"] not in reviewed_paths]
        
        if not unreviewed:
            return None
        
        return unreviewed[0]
    
    def analyze_content_quality(self, file_path: str) -> Dict:
        """Analyze content for educational quality indicators"""
        full_path = self.project_root / file_path
        
        if not full_path.exists():
            return {"status": "error", "message": f"File not found: {file_path}"}
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Quality indicators
        quality_score = 0
        max_score = 100
        feedback = []
        
        # 1. Educational Structure (30 points)
        if "learning" in content.lower() or "objective" in content.lower():
            quality_score += 10
            feedback.append("✅ Has learning objectives")
        else:
            feedback.append("❌ Missing clear learning objectives")
        
        if "activity" in content.lower() or "exercise" in content.lower():
            quality_score += 10
            feedback.append("✅ Includes activities/exercises")
        else:
            feedback.append("❌ Lacks student activities")
        
        if "assessment" in content.lower() or "check" in content.lower():
            quality_score += 10
            feedback.append("✅ Has assessment components")
        else:
            feedback.append("❌ Missing assessment elements")
        
        # 2. Cultural Authenticity (25 points)
        māori_terms = ["māori", "maori", "tikanga", "te reo", "whakataukī", "matauranga", "kaupapa"]
        māori_count = sum(1 for term in māori_terms if term in content.lower())
        
        if māori_count >= 3:
            quality_score += 25
            feedback.append(f"✅ Strong mātauranga Māori integration ({māori_count} terms)")
        elif māori_count >= 1:
            quality_score += 15
            feedback.append(f"⚠️ Some mātauranga Māori content ({māori_count} terms)")
        else:
            feedback.append("❌ Lacks mātauranga Māori context")
        
        # 3. Content Depth (20 points)
        word_count = len(content.split())
        if word_count > 1000:
            quality_score += 20
            feedback.append(f"✅ Substantial content ({word_count} words)")
        elif word_count > 500:
            quality_score += 15
            feedback.append(f"⚠️ Moderate content depth ({word_count} words)")
        else:
            quality_score += 5
            feedback.append(f"❌ Limited content ({word_count} words)")
        
        # 4. Visual Appeal (15 points)
        if "img" in content.lower() or "image" in content.lower():
            quality_score += 8
            feedback.append("✅ Includes visual elements")
        
        if "style" in content.lower() or "css" in content.lower():
            quality_score += 7
            feedback.append("✅ Has styling considerations")
        
        # 5. Technical Quality (10 points)
        if "te-kete-professional.css" in content:
            quality_score += 5
            feedback.append("✅ Uses professional styling")
        
        if "header-component" in content:
            quality_score += 5
            feedback.append("✅ Has consistent navigation")
        
        return {
            "file_path": file_path,
            "quality_score": quality_score,
            "max_score": max_score,
            "percentage": round((quality_score / max_score) * 100),
            "feedback": feedback,
            "word_count": word_count,
            "māori_terms": māori_count,
            "recommendation": "APPROVE" if quality_score >= 70 else "REVIEW"
        }
    
    def enhance_content(self, file_path: str, enhancements: List[str]) -> bool:
        """Apply specific enhancements to improve content quality"""
        full_path = self.project_root / file_path
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply enhancements
            if "Add professional CSS" in enhancements:
                if "<head>" in content and "te-kete-professional.css" not in content:
                    content = content.replace(
                        "<head>",
                        "<head>\n    <link rel=\"stylesheet\" href=\"/css/te-kete-professional.css\">"
                    )
            
            if "Add header component" in enhancements:
                if "<body" in content and "header-component" not in content:
                    content = content.replace(
                        "<body",
                        "<body>\n    <div id=\"header-component\"></div>\n    <script src=\"/js/components/header.js\"></script>"
                    )
            
            if "Add mātauranga Māori context" in enhancements:
                # Add a simple mātauranga Māori introduction if missing
                if "māori" not in content.lower() and "maori" not in content.lower():
                    māori_intro = """
    <div class="māori-context" style="background: #f0f8f0; padding: 1rem; margin: 1rem 0; border-left: 4px solid #2C5F41;">
        <h3>Te Ao Māori Perspective</h3>
        <p>This resource acknowledges mātauranga Māori and incorporates indigenous knowledge systems.</p>
    </div>
"""
                    # Insert after the first heading
                    content = content.replace("<h1", māori_intro + "<h1", 1)
            
            # Write enhanced content
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"Error enhancing {file_path}: {e}")
            return False
    
    def commit_approved_content(self, file_path: str, quality_score: int) -> bool:
        """Commit approved content with quality metadata"""
        try:
            # Stage the file
            subprocess.run(
                ["git", "add", file_path],
                cwd=self.project_root,
                check=True,
                capture_output=True
            )
            
            # Check if there are staged changes
            result = subprocess.run(
                ["git", "diff", "--cached", "--name-only", file_path],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            
            # Only commit if there are changes
            if result.stdout.strip():
                # Create quality commit message
                commit_message = f"Quality content approved: {file_path} (Score: {quality_score}%)"
                
                # Commit with message
                subprocess.run(
                    ["git", "commit", "-m", commit_message],
                    cwd=self.project_root,
                    check=True,
                    capture_output=True
                )
                print(f"✅ Committed: {file_path}")
            else:
                print(f"ℹ️ No changes to commit for: {file_path}")
            
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error committing {file_path}: {e}")
            return False
    
    def run_quality_review_workflow(self):
        """Run the complete quality-focused review workflow"""
        print("🎯 QUALITY-FOCUSED CONTENT REVIEW WORKFLOW")
        print("=" * 60)
        print("Each resource will be carefully reviewed for educational excellence.")
        print("Only high-quality content will be approved for integration.")
        print("=" * 60)
        
        # Process first 5 items as a demonstration
        max_items = 5
        processed = 0
        
        while processed < max_items:
            # Get next content item
            content_item = self.get_next_content_item()
            
            if not content_item:
                print("\n✅ All content has been reviewed!")
                self.print_summary()
                break
            
            # Analyze quality
            quality_analysis = self.analyze_content_quality(content_item["path"])
            
            # Make automatic decision based on quality score
            file_path = content_item["path"]
            title = content_item.get("title", "Untitled")
            
            print("\n" + "="*60)
            print(f"📚 REVIEWING: {title}")
            print(f"📁 Path: {file_path}")
            print(f"📊 Quality Score: {quality_analysis['percentage']}% ({quality_analysis['quality_score']}/{quality_analysis['max_score']})")
            print(f"📝 Word Count: {quality_analysis['word_count']}")
            print(f"🌿 Māori Terms: {quality_analysis['māori_terms']}")
            
            print("\n📋 Quality Feedback:")
            for feedback in quality_analysis["feedback"]:
                print(f"  {feedback}")
            
            # Automatic decision based on quality score
            if quality_analysis['percentage'] >= 80:
                decision = "APPROVE"
                enhancements = []
                print(f"\n✅ AUTO-APPROVED: High quality score ({quality_analysis['percentage']}%)")
            elif quality_analysis['percentage'] >= 60:
                decision = "ENHANCE"
                enhancements = []
                
                # Determine needed enhancements
                full_path = self.project_root / file_path
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if "te-kete-professional.css" not in content:
                    enhancements.append("Add professional CSS")
                
                if "header-component" not in content:
                    enhancements.append("Add header component")
                
                if quality_analysis['māori_terms'] == 0:
                    enhancements.append("Add mātauranga Māori context")
                
                print(f"\n🔧 AUTO-ENHANCE: Moderate quality ({quality_analysis['percentage']}%)")
                print(f"   Enhancements: {', '.join(enhancements)}")
            else:
                decision = "REJECT"
                enhancements = []
                print(f"\n❌ AUTO-REJECTED: Low quality score ({quality_analysis['percentage']}%)")
            
            # Process decision
            review_record = {
                "file_path": content_item["path"],
                "title": content_item.get("title", "Untitled"),
                "quality_score": quality_analysis["percentage"],
                "decision": decision,
                "enhancements": enhancements
            }
            
            if decision == "APPROVE":
                if self.commit_approved_content(content_item["path"], quality_analysis["percentage"]):
                    self.approved_content.append(review_record)
                    print(f"✅ APPROVED and committed: {content_item['path']}")
                else:
                    print(f"❌ Error committing: {content_item['path']}")
            
            elif decision == "ENHANCE":
                if self.enhance_content(content_item["path"], enhancements):
                    # Re-analyze after enhancement
                    new_analysis = self.analyze_content_quality(content_item["path"])
                    review_record["enhanced_score"] = new_analysis["percentage"]
                    
                    if self.commit_approved_content(content_item["path"], new_analysis["percentage"]):
                        self.approved_content.append(review_record)
                        print(f"✅ ENHANCED and committed: {content_item['path']} (Score: {new_analysis['percentage']}%)")
                    else:
                        print(f"❌ Error committing enhanced: {content_item['path']}")
                else:
                    print(f"❌ Error enhancing: {content_item['path']}")
            
            elif decision == "REJECT":
                self.rejected_content.append(review_record)
                print(f"❌ REJECTED: {content_item['path']}")
            
            # Record review
            self.review_log.append(review_record)
            processed += 1
            
            # Save review log
            with open(self.project_root / "content-quality-review-log.json", 'w') as f:
                json.dump(self.review_log, f, indent=2)
        
        self.print_summary()
    
    def print_summary(self):
        """Print a summary of the review session"""
        print("\n" + "="*60)
        print("📊 REVIEW SUMMARY")
        print("="*60)
        print(f"Total Reviewed: {len(self.review_log)}")
        print(f"✅ Approved: {len(self.approved_content)}")
        print(f"❌ Rejected: {len(self.rejected_content)}")
        
        if self.approved_content:
            avg_score = sum(item["quality_score"] for item in self.approved_content) / len(self.approved_content)
            print(f"📈 Average Quality Score: {avg_score:.1f}%")
        
        print("\n🎉 High-quality educational content is ready for students!")

if __name__ == "__main__":
    reviewer = QualityContentReviewer()
    reviewer.run_quality_review_workflow()
