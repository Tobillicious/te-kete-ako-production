"""
Curriculum Scraper with Selenium - Bypasses 403 Forbidden
Uses real browser automation to extract curriculum statements
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time
from typing import List, Dict, Optional
from pathlib import Path
from tqdm import tqdm
import logging

from config import CURRICULUM_VERSIONS, TAHURANGI_BASE

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SeleniumCurriculumScraper:
    """Scrapes curriculum using Selenium (real browser)"""
    
    def __init__(self, output_dir: str = "./scraped-data", headless: bool = True):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.headless = headless
        self.driver = None
        
    def setup_driver(self):
        """Initialize Chrome driver with options"""
        logger.info("Setting up Chrome driver...")
        
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # Automatically download and use correct ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(10)
        
        logger.info("✓ Chrome driver ready")
    
    def fetch_page_selenium(self, url: str, wait_seconds: int = 3) -> Optional[BeautifulSoup]:
        """Fetch page using Selenium (bypasses bot detection)"""
        try:
            logger.info(f"Fetching with Selenium: {url}")
            self.driver.get(url)
            
            # Wait for page to load
            time.sleep(wait_seconds)
            
            # Wait for main content
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "table"))
                )
            except:
                logger.warning("No tables found, continuing anyway...")
            
            # Get page source and parse
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
            
            logger.info(f"✓ Successfully fetched {url}")
            return soup
            
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_temataiaho_statements(
        self, 
        soup: BeautifulSoup, 
        learning_area: str,
        phase: str,
        strand: str,
        year_levels: List[int]
    ) -> List[Dict]:
        """Extract statements from Te Mātaiaho 2025 format"""
        statements = []
        
        # Find all tables
        tables = soup.find_all('table')
        logger.info(f"  Found {len(tables)} tables on page")
        
        for table_idx, table in enumerate(tables):
            # Check if this is a strand-specific table
            # Look for heading before table
            prev_elements = []
            current = table.find_previous()
            for _ in range(10):  # Check previous 10 elements
                if current and current.name in ['h2', 'h3', 'h4']:
                    prev_elements.append(current.get_text(strip=True))
                if current:
                    current = current.find_previous()
                else:
                    break
            
            # Check if any heading mentions the strand
            strand_match = any(strand.lower() in heading.lower() for heading in prev_elements)
            
            if not strand_match and tables.index(table) > 0:
                # Skip tables that don't match strand (unless it's the first table)
                continue
            
            logger.info(f"  Processing table {table_idx + 1} (potential strand: {strand})")
            
            # Extract rows
            rows = table.find_all('tr')
            
            for row_idx, row in enumerate(rows):
                cells = row.find_all(['td', 'th'])
                
                if len(cells) < 2:
                    continue
                
                # Skip header rows
                if all(cell.name == 'th' for cell in cells):
                    continue
                
                # Try to identify Knowledge and Practices columns
                # Format varies but usually:
                # [Year indicator?] [Knowledge] [Practices]
                # OR [Knowledge] [Practices]
                
                knowledge_cell = None
                practices_cell = None
                
                if len(cells) >= 3:
                    # Likely format: [Year] [Knowledge] [Practices]
                    knowledge_cell = cells[1]
                    practices_cell = cells[2]
                elif len(cells) == 2:
                    # Format: [Knowledge] [Practices]
                    knowledge_cell = cells[0]
                    practices_cell = cells[1]
                
                # Extract Knowledge
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
                            "year_levels": year_levels,
                            "context": None,
                            "examples": self._extract_examples(knowledge_cell)
                        })
                
                # Extract Practices
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
                            "year_levels": year_levels,
                            "context": None,
                            "examples": self._extract_examples(practices_cell)
                        })
        
        return statements
    
    def _clean_text(self, text: str) -> str:
        """Clean extracted text"""
        text = ' '.join(text.split())
        text = text.strip()
        text = text.replace('\u200b', '')
        text = text.replace('\xa0', ' ')
        return text
    
    def _is_valid_statement(self, text: str) -> bool:
        """Check if text is a valid curriculum statement"""
        if not text or len(text) < 10:
            return False
        
        # Skip header text
        if text.lower() in ['knowledge', 'practices', 'during year', 'year', 'phase']:
            return False
        
        # Check for placeholder text
        invalid_phrases = ['lorem ipsum', 'placeholder', 'TODO', 'TBD']
        text_lower = text.lower()
        if any(phrase in text_lower for phrase in invalid_phrases):
            return False
        
        return True
    
    def _extract_examples(self, cell) -> Optional[List[str]]:
        """Extract examples from cell"""
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
                logger.warning(f"Skipping {phase} - URL not configured")
                continue
            
            logger.info(f"\nPhase: {phase} (Years {years})")
            soup = self.fetch_page_selenium(url)
            
            if not soup:
                logger.error(f"Failed to fetch {phase}")
                continue
            
            # Extract statements for each strand
            for strand in learning_area_config.get('strands', []):
                logger.info(f"  Extracting strand: {strand}")
                
                statements = self.extract_temataiaho_statements(
                    soup, learning_area, phase, strand, years
                )
                
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
    
    def cleanup(self):
        """Close browser"""
        if self.driver:
            self.driver.quit()
            logger.info("✓ Browser closed")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape curriculum with Selenium')
    parser.add_argument('--output', default='./scraped-data', help='Output directory')
    parser.add_argument('--version', default='temataiaho_2025', help='Curriculum version')
    parser.add_argument('--learning-area', default='English', help='Learning area to scrape')
    parser.add_argument('--headless', action='store_true', help='Run browser in headless mode')
    parser.add_argument('--show-browser', action='store_true', help='Show browser (opposite of headless)')
    
    args = parser.parse_args()
    
    # Determine headless mode
    headless = args.headless or not args.show_browser
    
    scraper = SeleniumCurriculumScraper(output_dir=args.output, headless=headless)
    
    try:
        scraper.setup_driver()
        
        # Get config
        config = CURRICULUM_VERSIONS[args.version]
        learning_area_config = next(
            (la for la in config['learning_areas'] if la['name'] == args.learning_area),
            None
        )
        
        if not learning_area_config:
            logger.error(f"Learning area '{args.learning_area}' not found")
            return 1
        
        # Scrape
        statements = scraper.scrape_learning_area(args.version, learning_area_config)
        
        # Save
        if statements:
            scraper.save_statements(statements, args.version, args.learning_area)
            logger.info(f"\n✅ SUCCESS: Extracted {len(statements)} statements!")
            return 0
        else:
            logger.warning(f"\n⚠️  No statements extracted")
            return 1
    
    except Exception as e:
        logger.error(f"Scraping failed: {e}", exc_info=True)
        return 1
    
    finally:
        scraper.cleanup()


if __name__ == "__main__":
    exit(main())

