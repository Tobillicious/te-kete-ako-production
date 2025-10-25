#!/usr/bin/env python3
"""
UPDATE HOMEPAGE - Top 10 Starter Pack
Add curated excellence resources prominently to homepage
"""

from pathlib import Path

# Top 10 Excellence Resources (from GraphRAG query + manual curation)
TOP_10_STARTER_PACK = """
<!-- 🌟 TOP 10 STARTER PACK - Curated Excellence -->
<section class="top-10-starter-pack" style="background: linear-gradient(135deg, #1a4d2e 0%, #2d5a3d 100%); padding: 60px 20px; margin: 40px 0; border-radius: 12px;">
    <div class="container" style="max-width: 1200px; margin: 0 auto;">
        <h2 style="color: #f4d03f; font-size: 2.5em; text-align: center; margin-bottom: 20px;">
            🌟 Top 10 Starter Pack - Excellence Resources
        </h2>
        <p style="color: #ffffff; text-align: center; font-size: 1.2em; margin-bottom: 40px; max-width: 800px; margin-left: auto; margin-right: auto;">
            Begin your journey with our most culturally-integrated, pedagogically-sound resources.  
            Perfect for new teachers and experienced kaiako alike!
        </p>
        
        <div class="top-10-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
            
            <!-- 1. NZ Curriculum Science -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟🌟🌟 Excellence
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">NZ Curriculum Science Guide</h3>
                <p style="color: #555; margin: 12px 0;">Complete official NZ Curriculum for Science (Pūtaiao) with integrated mātauranga Māori</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Science</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">Year 7-8</span>
                </div>
                <a href="/curriculum-documents/science.html" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Explore Resource →
                </a>
            </div>
            
            <!-- 2. Student Dashboard -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟🌟🌟 Excellence
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">Student Dashboard</h3>
                <p style="color: #555; margin: 12px 0;">Personalized learning interface with progress tracking, cultural engagement, and My Kete</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Cross-Curricular</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">Year 7-13</span>
                </div>
                <a href="/students/dashboard.html" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Explore Resource →
                </a>
            </div>
            
            <!-- 3. Y8 Systems External Resources -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟🌟🌟 Excellence
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">Y8 Systems Unit</h3>
                <p style="color: #555; margin: 12px 0;">Comprehensive systems thinking unit with Treaty and colonisation lessons from authentic Māori sources</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Social Studies</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">Year 8</span>
                </div>
                <a href="/y8-systems/lessons/" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Explore Resource →
                </a>
            </div>
            
            <!-- 4. Health & PE Guide -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟🌟 High Quality
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">NZ Curriculum Health & PE</h3>
                <p style="color: #555; margin: 12px 0;">Te Whare Tapa Whā holistic model: tinana, hinengaro, whānau, wairua</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Health & PE</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">Year 7-8</span>
                </div>
                <a href="/curriculum-documents/health-pe.html" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Explore Resource →
                </a>
            </div>
            
            <!-- 5. Social Sciences Guide -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟🌟 High Quality
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">NZ Curriculum Social Sciences</h3>
                <p style="color: #555; margin: 12px 0;">Complete guide with tikanga Māori integration: whakapapa, manaakitanga, tika</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Social Studies</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">Year 7-8</span>
                </div>
                <a href="/curriculum-documents/social-sciences.html" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Explore Resource →
                </a>
            </div>
            
            <!-- 6. Technology Guide -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟🌟 High Quality
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">NZ Curriculum Technology</h3>
                <p style="color: #555; margin: 12px 0;">Deep integration of Māori innovation: waka technology, sustainable building, renewable energy</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Digital Tech</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">Year 7-8</span>
                </div>
                <a href="/curriculum-documents/technology.html" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Explore Resource →
                </a>
            </div>
            
            <!-- 7. Arts Guide -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟🌟 High Quality
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">NZ Curriculum Arts</h3>
                <p style="color: #555; margin: 12px 0;">Māori arts integration: whakairo (carving), raranga (weaving), kapa haka, tā moko</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Arts</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">Year 7-8</span>
                </div>
                <a href="/curriculum-documents/arts.html" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Explore Resource →
                </a>
            </div>
            
            <!-- 8. English Guide -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟🌟 High Quality
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">NZ Curriculum English</h3>
                <p style="color: #555; margin: 12px 0;">Complete guide with literacy progression framework and cultural text integration</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">English</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">Year 7-8</span>
                </div>
                <a href="/curriculum-documents/english.html" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Explore Resource →
                </a>
            </div>
            
            <!-- 9. PWA Offline Capability -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟 Good
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">Offline Learning (PWA)</h3>
                <p style="color: #555; margin: 12px 0;">Works offline in remote NZ areas! Smart caching, background sync, push notifications</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Technology</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">All Levels</span>
                </div>
                <a href="/service-worker.js" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Learn More →
                </a>
            </div>
            
            <!-- 10. PWA Manifest -->
            <div class="excellence-card" style="background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div class="badge" style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 20px; display: inline-block; font-weight: bold; margin-bottom: 12px;">
                    🌟🌟🌟 Good
                </div>
                <h3 style="color: #1a4d2e; margin: 12px 0;">Install as App (PWA)</h3>
                <p style="color: #555; margin: 12px 0;">Installable app experience with home screen, standalone display, app shortcuts</p>
                <div style="margin: 12px 0;">
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; margin-right: 8px;">Technology</span>
                    <span style="background: #e8f5e9; color: #1a4d2e; padding: 4px 8px; border-radius: 4px; font-size: 0.9em;">All Levels</span>
                </div>
                <a href="/manifest.json" style="display: inline-block; background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin-top: 12px; font-weight: bold;">
                    Learn More →
                </a>
            </div>
            
        </div>
        
        <div style="text-align: center; margin-top: 40px;">
            <p style="color: #f4d03f; font-size: 1.1em; margin-bottom: 20px;">
                ✨ These resources represent the pinnacle of cultural integration and pedagogical excellence
            </p>
            <a href="/resources" style="display: inline-block; background: #f4d03f; color: #1a4d2e; padding: 16px 32px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 1.1em;">
                Explore All 3,500+ Resources →
            </a>
        </div>
    </div>
</section>
"""

# Find homepage
homepage = Path('public/index.html')
content = homepage.read_text(encoding='utf-8')

# Insert Top 10 after main hero section (before existing content sections)
# Look for a good insertion point
if '<!-- 🌟 TOP 10 STARTER PACK' not in content:
    # Insert after hero, before features or resources section
    insertion_markers = [
        '</header>',
        '<section class="features',
        '<section class="resources',
        '<!-- Features Section -->',
    ]
    
    inserted = False
    for marker in insertion_markers:
        if marker in content:
            content = content.replace(marker, f'{marker}\n\n{TOP_10_STARTER_PACK}\n', 1)
            inserted = True
            print(f"✅ Inserted Top 10 after: {marker}")
            break
    
    if inserted:
        homepage.write_text(content, encoding='utf-8')
        print("🎊 HOMEPAGE UPDATED with Top 10 Starter Pack!")
    else:
        print("⚠️  Could not find insertion point, adding at end of body")
        content = content.replace('</body>', f'\n{TOP_10_STARTER_PACK}\n</body>')
        homepage.write_text(content, encoding='utf-8')
        print("🎊 HOMEPAGE UPDATED (added at end)!")
else:
    print("✅ Top 10 Starter Pack already present on homepage!")


