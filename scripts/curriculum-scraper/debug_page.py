"""
Debug script - Save page HTML to inspect structure
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from pathlib import Path

# Setup driver
chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Fetch Phase 1 page
    url = "https://newzealandcurriculum.tahurangi.education.govt.nz/new-zealand-curriculum-online/nzc---english-years-0---3/5637292337.p"
    print(f"Fetching: {url}")
    driver.get(url)
    time.sleep(5)
    
    # Save HTML
    html = driver.page_source
    output_file = Path("debug_phase1.html")
    output_file.write_text(html, encoding='utf-8')
    print(f"✓ Saved HTML to {output_file} ({len(html)} bytes)")
    
    # Quick analysis
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    
    # Find all h2 headings
    headings = soup.find_all(['h2', 'h3'])
    print(f"\nFound {len(headings)} headings:")
    for h in headings[:10]:
        print(f"  - {h.get_text(strip=True)}")
    
    # Find all tables
    tables = soup.find_all('table')
    print(f"\nFound {len(tables)} tables")
    
    # Check first table
    if tables:
        print(f"\nFirst table preview:")
        rows = tables[0].find_all('tr')[:3]
        for row in rows:
            cells = row.find_all(['td', 'th'])
            cell_texts = [c.get_text(strip=True)[:50] for c in cells]
            print(f"  Row: {cell_texts}")

finally:
    driver.quit()

