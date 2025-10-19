#!/usr/bin/env python3
"""
🚀 RESOURCE DEPLOYMENT ENGINE
Systematic deployment of 17,457 GraphRAG resources to website

GAP BRIDGING STRATEGY:
- GraphRAG shows 17,457 resources exist with metadata
- Website currently has ~1,934 deployed
- Need to deploy 15,523 additional resources systematically
- Use GraphRAG priorities and quality scores for deployment order
"""

import os
import shutil
import json
from pathlib import Path
from bs4 import BeautifulSoup

class ResourceDeploymentEngine:
    def __init__(self):
        self.public_dir = Path('public')
        self.backup_dir = Path('backup_before_css_migration')
        self.dist_dir = Path('dist')
        self.archive_dir = Path('archive')

        # GraphRAG deployment priorities
        self.deployment_priority = {
            'Platform Infrastructure': 1,  # Technical backbone first
            'Digital Technologies': 2,    # Y8 model exists
            'Cross-Curricular': 3,        # Strong foundation
            'Mathematics': 4,             # Excellent quality
            'Science': 5,                 # Y9 Ecology model
            'English': 6,                 # Pūrākau framework
            'Te Ao Māori': 7,             # Maintain excellence
            'Social Studies': 8,          # Cultural boost
            'Health & PE': 9,             # Te Whare Tapa Whā
            'Arts': 10,                   # Toi Māori framework
            'Languages': 11               # Bilingual approaches
        }

    def get_deployment_candidates(self, limit=100):
        """Get next batch of resources ready for deployment"""
        candidates = []

        # Check backup_before_css_migration first (largest repository)
        for html_file in self.backup_dir.rglob('*.html'):
            if html_file.stat().st_size > 1000:  # Skip tiny files
                target_path = self.public_dir / html_file.relative_to(self.backup_dir)

                # Skip component files that aren't standalone pages
                if self._is_component_file(html_file):
                    continue

                # Skip if already deployed
                if not target_path.exists():
                    priority = self._calculate_priority(html_file)

                    # Include more content types by lowering priority threshold
                    if priority <= 50:  # Include all content types
                        candidates.append({
                            'source_path': html_file,
                            'target_path': target_path,
                            'priority': priority,
                            'size': html_file.stat().st_size
                        })

        # Sort by priority and size (quality indicator)
        candidates.sort(key=lambda x: (x['priority'], -x['size']))

        return candidates[:limit]

    def _is_component_file(self, file_path):
        """Check if file is a component rather than standalone page"""
        path_str = str(file_path).lower()

        # Navigation components
        if 'navigation' in path_str and ('header' in path_str or 'component' in path_str):
            return True

        # Footer components
        if 'footer' in path_str and ('component' in path_str or 'footer' in path_str):
            return True

        # Mobile navigation
        if 'mobile' in path_str and 'nav' in path_str:
            return True

        # FAB components
        if 'fab' in path_str or 'floating' in path_str:
            return True

        # Other known components
        component_indicators = ['badge', 'tour', 'modal', 'tooltip', 'dropdown']
        if any(indicator in path_str for indicator in component_indicators):
            return True

        return False

    def _calculate_priority(self, file_path):
        """Calculate deployment priority based on file location and content"""
        path_str = str(file_path)

        # Platform infrastructure gets highest priority
        if any(keyword in path_str.lower() for keyword in ['admin', 'system', 'api', 'auth']):
            return 1

        # Digital technologies (Y8 model exists)
        if 'digital' in path_str.lower() or 'tech' in path_str.lower():
            return 2

        # Subject-based priority
        for subject, priority in self.deployment_priority.items():
            if subject.lower() in path_str.lower():
                return priority

        # Default priority for other content
        return 50

    def deploy_resource(self, candidate):
        """Deploy a single resource with proper styling and navigation"""
        source_path = candidate['source_path']
        target_path = candidate['target_path']

        try:
            # Create target directory if needed
            target_path.parent.mkdir(parents=True, exist_ok=True)

            # Read source content
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Apply transformations
            transformed_content = self._transform_content(content, source_path)

            # Write to public directory
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(transformed_content)

            print(f"✅ Deployed: {source_path} → {target_path}")
            return True

        except Exception as e:
            print(f"❌ Failed to deploy {source_path}: {e}")
            return False

    def _transform_content(self, content, source_path):
        """Apply standard transformations to ensure consistency"""
        soup = BeautifulSoup(content, 'html.parser')

        # Add standard meta tags if missing
        if not soup.find('meta', {'name': 'viewport'}):
            viewport = soup.new_tag('meta')
            viewport['name'] = 'viewport'
            viewport['content'] = 'width=device-width, initial-scale=1.0'
            soup.head.insert(0, viewport)

        # Add cultural context if not present
        if not soup.find('meta', {'name': 'cultural-context'}):
            cultural = soup.new_tag('meta')
            cultural['name'] = 'cultural-context'
            cultural['content'] = 'te-ao-maori-integrated'
            soup.head.insert(0, cultural)

        # Ensure proper DOCTYPE
        if not content.strip().startswith('<!DOCTYPE'):
            content = '<!DOCTYPE html>\n' + content

        return str(soup)

    def deploy_batch(self, batch_size=100):
        """Deploy a batch of resources"""
        candidates = self.get_deployment_candidates(batch_size)
        deployed = 0
        failed = 0

        for candidate in candidates:
            if self.deploy_resource(candidate):
                deployed += 1
            else:
                failed += 1

        return deployed, failed

    def get_deployment_stats(self):
        """Get current deployment statistics"""
        public_files = list(self.public_dir.rglob('*.html'))
        backup_files = list(self.backup_dir.rglob('*.html'))
        dist_files = list(self.dist_dir.rglob('*.html'))
        archive_files = list(self.archive_dir.rglob('*.html'))

        return {
            'public_deployed': len(public_files),
            'backup_available': len(backup_files),
            'dist_available': len(dist_files),
            'archive_available': len(archive_files),
            'total_available': len(backup_files) + len(dist_files) + len(archive_files),
            'deployment_gap': (len(backup_files) + len(dist_files) + len(archive_files)) - len(public_files)
        }

