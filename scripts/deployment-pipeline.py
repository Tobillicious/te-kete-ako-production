#!/usr/bin/env python3
"""
Deployment Pipeline for Te Kete Ako
Handles testing, validation, and deployment workflow
"""

import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

class DeploymentPipeline:
    def __init__(self):
        self.base_dir = Path("/Users/admin/Documents/te-kete-ako-clean")
        self.deployment_log = []
    
    def run_deployment_pipeline(self, skip_validation=False):
        """Run the complete deployment pipeline"""
        print("🚀 Starting Te Kete Ako deployment pipeline...")
        
        # 1. Run validation (unless skipped)
        if not skip_validation:
            print("\n📋 Step 1: Running validation...")
            validation_result = self.run_validation()
            if validation_result != 0:
                print("❌ Validation failed. Deployment aborted.")
                return False
            print("✅ Validation passed!")
        
        # 2. Stage changes for commit
        print("\n📦 Step 2: Staging changes...")
        if not self.stage_changes():
            print("❌ Failed to stage changes. Deployment aborted.")
            return False
        print("✅ Changes staged!")
        
        # 3. Create commit with proper message
        print("\n📝 Step 3: Creating commit...")
        if not self.create_commit():
            print("❌ Failed to create commit. Deployment aborted.")
            return False
        print("✅ Commit created!")
        
        # 4. Push to remote
        print("\n📤 Step 4: Pushing to remote...")
        if not self.push_to_remote():
            print("❌ Failed to push to remote. Deployment aborted.")
            return False
        print("✅ Pushed to remote!")
        
        # 5. Update deployment log
        print("\n📊 Step 5: Updating deployment log...")
        self.update_deployment_log()
        print("✅ Deployment log updated!")
        
        print("\n🎉 Deployment completed successfully!")
        return True
    
    def run_validation(self):
        """Run the validation pipeline"""
        try:
            result = subprocess.run(
                ["python3", "scripts/validation-deployment-pipeline.py"],
                cwd=self.base_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print(f"Validation output:\n{result.stdout}")
                if result.stderr:
                    print(f"Validation errors:\n{result.stderr}")
                return result.returncode
            
            return 0
        except Exception as e:
            print(f"Error running validation: {e}")
            return 1
    
    def stage_changes(self):
        """Stage changes for commit"""
        try:
            # Stage new content directories
            new_dirs = [
                "public/dist-handouts/",
                "public/dist-lessons/",
                "public/dist-units/",
                "public/dist-assessments/",
                "scripts/"
            ]
            
            for dir_path in new_dirs:
                result = subprocess.run(
                    ["git", "add", dir_path],
                    cwd=self.base_dir,
                    capture_output=True,
                    text=True
                )
                if result.returncode != 0:
                    print(f"Failed to stage {dir_path}: {result.stderr}")
                    return False
            
            # Stage modified critical files
            critical_files = [
                "public/css/te-kete-professional.css",
                "public/resource-hub.html",
                "public/index.html"
            ]
            
            for file_path in critical_files:
                result = subprocess.run(
                    ["git", "add", file_path],
                    cwd=self.base_dir,
                    capture_output=True,
                    text=True
                )
                # Don't fail if file doesn't exist, just continue
            
            return True
        except Exception as e:
            print(f"Error staging changes: {e}")
            return False
    
    def create_commit(self):
        """Create commit with proper message"""
        try:
            # Get count of integrated content
            handouts_count = len(list((self.base_dir / "public/dist-handouts").glob("*.html")))
            lessons_count = len(list((self.base_dir / "public/dist-lessons").glob("*.html")))
            
            commit_message = f"""Integrate treasure trove of teaching content

- Integrated {handouts_count} handouts from dist directory
- Integrated {lessons_count} lessons from dist directory
- Added resource-grid and resource-item CSS classes
- Fixed CSS paths in integrated content
- Updated resource hub with new content links

This represents a major expansion of educational content available on Te Kete Ako.
All content now uses te-kete-professional.css and proper navigation.

Deployment timestamp: {datetime.now().isoformat()}"""
            
            result = subprocess.run(
                ["git", "commit", "-m", commit_message],
                cwd=self.base_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print(f"Failed to create commit: {result.stderr}")
                return False
            
            return True
        except Exception as e:
            print(f"Error creating commit: {e}")
            return False
    
    def push_to_remote(self):
        """Push changes to remote repository"""
        try:
            result = subprocess.run(
                ["git", "push", "origin", "main"],
                cwd=self.base_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print(f"Failed to push to remote: {result.stderr}")
                return False
            
            return True
        except Exception as e:
            print(f"Error pushing to remote: {e}")
            return False
    
    def update_deployment_log(self):
        """Update the deployment log"""
        try:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "status": "success",
                "changes": {
                    "handouts_integrated": len(list((self.base_dir / "public/dist-handouts").glob("*.html"))),
                    "lessons_integrated": len(list((self.base_dir / "public/dist-lessons").glob("*.html")))
                }
            }
            
            self.deployment_log.append(log_entry)
            
            # Save deployment log
            log_file = self.base_dir / "deployment-log.json"
            with open(log_file, 'w') as f:
                json.dump(self.deployment_log, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error updating deployment log: {e}")
            return False
    
    def quick_deploy(self):
        """Quick deployment without full validation"""
        print("⚡ Running quick deployment...")
        return self.run_deployment_pipeline(skip_validation=True)
    
    def check_status(self):
        """Check current deployment status"""
        try:
            # Get git status
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.base_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print("Failed to get git status")
                return
            
            lines = result.stdout.strip().split('\n')
            modified_files = [line for line in lines if line.startswith(' M')]
            untracked_files = [line for line in lines if line.startswith('??')]
            
            print(f"📋 Current Status:")
            print(f"  Modified files: {len(modified_files)}")
            print(f"  Untracked files: {len(untracked_files)}")
            
            # Check integrated content
            handouts_count = len(list((self.base_dir / "public/dist-handouts").glob("*.html")))
            lessons_count = len(list((self.base_dir / "public/dist-lessons").glob("*.html")))
            
            print(f"\n📚 Integrated Content:")
            print(f"  Handouts: {handouts_count}")
            print(f"  Lessons: {lessons_count}")
            
            # Check last deployment
            log_file = self.base_dir / "deployment-log.json"
            if log_file.exists():
                with open(log_file, 'r') as f:
                    log = json.load(f)
                
                if log:
                    last_deployment = log[-1]
                    print(f"\n🚀 Last Deployment:")
                    print(f"  Timestamp: {last_deployment.get('timestamp', 'Unknown')}")
                    print(f"  Status: {last_deployment.get('status', 'Unknown')}")
            
        except Exception as e:
            print(f"Error checking status: {e}")

if __name__ == "__main__":
    import sys
    
    pipeline = DeploymentPipeline()
    
    if len(sys.argv) < 2:
        print("Usage: python deployment-pipeline.py <command>")
        print("Commands:")
        print("  deploy - Run full deployment pipeline")
        print("  quick - Quick deployment without validation")
        print("  status - Check current status")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "deploy":
        success = pipeline.run_deployment_pipeline()
        sys.exit(0 if success else 1)
    elif command == "quick":
        success = pipeline.quick_deploy()
        sys.exit(0 if success else 1)
    elif command == "status":
        pipeline.check_status()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
