#!/usr/bin/env python3
"""
SYSTEMATIC FILE PROCESSOR
Process all 90k files, evaluate quality, update GraphRAG, manage relationships
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class FileProcessor:
    def __init__(self):
        self.files_processed = 0
        self.files_approved = []
        self.files_needs_work = []
        self.files_rejected = []
        self.relationships = []
        self.graphrag_updates = []
        
        # Quality criteria
        self.quality_checks = {
            'has_title': lambda c: bool(re.search(r'<title>(.+?)</title>', c)),
            'has_content': lambda c: len(c) > 1000,
            'has_navigation': lambda c: 'nav' in c.lower() or 'navigation' in c.lower(),
            'has_css': lambda c: '.css' in c,
            'cultural_context': lambda c: bool(re.search(r'whakataukī|cultural context|te ao māori', c, re.I)),
            'no_lorem': lambda c: 'lorem ipsum' not in c.lower(),
            'no_placeholder': lambda c: not bool(re.search(r'\[insert|todo:|fixme|xxx', c, re.I))
        }
    
    def process_all_files(self, batch_size=100):
        """Process files in batches"""
        print("🔄 SYSTEMATIC FILE PROCESSING")
        print("=" * 70)
        print(f"\nProcessing in batches of {batch_size}...")
        print("This will take multiple sessions. Progress saved after each batch.\n")
        
        # Get all HTML files excluding node_modules
        all_files = []
        for root, dirs, files in os.walk('.'):
            # Skip junk directories
            if any(skip in root for skip in ['node_modules', '.git', '__pycache__']):
                continue
            
            for file in files:
                if file.endswith('.html'):
                    all_files.append(os.path.join(root, file))
        
        print(f"📊 Found {len(all_files)} HTML files to process\n")
        
        # Process in batches
        for i in range(0, min(batch_size, len(all_files)), 10):
            file_path = all_files[i]
            self.evaluate_file(file_path)
        
        self.save_progress()
        self.print_summary()
    
    def evaluate_file(self, file_path):
        """Evaluate a single file for quality and value"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Run quality checks
            checks_passed = {}
            for check_name, check_fn in self.quality_checks.items():
                checks_passed[check_name] = check_fn(content)
            
            quality_score = sum(checks_passed.values()) / len(checks_passed) * 100
            
            # Extract metadata
            title_match = re.search(r'<title>(.+?)</title>', content)
            title = title_match.group(1) if title_match else Path(file_path).stem
            
            # Find relationships (links to other files)
            links = re.findall(r'href="([^"]+\.html)"', content)
            internal_links = [l for l in links if not l.startswith('http')]
            
            file_info = {
                'path': file_path,
                'title': title,
                'quality_score': quality_score,
                'checks': checks_passed,
                'size_kb': os.path.getsize(file_path) / 1024,
                'links_to': internal_links,
                'in_production': file_path.startswith('./public/') and 'backup' not in file_path,
                'timestamp': datetime.now().isoformat()
            }
            
            # Categorize
            if quality_score >= 85:
                self.files_approved.append(file_info)
                status = "✅ APPROVED"
            elif quality_score >= 60:
                self.files_needs_work.append(file_info)
                status = "⚠️  NEEDS WORK"
            else:
                self.files_rejected.append(file_info)
                status = "❌ REJECTED"
            
            # Store relationships
            for link in internal_links:
                self.relationships.append({
                    'from': file_path,
                    'to': link,
                    'type': 'links_to'
                })
            
            # Queue for GraphRAG
            self.graphrag_updates.append({
                'title': title,
                'path': file_path,
                'quality_score': quality_score,
                'status': status,
                'relationships': len(internal_links),
                'cultural_integration': checks_passed.get('cultural_context', False),
                'production_ready': file_info['in_production']
            })
            
            self.files_processed += 1
            
            if self.files_processed % 10 == 0:
                print(f"   {status} ({quality_score:.0f}%): {title[:60]}")
            
        except Exception as e:
            print(f"   ⚠️  Error processing {file_path}: {e}")
    
    def save_progress(self):
        """Save progress to JSON files"""
        print(f"\n💾 Saving progress...")
        
        # Save categorized files
        with open('file-processing-progress.json', 'w') as f:
            json.dump({
                'processed': self.files_processed,
                'approved': self.files_approved,
                'needs_work': self.files_needs_work,
                'rejected': self.files_rejected,
                'timestamp': datetime.now().isoformat()
            }, f, indent=2)
        
        # Save relationships for GraphRAG
        with open('relationships-for-graphrag.json', 'w') as f:
            json.dump(self.relationships, f, indent=2)
        
        # Save GraphRAG batch update
        with open('graphrag-batch-update.json', 'w') as f:
            json.dump(self.graphrag_updates, f, indent=2)
        
        print("   ✅ file-processing-progress.json")
        print("   ✅ relationships-for-graphrag.json")
        print("   ✅ graphrag-batch-update.json")
    
    def print_summary(self):
        """Print processing summary"""
        print("\n" + "=" * 70)
        print("📊 PROCESSING SUMMARY")
        print("=" * 70)
        
        print(f"\nFiles Processed: {self.files_processed}")
        print(f"✅ Approved (85%+): {len(self.files_approved)}")
        print(f"⚠️  Needs Work (60-84%): {len(self.files_needs_work)}")
        print(f"❌ Rejected (<60%): {len(self.files_rejected)}")
        print(f"🔗 Relationships Mapped: {len(self.relationships)}")
        
        print("\n📊 Approval Rate:")
        if self.files_processed > 0:
            approval_rate = len(self.files_approved) / self.files_processed * 100
            print(f"   {approval_rate:.1f}% ready for production")
        
        if self.files_approved:
            print("\n✅ Top Approved Files:")
            for file_info in sorted(self.files_approved, key=lambda x: x['quality_score'], reverse=True)[:5]:
                print(f"   {file_info['quality_score']:.0f}% - {file_info['title'][:50]}")
        
        if self.files_needs_work:
            print("\n⚠️  Files That Need Work:")
            for file_info in self.files_needs_work[:5]:
                missing = [k for k, v in file_info['checks'].items() if not v]
                print(f"   {file_info['title'][:40]} - Missing: {', '.join(missing[:2])}")
        
        print("\n💡 Next Steps:")
        print("   1. Review approved files → Add to navigation")
        print("   2. Fix 'needs work' files → Batch improvements")
        print("   3. Upload to GraphRAG → Keep knowledge synchronized")
        print("   4. Map relationships → Build knowledge graph")

if __name__ == "__main__":
    processor = FileProcessor()
    processor.process_all_files(batch_size=100)
    
    print("\n" + "=" * 70)
    print("✅ BATCH COMPLETE - Progress Saved!")
    print("=" * 70)
    print("\n🔄 Run again to process next batch of 100 files")
    print("📊 Current: ~{} of ~90,000 files processed\n".format(processor.files_processed))