def main():
    """Main deployment execution"""
    engine = ResourceDeploymentEngine()

    print("🚀 TE KETE AKO RESOURCE DEPLOYMENT ENGINE")
    print("=" * 60)

    # Show current stats
    stats = engine.get_deployment_stats()
    print("📊 CURRENT DEPLOYMENT STATUS:")
    print(f"   Public deployed: {stats['public_deployed']:,}")
    print(f"   Backup available: {stats['backup_available']:,}")
    print(f"   Dist available: {stats['dist_available']:,}")
    print(f"   Archive available: {stats['archive_available']:,}")
    print(f"   Total available: {stats['total_available']:,}")
    print(f"   Deployment gap: {stats['deployment_gap']:,}")
    print()

    # Deploy multiple batches for systematic deployment
    print("🔄 DEPLOYING SYSTEMATIC BATCHES...")

    total_deployed = 0
    total_failed = 0

    for batch_num in range(1, 6):  # Deploy 5 batches of 50 each
        print(f"\n🔄 BATCH {batch_num}/5...")
        deployed, failed = engine.deploy_batch(50)
        total_deployed += deployed
        total_failed += failed

        if deployed == 0:
            print("   No more high-priority resources to deploy")
            break

        print(f"   ✅ {deployed} deployed, {failed} failed")

    print(f"\n🎉 SYSTEMATIC DEPLOYMENT COMPLETE!")
    print(f"   Total deployed: {total_deployed}")
    print(f"   Total failed: {total_failed}")
    if total_deployed + total_failed > 0:
        print(f"   Success rate: {total_deployed / (total_deployed + total_failed) * 100:.1f}%")
    else:
        print("   No resources processed in this batch")

    # Show final stats
    final_stats = engine.get_deployment_stats()
    print("\n📊 FINAL DEPLOYMENT STATUS:")
    print(f"   Public deployed: {final_stats['public_deployed']:,}")
    print(f"   Total available: {final_stats['total_available']:,}")
    print(f"   Overall progress: {final_stats['public_deployed'] / final_stats['total_available'] * 100:.1f}%")

if __name__ == "__main__":
    main()
