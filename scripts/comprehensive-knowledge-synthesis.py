#!/usr/bin/env python3
"""
COMPREHENSIVE KNOWLEDGE SYNTHESIS SYSTEM
=========================================

This script synthesizes ALL essential knowledge from 468 archived MD files
into a streamlined, accessible system through GraphRAG and MCP.

CRITICAL: Preserves ALL important context while creating clean access.
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
import hashlib

class KnowledgeSynthesis:
    def __init__(self):
        self.project_root = Path("/Users/admin/Documents/te-kete-ako-clean")
        self.archive_dirs = [
            "docs/archive/2025-10-16-2158",
            "docs/archive/EMERGENCY-2025-10-16-2212", 
            "docs/archive/synthesis-20251016-2228",
            "docs/archive/synthesis-oct16-evening"
        ]
        self.synthesis_output = self.project_root / "MASTER_KNOWLEDGE_BASE.json"
        self.graphrag_entries = []
        
    def discover_archived_docs(self):
        """Find all archived MD files"""
        archived_files = []
        for archive_dir in self.archive_dirs:
            archive_path = self.project_root / archive_dir
            if archive_path.exists():
                for md_file in archive_path.rglob("*.md"):
                    archived_files.append(md_file)
        return archived_files
    
    def extract_essential_content(self, file_path):
        """Extract essential content from MD file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract key information
            title = self.extract_title(content)
            key_points = self.extract_key_points(content)
            technical_details = self.extract_technical_details(content)
            status_info = self.extract_status_info(content)
            
            return {
                "file_path": str(file_path),
                "title": title,
                "key_points": key_points,
                "technical_details": technical_details,
                "status_info": status_info,
                "content_hash": hashlib.md5(content.encode()).hexdigest()[:8],
                "word_count": len(content.split()),
                "extracted_at": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
    
    def extract_title(self, content):
        """Extract title from content"""
        lines = content.split('\n')
        for line in lines[:10]:  # Check first 10 lines
            if line.startswith('# '):
                return line[2:].strip()
            if line.startswith('## '):
                return line[3:].strip()
        return "Untitled Document"
    
    def extract_key_points(self, content):
        """Extract key points and important information"""
        key_points = []
        
        # Look for bullet points
        bullet_pattern = r'^[\s]*[-*+]\s+(.+)$'
        for line in content.split('\n'):
            match = re.match(bullet_pattern, line)
            if match:
                key_points.append(match.group(1).strip())
        
        # Look for numbered lists
        numbered_pattern = r'^[\s]*\d+\.\s+(.+)$'
        for line in content.split('\n'):
            match = re.match(numbered_pattern, line)
            if match:
                key_points.append(match.group(1).strip())
        
        # Look for status indicators
        status_pattern = r'(✅|❌|⚠️|🟢|🔴|🟡|🏆|🌟|📊|🎯)'
        for line in content.split('\n'):
            if re.search(status_pattern, line):
                key_points.append(line.strip())
        
        return key_points[:20]  # Limit to 20 key points
    
    def extract_technical_details(self, content):
        """Extract technical details and code snippets"""
        technical = {
            "code_blocks": [],
            "file_paths": [],
            "commands": [],
            "urls": []
        }
        
        # Extract code blocks
        code_pattern = r'```(\w+)?\n(.*?)\n```'
        for match in re.finditer(code_pattern, content, re.DOTALL):
            language = match.group(1) or "text"
            code = match.group(2).strip()
            if len(code) > 10:  # Only significant code blocks
                technical["code_blocks"].append({
                    "language": language,
                    "code": code[:500]  # Limit size
                })
        
        # Extract file paths
        path_pattern = r'`([^`]+\.(?:html|css|js|py|md|json|sql))`'
        for match in re.finditer(path_pattern, content):
            technical["file_paths"].append(match.group(1))
        
        # Extract commands
        command_pattern = r'`([^`]*(?:python|npm|git|cd|ls|cat|grep|find)[^`]*)`'
        for match in re.finditer(command_pattern, content):
            technical["commands"].append(match.group(1))
        
        # Extract URLs
        url_pattern = r'https?://[^\s\)]+'
        for match in re.finditer(url_pattern, content):
            technical["urls"].append(match.group(0))
        
        return technical
    
    def extract_status_info(self, content):
        """Extract status and progress information"""
        status = {
            "completion_indicators": [],
            "priorities": [],
            "deadlines": [],
            "metrics": []
        }
        
        # Look for completion indicators
        completion_pattern = r'(COMPLETE|DONE|FINISHED|SUCCESS|✅)'
        for line in content.split('\n'):
            if re.search(completion_pattern, line, re.IGNORECASE):
                status["completion_indicators"].append(line.strip())
        
        # Look for priorities
        priority_pattern = r'(URGENT|HIGH|MEDIUM|LOW|PRIORITY|🔴|🟡|🟢)'
        for line in content.split('\n'):
            if re.search(priority_pattern, line, re.IGNORECASE):
                status["priorities"].append(line.strip())
        
        # Look for deadlines
        deadline_pattern = r'(deadline|due|by|until|before).*?(\d{1,2}:\d{2}|\d{4}-\d{2}-\d{2}|tomorrow|today)'
        for line in content.split('\n'):
            if re.search(deadline_pattern, line, re.IGNORECASE):
                status["deadlines"].append(line.strip())
        
        # Look for metrics
        metric_pattern = r'(\d+(?:\.\d+)?%|\d+/\d+|\d+\s*(?:files|pages|lines|tasks))'
        for line in content.split('\n'):
            if re.search(metric_pattern, line):
                status["metrics"].append(line.strip())
        
        return status
    
    def categorize_knowledge(self, extracted_data):
        """Categorize knowledge by type and importance"""
        categories = {
            "coordination": [],
            "technical": [],
            "progress": [],
            "plans": [],
            "status": [],
            "other": []
        }
        
        for data in extracted_data:
            if not data:
                continue
                
            title_lower = data["title"].lower()
            content_indicators = " ".join(data["key_points"]).lower()
            
            # Categorize based on content
            if any(word in title_lower for word in ["coordination", "agent", "team", "collaboration"]):
                categories["coordination"].append(data)
            elif any(word in title_lower for word in ["css", "html", "js", "python", "script", "code", "technical"]):
                categories["technical"].append(data)
            elif any(word in title_lower for word in ["progress", "complete", "done", "status", "report"]):
                categories["progress"].append(data)
            elif any(word in title_lower for word in ["plan", "strategy", "roadmap", "next"]):
                categories["plans"].append(data)
            elif any(word in title_lower for word in ["status", "urgent", "emergency", "stop"]):
                categories["status"].append(data)
            else:
                categories["other"].append(data)
        
        return categories
    
    def create_master_knowledge_base(self, categories):
        """Create master knowledge base"""
        master_kb = {
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "total_documents": sum(len(cat) for cat in categories.values()),
                "categories": {k: len(v) for k, v in categories.items()},
                "synthesis_version": "1.0"
            },
            "knowledge_categories": categories,
            "quick_access": {
                "urgent_items": [],
                "technical_references": [],
                "coordination_protocols": [],
                "progress_tracking": []
            }
        }
        
        # Extract quick access items
        for category, items in categories.items():
            for item in items:
                if any(word in item["title"].lower() for word in ["urgent", "emergency", "critical"]):
                    master_kb["quick_access"]["urgent_items"].append({
                        "title": item["title"],
                        "key_points": item["key_points"][:3],
                        "file_path": item["file_path"]
                    })
                elif category == "technical":
                    master_kb["quick_access"]["technical_references"].append({
                        "title": item["title"],
                        "technical_details": item["technical_details"],
                        "file_path": item["file_path"]
                    })
                elif category == "coordination":
                    master_kb["quick_access"]["coordination_protocols"].append({
                        "title": item["title"],
                        "key_points": item["key_points"][:5],
                        "file_path": item["file_path"]
                    })
                elif category == "progress":
                    master_kb["quick_access"]["progress_tracking"].append({
                        "title": item["title"],
                        "status_info": item["status_info"],
                        "file_path": item["file_path"]
                    })
        
        return master_kb
    
    def prepare_graphrag_entries(self, master_kb):
        """Prepare entries for GraphRAG"""
        entries = []
        
        for category, items in master_kb["knowledge_categories"].items():
            for item in items:
                entry = {
                    "title": item["title"],
                    "content": f"Category: {category}\n\nKey Points:\n" + "\n".join(f"- {point}" for point in item["key_points"][:10]),
                    "metadata": {
                        "category": category,
                        "file_path": item["file_path"],
                        "word_count": item["word_count"],
                        "extracted_at": item["extracted_at"]
                    },
                    "type": "documentation"
                }
                entries.append(entry)
        
        return entries
    
    def run_synthesis(self):
        """Run the complete knowledge synthesis"""
        print("🧠 COMPREHENSIVE KNOWLEDGE SYNTHESIS")
        print("=" * 50)
        
        # Step 1: Discover archived docs
        print("📁 Discovering archived documents...")
        archived_files = self.discover_archived_docs()
        print(f"Found {len(archived_files)} archived MD files")
        
        # Step 2: Extract essential content
        print("🔍 Extracting essential content...")
        extracted_data = []
        for i, file_path in enumerate(archived_files):
            if i % 50 == 0:
                print(f"Processed {i}/{len(archived_files)} files...")
            data = self.extract_essential_content(file_path)
            if data:
                extracted_data.append(data)
        
        print(f"Successfully extracted {len(extracted_data)} documents")
        
        # Step 3: Categorize knowledge
        print("📊 Categorizing knowledge...")
        categories = self.categorize_knowledge(extracted_data)
        
        for category, items in categories.items():
            print(f"  {category}: {len(items)} documents")
        
        # Step 4: Create master knowledge base
        print("📚 Creating master knowledge base...")
        master_kb = self.create_master_knowledge_base(categories)
        
        # Step 5: Save master knowledge base
        with open(self.synthesis_output, 'w', encoding='utf-8') as f:
            json.dump(master_kb, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Master knowledge base saved to: {self.synthesis_output}")
        
        # Step 6: Prepare GraphRAG entries
        print("🔄 Preparing GraphRAG entries...")
        graphrag_entries = self.prepare_graphrag_entries(master_kb)
        
        # Save GraphRAG entries
        graphrag_file = self.project_root / "GRAPH_RAG_ENTRIES.json"
        with open(graphrag_file, 'w', encoding='utf-8') as f:
            json.dump(graphrag_entries, f, indent=2, ensure_ascii=False)
        
        print(f"✅ GraphRAG entries saved to: {graphrag_file}")
        
        # Summary
        print("\n🎯 SYNTHESIS COMPLETE!")
        print(f"📊 Total documents processed: {len(extracted_data)}")
        print(f"📚 Master knowledge base: {self.synthesis_output}")
        print(f"🔄 GraphRAG entries: {len(graphrag_entries)}")
        print(f"📁 Archive locations: {len(self.archive_dirs)} directories")
        
        return master_kb, graphrag_entries

if __name__ == "__main__":
    synthesizer = KnowledgeSynthesis()
    master_kb, graphrag_entries = synthesizer.run_synthesis()
