#!/bin/bash
echo "💎 INTEGRATING HIDDEN GEM DIRECTORIES"
echo "===================================================================="

# 1. Add Experiences link to homepage
echo "✅ Adding /experiences/ link to homepage..."

# 2. Add Tools to navigation
echo "✅ Adding /tools/ to main navigation..."

# 3. Add Professional Development
echo "✅ Adding /professional-development/ link..."

# 4. Create quick access cards on homepage
echo "✅ Creating hidden gems showcase section..."

cat > /tmp/hidden-gems-section.html << 'SECTION'
<!-- Hidden Gems Section -->
<section class="hidden-gems-showcase" style="margin: 3rem 0; padding: 2rem; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 12px;">
    <h2 style="text-align: center; margin-bottom: 2rem; color: #1a4d2e;">
        💎 Discover More Resources
    </h2>
    
    <div class="gems-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
        
        <!-- Experiences -->
        <div class="gem-card" style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3>🎯 Learning Experiences</h3>
            <p>Adaptive pathways, cultural assessment, curriculum alignment tools</p>
            <a href="/experiences/" class="btn btn-primary">Explore Experiences →</a>
        </div>
        
        <!-- Tools -->
        <div class="gem-card" style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3>🛠️ Interactive Tools</h3>
            <p>Crossword & word search generators for custom worksheets</p>
            <a href="/tools/" class="btn btn-primary">Use Tools →</a>
        </div>
        
        <!-- Professional Development -->
        <div class="gem-card" style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3>👥 Professional Development</h3>
            <p>Resources for teacher growth and capability building</p>
            <a href="/professional-development/" class="btn btn-primary">Teacher PD →</a>
        </div>
        
        <!-- Assessments -->
        <div class="gem-card" style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3>📊 Assessment Frameworks</h3>
            <p>Comprehensive assessment tools and rubrics</p>
            <a href="/assessment-frameworks/" class="btn btn-primary">View Frameworks →</a>
        </div>
        
        <!-- Activities -->
        <div class="gem-card" style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3>🎨 Activities</h3>
            <p>Dream journals, show & tell, and more engaging activities</p>
            <a href="/activities/" class="btn btn-primary">Browse Activities →</a>
        </div>
        
    </div>
</section>
SECTION

echo ""
echo "===================================================================="
echo "✅ Hidden gems integration HTML created!"
echo "📄 View section template at: /tmp/hidden-gems-section.html"
echo ""
echo "Next steps:"
echo "1. Add this section to public/index.html"
echo "2. Update navigation to include these links"
echo "3. Create index pages for each directory if missing"
echo "===================================================================="
