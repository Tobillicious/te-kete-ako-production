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
from typing import Dict

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
    
    def run_file_validation(self, file_path: str) -> Dict:
        """Run validation on a specific file"""
        print(f"🔍 Validating file: {file_path}")
        
        file_path = self.base_dir / file_path
        validation_result = {
            "file": str(file_path),
            "status": "passed",
            "warnings": [],
            "errors": []
        }
        
        if not file_path.exists():
            validation_result["status"] = "failed"
            validation_result["errors"].append("File not found")
            return validation_result
        
        # Check file type and run appropriate validation
        if file_path.suffix == ".html":
            self._validate_html_file(file_path, validation_result)
        elif file_path.suffix == ".css":
            self._validate_css_file(file_path, validation_result)
        elif file_path.suffix == ".js":
            self._validate_js_file(file_path, validation_result)
        
        return validation_result
    
    def _validate_html_file(self, file_path: Path, result: Dict):
        """Validate HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for proper HTML structure
            if not content.strip().startswith("<!DOCTYPE html>") and not content.strip().startswith("<html"):
                result["warnings"].append("Missing DOCTYPE declaration")
            
            # Check for CSS link
            if "te-kete-professional.css" not in content:
                result["warnings"].append("Missing te-kete-professional.css link")
            
            # Check for header component
            if "header-component" not in content:
                result["warnings"].append("Missing header-component")
            
            # Check for cultural content
            māori_terms = ["māori", "maori", "tikanga", "te reo", "whakataukī"]
            if not any(term in content.lower() for term in māori_terms):
                result["warnings"].append("No mātauranga Māori content detected")
            
            # Check for accessibility
            if "alt=" not in content and "<img" in content:
                result["warnings"].append("Images without alt text detected")
            
        except Exception as e:
            result["status"] = "failed"
            result["errors"].append(f"Error reading file: {e}")
    
    def _validate_css_file(self, file_path: Path, result: Dict):
        """Validate CSS file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for CSS variables usage
            if "var(--" not in content:
                result["warnings"].append("No CSS variables usage detected")
            
            # Check for responsive design
            if "@media" not in content:
                result["warnings"].append("No responsive design media queries")
            
        except Exception as e:
            result["status"] = "failed"
            result["errors"].append(f"Error reading file: {e}")
    
    def _validate_js_file(self, file_path: Path, result: Dict):
        """Validate JavaScript file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for error handling
            if "try" not in content and "catch" not in content:
                result["warnings"].append("No error handling detected")
            
        except Exception as e:
            result["status"] = "failed"
            result["errors"].append(f"Error reading file: {e}")
    
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
