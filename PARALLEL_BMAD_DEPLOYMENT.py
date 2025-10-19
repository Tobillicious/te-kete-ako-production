#!/usr/bin/env python3
"""
PARALLEL BMAD DEPLOYMENT SYSTEM
Deploys BMAD across thousands of files using multiprocessing
"""

import os
import re
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Tuple
import time

class ParallelBMADDeployer:
    def __init__(self, public_dir: str, max_workers: int = 20):
        self.public_dir = Path(public_dir)
        self.max_workers = max_workers
        self.results = {
            'cleaned': [],
            'already_clean': [],
            'errors': [],
            'content_audit': []
        }
        
    def find_all_html_files(self) -> List[Path]:
        """Find all HTML files in public directory"""
        return list(self.public_dir.rglob('*.html'))
    
    def audit_content_type(self, content: str, filepath: Path) -> Dict:
        """Audit content type and quality"""
        audit = {
            'file': str(filepath.relative_to(self.public_dir)),
            'type': 'unknown',
            'has_placeholder': False,
            'needs_depth': False,
            'quality_indicators': []
        }
        
        # Detect content type
        if 'lesson-plan' in content.lower() or '<h1>Lesson' in content or 'class="lesson' in content:
            audit['type'] = 'lesson'
        elif 'handout' in content.lower() or 'worksheet' in content.lower():
            audit['type'] = 'handout'
        elif 'unit-overview' in content.lower() or 'unit plan' in content.lower():
            audit['type'] = 'unit'
        elif 'assessment' in content.lower() or 'rubric' in content.lower():
            audit['type'] = 'assessment'
        elif 'index' in filepath.name.lower():
            audit['type'] = 'index'
        
        # Check for placeholders
        placeholder_patterns = [
            r'Lorem ipsum',
            r'Placeholder',
            r'TODO:',
            r'COMING SOON',
            r'\[Add content here\]',
            r'\[INSERT.*?\]',
            r'XXX',
            r'TBD'
        ]
        for pattern in placeholder_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                audit['has_placeholder'] = True
                break
        
        # Check if content needs depth
        if len(content) < 5000:  # Less than 5KB might be too shallow
            audit['needs_depth'] = True
        
        # Quality indicators
        if 'te-kete-ultimate-beauty-system.css' in content:
            audit['quality_indicators'].append('BMAD_CSS')
        if 'framer-cultural-gestures-ultimate.js' in content:
            audit['quality_indicators'].append('FRAMER_MOTION')
        if 'tailwind.config.ultimate.js' in content:
            audit['quality_indicators'].append('TAILWIND')
        if 'whakapapa' in content.lower() or 'kaitiakitanga' in content.lower():
            audit['quality_indicators'].append('CULTURAL_CONTENT')
        
        return audit
    
    def clean_css_conflicts(self, content: str) -> Tuple[str, bool]:
        """Remove conflicting CSS, return (cleaned_content, was_modified)"""
        original = content
        
        # Remove all variations of te-kete-professional.css
        patterns_to_remove = [
            r'<link[^>]*href=["\']?/css/te-kete-professional\.css["\']?[^>]*>',
            r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']?/css/te-kete-professional\.css["\']?[^>]*>',
        ]
        
        for pattern in patterns_to_remove:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # Clean up extra whitespace
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        return content, content != original
    
    def process_single_file(self, filepath: Path) -> Dict:
        """Process a single HTML file"""
        result = {
            'file': str(filepath.relative_to(self.public_dir)),
            'status': 'unknown',
            'audit': None,
            'error': None
        }
        
        try:
            # Read file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Audit content
            audit = self.audit_content_type(content, filepath)
            result['audit'] = audit
            
            # Clean CSS conflicts
            cleaned_content, was_modified = self.clean_css_conflicts(content)
            
            if was_modified:
                # Write back
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                result['status'] = 'cleaned'
            else:
                result['status'] = 'already_clean'
                
        except Exception as e:
            result['status'] = 'error'
            result['error'] = str(e)
        
        return result
    
    def deploy(self):
        """Deploy in parallel across all files"""
        print("🚀 PARALLEL BMAD DEPLOYMENT STARTING...")
        print(f"💪 Using {self.max_workers} parallel workers\n")
        
        # Find all HTML files
        html_files = self.find_all_html_files()
        total_files = len(html_files)
        print(f"📊 Found {total_files} HTML files to process\n")
        
        start_time = time.time()
        
        # Process in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_file = {
                executor.submit(self.process_single_file, filepath): filepath 
                for filepath in html_files
            }
            
            # Process results as they complete
            completed = 0
            for future in as_completed(future_to_file):
                result = future.result()
                completed += 1
                
                # Categorize result
                if result['status'] == 'cleaned':
                    self.results['cleaned'].append(result)
                elif result['status'] == 'already_clean':
                    self.results['already_clean'].append(result)
                elif result['status'] == 'error':
                    self.results['errors'].append(result)
                
                if result['audit']:
                    self.results['content_audit'].append(result['audit'])
                
                # Progress indicator
                if completed % 50 == 0:
                    elapsed = time.time() - start_time
                    rate = completed / elapsed
                    eta = (total_files - completed) / rate if rate > 0 else 0
                    print(f"⚡ {completed}/{total_files} ({completed*100//total_files}%) | "
                          f"{rate:.1f} files/sec | ETA: {eta:.0f}s")
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
        self.save_reports()
    
    def print_summary(self, elapsed: float):
        """Print deployment summary"""
        print("\n" + "="*70)
        print("🎉 PARALLEL DEPLOYMENT COMPLETE!")
        print("="*70)
        print(f"\n⏱️  Total time: {elapsed:.1f} seconds")
        print(f"⚡ Processing rate: {len(self.results['cleaned'] + self.results['already_clean'])/ elapsed:.1f} files/sec")
        print(f"\n✅ Cleaned: {len(self.results['cleaned'])}")
        print(f"✨ Already clean: {len(self.results['already_clean'])}")
        print(f"❌ Errors: {len(self.results['errors'])}")
        
        # Content audit summary
        audits = self.results['content_audit']
        type_counts = {}
        placeholder_count = 0
        needs_depth_count = 0
        
        for audit in audits:
            type_counts[audit['type']] = type_counts.get(audit['type'], 0) + 1
            if audit['has_placeholder']:
                placeholder_count += 1
            if audit['needs_depth']:
                needs_depth_count += 1
        
        print(f"\n📊 CONTENT AUDIT:")
        print(f"   Content types detected:")
        for ctype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
            print(f"      {ctype}: {count}")
        print(f"   🚨 Has placeholders: {placeholder_count}")
        print(f"   📝 Needs depth: {needs_depth_count}")
        
        if self.results['errors']:
            print(f"\n❌ ERRORS ({len(self.results['errors'])}):")
            for err in self.results['errors'][:10]:  # Show first 10
                print(f"   {err['file']}: {err['error']}")
    
    def save_reports(self):
        """Save detailed reports to JSON"""
        reports_dir = self.public_dir.parent / 'deployment_reports'
        reports_dir.mkdir(exist_ok=True)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        # Save full results
        with open(reports_dir / f'deployment_{timestamp}.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        # Save content audit for GraphRAG indexing
        with open(reports_dir / f'content_audit_{timestamp}.json', 'w') as f:
            json.dump(self.results['content_audit'], f, indent=2)
        
        print(f"\n💾 Reports saved to: {reports_dir}")


if __name__ == '__main__':
    deployer = ParallelBMADDeployer(
        public_dir='/Users/admin/Documents/te-kete-ako-clean/public',
        max_workers=20  # 20 parallel workers
    )
    deployer.deploy()

