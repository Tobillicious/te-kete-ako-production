"""
Advanced Curriculum Scraper - Handles multiple HTML structures
Adapts to different table formats across subjects
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
import re

from config import CURRICULUM_VERSIONS, TAHURANGI_BASE

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AdvancedCurriculumScraper:
    """Scrapes curriculum using adaptive HTML parsing"""
    
    def __init__(self, output_dir: str = "./scraped-data", headless: bool = True):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.headless = headless
        self.driver = None
        
    def setup_driver(self):
        """Initialize Chrome driver"""
        logger.info("Setting up Chrome driver...")
        
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36')
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(10)
        
        logger.info("✓ Chrome driver ready")
    
    def fetch_page(self, url: str, wait_seconds: int = 3) -> Optional[BeautifulSoup]:
        """Fetch page using Selenium"""
        try:
            logger.info(f"Fetching: {url}")
            self.driver.get(url)
            time.sleep(wait_seconds)
            
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "table"))
                )
            except:
                pass
            
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            logger.info(f"✓ Page loaded")
            return soup
            
        except Exception as e:
            logger.error(f"Error: {e}")
            return None
    
    def extract_list_items_as_statement(self, cell) -> List[str]:
        """Extract bullet points from a cell as individual statements"""
        statements = []
        
        # Find all <li> items
        list_items = cell.find_all('li', recursive=True)
        
        for li in list_items:
            text = self._clean_text(li.get_text())
            if self._is_valid_statement(text):
                statements.append(text)
        
        # If no list items, try getting paragraph text
        if not statements:
            paragraphs = cell.find_all('p')
            for p in paragraphs:
                text = self._clean_text(p.get_text())
                if self._is_valid_statement(text):
                    statements.append(text)
        
        return statements
    
    def extract_from_complex_table(
        self,
        table,
        learning_area: str,
        phase: str,
        curriculum_version: str
    ) -> List[Dict]:
        """
        Extract from complex tables with year-specific columns
        Format: [Topic] [Y1 Knowledge] [Y2 Knowledge] [Y3 Knowledge] [Y1 Practices] [Y2 Practices] [Y3 Practices]
        """
        statements = []
        
        # Find all rows (skip header rows)
        rows = table.find_all('tr')
        
        # Try to identify header row to understand column structure
        header_row = None
        for row in rows:
            cells = row.find_all(['th', 'td'])
            cell_texts = [c.get_text(strip=True) for c in cells]
            
            # Look for "Knowledge" and "Practices" in headers
            if any('knowledge' in str(t).lower() for t in cell_texts) or any('practices' in str(t).lower() for t in cell_texts):
                header_row = row
                break
        
        # Try to find year-level headers
        year_row = None
        for row in rows:
            cells = row.find_all(['th', 'td'])
            cell_texts = [c.get_text(strip=True) for c in cells]
            
            # Look for "During Year" or "Year 1" patterns
            if any(re.search(r'(during\s+)?year\s+\d+', str(t), re.I) for t in cell_texts):
                year_row = row
                break
        
        # Parse year structure from year_row
        year_cols = {}
        if year_row:
            cells = year_row.find_all(['th', 'td'])
            for idx, cell in enumerate(cells):
                text = cell.get_text(strip=True)
                year_match = re.search(r'year\s+(\d+)', text, re.I)
                if year_match:
                    year = int(year_match.group(1))
                    year_cols[idx] = year
        
        # Process content rows
        for row in rows:
            # Skip header rows
            if row == header_row or row == year_row:
                continue
            
            cells = row.find_all('td')
            if len(cells) < 2:
                continue
            
            # First cell is usually the topic/strand name
            topic_cell = cells[0]
            topic_text = self._clean_text(topic_cell.get_text())
            
            if not topic_text or len(topic_text) < 3:
                continue
            
            # Determine strand from topic
            strand = topic_text
            
            # Process remaining cells
            for col_idx in range(1, len(cells)):
                cell = cells[col_idx]
                
                # Determine year level for this column
                year_level = year_cols.get(col_idx, None)
                
                # Determine if Knowledge or Practices based on column position
                # Usually: Knowledge columns first, then Practices columns
                # For Science: cols 1-3 are Knowledge (Y1, Y2, Y3), cols 4-6 are Practices
                mid_point = len(cells) // 2
                element = "Knowledge" if col_idx <= mid_point else "Practices"
                
                # Extract statements from list items
                cell_statements = self.extract_list_items_as_statement(cell)
                
                for stmt_text in cell_statements:
                    statements.append({
                        "curriculum_version": curriculum_version,
                        "learning_area": learning_area,
                        "phase": phase,
                        "strand": strand,
                        "element": element,
                        "statement_text": stmt_text,
                        "year_levels": [year_level] if year_level else self.get_phase_years(phase),
                        "context": None,
                        "examples": None
                    })
        
        return statements
    
    def get_phase_years(self, phase: str) -> List[int]:
        """Get year levels for a phase"""
        phase_mapping = {
            "Phase 1": [0, 1, 2, 3],
            "Phase 2": [4, 5, 6],
            "Phase 3": [7, 8],
            "Phase 4": [9, 10],
        }
        return phase_mapping.get(phase, [])
    
    def extract_statements(
        self,
        soup: BeautifulSoup,
        learning_area: str,
        phase: str,
        curriculum_version: str
    ) -> List[Dict]:
        """Auto-detect table structure and extract appropriately"""
        all_statements = []
        
        tables = soup.find_all('table')
        logger.info(f"  Found {len(tables)} tables")
        
        for table_idx, table in enumerate(tables):
            # Check table type by looking at headers
            header_cells = table.find_all('th')
            header_texts = [h.get_text(strip=True).lower() for h in header_cells]
            
            # Check if this looks like a year-specific table
            has_year_headers = any(re.search(r'year\s+\d+', h) for h in header_texts)
            
            if has_year_headers or len(tables) <= 3:  # Science/complex structure
                logger.info(f"  Table {table_idx + 1}: Complex/year-specific structure")
                stmts = self.extract_from_complex_table(table, learning_area, phase, curriculum_version)
            else:  # Simple structure (English/Math style)
                logger.info(f"  Table {table_idx + 1}: Simple structure (English/Math style)")
                # Use old extraction method
                stmts = []
            
            if stmts:
                logger.info(f"    → Extracted {len(stmts)} statements")
                all_statements.extend(stmts)
        
        return all_statements
    
    def _clean_text(self, text: str) -> str:
        """Clean text"""
        text = ' '.join(text.split())
        text = text.strip()
        text = text.replace('\u200b', '').replace('\xa0', ' ')
        return text
    
    def _is_valid_statement(self, text: str) -> bool:
        """Check if valid statement"""
        if not text or len(text) < 15:  # Minimum statement length
            return False
        
        # Skip obvious headers
        skip_phrases = ['knowledge', 'practices', 'during year', 'materials', 'tools', 'equipment']
        if text.lower() in skip_phrases:
            return False
        
        # Skip placeholder text
        if any(p in text.lower() for p in ['lorem ipsum', 'placeholder', 'TODO']):
            return False
        
        return True
    
    def scrape_subject(
        self,
        version: str,
        learning_area_config: Dict
    ) -> List[Dict]:
        """Scrape all phases for a subject"""
        all_statements = []
        learning_area = learning_area_config['name']
        
        logger.info(f"\n{'='*60}")
        logger.info(f"📚 SCRAPING: {learning_area} ({version})")
        logger.info(f"{'='*60}\n")
        
        for phase_config in tqdm(learning_area_config['phases'], desc=f"{learning_area}"):
            phase = phase_config['phase']
            url = phase_config['url']
            
            if url == "TBD":
                logger.warning(f"⚠️  {phase}: URL not configured")
                continue
            
            logger.info(f"\n{phase} (Years {phase_config['year_levels']})")
            soup = self.fetch_page(url)
            
            if not soup:
                logger.error(f"❌ Failed to fetch {phase}")
                continue
            
            # Auto-detect and extract
            statements = self.extract_statements(soup, learning_area, phase, version)
            
            logger.info(f"✓ {phase}: {len(statements)} statements\n")
            all_statements.extend(statements)
        
        return all_statements
    
    def save_and_upload(self, statements: List[Dict], version: str, learning_area: str):
        """Save to JSON and upload to Supabase"""
        if not statements:
            logger.warning(f"⚠️  No statements to save for {learning_area}")
            return
        
        # Save to JSON
        filename = self.output_dir / f"{version}_{learning_area.lower().replace(' ', '_').replace('&', 'and')}.json"
        
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
        
        # Auto-upload
        logger.info(f"📤 Uploading to Supabase...")
        import os
        os.system(f"cd {self.output_dir.parent} && SUPABASE_URL='https://nlgldaqtubrlcqddppbq.supabase.co' SUPABASE_SERVICE_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM' python3 uploader.py ./scraped-data --file {filename.name} 2>&1 | grep -E '(Inserted|Skipped|SUCCESS)'")
    
    def cleanup(self):
        """Close browser"""
        if self.driver:
            self.driver.quit()


def main():
    """Main entry point - scrape ALL subjects"""
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--headless', action='store_true', default=True)
    parser.add_argument('--show-browser', action='store_true')
    
    args = parser.parse_args()
    headless = args.headless and not args.show_browser
    
    scraper = AdvancedCurriculumScraper(headless=headless)
    
    try:
        scraper.setup_driver()
        
        total_statements = 0
        summary = []
        
        # Scrape Te Mātaiaho 2025 (skip English/Math - already done)
        # Scrape Draft 2025
        for version_key in ['draft_2025']:
            config = CURRICULUM_VERSIONS[version_key]
            
            for la_config in config['learning_areas']:
                learning_area = la_config['name']
                
                logger.info(f"\n\n{'#'*60}")
                logger.info(f"# {learning_area}")
                logger.info(f"{'#'*60}")
                
                statements = scraper.scrape_subject(version_key, la_config)
                
                if statements:
                    scraper.save_and_upload(statements, version_key, learning_area)
                    total_statements += len(statements)
                    summary.append({
                        'version': version_key,
                        'learning_area': learning_area,
                        'count': len(statements),
                        'status': 'success'
                    })
                else:
                    summary.append({
                        'version': version_key,
                        'learning_area': learning_area,
                        'count': 0,
                        'status': 'no_statements'
                    })
        
        logger.info(f"\n\n{'='*60}")
        logger.info(f"🎉 SCRAPING COMPLETE")
        logger.info(f"{'='*60}")
        logger.info(f"Total statements extracted: {total_statements}")
        for s in summary:
            status_emoji = '✅' if s['status'] == 'success' else '⚠️'
            logger.info(f"{status_emoji} {s['learning_area']}: {s['count']} statements")
        
    finally:
        scraper.cleanup()


if __name__ == "__main__":
    main()

