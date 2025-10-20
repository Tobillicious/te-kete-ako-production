#!/usr/bin/env python3
"""
🔗 PREREQUISITE CHAIN BUILDER
Replicate Y8 Digital Kaitiakitanga model (385 pathways from 18 lessons)

Target: Build complete sequential chains for 5+ units
Impact: 385 pathways per unit × 5 units = 1,925 new pathways!

Usage:
    python3 scripts/prerequisite-chain-builder.py
    python3 scripts/prerequisite-chain-builder.py --unit "Y7 Algebra"
    python3 scripts/prerequisite-chain-builder.py --dry-run
"""

import json
import argparse
from datetime import datetime
from supabase import create_client, Client
from collections import defaultdict

# Supabase configuration
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE7NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

# Gold Standard Model: Y8 Digital Kaitiakitanga
GOLD_STANDARD = {
    'unit_name': 'Y8 Digital Kaitiakitanga',
    'lessons': 18,
    'pathways': 385,
    'confidence': 0.958,
    'cultural_integration': 100,
    'quality': 90.5,
    'progression': [
        'Digital Whenua (Foundation)',
        'Digital Whare (Structure)', 
        'Digital Tinana (Body)',
        'Digital Data (Information)',
        'Digital Tikanga (Protocols)',
        'Digital Rangatiratanga (Leadership)'
    ]
}

# Target units for replication
TARGET_UNITS = {
    'Y7 Algebra': {
        'subject': 'Mathematics',
        'year_level': '7',
        'cultural_framework': 'Toi Māori (Mathematical Arts)',
        'progression': [
            'Basic Patterns',
            'Algebraic Thinking',
            'Geometric Patterns',
            'Statistical Patterns',
            'Applied Mathematics'
        ],
        'lessons_expected': 12
    },
    'Y9 Ecology': {
        'subject': 'Science',
        'year_level': '9',
        'cultural_framework': 'Kaitiakitanga Progression',
        'progression': [
            'Ecosystem Awareness',
            'Environmental Understanding',
            'Conservation Action',
            'Guardianship Practice'
        ],
        'lessons_expected': 8
    },
    'Y10 Physics': {
        'subject': 'Science',
        'year_level': '10',
        'cultural_framework': 'Waka Navigation',
        'progression': [
            'Forces and Motion',
            'Energy and Work',
            'Waves and Sound',
            'Light and Optics'
        ],
        'lessons_expected': 10
    },
    'Ranginui Walker Unit': {
        'subject': 'Social Studies',
        'year_level': '9',
        'cultural_framework': 'Tino Rangatiratanga',
        'progression': [
            'Historical Context',
            'Social Analysis',
            'Cultural Critique',
            'Contemporary Application'
        ],
        'lessons_expected': 6
    }
}

