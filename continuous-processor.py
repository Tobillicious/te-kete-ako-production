#!/usr/bin/env python3
"""
CONTINUOUS FILE PROCESSOR - Process ALL 8,253 files
Runs in batches, saves progress, updates GraphRAG
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

BATCH_SIZE = 500  # Process 500 files per batch
PROGRESS_FILE = 'processing-progress.json'

class ContinuousProcessor:
    def __init__(self):
        self.load_progress()
        
    def load_progress(self):
        """Load previous progress if exists"""
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, 'r') as f:
                data = json.load(f)
                self.processed_files = set(data.get('processed_files', []))
                self.approved = data.get('approved', [])
                self.needs_work = data.get('needs_work', [])
                self.rejected = data.get('rejected', [])
                self.relationships = data.get('relationships', [])
                print(f"📂 Loaded progress: {len(self.processed_files)} files already processed")
        else:
            self.processed_files = set()
            self.approved = []
            self.needs_work = []
            self.rejected = []
            self.relationships = []
            print("📂 Starting fresh - no previous progress found")
    
    def get_all_html_files(self):
        """Get all HTML files, excluding node_modules"""
        files = []
        for root, dirs, filenames in os.walk('.'):
            # Skip junk
            if any(skip in root for skip in ['node_modules', '.git', '__pycache__', 'dist']):
                continue
            
            for filename in filenames:
                if filename.endswith('.html'):
                    filepath = os.path.join(root, filename)
                    files.append(filepath)
        
        return files
    
    def evaluate_file(self, filepath):
        """Quick quality evaluation"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Quality checks
            score = 0
            checks = {}
            
            # Has title?
            if re.search(r'<title>(.+?)</title>', content):
                score += 15
                checks['title'] = True
            
            # Has content (>1KB)?
            if len(content) > 1000:
                score += 15
                checks['content'] = True
            
            # Has CSS?
            if '.css' in content:
                score += 15
                checks['css'] = True
            
            # Cultural context?
            if re.search(r'whakataukī|cultural|māori|maori', content, re.I):
                score += 20
                checks['cultural'] = True
            
            # No placeholders?
            if not re.search(r'\[insert|todo:|fixme', content, re.I):
                score += 15
                checks['clean'] = True
            
            # Has navigation?
            if 'nav' in content.lower():
                score += 10
                checks['nav'] = True
            
            # In production already?
            in_production = filepath.startswith('./public/') and 'backup' not in filepath
            if in_production:
                score += 10
                checks['production'] = True
            
            # Extract title
            title_match = re.search(r'<title>(.+?)</title>', content)
            title = title_match.group(1) if title_match else Path(filepath).stem
            
            # Find links
            links = re.findall(r'href="([^"]+\.html)"', content)
            internal_links = [l for l in links if not l.startswith('http')]
            
            # Store relationships
            for link in internal_links:
                self.relationships.append({
                    'from': filepath,
                    'to': link,
                    'type': 'links_to'
                })
            
            file_data = {
                'path': filepath,
                'title': title,
                'score': score,
                'checks': checks,
                'size_kb': round(len(content) / 1024, 2),
                'links': len(internal_links),
                'in_production': in_production
            }
            
            # Categorize
            if score >= 85:
                self.approved.append(file_data)
                return '✅'
            elif score >= 60:
                self.needs_work.append(file_data)
                return '⚠️'
            else:
                self.rejected.append(file_data)
                return '❌'
                
        except Exception as e:
            return '⚠️'
    
    def process_batch(self, batch_num=1):
        """Process one batch of files"""
        all_files = self.get_all_html_files()
        
        # Filter out already processed
        remaining = [f for f in all_files if f not in self.processed_files]
        
        print(f"\n🔄 BATCH {batch_num}")
        print(f"📊 Total files: {len(all_files)}")
        print(f"✅ Already processed: {len(self.processed_files)}")
        print(f"⏳ Remaining: {len(remaining)}")
        print(f"📦 This batch: {min(BATCH_SIZE, len(remaining))}\n")
        
        if not remaining:
            print("🎉 ALL FILES PROCESSED!")
            return False
        
        # Process batch
        batch = remaining[:BATCH_SIZE]
        for i, filepath in enumerate(batch):
            status = self.evaluate_file(filepath)
            self.processed_files.add(filepath)
            
            if (i + 1) % 50 == 0:
                print(f"   ... {i + 1}/{len(batch)} files processed")
        
        self.save_progress()
        return len(remaining) > BATCH_SIZE  # More batches needed?
    
    def save_progress(self):
        """Save all progress"""
        with open(PROGRESS_FILE, 'w') as f:
            json.dump({
                'processed_files': list(self.processed_files),
                'approved': self.approved,
                'needs_work': self.needs_work,
                'rejected': self.rejected,
                'relationships': self.relationships,
                'timestamp': datetime.now().isoformat(),
                'stats': {
                    'total_processed': len(self.processed_files),
                    'approved_count': len(self.approved),
                    'needs_work_count': len(self.needs_work),
                    'rejected_count': len(self.rejected),
                    'relationships_count': len(self.relationships)
                }
            }, f, indent=2)
    
    def print_stats(self):
        """Print current statistics"""
        total = len(self.processed_files)
        if total == 0:
            return
        
        print("\n" + "=" * 70)
        print("📊 CUMULATIVE STATISTICS")
        print("=" * 70)
        
        print(f"\n✅ Approved: {len(self.approved)} ({len(self.approved)/total*100:.1f}%)")
        print(f"⚠️  Needs Work: {len(self.needs_work)} ({len(self.needs_work)/total*100:.1f}%)")
        print(f"❌ Rejected: {len(self.rejected)} ({len(self.rejected)/total*100:.1f}%)")
        print(f"🔗 Relationships: {len(self.relationships)}")
        
        if self.approved:
            print("\n🌟 Top Quality Files:")
            for item in sorted(self.approved, key=lambda x: x['score'], reverse=True)[:10]:
                in_prod = "🌐" if item['in_production'] else "📦"
                print(f"   {in_prod} {item['score']}% - {item['title'][:55]}")
        
        print(f"\n📊 Progress: {total} / ~8,253 files ({total/8253*100:.1f}%)")

if __name__ == "__main__":
    processor = ContinuousProcessor()
    
    batch_num = 1
    more_batches = True
    
    while more_batches and batch_num <= 20:  # Process up to 20 batches per run
        more_batches = processor.process_batch(batch_num)
        batch_num += 1
    
    processor.print_stats()
    
    print("\n" + "=" * 70)
    print("✅ SESSION COMPLETE")
    print("=" * 70)
    print(f"\n📁 Progress saved to: {PROGRESS_FILE}")
    print("🔄 Run again to continue processing remaining files\n")

