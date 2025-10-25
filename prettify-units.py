#!/usr/bin/env python3
"""Prettify the minified units/index.html file to make it readable."""

from bs4 import BeautifulSoup

# Read the minified HTML
with open('public/units/index.html', 'r', encoding='utf-8') as f:
    minified_html = f.read()

# Parse and prettify
soup = BeautifulSoup(minified_html, 'html.parser')
prettified = soup.prettify()

# Write formatted version
with open('public/units/index-formatted.html', 'w', encoding='utf-8') as f:
    f.write(prettified)

print(f"✅ Formatted HTML ({len(prettified):,} chars)")
print(f"   Original: {len(minified_html):,} chars")
print(f"   Saved to: public/units/index-formatted.html")

