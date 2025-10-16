#!/bin/bash
# KNOWLEDGE BASE QUERY HELPER
# Quick access to synthesized knowledge from archived MD files

SUPABASE_URL="https://nlgldaqtubrlcqddppbq.supabase.co"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🧠 TE KETE AKO KNOWLEDGE BASE QUERY HELPER${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

show_help() {
    echo "Usage: ./scripts/query-knowledge.sh [OPTION]"
    echo ""
    echo "Options:"
    echo "  all              Show all archived knowledge"
    echo "  architecture     Show architecture decisions"
    echo "  best-practices   Show best practices & guidelines"
    echo "  issues           Show issues & solutions"
    echo "  stats            Show knowledge statistics"
    echo "  search <term>    Search for specific term in knowledge"
    echo "  help             Show this help message"
    echo ""
}

query_all() {
    echo -e "${GREEN}📚 ALL ARCHIVED KNOWLEDGE:${NC}"
    echo ""
    psql "$SUPABASE_URL" -c "
        SELECT 
            doc_type,
            array_length(key_insights, 1) as insights,
            array_length(agents_involved, 1) as agents,
            created_at::date as date
        FROM agent_knowledge
        WHERE source_type = 'md-archive-synthesis'
        ORDER BY doc_type;
    "
}

query_architecture() {
    echo -e "${GREEN}🏗️  ARCHITECTURE DECISIONS:${NC}"
    echo ""
    psql "$SUPABASE_URL" -c "
        SELECT 
            unnest(key_insights) as insight
        FROM agent_knowledge
        WHERE source_type = 'md-archive-synthesis'
        AND doc_type = 'architecture-knowledge';
    "
}

query_best_practices() {
    echo -e "${GREEN}✅ BEST PRACTICES & GUIDELINES:${NC}"
    echo ""
    psql "$SUPABASE_URL" -c "
        SELECT 
            unnest(key_insights) as practice
        FROM agent_knowledge
        WHERE source_type = 'md-archive-synthesis'
        AND doc_type = 'best-practices-knowledge';
    "
}

query_issues() {
    echo -e "${GREEN}🔧 ISSUES & SOLUTIONS:${NC}"
    echo ""
    psql "$SUPABASE_URL" -c "
        SELECT 
            unnest(key_insights) as issue_solution
        FROM agent_knowledge
        WHERE source_type = 'md-archive-synthesis'
        AND doc_type = 'issues-solutions-knowledge';
    "
}

query_stats() {
    echo -e "${GREEN}📊 KNOWLEDGE STATISTICS:${NC}"
    echo ""
    psql "$SUPABASE_URL" -c "
        SELECT 
            COUNT(*) as total_entries,
            SUM(array_length(key_insights, 1)) as total_insights,
            (SELECT technical_details->>'files_archived' 
             FROM agent_knowledge 
             WHERE source_type = 'md-archive-synthesis' 
             LIMIT 1) as files_archived,
            (SELECT technical_details->>'files_with_knowledge' 
             FROM agent_knowledge 
             WHERE source_type = 'md-archive-synthesis' 
             LIMIT 1) as files_with_knowledge
        FROM agent_knowledge
        WHERE source_type = 'md-archive-synthesis';
    "
}

# Main execution
case "$1" in
    all)
        query_all
        ;;
    architecture)
        query_architecture
        ;;
    best-practices)
        query_best_practices
        ;;
    issues)
        query_issues
        ;;
    stats)
        query_stats
        ;;
    help|"")
        show_help
        ;;
    *)
        echo -e "${YELLOW}Unknown option: $1${NC}"
        echo ""
        show_help
        exit 1
        ;;
esac

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

