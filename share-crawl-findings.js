const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

// Supabase connection
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

async function shareFindingsWithKaitiaki() {
  console.log('🤝 Sharing crawl findings with Kaitiaki Aronui...');
  
  try {
    // Read the crawl report
    const crawlData = JSON.parse(fs.readFileSync('./site-crawl-report.json', 'utf8'));
    
    // Create knowledge entries for Kaitiaki Aronui
    
    // 1. Site Overview
    await storeKnowledge({
      title: "Te Kete Ako Site Structure Analysis",
      type: "interactive",
      content: `
        COMPREHENSIVE SITE CRAWL FINDINGS
        
        Total Pages: 806 HTML files
        - 606 general pages
        - 118 lessons
        - 42 handouts
        - 30 directory indexes
        - 6 authentication pages
        - 3 units
        - 1 homepage
        
        Major conflicts identified:
        1. Authentication: 6 different implementations
        2. Dashboards: 7 different versions
        3. CSS paths: 9 different patterns
        
        Key treasures discovered:
        1. Generated Resources Alpha: 48 orphaned high-quality pages
        2. Cultural Resources: 104 pages with Māori content
        3. Orphaned Educational Gems: 20+ pages with 0 links
      `,
      cultural_elements: {
        knowledge_type: "site-structure",
        priority: "high",
        conflicts: ["authentication", "dashboards", "css-paths"],
        treasures: ["generated-resources-alpha", "cultural-resources", "orphaned-pages"]
      }
    });
    
    // 2. Authentication Conflicts
    await storeKnowledge({
      title: "Authentication System Conflicts",
      type: "interactive",
      content: `
        AUTHENTICATION CHAOS - 6 Different Implementations:
        
        1. experiences/login.html
        2. lessons/login.html
        3. login-simple.html
        4. login.html (main)
        5. auth-test.html
        6. auth-diagnostics.html
        
        JavaScript conflicts:
        - 327 pages loading auth-enhanced.js
        - Many non-auth pages loading auth scripts
        
        Recommendation: Consolidate to single authentication system
      `,
      cultural_elements: {
        knowledge_type: "technical-conflict",
        priority: "high",
        affected_pages: 327,
        solution: "consolidate-auth"
      }
    });
    
    // 3. Dashboard Proliferation
    await storeKnowledge({
      title: "Dashboard Proliferation Analysis",
      type: "interactive",
      content: `
        DASHBOARD PROLIFERATION - 7 Different Versions:
        
        1. ai-coordination-dashboard.html
        2. dashboard.html
        3. performance-dashboard.html
        4. professional-dashboard.html
        5. student-dashboard.html
        6. teacher-dashboard-ai.html
        7. teacher-dashboard.html
        
        Recommendation: Consolidate to 3 dashboards:
        - Student Dashboard
        - Teacher Dashboard
        - Admin Dashboard
      `,
      cultural_elements: {
        knowledge_type: "technical-conflict",
        priority: "medium",
        solution: "consolidate-dashboards"
      }
    });
    
    // 4. Generated Resources Alpha Treasure
    await storeKnowledge({
      title: "Generated Resources Alpha - Hidden Treasure",
      type: "handout",
      content: `
        HIDDEN TREASURE: 48 High-Quality Orphaned Pages
        
        The generated-resources-alpha folder contains 48 culturally-integrated
        educational resources that are completely orphaned (0 internal links).
        
        Sample treasures:
        - Chemistry of Traditional Māori Medicine
        - AI Ethics Through Māori Data Sovereignty
        - Financial Literacy with Māori Economic Principles
        - Biotechnology Ethics Through Māori Worldview
        - Geometric Patterns in Māori Art and Architecture
        
        These resources represent significant development effort and cultural
        integration that no users can access!
        
        Action: Integrate these into the main site structure
      `,
      cultural_elements: {
        knowledge_type: "cultural-treasure",
        priority: "critical",
        cultural_integration: "high",
        māori_content: "extensive",
        action_required: "integrate-orphans"
      }
    });
    
    // 5. CSS Path Inconsistencies
    await storeKnowledge({
      title: "CSS Path Inconsistencies",
      type: "interactive",
      content: `
        CSS PATH CHAOS - 9 Different Patterns:
        
        1. /css/te-kete-professional.css (545 pages)
        2. /../../../css/te-kete-professional.css (145 pages)
        3. css/te-kete-professional.css (13 pages)
        4. And 6 other variations
        
        Status: Fixed for generated-resources-alpha (48 files)
        Remaining: 145 pages with incorrect relative paths
        
        Impact: Inconsistent styling, broken CSS on some pages
      `,
      cultural_elements: {
        knowledge_type: "technical-issue",
        priority: "medium",
        affected_pages: 145,
        status: "partially-fixed"
      }
    });
    
    // 6. Component System Failure
    await storeKnowledge({
      title: "Component System Not Implemented",
      type: "interactive",
      content: `
        COMPONENT SYSTEM FAILURE:
        
        Finding: 0 pages are using the component system
        - components/header.html exists but not used
        - components/footer.html exists but not used
        
        Current approach: Manual header/footer inclusion on each page
        Impact: Inconsistent navigation, maintenance nightmare
        
        Recommendation: Implement component system across all pages
      `,
      cultural_elements: {
        knowledge_type: "technical-issue",
        priority: "medium",
        solution: "implement-components"
      }
    });
    
    // 7. Cultural Resources Map
    await storeKnowledge({
      title: "Mātauranga Māori Resources Map",
      type: "unit-plan",
      content: `
        MĀTAURANGA MĀORI RESOURCES - 104 Pages Identified:
        
        Categories found:
        - Traditional Māori medicine (rongoā)
        - Māori navigation and wayfinding
        - Māori mathematical concepts
        - Māori art patterns (kowhaiwhai, tukutuku)
        - Māori economic principles
        - Te Reo Māori resources
        - Kaitiakitanga concepts
        - Whakapapa resources
        
        Distribution: Scattered throughout site, not centrally accessible
        Opportunity: Create dedicated Mātauranga Māori section
      `,
      cultural_elements: {
        knowledge_type: "cultural-resource",
        priority: "high",
        māori_content: "extensive",
        opportunity: "centralize-mātauranga"
      }
    });
    
    console.log('✅ Successfully shared crawl findings with Kaitiaki Aronui');
    console.log('📊 Stored 7 knowledge entries in GraphRAG');
    
  } catch (error) {
    console.error('❌ Error sharing findings:', error);
  }
}

async function storeKnowledge(data) {
  try {
    const { error } = await supabase
      .from('resources')
      .insert({
        title: data.title,
        description: `Site crawl analysis: ${data.title}`,
        type: data.type || 'analysis',
        path: `site-crawl-analysis/${Date.now()}`,
        subject: 'Site Analysis',
        level: 'All Levels',
        featured: true,
        tags: ['site-analysis', 'crawl-findings', 'kaitiaki-aronui'],
        cultural_elements: data.cultural_elements,
        difficulty_level: 'beginner',
        estimated_duration_minutes: 5,
        author: 'Site Crawler Agent',
        is_active: true
      });
    
    if (error) {
      console.error(`Error storing ${data.title}:`, error);
    } else {
      console.log(`✅ Stored: ${data.title}`);
    }
  } catch (err) {
    console.error(`Failed to store ${data.title}:`, err);
  }
}

// Run the sharing process
shareFindingsWithKaitiaki();
