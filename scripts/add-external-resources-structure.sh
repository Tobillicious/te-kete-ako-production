#!/bin/bash
# Add External Resources Structure to Lessons
# Kaiārahi Hoahoa - Supporting Content Enrichment
# Creates professional structure for Whakaū/Ako to fill with content

echo "📚 Adding External Resources Structure to Lessons"
echo "================================================"

add_resources_section() {
    local file="$1"
    local topic="$2"
    
    # Check if already has external resources
    if grep -q "external-resources" "$file"; then
        echo "  ⏭️  Already has external resources: $(basename $file)"
        return
    fi
    
    # Backup
    cp "$file" "$file.resources-backup"
    
    # Find insertion point (before </main> or <footer>)
    if grep -q "</main>" "$file"; then
        # Insert before </main>
        sed -i.res "/^[[:space:]]*<\/main>/i\\
\\
    <!-- External Resources Section - Ready for Content Enrichment -->\\
    <section class=\"external-resources no-print\">\\
        <h2 class=\"section-title\">\\
            <span>🔗</span>\\
            <span>External Resources | Ngā Rauemi o Waho</span>\\
        </h2>\\
        \\
        <p><em>📝 Ready for enrichment: Kaitiaki Whakaū/Ako to curate NZ-specific $topic resources</em></p>\\
        \\
        <div class=\"resource-links\">\\
            <div class=\"resource-card\">\\
                <h3>📚 $topic Resources</h3>\\
                <ul>\\
                    <li><a href=\"https://www.tki.org.nz/\" target=\"_blank\" rel=\"noopener\">TKI - NZ Curriculum</a></li>\\
                    <li><em>Awaiting: Topic-specific NZ resources</em></li>\\
                </ul>\\
            </div>\\
            \\
            <div class=\"resource-card\">\\
                <h3>🌿 Cultural Context</h3>\\
                <ul>\\
                    <li><a href=\"https://teara.govt.nz/\" target=\"_blank\" rel=\"noopener\">Te Ara - Encyclopedia of NZ</a></li>\\
                    <li><em>Awaiting: Māori perspectives on $topic</em></li>\\
                </ul>\\
            </div>\\
            \\
            <div class=\"resource-card\">\\
                <h3>🎓 Teaching Resources</h3>\\
                <ul>\\
                    <li><a href=\"https://nzcer.org.nz/\" target=\"_blank\" rel=\"noopener\">NZCER - Educational Research</a></li>\\
                    <li><em>Awaiting: Teaching guides and strategies</em></li>\\
                </ul>\\
            </div>\\
            \\
            <div class=\"resource-card\">\\
                <h3>📄 Lesson Materials</h3>\\
                <ul>\\
                    <li><button onclick=\"window.print()\" class=\"btn-print\">Print Lesson Materials</button></li>\\
                </ul>\\
            </div>\\
        </div>\\
    </section>\\
" "$file"
        echo "  ✅ Added resources structure: $(basename $file)"
    fi
}

# Process Y7 Maths Algebra
for file in public/units/y7-maths-algebra/lessons/lesson-*.html; do
    [ -f "$file" ] && add_resources_section "$file" "Mathematics - Algebra"
done

# Process Y7 Science Ecosystems
for file in public/units/y7-science-ecosystems/lessons/lesson-*.html; do
    [ -f "$file" ] && add_resources_section "$file" "Science - Ecosystems"
done

echo "================================================"
echo "✅ External Resources Structure Added!"
echo "📝 Ready for content specialists to enrich with NZ resources"
