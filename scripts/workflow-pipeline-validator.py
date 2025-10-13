#!/usr/bin/env python3
"""
Workflow Pipeline Validator
Comprehensive validation system for Te Kete Ako deployment pipeline
"""

import os
import subprocess
import json
import re
from pathlib import Path
from datetime import datetime

class WorkflowPipelineValidator:
    def __init__(self):
        self.base_dir = Path("/Users/admin/Documents/te-kete-ako-clean")
        self.validation_results = {
            "timestamp": datetime.now().isoformat(),
            "checks": {},
            "overall_status": "pending",
            "recommendations": []
        }
    
    def run_full_validation(self):
        """Run complete validation pipeline"""
        print("🔍 Starting comprehensive workflow validation...")
        
        # 1. Git status validation
        self.validate_git_status()
        
        # 2. Content structure validation
        self.validate_content_structure()
        
        # 3. CSS and styling validation
        self.validate_css_styling()
        
        # 4. Navigation validation
        self.validate_navigation()
        
        # 5. Cultural content validation
        self.validate_cultural_content()
        
        # 6. Performance validation
        self.validate_performance()
        
        # 7. Accessibility validation
        self.validate_accessibility()
        
        # 8. Integration validation
        self.validate_integrated_content()
        
        # Generate final report
        self.generate_validation_report()
        
        return self.validation_results
    
    def validate_git_status(self):
        """Validate git status and changes"""
        print("\n📋 Validating git status...")
        
        try:
            # Get git status
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.base_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                self.validation_results["checks"]["git_status"] = {
                    "status": "error",
                    "message": "Failed to get git status"
                }
                return
            
            # Parse git status
            lines = result.stdout.strip().split('\n')
            modified_files = [line for line in lines if line.startswith(' M')]
            untracked_files = [line for line in lines if line.startswith('??')]
            
            self.validation_results["checks"]["git_status"] = {
                "status": "success",
                "modified_count": len(modified_files),
                "untracked_count": len(untracked_files),
                "details": {
                    "modified": modified_files[:10],  # First 10
                    "untracked": untracked_files[:10]  # First 10
                }
            }
            
            # Check for critical files
            critical_patterns = [
                "public/index.html",
                "public/css/te-kete-professional.css",
                "public/components/header.html"
            ]
            
            critical_changes = []
            for pattern in critical_patterns:
                for file in modified_files:
                    if pattern in file:
                        critical_changes.append(file)
            
            if critical_changes:
                self.validation_results["recommendations"].append(
                    f"Critical files modified: {', '.join(critical_changes)}. These require careful review."
                )
            
            print(f"  ✅ Found {len(modified_files)} modified and {len(untracked_files)} untracked files")
            
        except Exception as e:
            self.validation_results["checks"]["git_status"] = {
                "status": "error",
                "message": str(e)
            }
            print(f"  ❌ Error validating git status: {e}")
    
    def validate_content_structure(self):
        """Validate content structure and organization"""
        print("\n📁 Validating content structure...")
        
        try:
            # Check key directories exist
            required_dirs = [
                "public/css",
                "public/js",
                "public/components",
                "public/generated-resources-alpha",
                "public/dist-handouts",
                "public/dist-lessons",
                "public/dist-units",
                "public/dist-assessments"
            ]
            
            missing_dirs = []
            for dir_path in required_dirs:
                full_path = self.base_dir / dir_path
                if not full_path.exists():
                    missing_dirs.append(dir_path)
            
            if missing_dirs:
                self.validation_results["checks"]["content_structure"] = {
                    "status": "error",
                    "message": f"Missing directories: {', '.join(missing_dirs)}"
                }
                print(f"  ❌ Missing directories: {', '.join(missing_dirs)}")
                return
            
            # Count files in key directories
            public_dir = self.base_dir / "public"
            handouts_count = len(list((public_dir / "dist-handouts").glob("*.html")))
            lessons_count = len(list((public_dir / "dist-lessons").glob("*.html")))
            
            self.validation_results["checks"]["content_structure"] = {
                "status": "success",
                "integrated_content": {
                    "handouts": handouts_count,
                    "lessons": lessons_count
                }
            }
            
            print(f"  ✅ Content structure valid. Integrated: {handouts_count} handouts, {lessons_count} lessons")
            
        except Exception as e:
            self.validation_results["checks"]["content_structure"] = {
                "status": "error",
                "message": str(e)
            }
            print(f"  ❌ Error validating content structure: {e}")
    
    def validate_css_styling(self):
        """Validate CSS and styling consistency"""
        print("\n🎨 Validating CSS styling...")
        
        try:
            # Check if main CSS file exists
            css_file = self.base_dir / "public/css/te-kete-professional.css"
            if not css_file.exists():
                self.validation_results["checks"]["css_styling"] = {
                    "status": "error",
                    "message": "Main CSS file missing"
                }
                print("  ❌ Main CSS file missing")
                return
            
            # Check for required CSS classes
            with open(css_file, 'r') as f:
                css_content = f.read()
            
            required_classes = [
                ".hero-description",
                ".hero-actions",
                ".resource-grid",
                ".resource-item",
                ".container"
            ]
            
            missing_classes = []
            for class_name in required_classes:
                if class_name not in css_content:
                    missing_classes.append(class_name)
            
            if missing_classes:
                self.validation_results["checks"]["css_styling"] = {
                    "status": "warning",
                    "message": f"Missing CSS classes: {', '.join(missing_classes)}"
                }
                print(f"  ⚠️ Missing CSS classes: {', '.join(missing_classes)}")
            else:
                self.validation_results["checks"]["css_styling"] = {
                    "status": "success",
                    "message": "All required CSS classes present"
                }
                print("  ✅ All required CSS classes present")
            
        except Exception as e:
            self.validation_results["checks"]["css_styling"] = {
                "status": "error",
                "message": str(e)
            }
            print(f"  ❌ Error validating CSS: {e}")
    
    def validate_navigation(self):
        """Validate navigation and links"""
        print("\n🔗 Validating navigation...")
        
        try:
            # Check header component exists
            header_file = self.base_dir / "public/components/header.html"
            if not header_file.exists():
                self.validation_results["checks"]["navigation"] = {
                    "status": "error",
                    "message": "Header component missing"
                }
                print("  ❌ Header component missing")
                return
            
            # Check resource hub exists and has links to integrated content
            resource_hub = self.base_dir / "public/resource-hub.html"
            if not resource_hub.exists():
                self.validation_results["checks"]["navigation"] = {
                    "status": "error",
                    "message": "Resource hub missing"
                }
                print("  ❌ Resource hub missing")
                return
            
            with open(resource_hub, 'r') as f:
                hub_content = f.read()
            
            # Check for links to integrated content
            required_links = [
                "/dist-handouts/",
                "/dist-lessons/",
                "/dist-units/",
                "/dist-assessments/"
            ]
            
            missing_links = []
            for link in required_links:
                if link not in hub_content:
                    missing_links.append(link)
            
            if missing_links:
                self.validation_results["checks"]["navigation"] = {
                    "status": "warning",
                    "message": f"Missing navigation links: {', '.join(missing_links)}"
                }
                print(f"  ⚠️ Missing navigation links: {', '.join(missing_links)}")
            else:
                self.validation_results["checks"]["navigation"] = {
                    "status": "success",
                    "message": "Navigation links present"
                }
                print("  ✅ Navigation links present")
            
        except Exception as e:
            self.validation_results["checks"]["navigation"] = {
                "status": "error",
                "message": str(e)
            }
            print(f"  ❌ Error validating navigation: {e}")
    
    def validate_cultural_content(self):
        """Validate cultural content and authenticity"""
        print("\n🌺 Validating cultural content...")
        
        try:
            # Sample check for cultural elements in integrated content
            handouts_dir = self.base_dir / "public/dist-handouts"
            cultural_keywords = [
                "māori", "maori", "whakataukī", "whakapapa", "marae", 
                "tangata whenua", "kaitiakitanga", "mana", "tikanga"
            ]
            
            cultural_files = 0
            total_files = 0
            
            for handout in handouts_dir.glob("*.html"):
                if handout.name == "index.html":
                    continue
                    
                total_files += 1
                with open(handout, 'r') as f:
                    content = f.read().lower()
                
                if any(keyword in content for keyword in cultural_keywords):
                    cultural_files += 1
            
            cultural_percentage = (cultural_files / total_files * 100) if total_files > 0 else 0
            
            self.validation_results["checks"]["cultural_content"] = {
                "status": "success",
                "cultural_files": cultural_files,
                "total_files": total_files,
                "cultural_percentage": round(cultural_percentage, 1)
            }
            
            print(f"  ✅ Cultural content: {cultural_files}/{total_files} files ({cultural_percentage:.1f}%)")
            
            if cultural_percentage < 50:
                self.validation_results["recommendations"].append(
                    f"Only {cultural_percentage:.1f}% of integrated content includes cultural elements. Consider enhancing cultural integration."
                )
            
        except Exception as e:
            self.validation_results["checks"]["cultural_content"] = {
                "status": "error",
                "message": str(e)
            }
            print(f"  ❌ Error validating cultural content: {e}")
    
    def validate_performance(self):
        """Validate performance metrics"""
        print("\n⚡ Validating performance...")
        
        try:
            # Check for large files that might impact performance
            large_files = []
            total_size = 0
            
            for root, dirs, files in os.walk(self.base_dir / "public"):
                for file in files:
                    if file.endswith(('.html', '.css', '.js')):
                        file_path = Path(root) / file
                        file_size = file_path.stat().st_size
                        total_size += file_size
                        
                        if file_size > 100000:  # 100KB
                            large_files.append({
                                "path": str(file_path.relative_to(self.base_dir)),
                                "size": file_size
                            })
            
            self.validation_results["checks"]["performance"] = {
                "status": "success",
                "total_size_mb": round(total_size / 1024 / 1024, 2),
                "large_files_count": len(large_files),
                "large_files": large_files[:5]  # First 5
            }
            
            print(f"  ✅ Total size: {total_size / 1024 / 1024:.2f}MB, Large files: {len(large_files)}")
            
            if len(large_files) > 10:
                self.validation_results["recommendations"].append(
                    f"Found {len(large_files)} large files (>100KB). Consider optimizing for better performance."
                )
            
        except Exception as e:
            self.validation_results["checks"]["performance"] = {
                "status": "error",
                "message": str(e)
            }
            print(f"  ❌ Error validating performance: {e}")
    
    def validate_accessibility(self):
        """Validate accessibility features"""
        print("\n♿ Validating accessibility...")
        
        try:
            # Check for alt text in images (sample check)
            missing_alt = 0
            total_images = 0
            
            for handout in (self.base_dir / "public/dist-handouts").glob("*.html")[:10]:  # Sample 10 files
                if handout.name == "index.html":
                    continue
                    
                with open(handout, 'r') as f:
                    content = f.read()
                
                # Find all img tags
                img_tags = re.findall(r'<img[^>]*>', content)
                total_images += len(img_tags)
                
                for img in img_tags:
                    if 'alt=' not in img:
                        missing_alt += 1
            
            alt_percentage = ((total_images - missing_alt) / total_images * 100) if total_images > 0 else 100
            
            self.validation_results["checks"]["accessibility"] = {
                "status": "success",
                "images_with_alt": total_images - missing_alt,
                "total_images": total_images,
                "alt_percentage": round(alt_percentage, 1)
            }
            
            print(f"  ✅ Alt text: {total_images - missing_alt}/{total_images} images ({alt_percentage:.1f}%)")
            
            if alt_percentage < 80:
                self.validation_results["recommendations"].append(
                    f"Only {alt_percentage:.1f}% of images have alt text. Improve accessibility by adding alt text to all images."
                )
            
        except Exception as e:
            self.validation_results["checks"]["accessibility"] = {
                "status": "error",
                "message": str(e)
            }
            print(f"  ❌ Error validating accessibility: {e}")
    
    def validate_integrated_content(self):
        """Validate integrated content quality"""
        print("\n📚 Validating integrated content...")
        
        try:
            # Check if integrated content has proper structure
            issues = []
            
            # Check handouts
            for handout in (self.base_dir / "public/dist-handouts").glob("*.html")[:5]:  # Sample 5 files
                if handout.name == "index.html":
                    continue
                    
                with open(handout, 'r') as f:
                    content = f.read()
                
                # Check for proper CSS
                if 'te-kete-professional.css' not in content:
                    issues.append(f"{handout.name}: Missing te-kete-professional.css")
                
                # Check for header component
                if 'header-component' not in content:
                    issues.append(f"{handout.name}: Missing header component")
            
            # Check lessons
            for lesson in (self.base_dir / "public/dist-lessons").glob("*.html")[:5]:  # Sample 5 files
                if lesson.name == "index.html":
                    continue
                    
                with open(lesson, 'r') as f:
                    content = f.read()
                
                # Check for proper CSS
                if 'te-kete-professional.css' not in content:
                    issues.append(f"{lesson.name}: Missing te-kete-professional.css")
                
                # Check for header component
                if 'header-component' not in content:
                    issues.append(f"{lesson.name}: Missing header component")
            
            if issues:
                self.validation_results["checks"]["integrated_content"] = {
                    "status": "warning",
                    "issues": issues[:10]  # First 10
                }
                print(f"  ⚠️ Found {len(issues)} issues in integrated content")
            else:
                self.validation_results["checks"]["integrated_content"] = {
                    "status": "success",
                    "message": "Integrated content structure looks good"
                }
                print("  ✅ Integrated content structure looks good")
            
        except Exception as e:
            self.validation_results["checks"]["integrated_content"] = {
                "status": "error",
                "message": str(e)
            }
            print(f"  ❌ Error validating integrated content: {e}")
    
    def generate_validation_report(self):
        """Generate final validation report"""
        print("\n📊 Generating validation report...")
        
        # Calculate overall status
        statuses = [check.get("status", "unknown") for check in self.validation_results["checks"].values()]
        
        if "error" in statuses:
            overall_status = "error"
        elif "warning" in statuses:
            overall_status = "warning"
        else:
            overall_status = "success"
        
        self.validation_results["overall_status"] = overall_status
        
        # Save report
        report_file = self.base_dir / "validation-report.json"
        with open(report_file, 'w') as f:
            json.dump(self.validation_results, f, indent=2)
        
        print(f"  ✅ Validation report saved to {report_file}")
        print(f"\n🎯 Overall Status: {overall_status.upper()}")
        
        if self.validation_results["recommendations"]:
            print("\n💡 Recommendations:")
            for rec in self.validation_results["recommendations"]:
                print(f"  - {rec}")
        
        return overall_status

if __name__ == "__main__":
    validator = WorkflowPipelineValidator()
    results = validator.run_full_validation()
    
    # Exit with appropriate code
    if results["overall_status"] == "error":
        exit(1)
    elif results["overall_status"] == "warning":
        exit(2)
    else:
        exit(0)
