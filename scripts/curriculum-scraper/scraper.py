"""
Curriculum Scraper - Extract NZ Curriculum Statements from Tahurangi
Extracts verbatim curriculum content and saves to structured JSON
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
from typing import List, Dict, Optional
from pathlib import Path
from tqdm import tqdm
import logging

from config import CURRICULUM_VERSIONS, STATEMENT_PATTERNS, TAHURANGI_BASE

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class CurriculumScraper:
    """Scrapes curriculum statements from Tahurangi website"""
    
    def __init__(self, output_dir: str = "./scraped-data", delay: float = 1.0):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Te Kete Ako Curriculum Scraper/1.0 (Educational Resource Platform)'
        })
    
    def fetch_page(self, url: str, max_retries: int = 3) -> Optional[BeautifulSoup]:
        """Fetch and parse a page with retries"""
        for attempt in range(max_retries):
            try:
                logger.info(f"Fetching: {url} (attempt {attempt + 1}/{max_retries})")
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                
                # Be respectful - delay between requests
                time.sleep(self.delay)
                
                soup = BeautifulSoup(response.content, 'lxml')
                logger.info(f"✓ Successfully fetched {url}")
                return soup
                
            except requests.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(self.delay * 2)  # Longer delay on retry
                else:
                    logger.error(f"Failed to fetch {url} after {max_retries} attempts")
                    return None
    
    def extract_temataiaho_statements(
        self, 
        soup: BeautifulSoup, 
        learning_area: str,
        phase: str,
        strand: str,
        year_levels: List[int]
    ) -> List[Dict]:
        """Extract statements from Te Mātaiaho 2025 format (tables)"""
        statements = []
        
        # Find all tables (Te Mātaiaho uses tables for Knowledge/Practices)
        tables = soup.find_all('table')
        
        for table in tables:
            # Check if this table is for the current strand
            # (Strand name usually appears in heading before table)
            prev_heading = table.find_previous(['h2', 'h3'])
            if prev_heading and strand.lower() not in prev_heading.get_text().lower():
                continue
            
            # Extract rows
            rows = table.find_all('tr')
            
            for row in rows:
                cells = row.find_all('td')
                
                if len(cells) < 2:
                    continue  # Header row or invalid
                
                # First column might be year indicator, check
                first_cell_text = cells[0].get_text(strip=True)
                year_match = re.search(r'Year (\d+)', first_cell_text, re.IGNORECASE)
                
                # Determine which cells contain Knowledge and Practices
                if year_match:
                    # Format: [Year X] [Knowledge] [Practices]
                    specific_year = int(year_match.group(1))
                    knowledge_cell = cells[1] if len(cells) > 1 else None
                    practices_cell = cells[2] if len(cells) > 2 else None
                else:
                    # Format: [Knowledge] [Practices]
                    knowledge_cell = cells[0] if len(cells) > 0 else None
                    practices_cell = cells[1] if len(cells) > 1 else None
                    specific_year = None
                
                # Extract Knowledge statements
                if knowledge_cell:
                    knowledge_text = self._clean_text(knowledge_cell.get_text())
                    if self._is_valid_statement(knowledge_text):
                        statements.append({
                            "curriculum_version": "temataiaho_2025",
                            "learning_area": learning_area,
                            "phase": phase,
                            "strand": strand,
                            "element": "Knowledge",
                            "statement_text": knowledge_text,
                            "year_levels": [specific_year] if specific_year else year_levels,
                            "context": None,
                            "examples": self._extract_examples(knowledge_cell)
                        })
                
                # Extract Practices statements
                if practices_cell:
                    practices_text = self._clean_text(practices_cell.get_text())
                    if self._is_valid_statement(practices_text):
                        statements.append({
                            "curriculum_version": "temataiaho_2025",
                            "learning_area": learning_area,
                            "phase": phase,
                            "strand": strand,
                            "element": "Practices",
                            "statement_text": practices_text,
                            "year_levels": [specific_year] if specific_year else year_levels,
                            "context": None,
                            "examples": self._extract_examples(practices_cell)
                        })
        
        return statements
    
    def _clean_text(self, text: str) -> str:
        """Clean extracted text"""
        # Remove extra whitespace
        text = ' '.join(text.split())
        # Remove leading/trailing whitespace
        text = text.strip()
        # Remove weird Unicode characters
        text = text.replace('\u200b', '')  # Zero-width space
        text = text.replace('\xa0', ' ')  # Non-breaking space
        return text
    
    def _is_valid_statement(self, text: str) -> bool:
        """Check if extracted text is a valid curriculum statement"""
        if not text or len(text) < 10:
            return False
        
        # Check for placeholder text
        invalid_phrases = ['lorem ipsum', 'placeholder', 'TODO', 'TBD', '[INSERT']
        text_lower = text.lower()
        if any(phrase in text_lower for phrase in invalid_phrases):
            logger.warning(f"Invalid placeholder found: {text[:50]}...")
            return False
        
        return True
    
    def _extract_examples(self, cell) -> Optional[List[str]]:
        """Extract examples from a cell (if they exist)"""
        # Examples are often in <ul> or <li> tags
        examples = []
        for li in cell.find_all('li'):
            example = self._clean_text(li.get_text())
            if example and len(example) > 5:
                examples.append(example)
        
        return examples if examples else None
    
    def scrape_learning_area(
        self,
        version: str,
        learning_area_config: Dict
    ) -> List[Dict]:
        """Scrape all statements for a learning area"""
        all_statements = []
        learning_area = learning_area_config['name']
        
        logger.info(f"\n{'='*60}")
        logger.info(f"Scraping: {learning_area} ({version})")
        logger.info(f"{'='*60}")
        
        # Iterate through phases
        for phase_config in tqdm(learning_area_config['phases'], desc=f"{learning_area} Phases"):
            phase = phase_config['phase']
            years = phase_config['year_levels']
            url = phase_config['url']
            
            if url == "TBD":
                logger.warning(f"Skipping {phase} - URL not configured yet")
                continue
            
            logger.info(f"\nPhase: {phase} (Years {years})")
            soup = self.fetch_page(url)
            
            if not soup:
                logger.error(f"Failed to fetch {phase}")
                continue
            
            # Extract statements for each strand
            for strand in learning_area_config.get('strands', []):
                logger.info(f"  Extracting strand: {strand}")
                
                if version == "temataiaho_2025":
                    statements = self.extract_temataiaho_statements(
                        soup, learning_area, phase, strand, years
                    )
                elif version == "2007_nzc":
                    # TODO: Implement 2007 NZC extraction
                    statements = []
                else:
                    statements = []
                
                logger.info(f"    → Found {len(statements)} statements")
                all_statements.extend(statements)
        
        return all_statements
    
    def save_statements(self, statements: List[Dict], version: str, learning_area: str):
        """Save statements to JSON file"""
        filename = self.output_dir / f"{version}_{learning_area.lower().replace(' ', '_')}.json"
        
        output = {
            "curriculum_version": version,
            "learning_area": learning_area,
            "statement_count": len(statements),
            "extracted_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "statements": statements
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        logger.info(f"\n✓ Saved {len(statements)} statements to {filename}")
    
    def scrape_all(self):
        """Scrape all configured curriculum versions and learning areas"""
        summary = []
        
        for version, config in CURRICULUM_VERSIONS.items():
            logger.info(f"\n{'#'*60}")
            logger.info(f"SCRAPING: {config['name']}")
            logger.info(f"{'#'*60}")
            
            for learning_area_config in config.get('learning_areas', []):
                try:
                    statements = self.scrape_learning_area(version, learning_area_config)
                    
                    if statements:
                        self.save_statements(statements, version, learning_area_config['name'])
                        summary.append({
                            "version": version,
                            "learning_area": learning_area_config['name'],
                            "statement_count": len(statements),
                            "status": "success"
                        })
                    else:
                        logger.warning(f"No statements extracted for {learning_area_config['name']}")
                        summary.append({
                            "version": version,
                            "learning_area": learning_area_config['name'],
                            "statement_count": 0,
                            "status": "no_statements"
                        })
                
                except Exception as e:
                    logger.error(f"Error scraping {learning_area_config['name']}: {e}", exc_info=True)
                    summary.append({
                        "version": version,
                        "learning_area": learning_area_config['name'],
                        "statement_count": 0,
                        "status": "error",
                        "error": str(e)
                    })
        
        # Save summary
        summary_file = self.output_dir / "scraping_summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        logger.info(f"\n{'='*60}")
        logger.info("SCRAPING COMPLETE")
        logger.info(f"{'='*60}")
        logger.info(f"Summary saved to: {summary_file}")
        
        return summary


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape NZ Curriculum statements from Tahurangi')
    parser.add_argument('--output', default='./scraped-data', help='Output directory')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between requests (seconds)')
    parser.add_argument('--version', help='Scrape specific version only (temataiaho_2025, draft_2025, 2007_nzc)')
    parser.add_argument('--learning-area', help='Scrape specific learning area only')
    
    args = parser.parse_args()
    
    scraper = CurriculumScraper(output_dir=args.output, delay=args.delay)
    
    if args.version and args.learning_area:
        # Scrape specific combination
        config = CURRICULUM_VERSIONS[args.version]
        learning_area_config = next(
            (la for la in config['learning_areas'] if la['name'] == args.learning_area),
            None
        )
        if learning_area_config:
            statements = scraper.scrape_learning_area(args.version, learning_area_config)
            scraper.save_statements(statements, args.version, args.learning_area)
        else:
            logger.error(f"Learning area '{args.learning_area}' not found in version '{args.version}'")
    else:
        # Scrape everything
        scraper.scrape_all()


if __name__ == "__main__":
    main()