class PrerequisiteChainBuilder:
    """Build complete prerequisite chains following Y8 Digital model"""
    
    def __init__(self, dry_run=False):
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.dry_run = dry_run
        self.chains_built = []
        self.relationships_created = []
        
    def build_all_chains(self):
        """Build prerequisite chains for all target units"""
        print("🔗 PREREQUISITE CHAIN BUILDER")
        print("=" * 70)
        print(f"Gold Standard: {GOLD_STANDARD['unit_name']}")
        print(f"  Lessons: {GOLD_STANDARD['lessons']}")
        print(f"  Pathways: {GOLD_STANDARD['pathways']}")
        print(f"  Confidence: {GOLD_STANDARD['confidence']}")
        print(f"  Cultural: {GOLD_STANDARD['cultural_integration']}%")
        print(f"  Quality: {GOLD_STANDARD['quality']}")
        
        # Step 1: Analyze existing chains
        print(f"\n📊 Step 1: Analyzing existing prerequisite chains...")
        existing_chains = self._analyze_existing_chains()
        
        # Step 2: Build chains for each target unit
        print(f"\n🎯 Step 2: Building chains for target units...")
        for unit_name, unit_config in TARGET_UNITS.items():
            print(f"\n  📌 Building chain: {unit_name}")
            chain = self._build_unit_chain(unit_name, unit_config)
            if chain:
                self.chains_built.append(chain)
        
        # Step 3: Create relationships
        if not self.dry_run and self.relationships_created:
            print(f"\n💾 Step 3: Creating {len(self.relationships_created)} relationships...")
            self._create_relationships()
        
        print(f"\n✅ Chain building complete!")
        print(f"📊 Chains built: {len(self.chains_built)}")
        print(f"📊 Relationships created: {len(self.relationships_created)}")
        
        if self.dry_run:
            print("🔍 DRY RUN - No relationships created")
        else:
            print("✨ Prerequisite chains created in GraphRAG!")
        
        return self.chains_built
    
    def _analyze_existing_chains(self):
        """Analyze existing prerequisite chains"""
        try:
            # Get existing prerequisite relationships
            result = self.supabase.table('graphrag_relationships')\
                .select('source_path, target_path, confidence')\
                .eq('relationship_type', 'prerequisite_for')\
                .execute()
            
            if not result.data:
                print("   No existing prerequisite chains found")
                return {}
            
            # Analyze chain patterns
            chains = defaultdict(list)
            for rel in result.data:
                source = rel['source_path']
                target = rel['target_path']
                confidence = rel.get('confidence', 0.8)
                
                # Group by unit (simplified - in production would be more sophisticated)
                unit_key = self._extract_unit_key(source)
                chains[unit_key].append({
                    'source': source,
                    'target': target,
                    'confidence': confidence
                })
            
            print(f"   Found {len(chains)} existing chain groups")
            for unit, chain_rels in chains.items():
                print(f"     {unit}: {len(chain_rels)} relationships")
            
            return dict(chains)
            
        except Exception as e:
            print(f"   ⚠️  Error analyzing chains: {e}")
            return {}
    
    def _extract_unit_key(self, file_path):
        """Extract unit key from file path"""
        # Simplified extraction - in production would be more sophisticated
        if 'y8-digital' in file_path.lower():
            return 'Y8 Digital'
        elif 'y7' in file_path.lower():
            return 'Y7'
        elif 'y9' in file_path.lower():
            return 'Y9'
        elif 'y10' in file_path.lower():
            return 'Y10'
        else:
            return 'Other'
    
    def _build_unit_chain(self, unit_name, unit_config):
        """Build prerequisite chain for a specific unit"""
        try:
            # Find resources for this unit
            resources = self._find_unit_resources(unit_name, unit_config)
            
            if len(resources) < 3:
                print(f"     ⚠️  Insufficient resources ({len(resources)}) for {unit_name}")
                return None
            
            print(f"     Found {len(resources)} resources")
            
            # Sort resources by progression
            sorted_resources = self._sort_by_progression(resources, unit_config)
            
            # Build sequential chain
            chain_relationships = self._build_sequential_chain(sorted_resources, unit_config)
            
            if chain_relationships:
                chain = {
                    'unit_name': unit_name,
                    'resources_count': len(resources),
                    'relationships_count': len(chain_relationships),
                    'cultural_framework': unit_config['cultural_framework'],
                    'progression': unit_config['progression'],
                    'relationships': chain_relationships
                }
                
                self.relationships_created.extend(chain_relationships)
                print(f"     ✅ Built chain: {len(chain_relationships)} relationships")
                
                return chain
            
        except Exception as e:
            print(f"     ⚠️  Error building chain for {unit_name}: {e}")
            return None
    
    def _find_unit_resources(self, unit_name, unit_config):
        """Find resources for a specific unit"""
        try:
            # Search by subject and year level
            result = self.supabase.table('graphrag_resources')\
                .select('*')\
                .eq('subject', unit_config['subject'])\
                .eq('year_level', unit_config['year_level'])\
                .gte('quality_score', 80)\
                .limit(50)\
                .execute()
            
            if not result.data:
                return []
            
            # Filter by unit name keywords
            unit_keywords = unit_name.lower().split()
            filtered_resources = []
            
            for resource in result.data:
                title = resource.get('title', '').lower()
                content = resource.get('content_preview', '').lower()
                
                # Check if resource matches unit
                if any(keyword in title or keyword in content for keyword in unit_keywords):
                    filtered_resources.append(resource)
            
            return filtered_resources
            
        except Exception as e:
            print(f"     ⚠️  Error finding resources: {e}")
            return []
    
    def _sort_by_progression(self, resources, unit_config):
        """Sort resources by pedagogical progression"""
        progression = unit_config['progression']
        
        # Score each resource based on progression keywords
        scored_resources = []
        for resource in resources:
            score = 0
            title = resource.get('title', '').lower()
            content = resource.get('content_preview', '').lower()
            
            # Check progression keywords
            for i, stage in enumerate(progression):
                stage_keywords = stage.lower().split()
                if any(keyword in title or keyword in content for keyword in stage_keywords):
                    score = i
                    break
            
            # Quality bonus
            quality = resource.get('quality_score', 0)
            score += quality / 1000  # Small quality influence
            
            scored_resources.append((score, resource))
        
        # Sort by score
        scored_resources.sort(key=lambda x: x[0])
        
        return [resource for score, resource in scored_resources]
    
    def _build_sequential_chain(self, sorted_resources, unit_config):
        """Build sequential prerequisite chain"""
        relationships = []
        
        # Create sequential relationships (lesson N → lesson N+1)
        for i in range(len(sorted_resources) - 1):
            source = sorted_resources[i]
            target = sorted_resources[i + 1]
            
            # Calculate confidence based on progression
            confidence = self._calculate_chain_confidence(source, target, i, len(sorted_resources))
            
            relationship = {
                'source_path': source['file_path'],
                'target_path': target['file_path'],
                'relationship_type': 'prerequisite_for',
                'confidence': confidence,
                'reasoning': f"Sequential progression in {unit_config['cultural_framework']} framework (step {i+1}→{i+2})"
            }
            
            relationships.append(relationship)
        
        # Create cross-connections for cultural framework
        cultural_relationships = self._create_cultural_connections(sorted_resources, unit_config)
        relationships.extend(cultural_relationships)
        
        return relationships
    
    def _calculate_chain_confidence(self, source, target, position, total):
        """Calculate confidence for chain relationship"""
        # Base confidence
        confidence = 0.90
        
        # Sequential bonus
        if position < total - 1:
            confidence += 0.05
        
        # Quality bonus
        source_quality = source.get('quality_score', 0)
        target_quality = target.get('quality_score', 0)
        
        if source_quality >= 90 and target_quality >= 90:
            confidence += 0.03
        elif source_quality >= 85 and target_quality >= 85:
            confidence += 0.02
        
        # Cultural bonus
        if source.get('cultural_context') and target.get('cultural_context'):
            confidence += 0.02
        
        return min(confidence, 0.98)
    
    def _create_cultural_connections(self, resources, unit_config):
        """Create cultural framework connections"""
        relationships = []
        cultural_framework = unit_config['cultural_framework']
        
        # Connect resources sharing cultural framework
        for i, source in enumerate(resources):
            if not source.get('cultural_context'):
                continue
            
            for j, target in enumerate(resources[i+1:], i+1):
                if not target.get('cultural_context'):
                    continue
                
                # Create cultural connection
                relationship = {
                    'source_path': source['file_path'],
                    'target_path': target['file_path'],
                    'relationship_type': 'shared_cultural_wisdom',
                    'confidence': 0.92,
                    'reasoning': f"Both resources share {cultural_framework} cultural framework"
                }
                
                relationships.append(relationship)
        
        return relationships
    
    def _create_relationships(self):
        """Create relationships in GraphRAG"""
        for rel in self.relationships_created:
            try:
                self.supabase.table('graphrag_relationships').insert({
                    'source_path': rel['source_path'],
                    'target_path': rel['target_path'],
                    'relationship_type': rel['relationship_type'],
                    'confidence': rel['confidence'],
                    'reasoning': rel['reasoning'],
                    'created_at': datetime.now().isoformat()
                }).execute()
                
            except Exception as e:
                print(f"   ⚠️  Error creating relationship: {e}")
    
    def display_chain_results(self):
        """Display chain building results"""
        if not self.chains_built:
            print("No chains built")
            return
        
        print(f"\n📋 Chain Building Results ({len(self.chains_built)} chains):")
        print("-" * 70)
        
        for chain in self.chains_built:
            print(f"\n🔗 {chain['unit_name']}")
            print(f"   Resources: {chain['resources_count']}")
            print(f"   Relationships: {chain['relationships_count']}")
            print(f"   Framework: {chain['cultural_framework']}")
            print(f"   Progression: {' → '.join(chain['progression'][:3])}...")
        
        # Calculate total pathways
        total_pathways = sum(chain['relationships_count'] for chain in self.chains_built)
        print(f"\n📊 Total pathways created: {total_pathways}")
        print(f"📊 Average pathways per unit: {total_pathways / len(self.chains_built):.1f}")


def main():
    """Main execution"""
    parser = argparse.ArgumentParser(description='Build prerequisite chains')
    parser.add_argument('--unit', help='Specific unit to build chain for')
    parser.add_argument('--dry-run', action='store_true', help='Analyze without creating')
    
    args = parser.parse_args()
    
    builder = PrerequisiteChainBuilder(dry_run=args.dry_run)
    
    if args.unit:
        print(f"Building chain for: {args.unit}")
        if args.unit in TARGET_UNITS:
            # Build specific unit
            chain = builder._build_unit_chain(args.unit, TARGET_UNITS[args.unit])
            if chain:
                builder.chains_built.append(chain)
        else:
            print(f"Unknown unit: {args.unit}")
            print(f"Available units: {', '.join(TARGET_UNITS.keys())}")
            return
    else:
        # Build all chains
        builder.build_all_chains()
    
    # Display results
    builder.display_chain_results()
    
    # Save chain log
    if builder.chains_built:
        log_file = f"prerequisite_chains_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(log_file, 'w') as f:
            json.dump(builder.chains_built, f, indent=2, default=str)
        print(f"\n📝 Chain log saved to: {log_file}")


if __name__ == '__main__':
    main()