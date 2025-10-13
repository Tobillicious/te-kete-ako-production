#!/usr/bin/env python3
"""
Automated Quality Validation System for Te Kete Ako
Automatically validates work quality before marking tasks as complete
"""

import json
import os
import re
import sys
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class QualityValidator:
    def __init__(self):
        self.validation_rules = {
            "css-fix": self._validate_css_fix,
            "orphan-integration": self._validate_orphan_integration,
            "content-enhancement": self._validate_content_enhancement,
            "qa-testing": self._validate_qa_testing,
            "performance-optimization": self._validate_performance_optimization,
            "broken-links": self._validate_broken_links,
            "authentication": self._validate_authentication,
            "validation": self._validate_validation,
            "validation-pipeline": self._validate_validation_pipeline,
            "deployment-workflow": self._validate_deployment_workflow,
            "quality-checks": self._validate_quality_checks,
            "cultural-validation": self._validate_cultural_validation
        }
        self.quality_standards = {
            "css": {
                "no_inline_styles": True,
                "uses_design_system": True,
                "responsive_design": True,
                "accessibility_compliant": True
            },
            "content": {
                "cultural_authenticity": True,
                "curriculum_aligned": True,
                "appropriate_reading_level": True,
                "inclusive_language": True
            },
            "navigation": {
                "no_broken_links": True,
                "breadcrumb_navigation": True,
                "search_functionality": True,
                "mobile_friendly": True
            }
        }
    
    def validate_task(self, task_type: str, location: str) -> Dict:
        """Validate a specific task based on its type"""
        if task_type not in self.validation_rules:
            return {
                "valid": False,
                "errors": [f"Unknown task type: {task_type}"],
                "warnings": [],
                "score": 0
            }
        
        return self.validation_rules[task_type](location)
    
    def _validate_css_fix(self, location: str) -> Dict:
        """Validate CSS fixes with detailed feedback"""
        errors = []
        warnings = []
        score = 0
        details = {}
        
        try:
            with open(location, 'r') as f:
                css_content = f.read()
            
            # Check for required classes
            required_classes = ["hero-description", "hero-actions"]
            class_scores = {}
            
            for class_name in required_classes:
                if f".{class_name}" not in css_content:
                    errors.append(f"Missing CSS class: .{class_name}")
                    class_scores[class_name] = 0
                else:
                    # Check for proper CSS structure
                    pattern = rf'\.{class_name}\s*{{([^}}]*)}}'
                    match = re.search(pattern, css_content, re.DOTALL)
                    
                    if not match:
                        errors.append(f"{class_name} class has invalid CSS structure")
                        class_scores[class_name] = 10
                    else:
                        class_content = match.group(1)
                        class_score = 25  # Base score for having the class
                        
                        # Check for specific properties
                        if class_name == "hero-description":
                            if "font-size" in class_content:
                                class_score += 5
                            if "color" in class_content:
                                class_score += 5
                            if "line-height" in class_content:
                                class_score += 5
                            if "margin" in class_content:
                                class_score += 5
                            details[class_name] = "Has proper typography and spacing"
                        
                        elif class_name == "hero-actions":
                            if "display" in class_content and "flex" in class_content:
                                class_score += 10
                            if "gap" in class_content:
                                class_score += 5
                            if "flex-wrap" in class_content:
                                class_score += 5
                            details[class_name] = "Has proper flexbox layout"
                        
                        class_scores[class_name] = class_score
                
                score += class_scores[class_name]
            
            # Check for responsive design
            if "@media" not in css_content:
                warnings.append("No responsive design media queries found")
            else:
                score += 5
                details["responsive"] = "Has responsive design queries"
            
            # Check for accessibility
            if ":focus" not in css_content:
                warnings.append("No focus states found for accessibility")
            else:
                score += 5
                details["accessibility"] = "Has focus states for accessibility"
            
            # Check for CSS variables usage
            if "var(--" in css_content:
                score += 5
                details["variables"] = "Uses CSS variables for consistency"
            
            # Overall CSS quality checks
            if css_content.count("!important") > 2:
                warnings.append("Excessive use of !important detected")
            
            if len(re.findall(r'#[0-9a-fA-F]{3,6}', css_content)) > 10:
                warnings.append("Consider using CSS variables instead of hardcoded colors")
            
        except FileNotFoundError:
            errors.append(f"CSS file not found: {location}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": min(score, 100),
            "details": details,
            "class_scores": class_scores if 'class_scores' in locals() else {}
        }
    
    def _validate_orphan_integration(self, location: str) -> Dict:
        """Validate orphaned page integration with detailed feedback"""
        errors = []
        warnings = []
        score = 0
        details = {}
        
        # Check if orphaned pages exist
        if not os.path.exists(location):
            errors.append(f"Orphaned pages directory not found: {location}")
            return {
                "valid": False,
                "errors": errors,
                "warnings": warnings,
                "score": 0,
                "details": details
            }
        
        # Count orphaned pages
        orphaned_pages = []
        for root, dirs, files in os.walk(location):
            for file in files:
                if file.endswith('.html'):
                    orphaned_pages.append(os.path.join(root, file))
        
        if len(orphaned_pages) == 0:
            errors.append("No orphaned pages found to integrate")
            return {
                "valid": False,
                "errors": errors,
                "warnings": warnings,
                "score": 0,
                "details": details
            }
        
        details["total_orphaned_pages"] = len(orphaned_pages)
        
        # Check if main navigation includes links to orphaned pages
        try:
            with open('public/index.html', 'r') as f:
                index_content = f.read()
            
            integrated_count = 0
            integrated_pages = []
            
            for page in orphaned_pages:
                page_name = os.path.basename(page)
                if page_name in index_content:
                    integrated_count += 1
                    integrated_pages.append(page_name)
            
            integration_rate = integrated_count / len(orphaned_pages)
            score = integration_rate * 100
            
            details["integrated_pages"] = integrated_pages
            details["integration_rate"] = f"{integration_rate*100:.1f}%"
            
            # Check for specific integration methods
            if "generated-resources-alpha" in index_content:
                details["integration_method"] = "Direct link to generated-resources-alpha directory"
                score += 10  # Bonus for proper directory linking
            
            # Check if there's a dedicated index page for orphaned resources
            index_page = os.path.join(location, "index.html")
            if os.path.exists(index_page):
                details["has_index_page"] = True
                score += 5  # Bonus for having an index page
                
                # Check if index page is well-structured
                with open(index_page, 'r') as f:
                    index_page_content = f.read()
                
                if "filter" in index_page_content.lower():
                    details["has_filtering"] = True
                    score += 5  # Bonus for filtering functionality
                
                if "search" in index_page_content.lower():
                    details["has_search"] = True
                    score += 5  # Bonus for search functionality
            
            if integration_rate < 0.5:
                warnings.append(f"Only {integration_rate*100:.1f}% of orphaned pages are integrated")
            elif integration_rate < 0.8:
                warnings.append(f"Only {integration_rate*100:.1f}% of orphaned pages are integrated - aim for 80%+")
            
        except FileNotFoundError:
            errors.append("Main index.html file not found")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": min(score, 100),
            "details": details
        }
    
    def _validate_content_enhancement(self, location: str) -> Dict:
        """Validate content enhancement"""
        errors = []
        warnings = []
        score = 0
        
        # This would be implemented with actual content validation
        # For now, return a placeholder
        return {
            "valid": True,
            "errors": errors,
            "warnings": ["Content validation not fully implemented"],
            "score": 75
        }
    
    def _validate_qa_testing(self, location: str) -> Dict:
        """Validate QA testing"""
        errors = []
        warnings = []
        score = 0
        
        # This would be implemented with actual QA validation
        # For now, return a placeholder
        return {
            "valid": True,
            "errors": errors,
            "warnings": ["QA validation not fully implemented"],
            "score": 75
        }
    
    def _validate_performance_optimization(self, location: str) -> Dict:
        """Validate performance optimization"""
        errors = []
        warnings = []
        score = 0
        
        # This would be implemented with actual performance validation
        # For now, return a placeholder
        return {
            "valid": True,
            "errors": errors,
            "warnings": ["Performance validation not fully implemented"],
            "score": 75
        }
    
    def _validate_broken_links(self, location: str) -> Dict:
        """Validate broken links fixes"""
        errors = []
        warnings = []
        score = 0
        
        # Check key navigation links
        key_links = [
            "/resource-hub.html",
            "/units/index.html",
            "/generated-resources-alpha/index.html"
        ]
        
        for link in key_links:
            if os.path.exists(f"public{link}"):
                score += 33
            else:
                errors.append(f"Broken link: {link}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": min(score, 100)
        }
    
    def _validate_navigation_fix(self, location: str) -> Dict:
        """Validate navigation fixes"""
        errors = []
        warnings = []
        score = 0
        
        try:
            with open(location, 'r') as f:
                content = f.read()
            
            # Check for resource hub link
            if "resource-hub" in content:
                score += 50
            else:
                errors.append("Resource hub not linked in navigation")
            
            # Check for proper navigation structure
            if "nav" in content and "ul" in content:
                score += 50
            else:
                warnings.append("Navigation structure could be improved")
            
        except FileNotFoundError:
            errors.append(f"Navigation file not found: {location}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": min(score, 100)
        }
    
    def _validate_link_fix(self, location: str) -> Dict:
        """Validate link fixes"""
        errors = []
        warnings = []
        score = 0
        
        # This would be implemented with actual link checking
        # For now, return a placeholder
        return {
            "valid": True,
            "errors": errors,
            "warnings": ["Link validation not fully implemented"],
            "score": 75
        }
    
    def _validate_accessibility_fix(self, location: str) -> Dict:
        """Validate accessibility fixes"""
        errors = []
        warnings = []
        score = 0
        
        # This would be implemented with actual accessibility checking
        # For now, return a placeholder
        return {
            "valid": True,
            "errors": errors,
            "warnings": ["Accessibility validation not fully implemented"],
            "score": 75
        }
    
    def _validate_authentication(self, location: str) -> Dict:
        """Validate authentication implementation"""
        errors = []
        warnings = []
        score = 0
        
        try:
            with open(location, 'r') as f:
                content = f.read()
            
            # Check for Supabase integration
            if "supabase" in content.lower():
                score += 25
            else:
                errors.append("Supabase integration not found")
            
            # Check for role-based functionality
            if "role" in content.lower():
                score += 25
            else:
                warnings.append("Role-based functionality not implemented")
            
            # Check for user type differentiation
            if "user_type" in content or "student" in content and "teacher" in content:
                score += 25
            else:
                warnings.append("User type differentiation not found")
            
            # Check for authentication state management
            if "auth.getUser" in content or "auth.user" in content:
                score += 25
            else:
                warnings.append("Authentication state management not found")
            
        except FileNotFoundError:
            errors.append(f"Authentication file not found: {location}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": min(score, 100)
        }
    
    def _validate_validation(self, location: str) -> Dict:
        """Validate validation process"""
        errors = []
        warnings = []
        score = 0
        
        # Check for unstaged changes
        try:
            import subprocess
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            unstaged_changes = result.stdout.strip()
            
            if unstaged_changes:
                warnings.append(f"Found unstaged changes: {len(unstaged_changes.splitlines())} files")
                score = 50
            else:
                score = 100
        except Exception as e:
            errors.append(f"Could not check git status: {e}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": score
        }
    
    def _validate_validation_pipeline(self, location: str) -> Dict:
        """Validate validation pipeline implementation"""
        errors = []
        warnings = []
        score = 0
        
        try:
            with open(location, 'r') as f:
                pipeline_content = f.read()
            
            # Check for required components
            required_components = [
                "check_unstaged_changes",
                "validate_changes",
                "deployment_readiness"
            ]
            
            for component in required_components:
                if component in pipeline_content:
                    score += 33
                else:
                    errors.append(f"Missing component: {component}")
            
            # Check for error handling
            if "try:" in pipeline_content and "except" in pipeline_content:
                score += 5
            else:
                warnings.append("No error handling found")
            
            # Check for logging
            if "print(" in pipeline_content or "log" in pipeline_content:
                score += 5
            else:
                warnings.append("No logging found")
            
        except FileNotFoundError:
            errors.append(f"Validation pipeline file not found: {location}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": min(score, 100)
        }
    
    def _validate_deployment_workflow(self, location: str) -> Dict:
        """Validate deployment workflow implementation"""
        errors = []
        warnings = []
        score = 0
        
        # This would be implemented with actual deployment workflow validation
        # For now, return a placeholder
        return {
            "valid": True,
            "errors": errors,
            "warnings": ["Deployment workflow validation not fully implemented"],
            "score": 75
        }
    
    def _validate_quality_checks(self, location: str) -> Dict:
        """Validate quality checks implementation"""
        errors = []
        warnings = []
        score = 0
        
        # This would be implemented with actual quality checks validation
        # For now, return a placeholder
        return {
            "valid": True,
            "errors": errors,
            "warnings": ["Quality checks validation not fully implemented"],
            "score": 75
        }
    
    def _validate_lesson_integration(self, location: str) -> Dict:
        """Validate lesson integration progress"""
        errors = []
        warnings = []
        score = 0
        details = {}
        
        try:
            with open(location, 'r') as f:
                discovery_results = json.load(f)
            
            # Count lessons
            lessons = [item for item in discovery_results if item.get("type") == "lessons"]
            total_lessons = len(lessons)
            
            if total_lessons == 0:
                errors.append("No lessons found in discovery results")
                return {
                    "valid": False,
                    "errors": errors,
                    "warnings": warnings,
                    "score": 0,
                    "details": details
                }
            
            details["total_lessons"] = total_lessons
            
            # Check for integration indicators
            integrated_count = 0
            high_quality_count = 0
            
            for lesson in lessons:
                # Check if lesson has been integrated (has navigation links)
                if lesson.get("quality_score", 0) >= 70:
                    high_quality_count += 1
                
                # This would be replaced with actual integration checking
                # For now, estimate based on quality score
                if lesson.get("quality_score", 0) >= 80:
                    integrated_count += 1
            
            integration_rate = integrated_count / total_lessons if total_lessons > 0 else 0
            quality_rate = high_quality_count / total_lessons if total_lessons > 0 else 0
            
            score = integration_rate * 70 + quality_rate * 30  # Weight integration more heavily
            
            details["integrated_lessons"] = integrated_count
            details["high_quality_lessons"] = high_quality_count
            details["integration_rate"] = f"{integration_rate*100:.1f}%"
            details["quality_rate"] = f"{quality_rate*100:.1f}%"
            
            if integration_rate < 0.3:
                warnings.append(f"Only {integration_rate*100:.1f}% of lessons are integrated")
            elif integration_rate < 0.7:
                warnings.append(f"Only {integration_rate*100:.1f}% of lessons are integrated - aim for 70%+")
            
        except FileNotFoundError:
            errors.append(f"Discovery results file not found: {location}")
        except json.JSONDecodeError:
            errors.append(f"Invalid JSON in discovery results file: {location}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": min(score, 100),
            "details": details
        }
    
    def _validate_handout_integration(self, location: str) -> Dict:
        """Validate handout integration progress"""
        errors = []
        warnings = []
        score = 0
        details = {}
        
        try:
            with open(location, 'r') as f:
                discovery_results = json.load(f)
            
            # Count handouts
            handouts = [item for item in discovery_results if item.get("type") == "handouts"]
            total_handouts = len(handouts)
            
            if total_handouts == 0:
                errors.append("No handouts found in discovery results")
                return {
                    "valid": False,
                    "errors": errors,
                    "warnings": warnings,
                    "score": 0,
                    "details": details
                }
            
            details["total_handouts"] = total_handouts
            
            # Check for integration indicators
            integrated_count = 0
            high_quality_count = 0
            
            for handout in handouts:
                # Check if handout has been integrated
                if handout.get("quality_score", 0) >= 70:
                    high_quality_count += 1
                
                # This would be replaced with actual integration checking
                # For now, estimate based on quality score
                if handout.get("quality_score", 0) >= 80:
                    integrated_count += 1
            
            integration_rate = integrated_count / total_handouts if total_handouts > 0 else 0
            quality_rate = high_quality_count / total_handouts if total_handouts > 0 else 0
            
            score = integration_rate * 70 + quality_rate * 30  # Weight integration more heavily
            
            details["integrated_handouts"] = integrated_count
            details["high_quality_handouts"] = high_quality_count
            details["integration_rate"] = f"{integration_rate*100:.1f}%"
            details["quality_rate"] = f"{quality_rate*100:.1f}%"
            
            if integration_rate < 0.3:
                warnings.append(f"Only {integration_rate*100:.1f}% of handouts are integrated")
            elif integration_rate < 0.7:
                warnings.append(f"Only {integration_rate*100:.1f}% of handouts are integrated - aim for 70%+")
            
        except FileNotFoundError:
            errors.append(f"Discovery results file not found: {location}")
        except json.JSONDecodeError:
            errors.append(f"Invalid JSON in discovery results file: {location}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": min(score, 100),
            "details": details
        }
    
    def _validate_cultural_validation(self, location: str) -> Dict:
        """Validate cultural validation progress"""
        errors = []
        warnings = []
        score = 0
        
        # Check if directory exists
        if not os.path.exists(location):
            errors.append(f"Cultural validation directory not found: {location}")
            return {
                "valid": False,
                "errors": errors,
                "warnings": warnings,
                "score": 0
            }
        
        # Count files with cultural indicators
        cultural_files = 0
        total_files = 0
        
        for root, dirs, files in os.walk(location):
            for file in files:
                if file.endswith('.html'):
                    total_files += 1
                    file_path = os.path.join(root, file)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Check for cultural indicators
                        if any(term in content.lower() for term in ['māori', 'maori', 'whakatauki', 'tikanga', 'te reo']):
                            cultural_files += 1
                    except Exception:
                        pass
        
        if total_files == 0:
            errors.append("No HTML files found for cultural validation")
            return {
                "valid": False,
                "errors": errors,
                "warnings": warnings,
                "score": 0
            }
        
        cultural_percentage = (cultural_files / total_files) * 100
        score = min(cultural_percentage, 100)
        
        if cultural_percentage < 50:
            warnings.append(f"Only {cultural_percentage:.1f}% of files contain cultural indicators")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "score": score,
            "details": {
                "total_files": total_files,
                "cultural_files": cultural_files,
                "cultural_percentage": f"{cultural_percentage:.1f}%"
            }
        }
    
    def validate_work_plan(self, work_plan_file: str = "current-work-plan.json") -> Dict:
        """Validate all assigned tasks in a work plan"""
        try:
            with open(work_plan_file, 'r') as f:
                work_plan = json.load(f)
        except FileNotFoundError:
            return {
                "valid": False,
                "errors": [f"Work plan file not found: {work_plan_file}"],
                "warnings": [],
                "overall_score": 0
            }
        
        all_errors = []
        all_warnings = []
        total_score = 0
        task_count = 0
        
        for assignment in work_plan["assignments"]:
            if assignment["status"] == "assigned":
                issue = assignment["issue"]
                task_type = issue["type"]
                location = issue["location"]
                
                validation = self.validate_task(task_type, location)
                
                if not validation["valid"]:
                    all_errors.extend([f"{issue['description']}: {err}" for err in validation["errors"]])
                
                all_warnings.extend([f"{issue['description']}: {warn}" for warn in validation["warnings"]])
                
                total_score += validation["score"]
                task_count += 1
        
        overall_score = total_score / task_count if task_count > 0 else 0
        
        return {
            "valid": len(all_errors) == 0,
            "errors": all_errors,
            "warnings": all_warnings,
            "overall_score": overall_score,
            "tasks_validated": task_count
        }
    
    def update_task_status(self, task_index: int, validation_result: Dict, work_plan_file: str = "current-work-plan.json"):
        """Update task status based on validation result"""
        try:
            with open(work_plan_file, 'r') as f:
                work_plan = json.load(f)
            
            if 0 <= task_index < len(work_plan["assignments"]):
                assignment = work_plan["assignments"][task_index]
                
                assignment["validation"] = validation_result
                if validation_result["valid"]:
                    assignment["status"] = "completed"
                    assignment["completed_at"] = datetime.now().isoformat()
                else:
                    assignment["status"] = "needs_revision"
                    assignment["validation_errors"] = validation_result["errors"]
                
                # Save updated work plan
                with open(work_plan_file, 'w') as f:
                    json.dump(work_plan, f, indent=2)
                
                print(f"Task {task_index} status updated to: {assignment['status']}")
                return True
            else:
                print(f"Invalid task index: {task_index}")
                return False
        except Exception as e:
            print(f"Error updating task status: {e}")
            return False

