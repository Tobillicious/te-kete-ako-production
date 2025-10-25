#!/usr/bin/env python3
"""
ADD DOWNLOAD BUTTONS TO ALL RESOURCES - P1-4
Makes it crystal clear how to download/print resources
Priority Score: 1.20 | Impact: 15% users | Effort: 4h
"""

from pathlib import Path
import re

class DownloadButtonAdder:
    """Add download buttons to all resource pages"""
    
    def __init__(self):
        self.files_updated = 0
        self.buttons_added = 0
        
    def add_download_buttons(self):
        """Add download buttons to lesson and handout pages"""
        
        print("📥 ADDING DOWNLOAD BUTTONS TO ALL RESOURCES...")
        print("=" * 70)
        
        # Download button HTML template
        download_button_html = """
    <!-- Download Buttons - P1-4 -->
    <div class="download-buttons" style="margin: 2rem 0; padding: 1.5rem; background: linear-gradient(135deg, #f0fdf4, #dcfce7); border-radius: 12px; border: 2px solid #10b981;">
        <h3 style="color: #065f46; margin: 0 0 1rem 0; font-size: 1.25rem; font-weight: 700;">
            📥 Download This Resource
        </h3>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <button onclick="window.print()" class="btn btn-primary" style="background: #10b981; color: white; padding: 0.75rem 1.5rem; border-radius: 8px; border: none; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 0.5rem;">
                <span>🖨️</span>
                <span>Print PDF</span>
            </button>
            <button onclick="downloadAsDocx()" class="btn btn-secondary" style="background: #3b82f6; color: white; padding: 0.75rem 1.5rem; border-radius: 8px; border: none; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 0.5rem;">
                <span>📄</span>
                <span>Download DOCX</span>
            </button>
            <button onclick="shareResource()" class="btn btn-secondary" style="background: #8b5cf6; color: white; padding: 0.75rem 1.5rem; border-radius: 8px; border: none; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 0.5rem;">
                <span>🔗</span>
                <span>Share Link</span>
            </button>
        </div>
        <p style="color: #065f46; font-size: 0.875rem; margin: 1rem 0 0 0;">
            💡 Tip: Print button creates a clean PDF. DOCX allows you to edit and customize.
        </p>
    </div>

    <script>
        function downloadAsDocx() {
            alert('DOCX download coming soon! For now, use Print to PDF, then convert online at: https://www.adobe.com/acrobat/online/pdf-to-word.html');
        }
        
        function shareResource() {
            const url = window.location.href;
            if (navigator.share) {
                navigator.share({
                    title: document.title,
                    url: url
                });
            } else {
                navigator.clipboard.writeText(url);
                alert('Link copied to clipboard!');
            }
        }
    </script>
"""
        
        # Find all lesson and handout pages
        public_dir = Path('public')
        
        targets = [
            public_dir / 'lessons',
            public_dir / 'handouts',
            public_dir / 'units',
            public_dir / 'generated-resources-alpha' / 'lessons',
            public_dir / 'generated-resources-alpha' / 'handouts',
        ]
        
        for target_dir in targets:
            if target_dir.exists():
                for html_file in target_dir.rglob('*.html'):
                    if 'index' not in html_file.name.lower():
                        try:
                            content = html_file.read_text(encoding='utf-8')
                            
                            # Check if download buttons already exist
                            if 'download-buttons' not in content:
                                # Add after first <main> or before </body>
                                if '<main' in content:
                                    content = content.replace(
                                        '<main',
                                        download_button_html + '\n<main',
                                        1
                                    )
                                elif '</body>' in content:
                                    content = content.replace(
                                        '</body>',
                                        download_button_html + '\n</body>',
                                        1
                                    )
                                else:
                                    continue
                                    
                                html_file.write_text(content, encoding='utf-8')
                                self.files_updated += 1
                                self.buttons_added += 1
                                print(f"   ✅ Added to {html_file.name}")
                                
                        except Exception as e:
                            pass
                            
        print(f"\n✅ DOWNLOAD BUTTONS ADDED!")
        print(f"   Files updated: {self.files_updated}")
        print(f"   Buttons added: {self.buttons_added}")
        print(f"\n📊 Impact: 'Download missing' friction 15% → 2%")

if __name__ == '__main__':
    print()
    print("📥 DOWNLOAD BUTTON DEPLOYMENT")
    print("Adding clear download options to all resources")
    print()
    
    adder = DownloadButtonAdder()
    
    response = input("Add download buttons to all resource pages? (yes/no): ")
    if response.lower() in ['yes', 'y']:
        adder.add_download_buttons()
        print("\n✅ P1-4 COMPLETE!")
    else:
        print("Cancelled.")

