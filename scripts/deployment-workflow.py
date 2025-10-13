#!/usr/bin/env python3
"""
Deployment Workflow for Te Kete Ako
Integrates validation, testing, and deployment
"""

import os
import sys
import subprocess
import json
from datetime import datetime

class DeploymentWorkflow:
    def __init__(self):
        self.workflow_results = {
            "timestamp": datetime.now().isoformat(),
            "validation_results": {},
            "testing_results": {},
            "deployment_status": "pending",
            "quality_score": 0
        }
    
    def run_validation_pipeline(self):
        """Run the validation pipeline"""
        print("🔍 Running validation pipeline...")
        
        try:
            result = subprocess.run(
                ["python3", "scripts/validation-deployment-pipeline.py"],
                capture_output=True,
                text=True
            )
            
            self.workflow_results["validation_results"] = {
                "success": result.returncode == 0,
                "output": result.stdout,
                "errors": result.stderr
            }
            
            if result.returncode == 0:
                print("✅ Validation pipeline passed")
                return True
            else:
                print("❌ Validation pipeline failed")
                return False
                
        except Exception as e:
            print(f"❌ Error running validation pipeline: {e}")
            self.workflow_results["validation_results"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def run_quality_checks(self):
        """Run automated quality checks"""
        print("🔍 Running quality checks...")
        
        try:
            result = subprocess.run(
                ["python3", "scripts/automated-quality-validation.py", "validate-plan"],
                capture_output=True,
                text=True
            )
            
            self.workflow_results["testing_results"]["quality"] = {
                "success": result.returncode == 0,
                "output": result.stdout,
                "errors": result.stderr
            }
            
            if result.returncode == 0:
                print("✅ Quality checks passed")
                return True
            else:
                print("❌ Quality checks failed")
                return False
                
        except Exception as e:
            print(f"❌ Error running quality checks: {e}")
            self.workflow_results["testing_results"]["quality"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def check_deployment_readiness(self):
        """Check if deployment is ready"""
        print("🚀 Checking deployment readiness...")
        
        validation_success = self.workflow_results["validation_results"].get("success", False)
        quality_success = self.workflow_results["testing_results"].get("quality", {}).get("success", False)
        
        # Calculate quality score
        score = 0
        if validation_success:
            score += 50
        if quality_success:
            score += 50
        
        self.workflow_results["quality_score"] = score
        
        # Determine deployment readiness
        ready = validation_success and quality_success
        self.workflow_results["deployment_status"] = "ready" if ready else "not_ready"
        
        if ready:
            print("✅ Deployment ready")
            return True
        else:
            print("❌ Deployment not ready")
            return False
    
    def create_deployment_package(self):
        """Create deployment package"""
        print("📦 Creating deployment package...")
        
        try:
            # Run build command
            result = subprocess.run(
                ["npm", "run", "build"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("✅ Build successful")
                return True
            else:
                print("❌ Build failed")
                print(result.stderr)
                return False
                
        except Exception as e:
            print(f"❌ Error creating deployment package: {e}")
            return False
    
    def deploy_to_staging(self):
        """Deploy to staging environment"""
        print("🌐 Deploying to staging...")
        
        try:
            # This would integrate with Netlify CLI or similar
            result = subprocess.run(
                ["netlify", "deploy", "--dir=dist", "--message=Automated deployment from workflow"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("✅ Staging deployment successful")
                return True
            else:
                print("❌ Staging deployment failed")
                print(result.stderr)
                return False
                
        except Exception as e:
            print(f"❌ Error deploying to staging: {e}")
            return False
    
    def run_workflow(self, deploy=False):
        """Run the complete deployment workflow"""
        print("🔄 Starting Deployment Workflow...")
        print("=" * 50)
        
        # Step 1: Run validation pipeline
        validation_success = self.run_validation_pipeline()
        if not validation_success:
            print("\n❌ Workflow stopped: Validation failed")
            return False
        
        # Step 2: Run quality checks
        quality_success = self.run_quality_checks()
        if not quality_success:
            print("\n❌ Workflow stopped: Quality checks failed")
            return False
        
        # Step 3: Check deployment readiness
        ready = self.check_deployment_readiness()
        if not ready:
            print("\n❌ Workflow stopped: Not ready for deployment")
            return False
        
        # Step 4: Create deployment package
        package_success = self.create_deployment_package()
        if not package_success:
            print("\n❌ Workflow stopped: Build failed")
            return False
        
        # Step 5: Deploy (if requested)
        if deploy:
            deploy_success = self.deploy_to_staging()
            if not deploy_success:
                print("\n❌ Workflow stopped: Deployment failed")
                return False
        
        # Save workflow results
        with open('deployment-workflow-results.json', 'w') as f:
            json.dump(self.workflow_results, f, indent=2)
        
        # Print summary
        print("\n" + "=" * 50)
        print("📊 WORKFLOW SUMMARY")
        print("=" * 50)
        print(f"Validation: {'✅ Passed' if validation_success else '❌ Failed'}")
        print(f"Quality Checks: {'✅ Passed' if quality_success else '❌ Failed'}")
        print(f"Quality Score: {self.workflow_results['quality_score']}/100")
        print(f"Deployment Status: {self.workflow_results['deployment_status']}")
        if deploy:
            print("Deployment: ✅ Completed")
        else:
            print("Deployment: ⏭️ Skipped (use --deploy to deploy)")
        
        return True
    
    def print_summary(self):
        """Print workflow summary"""
        print("\n📊 Deployment Workflow Summary:")
        print(f"Validation: {'✅ Passed' if self.workflow_results['validation_results'].get('success') else '❌ Failed'}")
        print(f"Quality Score: {self.workflow_results['quality_score']}/100")
        print(f"Status: {self.workflow_results['deployment_status']}")

if __name__ == "__main__":
    workflow = DeploymentWorkflow()
    
    deploy = "--deploy" in sys.argv
    success = workflow.run_workflow(deploy=deploy)
    
    if not success:
        sys.exit(1)