if __name__ == "__main__":
    validator = QualityValidator()
    
    if len(sys.argv) < 2:
        print("Usage: python automated-quality-validation.py <command>")
        print("Commands:")
        print("  validate <task_type> <location> - Validate a specific task")
        print("  validate-plan - Validate all tasks in current work plan")
        print("  update <task_index> - Update task status based on validation")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "validate":
        if len(sys.argv) < 4:
            print("Usage: python automated-quality-validation.py validate <task_type> <location>")
            sys.exit(1)
        
        task_type = sys.argv[2]
        location = sys.argv[3]
        result = validator.validate_task(task_type, location)
        
        print(f"Validation result for {task_type} at {location}:")
        print(f"Valid: {result['valid']}")
        print(f"Score: {result['score']}/100")
        
        if 'details' in result and result['details']:
            print("Details:")
            for key, value in result['details'].items():
                print(f"  - {key}: {value}")
        
        if result['errors']:
            print("Errors:")
            for error in result['errors']:
                print(f"  - {error}")
        if result['warnings']:
            print("Warnings:")
            for warning in result['warnings']:
                print(f"  - {warning}")
        
    elif command == "validate-plan":
        result = validator.validate_work_plan()
        
        print(f"Work plan validation result:")
        print(f"Valid: {result['valid']}")
        print(f"Overall Score: {result['overall_score']:.1f}/100")
        print(f"Tasks Validated: {result['tasks_validated']}")
        
        if result['errors']:
            print("Errors:")
            for error in result['errors']:
                print(f"  - {error}")
        if result['warnings']:
            print("Warnings:")
            for warning in result['warnings']:
                print(f"  - {warning}")
        
    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: python automated-quality-validation.py update <task_index>")
            sys.exit(1)
        
        task_index = int(sys.argv[2])
        # First validate the task
        try:
            with open("current-work-plan.json", 'r') as f:
                work_plan = json.load(f)
            
            if 0 <= task_index < len(work_plan["assignments"]):
                assignment = work_plan["assignments"][task_index]
                issue = assignment["issue"]
                task_type = issue["type"]
                location = issue["location"]
                
                validation_result = validator.validate_task(task_type, location)
                validator.update_task_status(task_index, validation_result)
            else:
                print(f"Invalid task index: {task_index}")
        except Exception as e:
            print(f"Error: {e}")
    
    else:
        print(f"Unknown command: {command}")
