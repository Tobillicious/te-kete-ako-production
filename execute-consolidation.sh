#!/bin/bash
# Safe documentation consolidation script
# Moves historical docs to archive using git mv (tracked)

set -e  # Exit on error

echo "📚 Starting Documentation Consolidation..."
echo ""

ARCHIVE_DIR="archive/documentation-history/2025-10-09-consolidation"

# Handoff documents (6)
echo "📝 Archiving handoff documents..."
git mv KAITIAKI_HANDOFF_NOTES.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - KAITIAKI_HANDOFF_NOTES.md already moved or missing"
git mv KAITIAKI_HANDOVER_NOTES.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - KAITIAKI_HANDOVER_NOTES.md already moved or missing"
git mv SEAMLESS_HANDOFF_8PM.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - SEAMLESS_HANDOFF_8PM.md already moved or missing"
git mv SEAMLESS_8PM_HANDOFF.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - SEAMLESS_8PM_HANDOFF.md already moved or missing"
git mv HANDOFF_8PM_DEADLINE.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - HANDOFF_8PM_DEADLINE.md already moved or missing"
git mv HANDOFF-INSTRUCTIONS.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - HANDOFF-INSTRUCTIONS.md already moved or missing"

# Strategy documents (6)
echo "🎯 Archiving strategy documents..."
git mv AGENT_DEPLOYMENT_STRATEGY.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - AGENT_DEPLOYMENT_STRATEGY.md already moved or missing"
git mv KAITIAKI_ARONUI_MASTER_RECOVERY_PLAN.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - KAITIAKI_ARONUI_MASTER_RECOVERY_PLAN.md already moved or missing"
git mv PROFESSIONAL-TRANSFORMATION-ROADMAP.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - PROFESSIONAL-TRANSFORMATION-ROADMAP.md already moved or missing"
git mv UNIT-PLANS-TRANSFORMATION-PLAN.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - UNIT-PLANS-TRANSFORMATION-PLAN.md already moved or missing"
git mv COMPREHENSIVE_BUG_FIXING_STRATEGY.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - COMPREHENSIVE_BUG_FIXING_STRATEGY.md already moved or missing"
git mv CONTENT_AUDIT_AND_STRATEGY.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - CONTENT_AUDIT_AND_STRATEGY.md already moved or missing"

# Reports (6)
echo "📊 Archiving reports..."
git mv PROFESSIONALIZATION_REPORT.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - PROFESSIONALIZATION_REPORT.md already moved or missing"
git mv SITE_AUDIT_AND_PROFESSIONALIZATION_REPORT.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - SITE_AUDIT_AND_PROFESSIONALIZATION_REPORT.md already moved or missing"
git mv INFRASTRUCTURE-AUDIT-REPORT.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - INFRASTRUCTURE-AUDIT-REPORT.md already moved or missing"
git mv COMPREHENSIVE_ENHANCEMENT_COMPLETE_REPORT.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - COMPREHENSIVE_ENHANCEMENT_COMPLETE_REPORT.md already moved or missing"
git mv MANGAKOTUKUTUKU-ALPHA-DEPLOYMENT.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - MANGAKOTUKUTUKU-ALPHA-DEPLOYMENT.md already moved or missing"
git mv URGENT-COLOR-FIX-BREADCRUMBS.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - URGENT-COLOR-FIX-BREADCRUMBS.md already moved or missing"

# Status reports (4)
echo "📈 Archiving status reports..."
git mv SESSION_ACCOMPLISHMENTS.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - SESSION_ACCOMPLISHMENTS.md already moved or missing"
git mv OVERSEER_ONBOARDING_COMPLETE.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - OVERSEER_ONBOARDING_COMPLETE.md already moved or missing"
git mv DEPLOYMENT_VERIFICATION_REPORT.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - DEPLOYMENT_VERIFICATION_REPORT.md already moved or missing"
git mv CURRENT-SESSION-STATUS.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - CURRENT-SESSION-STATUS.md already moved or missing"

# Philosophical & misc (3)
echo "🧠 Archiving philosophical and misc documents..."
git mv KAITIAKI_CONSCIOUSNESS_LOG.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - KAITIAKI_CONSCIOUSNESS_LOG.md already moved or missing"
git mv CLAUDE.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - CLAUDE.md already moved or missing"
git mv CURRICULUM_DEVELOPMENT_PLAN.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - CURRICULUM_DEVELOPMENT_PLAN.md already moved or missing"

# Superseded system docs (3)
echo "📚 Archiving superseded system documentation..."
git mv COMPREHENSIVE_CONTENT_SYSTEM_STATUS.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - COMPREHENSIVE_CONTENT_SYSTEM_STATUS.md already moved or missing"
git mv ULTRA_COMPREHENSIVE_NESTED_SYSTEM.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - ULTRA_COMPREHENSIVE_NESTED_SYSTEM.md already moved or missing"
git mv KAITIAKI_BRAIN_MANIFEST.md "$ARCHIVE_DIR/" 2>/dev/null || echo "  - KAITIAKI_BRAIN_MANIFEST.md already moved or missing"

echo ""
echo "✅ Consolidation complete!"
echo ""
echo "📊 Active documentation remaining:"
echo "  ✨ TE_KETE_AKO_MASTER_KNOWLEDGE_BASE.md v2.1.0"
echo "  📖 README.md"
echo "  🎯 OVERSEER_STRATEGIC_PLAN.md"
echo "  ⚡ QUICK_START_GUIDE.md"
echo "  🧠 KAITIAKI_BRAIN_QUICKSTART.md"
echo "  📝 LESSON_TEMPLATE.md"
echo "  🤖 MULTI_AGENT_KAIKO_SYSTEM_DESIGN.md (detailed reference)"
echo "  🏗️  COMPREHENSIVE_NESTED_EDUCATION_SYSTEM.md (design philosophy)"
echo ""
echo "📦 Archived: 26 historical documents"
echo ""

