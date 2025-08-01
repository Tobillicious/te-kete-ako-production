#!/usr/bin/env python3
"""
Te Kete Ako - Content Enrichment System using Exa.ai Research
============================================================

This system strategically enriches our educational resources with high-quality
external links from authoritative sources, organized by content type and 
cultural relevance.

Key Features:
- Prioritizes NZ government and educational sites
- Focuses on cultural authenticity for Te Ao Māori content
- Maps to curriculum standards
- Provides contextual relevance scoring
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any

class TeKeteContentEnricher:
    """
    Content enrichment system for Te Kete Ako educational resources.
    """
    
    def __init__(self):
        self.base_path = Path('.')
        self.enrichment_data = {
            'cultural_maori': {
                'priority': 1,
                'target_domains': [
                    'education.govt.nz',
                    'tahurangi.education.govt.nz', 
                    'tepapa.govt.nz',
                    'teara.govt.nz',
                    'maori.nz',
                    'tewhanake.maori.nz'
                ],
                'resources': [
                    {
                        'title': 'Tāhūrangi - Te Reo Māori Education Hub',
                        'url': 'https://tahurangi.education.govt.nz/',
                        'description': 'Official NZ government hub for te reo Māori resources, guidance, and teaching support',
                        'relevance_keywords': ['māori', 'te reo', 'cultural', 'tikanga', 'whakapapa', 'kaitiakitanga'],
                        'year_levels': ['7-13'],
                        'subjects': ['te_reo_maori', 'social_sciences', 'cultural']
                    },
                    {
                        'title': 'Te Reo Māori - The New Zealand Curriculum',
                        'url': 'https://newzealandcurriculum.tahurangi.education.govt.nz/5637157326.c',
                        'description': 'Official curriculum guidelines for teaching te reo Māori in English-medium schools',
                        'relevance_keywords': ['curriculum', 'te reo', 'māori', 'guidelines', 'teaching'],
                        'year_levels': ['1-13'],
                        'subjects': ['te_reo_maori', 'curriculum']
                    },
                    {
                        'title': 'Te Mana o te Reo Māori Education Resources',
                        'url': 'https://teara.govt.nz/en/te-tai/education/te-mana-o-te-reo-maori-resources',
                        'description': 'Comprehensive resources covering Whakapapa, Tūrangawaewae, Whanaungatanga, Mana Motuhake, and Kaitiakitanga',
                        'relevance_keywords': ['whakapapa', 'tūrangawaewae', 'whanaungatanga', 'mana motuhake', 'kaitiakitanga', 'history'],
                        'year_levels': ['7-8'],
                        'subjects': ['social_sciences', 'te_reo_maori', 'history']
                    }
                ]
            },
            'science_stem': {
                'priority': 2,
                'target_domains': [
                    'sciencelearn.org.nz',
                    'education.govt.nz',
                    'nzcer.org.nz'
                ],
                'resources': [
                    {
                        'title': 'Science Learning Hub',
                        'url': 'https://www.sciencelearn.org.nz/',
                        'description': 'Over 11,550 NZ science education resources for teachers, students and community',
                        'relevance_keywords': ['science', 'stem', 'research', 'experiments', 'investigation'],
                        'year_levels': ['1-13'],
                        'subjects': ['science', 'stem', 'technology']
                    },
                    {
                        'title': 'Science in the NZ Curriculum',
                        'url': 'https://newzealandcurriculum.tahurangi.education.govt.nz/science-in-the-nz-curriculum/5637208467.p',
                        'description': 'Official NZ science curriculum with Nature of Science, Living World, Physical World strands',
                        'relevance_keywords': ['curriculum', 'nature of science', 'living world', 'physical world', 'material world'],
                        'year_levels': ['1-10'],
                        'subjects': ['science', 'curriculum']
                    }
                ]
            },
            'english_writing': {
                'priority': 3,
                'target_domains': [
                    'education.govt.nz',
                    'literacyonline.tki.org.nz',
                    'tki.org.nz'
                ],
                'resources': [
                    {
                        'title': 'English - The New Zealand Curriculum',
                        'url': 'https://newzealandcurriculum.tahurangi.education.govt.nz/new-zealand-curriculum-online/learning-content-resources/english/5637144622.c',
                        'description': 'Official English curriculum resources for oral, written, and visual texts',
                        'relevance_keywords': ['english', 'writing', 'literacy', 'reading', 'oral language', 'visual language'],
                        'year_levels': ['0-13'],
                        'subjects': ['english', 'literacy']
                    },
                    {
                        'title': 'Literacy Online Resources',
                        'url': 'https://newzealandcurriculum.tahurangi.education.govt.nz/new-zealand-curriculum-online/learning-content-resources/literacy-inc-instructional-series/5637144635.c',
                        'description': 'Instructional series and literacy resources for Years 1-8',
                        'relevance_keywords': ['literacy', 'instructional', 'reading', 'writing', 'comprehension'],
                        'year_levels': ['1-8'],
                        'subjects': ['english', 'literacy']
                    }
                ]
            },
            'social_studies': {
                'priority': 4,
                'target_domains': [
                    'tki.org.nz',
                    'education.govt.nz',
                    'nzcer.org.nz'
                ],
                'resources': [
                    {
                        'title': 'Social Sciences - NZ Curriculum',
                        'url': 'https://nzcurriculum.tki.org.nz/The-New-Zealand-Curriculum/Social-sciences',
                        'description': 'Social studies curriculum for critical, informed, and responsible citizens',
                        'relevance_keywords': ['social studies', 'critical thinking', 'citizenship', 'society', 'contemporary issues'],
                        'year_levels': ['1-10'],
                        'subjects': ['social_sciences', 'social_studies']
                    },
                    {
                        'title': 'Media Studies Resources',
                        'url': 'https://seniorsecondary.tki.org.nz/Social-sciences/Media-studies/Resources',
                        'description': 'Media literacy and critical analysis resources for senior students',
                        'relevance_keywords': ['media literacy', 'critical analysis', 'contemporary issues', 'digital citizenship'],
                        'year_levels': ['11-13'],
                        'subjects': ['media_studies', 'social_sciences']
                    }
                ]
            }
        }
    
    def analyze_content_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Analyze a content file to determine its subject, keywords, and enrichment needs.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract metadata
            title_match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
            title = title_match.group(1) if title_match else file_path.stem
            
            # Extract description from meta or first paragraph
            desc_match = re.search(r'<meta[^>]*description[^>]*content="([^"]*)"', content, re.IGNORECASE)
            if not desc_match:
                desc_match = re.search(r'<p[^>]*>([^<]{50,200})</p>', content, re.IGNORECASE)
            
            description = desc_match.group(1) if desc_match else ""
            
            # Content analysis
            content_lower = content.lower()
            
            # Determine subject areas
            subject_scores = {
                'te_reo_maori': self._count_keywords(content_lower, ['māori', 'maori', 'te reo', 'tikanga', 'whakapapa', 'kaitiakitanga', 'manaakitanga']),
                'science': self._count_keywords(content_lower, ['science', 'stem', 'experiment', 'hypothesis', 'investigation', 'research']),
                'english': self._count_keywords(content_lower, ['writing', 'english', 'literacy', 'reading', 'essay', 'analysis', 'literature']),
                'social_sciences': self._count_keywords(content_lower, ['social', 'society', 'history', 'geography', 'civics', 'contemporary', 'issues']),
                'mathematics': self._count_keywords(content_lower, ['math', 'statistics', 'probability', 'graph', 'calculation', 'number']),
                'arts': self._count_keywords(content_lower, ['art', 'creative', 'design', 'music', 'drama', 'visual']),
                'technology': self._count_keywords(content_lower, ['technology', 'digital', 'computer', 'ai', 'coding', 'programming'])
            }
            
            primary_subject = max(subject_scores, key=subject_scores.get) if max(subject_scores.values()) > 0 else 'general'
            
            # Determine year level
            year_matches = re.findall(r'year\s*(\d+)', content_lower)
            if year_matches:
                years = [int(y) for y in year_matches if y.isdigit()]
                year_level = f"{min(years)}-{max(years)}" if len(set(years)) > 1 else str(years[0])
            else:
                year_level = "7-10"  # Default assumption
            
            return {
                'file_path': str(file_path),
                'title': title.strip(),
                'description': description.strip(),
                'primary_subject': primary_subject,
                'subject_scores': subject_scores,
                'year_level': year_level,
                'cultural_level': self._assess_cultural_level(content_lower),
                'keywords': self._extract_key_concepts(content_lower)
            }
            
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return None
    
    def _count_keywords(self, content: str, keywords: List[str]) -> int:
        """Count occurrences of keywords in content."""
        return sum(content.count(keyword) for keyword in keywords)
    
    def _assess_cultural_level(self, content: str) -> str:
        """Assess the cultural integration level of content."""
        cultural_indicators = {
            'high': ['whakapapa', 'kaitiakitanga', 'manaakitanga', 'tino rangatiratanga', 'te ao māori', 'mātauranga'],
            'medium': ['māori', 'maori', 'cultural', 'treaty', 'waitangi', 'indigenous'],
            'low': ['new zealand', 'aotearoa', 'nz']
        }
        
        for level, indicators in cultural_indicators.items():
            if any(indicator in content for indicator in indicators):
                return level
        
        return 'general'
    
    def _extract_key_concepts(self, content: str) -> List[str]:
        """Extract key educational concepts from content."""
        concept_patterns = [
            r'critical thinking', r'problem solving', r'collaboration', r'communication',
            r'creativity', r'digital literacy', r'media literacy', r'sustainability',
            r'systems thinking', r'design thinking', r'inquiry learning'
        ]
        
        concepts = []
        for pattern in concept_patterns:
            if re.search(pattern, content):
                concepts.append(pattern.replace(r'\\s+', ' '))
        
        return concepts
    
    def find_relevant_enrichments(self, content_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Find relevant external resources for enriching content.
        """
        relevant_resources = []
        
        # Check each enrichment category
        for category, data in self.enrichment_data.items():
            for resource in data['resources']:
                relevance_score = self._calculate_relevance(content_analysis, resource)
                
                if relevance_score > 0.3:  # Minimum relevance threshold
                    relevant_resources.append({
                        **resource,
                        'category': category,
                        'relevance_score': relevance_score,
                        'priority': data['priority']
                    })
        
        # Sort by relevance score and priority
        relevant_resources.sort(key=lambda x: (x['priority'], -x['relevance_score']))
        return relevant_resources[:5]  # Top 5 most relevant
    
    def _calculate_relevance(self, content_analysis: Dict[str, Any], resource: Dict[str, Any]) -> float:
        """
        Calculate relevance score between content and external resource.
        """
        score = 0.0
        
        # Subject match
        if content_analysis['primary_subject'] in resource['subjects']:
            score += 0.4
        
        # Keyword overlap
        content_text = (content_analysis['title'] + ' ' + content_analysis['description']).lower()
        keyword_matches = sum(1 for keyword in resource['relevance_keywords'] if keyword in content_text)
        score += (keyword_matches / len(resource['relevance_keywords'])) * 0.3
        
        # Year level compatibility
        if self._year_levels_compatible(content_analysis['year_level'], resource['year_levels']):
            score += 0.2
        
        # Cultural level match (bonus for cultural content)
        if content_analysis['cultural_level'] in ['high', 'medium'] and 'cultural' in resource['subjects']:
            score += 0.1
        
        return min(score, 1.0)
    
    def _year_levels_compatible(self, content_years: str, resource_years: List[str]) -> bool:
        """Check if year levels are compatible."""
        try:
            if '-' in content_years:
                content_range = [int(x) for x in content_years.split('-')]
                content_set = set(range(content_range[0], content_range[1] + 1))
            else:
                content_set = {int(content_years)}
            
            for year_range in resource_years:
                if '-' in year_range:
                    resource_range = [int(x) for x in year_range.split('-')]
                    resource_set = set(range(resource_range[0], resource_range[1] + 1))
                else:
                    resource_set = {int(year_range)}
                    
                if content_set & resource_set:  # Any overlap
                    return True
                    
            return False
        except:
            return True  # Default to compatible if parsing fails
    
    def generate_enrichment_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive enrichment report for all content.
        """
        print("🔍 ANALYZING ALL EDUCATIONAL CONTENT FOR ENRICHMENT...")
        
        content_dirs = ['handouts', 'y8-systems', 'guided-inquiry-unit', 'units', 'lessons', 'games', 'experiences']
        analysis_results = []
        
        total_files = 0
        enriched_files = 0
        
        for content_dir in content_dirs:
            dir_path = self.base_path / content_dir
            if dir_path.exists():
                html_files = list(dir_path.glob('**/*.html'))
                print(f"📂 {content_dir}: {len(html_files)} files")
                
                for file_path in html_files:
                    total_files += 1
                    analysis = self.analyze_content_file(file_path)
                    
                    if analysis:
                        enrichments = self.find_relevant_enrichments(analysis)
                        if enrichments:
                            enriched_files += 1
                            analysis['enrichments'] = enrichments
                            analysis_results.append(analysis)
        
        # Generate summary statistics
        subject_distribution = {}
        cultural_distribution = {}
        
        for result in analysis_results:
            subject = result['primary_subject']
            cultural = result['cultural_level']
            
            subject_distribution[subject] = subject_distribution.get(subject, 0) + 1
            cultural_distribution[cultural] = cultural_distribution.get(cultural, 0) + 1
        
        return {
            'total_files_analyzed': total_files,
            'files_with_enrichments': enriched_files,
            'enrichment_rate': enriched_files / total_files if total_files > 0 else 0,
            'subject_distribution': subject_distribution,
            'cultural_distribution': cultural_distribution,
            'enrichment_recommendations': analysis_results  # ALL recommendations, not just top 20
        }

def main():
    """Generate content enrichment analysis and recommendations."""
    enricher = TeKeteContentEnricher()
    report = enricher.generate_enrichment_report()
    
    print(f"\n📊 CONTENT ENRICHMENT ANALYSIS COMPLETE")
    print(f"=" * 50)
    print(f"📁 Total files analyzed: {report['total_files_analyzed']}")
    print(f"✨ Files with enrichment opportunities: {report['files_with_enrichments']}")
    print(f"📈 Enrichment rate: {report['enrichment_rate']:.1%}")
    
    print(f"\n📚 SUBJECT DISTRIBUTION:")
    for subject, count in sorted(report['subject_distribution'].items(), key=lambda x: x[1], reverse=True):
        print(f"  • {subject}: {count} files")
    
    print(f"\n🌿 CULTURAL INTEGRATION DISTRIBUTION:")
    for level, count in sorted(report['cultural_distribution'].items(), key=lambda x: x[1], reverse=True):
        print(f"  • {level}: {count} files")
    
    print(f"\n🎯 TOP ENRICHMENT OPPORTUNITIES:")
    for i, rec in enumerate(report['enrichment_recommendations'][:10], 1):
        print(f"{i}. {rec['title']}")
        print(f"   Subject: {rec['primary_subject']} | Cultural: {rec['cultural_level']}")
        print(f"   Enrichments: {len(rec['enrichments'])} relevant resources")
        if rec['enrichments']:
            top_enrichment = rec['enrichments'][0]
            print(f"   → {top_enrichment['title']} ({top_enrichment['relevance_score']:.2f} relevance)")
        print()
    
    # Save detailed report
    output_file = 'content_enrichment_analysis.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Detailed analysis saved to: {output_file}")
    return report

if __name__ == "__main__":
    main()