#!/usr/bin/env python3
"""
Validation and Deployment Pipeline for Te Kete Ako
Validates unstaged changes before deployment
"""

import os
import sys
import subprocess
import json
from datetime import datetime

class ValidationDeploymentPipeline:
    def __init__(self):
        self.validation_results = {
            "timestamp": datetime.now().isoformat(),
            "unstaged_changes": {},
            "validation_checks": {},
            "deployment_readiness": False
        }
    
    def check_unstaged_changes(self):
        """Check for unstaged changes"""
        print("🔍 Checking for unstaged changes...")
        
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            unstaged_output = result.stdout.strip()
            
            if not unstaged_output:
                print("✅ No unstaged changes found")
                self.validation_results["unstaged_changes"] = {"count": 0, "files": []}
                return True
            
            # Parse unstaged changes
            unstaged_files = []
            for line in unstaged_output.splitlines():
                parts = line.split()
                if len(parts) >= 2:
                    status = parts[0]
                    file_path = parts[1]
                    unstaged_files.append({
                        "status": status,
                        "file": file_path,
                        "type": self._get_file_type(file_path)
                    })
            
            print(f"⚠️ Found {len(unstaged_files)} unstaged changes")
            self.validation_results["unstaged_changes"] = {
                "count": len(unstaged_files),
                "files": unstaged_files
            }
            
            return False
            
        except Exception as e:
            print(f"❌ Error checking unstaged changes: {e}")
            return False
    
    def _get_file_type(self, file_path):
        """Determine the type of file based on path"""
        if file_path.endswith('.html'):
            return 'html'
        elif file_path.endswith('.css'):
            return 'css'
        elif file_path.endswith('.js'):
            return 'javascript'
        elif file_path.endswith('.py'):
            return 'python'
        elif file_path.endswith('.md'):
            return 'markdown'
        elif file_path.endswith('.json'):
            return 'json'
        else:
            return 'other'
    
    def validate_html_files(self, unstaged_files):
        """Validate HTML files"""
        print("📄 Validating HTML files...")
        
        html_files = [f for f in unstaged_files if f["type"] == "html"]
        validation_results = []
        
        for file_info in html_files:
            file_path = file_info["file"]
            result = self._validate_html_file(file_path)
            validation_results.append({
                "file": file_path,
                "valid": result["valid"],
                "errors": result.get("errors", []),
                "warnings": result.get("warnings", [])
            })
        
        self.validation_results["validation_checks"]["html"] = validation_results
        return all(r["valid"] for r in validation_results)
    
    def _validate_html_file(self, file_path):
        """Validate a single HTML file"""
        result = {"valid": True, "errors": [], "warnings": []}
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Check if this is a component file (included in other files)
            is_component = "components/" in file_path
            
            # Skip some validations for component files
            if not is_component:
                # Check for basic HTML structure
                if not content.strip().startswith('<!DOCTYPE html>') and not content.strip().startswith('<html'):
                    result["warnings"].append("Missing DOCTYPE declaration")
                
                # Check for required meta tags
                if '<meta charset=' not in content:
                    result["errors"].append("Missing charset meta tag")
                    result["valid"] = False
                
                if '<meta name="viewport"' not in content:
                    result["warnings"].append("Missing viewport meta tag")
            
            # Check for alt text on images
            import re
            img_tags = re.findall(r'<img[^>]*>', content)
            for img in img_tags:
                if 'alt=' not in img:
                    result["warnings"].append(f"Image missing alt text: {img[:50]}...")
            
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"Error reading file: {e}")
        
        return result
    
    def validate_css_files(self, unstaged_files):
        """Validate CSS files"""
        print("🎨 Validating CSS files...")
        
        css_files = [f for f in unstaged_files if f["type"] == "css"]
        validation_results = []
        
        for file_info in css_files:
            file_path = file_info["file"]
            result = self._validate_css_file(file_path)
            validation_results.append({
                "file": file_path,
                "valid": result["valid"],
                "errors": result.get("errors", []),
                "warnings": result.get("warnings", [])
            })
        
        self.validation_results["validation_checks"]["css"] = validation_results
        return all(r["valid"] for r in validation_results)
    
    def _validate_css_file(self, file_path):
        """Validate a single CSS file"""
        result = {"valid": True, "errors": [], "warnings": []}
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Check for CSS syntax errors (basic check)
            import re
            # Check for unmatched braces
            open_braces = content.count('{')
            close_braces = content.count('}')
            
            if open_braces != close_braces:
                result["errors"].append(f"Unmatched braces: {open_braces} open, {close_braces} close")
                result["valid"] = False
            
            # Check for important declarations (should be used sparingly)
            important_count = content.count('!important')
            if important_count > 5:
                result["warnings"].append(f"High number of !important declarations: {important_count}")
            
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"Error reading file: {e}")
        
        return result
    
    def validate_javascript_files(self, files):
        """Validate JavaScript files for syntax and best practices"""
        print("⚡ Validating JavaScript files...")
        
        js_files = [f for f in files if f["type"] == "javascript"]
        results = {}
        
        for file_info in js_files:
            file_path = file_info["file"]
            result = self._validate_js_file(file_path)
            results[file_info["file"]] = {
                "status": "validated" if not result["errors"] else "issues_found",
                "score": 100 - (len(result["errors"]) * 5),
                "issues": result["errors"]
            }
        
        self.validation_results["validation_checks"]["javascript"] = results
        print(f"✅ Validated {len(js_files)} JavaScript files")
        
        return results
    
    def _validate_js_file(self, file_path):
        """Validate a single JavaScript file"""
        result = {"valid": True, "errors": []}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic JavaScript validation
            issues = []
            
            # Check for syntax errors (basic)
            if 'console.log' in content and 'production' not in file_path.lower():
                issues.append("Console.log found in production code")
            
            # Check for use of eval
            if 'eval(' in content:
                issues.append("Use of eval() detected")
            
            result["errors"] = issues
            
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"Error reading file: {e}")
        
        return result
    
    def run_validation_pipeline(self):
        """Run the complete validation pipeline"""
        print("🔄 Starting Validation and Deployment Pipeline...")
        print("=" * 50)
        
        # Check for unstaged changes
        has_no_changes = self.check_unstaged_changes()
        if has_no_changes:
            self.validation_results["deployment_readiness"] = True
            return True
        
        unstaged_files = self.validation_results["unstaged_changes"]["files"]
        
        # Validate different file types
        html_valid = self.validate_html_files(unstaged_files)
        css_valid = self.validate_css_files(unstaged_files)
        js_valid = self.validate_javascript_files(unstaged_files)
        
        # Determine overall deployment readiness
        all_valid = html_valid and css_valid and js_valid
        self.validation_results["deployment_readiness"] = all_valid
        
        # Save validation results
        with open('validation-results.json', 'w') as f:
            json.dump(self.validation_results, f, indent=2)
        
        return all_valid
    
    def print_summary(self):
        """Print validation summary"""
        print("\n📊 Validation Summary:")
        print(f"Unstaged changes: {self.validation_results['unstaged_changes']['count']} files")
        
        for file_type, results in self.validation_results["validation_checks"].items():
            if isinstance(results, dict): # Changed from list to dict for JavaScript results
                valid_count = sum(1 for r in results.values() if r["valid"])
                total_count = len(results)
                print(f"{file_type.capitalize()}: {valid_count}/{total_count} files valid")
        
        print(f"Deployment ready: {'✅ Yes' if self.validation_results['deployment_readiness'] else '❌ No'}")
        
        if not self.validation_results["deployment_readiness"]:
            print("\n❌ Validation failed. Please fix errors before deployment.")
            return False
        else:
            print("\n✅ All validations passed. Ready for deployment!")
            return True

if __name__ == "__main__":
    pipeline = ValidationDeploymentPipeline()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--fix":
        print("🔧 Auto-fix mode not implemented yet")
        sys.exit(1)
    
    success = pipeline.run_validation_pipeline()
    pipeline.print_summary()
    
    sys.exit(0 if success else 1)
