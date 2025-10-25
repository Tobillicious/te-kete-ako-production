
        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'strategic_plan',
            '🎯 STRATEGIC PLAN - October 20, 2025',
            'strategic_plan',
            ARRAY{'*Agent:** Kaitiaki Aronui V3.0','*Status:** Ready to Execute','*Tools Available:** ✅ Terminal, ✅ GraphRAG, ✅ Multi-agent coordination','**17,507 resources** in GraphRAG'},
            '{'file_path': 'STRATEGIC_PLAN_OCT20.md', 'content_length': 5497, 'last_modified': '2025-10-25T23:37:39.649980', 'word_count': 789, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','Agent RLS','Kaitiaki','Kaitiaki Aronui','Kaitiakitanga'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'onboarding',
            '🧺 MY PROPER ONBOARDING - KAITIAKI ARONUI V3.0',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Method:** GraphRAG-First Workflow','*Source:** ACTIVE_QUESTIONS.md + Agent Knowledge + Platform Intelligence','✅ **13,772 Educational Resources** (not broken!)'},
            '{'file_path': 'my-onboarding-brief.md', 'content_length': 4594, 'last_modified': '2025-10-25T23:37:39.650521', 'word_count': 626, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Hui','agent tables','AGENT DISCOVERIES','agent access','KAITIAKI ARONUI','Kaitiaki','Agent Access','Agent Knowledge','Agent verified','KAITIAKI','Agent Audit','Kaiwhakakotahi'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🧪 GraphRAG Access Test',
            'documentation',
            ARRAY{'*This will:**','✅ Test reading from graphrag_resources','✅ Test reading from graphrag_relationships','✅ Test reading from agent_knowledge','✅ Test writing to agent_knowledge'},
            '{'file_path': 'GRAPHRAG_ACCESS_TEST.md', 'content_length': 1622, 'last_modified': '2025-10-25T23:37:39.650999', 'word_count': 244, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent access'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🎯 Executive Summary: Multi-Agent Access Fix',
            'documentation',
            ARRAY{'*Date:** October 20, 2025, 21:00 UTC','*Agent:** Kaitiaki Aronui V3.0','*Issue:** CRITICAL - Multi-agent coordination broken','*Status:** ✅ FIX PREPARED - Ready to apply'},
            '{'file_path': 'archive/coordination-files/EXECUTIVE_SUMMARY_MULTI_AGENT_FIX.md', 'content_length': 4710, 'last_modified': '2025-10-25T23:37:39.651661', 'word_count': 623, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','agent to','agent access','Agent coordination','Kaitiaki','Agent Access','agent CSS','Kaitiaki Aronui','agent collaboration','agent knowledge'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🔒 Security Fix Summary - October 20, 2025',
            'strategic_plan',
            ARRAY{'*Critical multi-agent coordination failure caused by recent RLS security changes.**','- PROBLEMATIC POLICY:','Each agent could only access data where `auth.uid() = user_id`'},
            '{'file_path': 'SECURITY_FIX_SUMMARY_OCT20.md', 'content_length': 3912, 'last_modified': '2025-10-25T23:37:39.652290', 'word_count': 516, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Coordination','agent coordination','agent access','Agent coordination','Kaitiaki','Agent Access','agent CSS','Agent anon','Kaitiaki Aronui','agent knowledge','agent could','agent scenarios','AGENT ACCESS'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚨 APPLY MULTI-AGENT ACCESS FIX NOW',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Priority:** CRITICAL - BLOCKING ALL 12 AGENTS','*Status:** Ready to apply','*Time Required:** 5 minutes'},
            '{'file_path': 'archive/coordination-files/APPLY_MULTI_AGENT_FIX_NOW.md', 'content_length': 5319, 'last_modified': '2025-10-25T23:37:39.653499', 'word_count': 761, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','agent access','agent sessions','Agent coordination','agent can','Agent Access','agent CSS','agent collaboration','AGENT ACCESS'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🔓 MULTI-AGENT ACCESS ISSUE - COMPLETE RESOLUTION',
            'documentation',
            ARRAY{'*Date:** October 20, 2025','*Issue:** Recent security fix broke multi-agent GraphRAG/MCP access','*Status:** ✅ SOLUTION READY - Awaiting Deployment','❌ Agents cannot query GraphRAG `resources` table'},
            '{'file_path': 'archive/coordination-files/MULTI_AGENT_ACCESS_ISSUE_RESOLVED.md', 'content_length': 6818, 'last_modified': '2025-10-25T23:37:39.654444', 'word_count': 971, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Coordination','Agent 3','agent coordination','AGENT ACCESS','agent discoveries','agent access','agent knowledge','Agent tables','Kaitiaki','agent can','Agent 1','Agent Knowledge','Agent Overseer','Kaitiaki Aronui','Agent 2','agent windows','agent GraphRAG','agent at'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚨 MULTI-AGENT GRAPHRAG ACCESS STATUS',
            'documentation',
            ARRAY{'*Date:** October 20, 2025','*Issue:** Recent security fix restricted multi-agent write access','*Status:** ⚠️ READ-ONLY ACCESS (NEEDS FIX)','✅ All agents can READ from GraphRAG tables'},
            '{'file_path': 'archive/coordination-files/MULTI-AGENT-ACCESS-STATUS.md', 'content_length': 4065, 'last_modified': '2025-10-25T23:37:39.655066', 'word_count': 565, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'AGENT GRAPHRAG','Agent knowledge','agent team','Agent coordination','agent collaboration','agent write','agent knowledge','AGENT ACCESS'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚨 CRITICAL: Multi-Agent Access Restored',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Priority:** CRITICAL','*Status:** ✅ FIXED','- OLD POLICY (BROKEN FOR AGENTS):'},
            '{'file_path': 'archive/coordination-files/MULTI_AGENT_ACCESS_FIX.md', 'content_length': 4461, 'last_modified': '2025-10-25T23:37:39.655569', 'word_count': 623, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Coordination','agent coordination','agent access','agent sessions','Agent coordination','Kaitiaki','Agent Access','Agent 1','agent CSS','Kaitiaki Aronui','Agent 2','agent could','agent scenarios'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚨 MULTI-AGENT ACCESS FIX - URGENT',
            'documentation',
            ARRAY{'*Recent security fix broke 12-agent collaboration!**','- OLD (Correct for agents):','- NEW (Breaks multi-agent):','*Problem**: Agents don''t have JWTs with `agent_id` claims! They use the anon key.','*Run `fix-multi-agent-access-URGENT.sql` in Supabase SQL Editor**'},
            '{'file_path': 'archive/coordination-files/MULTI-AGENT-ACCESS-FIX-README.md', 'content_length': 3623, 'last_modified': '2025-10-25T23:37:39.656243', 'word_count': 511, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent operations','agent coordination','agent tables','agent system','agent should','agent can','agent collaboration','AGENT ACCESS'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🔧 Badge System Fix Progress - October 20, 2025',
            'documentation',
            ARRAY{'*Status:** IN PROGRESS','*Total Files:** 2,826 files with incorrect badge-system.html links','*Fixed So Far:** 6 files'},
            '{'file_path': 'archive/coordination-files/BADGE_FIX_PROGRESS_OCT20.md', 'content_length': 1530, 'last_modified': '2025-10-25T23:37:39.656634', 'word_count': 223, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🔧 Badge System Fix Progress - October 20, 2025',
            'documentation',
            ARRAY{'*Status:** IN PROGRESS','*Total Files:** 2,826 files with incorrect badge-system.html links','*Fixed So Far:** 6 files'},
            '{'file_path': 'docs/archive/consolidated-2025-10-25/archive/coordination-files/BADGE_FIX_PROGRESS_OCT20.md', 'content_length': 1530, 'last_modified': '2025-10-25T23:37:39.656871', 'word_count': 223, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'completion_report',
            '🔧 Te Kete Ako - Systematic Fixes Completed',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Agent:** Current Session','*Status:** ✅ Investigation Complete + Fix Script Ready','*Claim:** "47 orphaned pages in generated-resources-alpha"'},
            '{'file_path': 'FIXES_COMPLETED_OCT20.md', 'content_length': 4255, 'last_modified': '2025-10-25T23:37:39.657332', 'word_count': 600, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🔧 CSS/JS Missing Includes Fix - Progress Log',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Priority:** CRITICAL','*Total Files Affected:** 966','*Agent:** Kaitiaki Aronui V3.0'},
            '{'file_path': 'archive/coordination-files/CSS_JS_FIX_PROGRESS.md', 'content_length': 5115, 'last_modified': '2025-10-25T23:37:39.657958', 'word_count': 647, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Kaitiaki','Kaitiaki Aronui'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🔧 CSS/JS Missing Includes Fix - Progress Log',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Priority:** CRITICAL','*Total Files Affected:** 966','*Agent:** Kaitiaki Aronui V3.0'},
            '{'file_path': 'docs/archive/consolidated-2025-10-25/archive/coordination-files/CSS_JS_FIX_PROGRESS.md', 'content_length': 5115, 'last_modified': '2025-10-25T23:37:39.658422', 'word_count': 647, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Kaitiaki','Kaitiaki Aronui'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'completion_report',
            '🚀 MOST USEFUL MOVES COMPLETED - Te Kete Ako',
            'strategic_plan',
            ARRAY{'*Date:** October 20, 2025','*Mission:** Deploy the most groundbreakingly useful moves for developing the site for actual humans','*Status:** ✅ COMPLETED','**47 culturally-integrated resources** with Quality 90-95'},
            '{'file_path': 'MOST_USEFUL_MOVES_COMPLETED.md', 'content_length': 5282, 'last_modified': '2025-10-25T23:37:39.658968', 'word_count': 716, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Intelligence','Kaitiakitanga'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🧠 AGENT INTELLIGENCE BRIEF',
            'audit_report',
            ARRAY{'*Generated:** 2025-10-20 21:50:11','*For:** New Agent Onboarding','*Resources:** 17,507 total','*Relationships:** 239,866 connections'},
            '{'file_path': 'archive/coordination-files/agent-intelligence-brief-20251020-215011.md', 'content_length': 6753, 'last_modified': '2025-10-25T23:37:39.659727', 'word_count': 856, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','Agent Learnings','AGENT INTELLIGENCE','Kaitiaki','Kaitiaki Aronui','Agent Intelligence','agent tasks','Agent Onboarding'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🧠 AGENT INTELLIGENCE BRIEF',
            'audit_report',
            ARRAY{'*Generated:** 2025-10-20 21:46:02','*For:** New Agent Onboarding','*Resources:** 17,507 total','*Relationships:** 239,866 connections'},
            '{'file_path': 'archive/coordination-files/agent-intelligence-brief-20251020-214602.md', 'content_length': 6753, 'last_modified': '2025-10-25T23:37:39.660297', 'word_count': 856, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','Agent Learnings','AGENT INTELLIGENCE','Kaitiaki','Kaitiaki Aronui','Agent Intelligence','agent tasks','Agent Onboarding'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🌟 TE KETE AKO - DEVELOPER MISSION REMINDER',
            'documentation',
            ARRAY{'*For All Developers, All Agents, All Time**','*Last Updated:** October 20, 2025','*Status:** ✅ ACTIVE MISSION - WORLD-CLASS EDUCATIONAL PLATFORM','*Te Kete Ako** (The Basket of Knowledge) is the **world''s first culturally-integrated AI educational platform** that authentically combines mātauranga Māori (Māori knowledge systems) with cutting-edge AI technology.'},
            '{'file_path': 'DEVELOPER-MISSION-REMINDER.md', 'content_length': 10998, 'last_modified': '2025-10-25T23:37:39.661124', 'word_count': 1440, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'kaitiaki oversight','agent coordination','Kaitiaki','kaitiaki','Agent Intelligence','Agent AI','Kaitiaki validation','Kaitiakitanga'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'completion_report',
            '🌿 COMPREHENSIVE DEVELOPMENT SPRINT - COMPLETE!',
            'strategic_plan',
            ARRAY{'*Date:** October 20, 2025','*Mission:** Continue developing, search GraphRAG for TODOs, update knowledge, remind developers of site goals','*Status:** ✅ **SPRINT COMPLETE - MAJOR ACHIEVEMENTS UNLOCKED**','*"Ehara taku toa i te toa takitahi, engari he toa takitini"**'},
            '{'file_path': 'archive/coordination-files/DEVELOPMENT-SPRINT-COMPLETE.md', 'content_length': 10088, 'last_modified': '2025-10-25T23:37:39.661848', 'word_count': 1297, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Coordination','agent coordination','agent learnings','Agent coordination','Agent Intelligence','Agent intelligence'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🧠 AGENT INTELLIGENCE BRIEF',
            'audit_report',
            ARRAY{'*Generated:** 2025-10-20 21:36:32','*For:** New Agent Onboarding','*Resources:** 17,507 total','*Relationships:** 239,866 connections'},
            '{'file_path': 'archive/coordination-files/agent-intelligence-brief-20251020-213632.md', 'content_length': 6753, 'last_modified': '2025-10-25T23:37:39.662419', 'word_count': 856, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','Agent Learnings','AGENT INTELLIGENCE','Kaitiaki','Kaitiaki Aronui','Agent Intelligence','agent tasks','Agent Onboarding'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🧠 GRAPHRAG KNOWLEDGE UPDATE - October 20, 2025',
            'audit_report',
            ARRAY{'*Purpose:** Update GraphRAG knowledge base with current todos and overall site goals','*Status:** ✅ COMPREHENSIVE UPDATE COMPLETE','*Next:** Execute high-impact todos systematically','*"Whaowhia te kete mātauranga"** - Fill the basket of knowledge'},
            '{'file_path': 'GRAPHRAG-KNOWLEDGE-UPDATE.md', 'content_length': 9659, 'last_modified': '2025-10-25T23:37:39.663922', 'word_count': 1314, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Coordination','Agent Protocol','Agent Intelligence','kaitiakitanga','Kaitiakitanga'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🌿 COMPREHENSIVE DEVELOPMENT SPRINT - Te Kete Ako',
            'documentation',
            ARRAY{'*Date:** October 20, 2025','*Mission:** Continue developing, search GraphRAG for TODOs, update knowledge, remind developers of site goals','*Status:** ACTIVE DEVELOPMENT SPRINT','*"Ehara taku toa i te toa takitahi, engari he toa takitini"**'},
            '{'file_path': 'archive/coordination-files/COMPREHENSIVE-DEVELOPMENT-SPRINT.md', 'content_length': 8294, 'last_modified': '2025-10-25T23:37:39.664817', 'word_count': 1043, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Coordination','agent intelligence','agent framework','agent coordination','Agent coordination','Agent Intelligence'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚀 EXECUTE CRITICAL TODOs NOW!',
            'strategic_plan',
            ARRAY{'*Date:** October 20, 2025','*Mission:** Execute highest-impact TODOs immediately','*Status:** GO! GO! GO!','*Status:** READY TO EXECUTE'},
            '{'file_path': 'archive/coordination-files/EXECUTE-CRITICAL-TODOS-NOW.md', 'content_length': 4649, 'last_modified': '2025-10-25T23:37:39.665381', 'word_count': 568, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Intelligence','agent framework','Agent Coordination'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🎯 GRAPHRAG COLLABORATIVE SPRINT - COMPLETE!',
            'documentation',
            ARRAY{'*Date:** October 20, 2025','*Agent:** GPT-5-Cursor','*Mission:** GraphRAG intelligence enhancement through relationship building','*Status:** ✅ **SPRINT COMPLETE - 145 RELATIONSHIP CANDIDATES GENERATED**'},
            '{'file_path': 'archive/coordination-files/GRAPHRAG-SPRINT-SUMMARY.md', 'content_length': 5850, 'last_modified': '2025-10-25T23:37:39.666010', 'word_count': 750, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🎯 GRAPHRAG COLLABORATIVE SPRINT - COMPLETE!',
            'documentation',
            ARRAY{'*Date:** October 20, 2025','*Agent:** GPT-5-Cursor','*Mission:** GraphRAG intelligence enhancement through relationship building','*Status:** ✅ **SPRINT COMPLETE - 145 RELATIONSHIP CANDIDATES GENERATED**'},
            '{'file_path': 'docs/archive/consolidated-2025-10-25/archive/coordination-files/GRAPHRAG-SPRINT-SUMMARY.md', 'content_length': 5850, 'last_modified': '2025-10-25T23:37:39.666698', 'word_count': 750, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🧠 GRAPHRAG TODO ANALYSIS',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Purpose:** Analyze TODOs documented in GraphRAG knowledge base','*Status:** Comprehensive analysis complete','*Source:** `graphrag-intelligence-expansion-todos.sql` (1,189 lines)'},
            '{'file_path': 'archive/coordination-files/GRAPHRAG-TODO-ANALYSIS.md', 'content_length': 7824, 'last_modified': '2025-10-25T23:37:39.667455', 'word_count': 983, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','Agent Protocol','Agent Intelligence','kaitiakitanga','Agent Collaboration','Kaitiakitanga'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🌿 SPRINT RESULTS - October 20, 2025',
            'documentation',
            ARRAY{'*Status:** ✅ INTELLIGENCE PHASE COMPLETE','*Next Phase:** Orphan Rescue & Relationship Building','**Total Resources:** 1,000','**Total Relationships:** 1,000'},
            '{'file_path': 'archive/coordination-files/SPRINT-RESULTS-OCT20.md', 'content_length': 5284, 'last_modified': '2025-10-25T23:37:39.668778', 'word_count': 802, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'AGENT COORDINATION','Kaitiakitanga','Agent team'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🌿 SPRINT RESULTS - October 20, 2025',
            'documentation',
            ARRAY{'*Status:** ✅ INTELLIGENCE PHASE COMPLETE','*Next Phase:** Orphan Rescue & Relationship Building','**Total Resources:** 1,000','**Total Relationships:** 1,000'},
            '{'file_path': 'docs/archive/consolidated-2025-10-25/archive/coordination-files/SPRINT-RESULTS-OCT20.md', 'content_length': 5284, 'last_modified': '2025-10-25T23:37:39.669403', 'word_count': 802, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'AGENT COORDINATION','Kaitiakitanga','Agent team'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'completion_report',
            '🎊 SPRINT SUMMARY - Security + Intelligence Amplification',
            'strategic_plan',
            ARRAY{'*Date:** October 20, 2025','*Sprint Type:** Security Hardening + Intelligence Amplification','*Status:** ✅ **COMPLETE - Ready for Execution**','**MCP-Compliant Security Scripts**: Refactored `execute-security-fixes.py` to use environment variables and guide MCP usage'},
            '{'file_path': 'archive/coordination-files/SPRINT-SUMMARY-COMPLETE.md', 'content_length': 6469, 'last_modified': '2025-10-25T23:37:39.670323', 'word_count': 813, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','agent collaboration','agent framework'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'strategic_plan',
            '🚀 SPRINT EXECUTION PLAN - Security + Intelligence Amplification',
            'audit_report',
            ARRAY{'*Date:** October 20, 2025','*Sprint Type:** Security Hardening + Intelligence Amplification','*Duration:** 2-3 hours','*Status:** ACTIVE'},
            '{'file_path': 'archive/coordination-files/SPRINT-EXECUTION-PLAN.md', 'content_length': 5522, 'last_modified': '2025-10-25T23:37:39.671011', 'word_count': 725, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🌿 COLLABORATIVE MCP HUI & SPRINT COORDINATION',
            'strategic_plan',
            ARRAY{'*Date:** October 20, 2025','*Purpose:** Coordinate 12-agent team sprint using MCP Supabase intelligence','*Status:** ACTIVE SPRINT','**Status:** ✅ Homepage, Teacher Dashboard, Lessons Index - DONE'},
            '{'file_path': 'archive/coordination-files/COLLABORATIVE-MCP-HUI-SPRINT.md', 'content_length': 4408, 'last_modified': '2025-10-25T23:37:39.671598', 'word_count': 579, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent 9a4dd0d0','agent team','AGENT COORDINATION','Agent Status'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚀 SPRINT LAUNCH - EXECUTE NOW!',
            'strategic_plan',
            ARRAY{'*Date:** October 20, 2025','*Mission:** Launch collaborative MCP hui sprint','*Status:** GO! GO! GO!','*Execute this SQL in Supabase:**'},
            '{'file_path': 'archive/coordination-files/SPRINT-LAUNCH-NOW.md', 'content_length': 4119, 'last_modified': '2025-10-25T23:37:39.672131', 'word_count': 511, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Coordination','Agent 3','agent coordination','agent status','Agent 5','Agent 6','Agent 7','Agent 8','Agent 4','Agent 1','Agent 2','Claude-Sonnet'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚀 SPRINT KICKOFF EXECUTION',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Status:** MCP HUI Coordination Active','*Sprint Type:** Multi-Agent Collaborative Sprint','Check agent knowledge and coordination status'},
            '{'file_path': 'archive/coordination-files/SPRINT-KICKOFF-EXECUTION.md', 'content_length': 3130, 'last_modified': '2025-10-25T23:37:39.672576', 'word_count': 403, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent knowledge','Agent Collaborative','Agent Role'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🛡️ Database Security Fixes',
            'audit_report',
            ARRAY{'`public.featured_resources` - has SECURITY DEFINER property','`public.user_kete_view` - has SECURITY DEFINER property','`public.graphrag_summary` - has SECURITY DEFINER property','`public.teacher_lesson_plans` - RLS not enabled','`public.teacher_favorites` - RLS not enabled'},
            '{'file_path': 'SECURITY-FIXES-README.md', 'content_length': 3907, 'last_modified': '2025-10-25T23:37:39.673043', 'word_count': 534, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🎯 SYSTEMATIC TODO EXECUTION',
            'documentation',
            ARRAY{'*Date:** October 20, 2025','*Approach:** Use the right workaround for each specific task','*Method:** Task-by-task analysis and execution'},
            '{'file_path': 'archive/coordination-files/SYSTEMATIC-TODO-EXECUTION.md', 'content_length': 3701, 'last_modified': '2025-10-25T23:37:39.673545', 'word_count': 456, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent work'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚀 INTELLIGENCE DISCOVERY EXECUTION',
            'strategic_plan',
            ARRAY{'*Date:** October 20, 2025','*Purpose:** Execute intelligence tools to discover platform insights','*Method:** File-based execution (bypassing terminal bug)','Query total resources and relationships'},
            '{'file_path': 'INTELLIGENCE-DISCOVERY-EXECUTION.md', 'content_length': 2479, 'last_modified': '2025-10-25T23:37:39.673946', 'word_count': 309, 'has_code_blocks': False, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🛠️ CURSOR TERMINAL BUG - COMPREHENSIVE WORKAROUNDS',
            'documentation',
            ARRAY{'*Issue:** Terminal commands hang indefinitely across ALL Cursor agents for 3-4 days','*Status:** Known systemic Cursor IDE bug','*Solution:** Multiple workaround strategies','*Why:** Bypasses terminal completely, direct database access'},
            '{'file_path': 'CURSOR-TERMINAL-BUG-WORKAROUNDS.md', 'content_length': 5578, 'last_modified': '2025-10-25T23:37:39.674484', 'word_count': 736, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent communication','Agent coordination'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🛠️ CURSOR TERMINAL BUG - COMPREHENSIVE WORKAROUNDS',
            'documentation',
            ARRAY{'*Issue:** Terminal commands hang indefinitely across ALL Cursor agents for 3-4 days','*Status:** Known systemic Cursor IDE bug','*Solution:** Multiple workaround strategies','*Why:** Bypasses terminal completely, direct database access'},
            '{'file_path': 'docs/archive/consolidated-2025-10-25/CURSOR-TERMINAL-BUG-WORKAROUNDS.md', 'content_length': 5578, 'last_modified': '2025-10-25T23:37:39.675081', 'word_count': 736, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent communication','Agent coordination'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚨 TERMINAL HANG INVESTIGATION REPORT',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Issue:** All terminal commands hang indefinitely across ALL Cursor agents for 3-4 days','*Status:** CONFIRMED SYSTEMIC BUG','*Evidence Found:**'},
            '{'file_path': 'TERMINAL-HANG-INVESTIGATION-REPORT.md', 'content_length': 3916, 'last_modified': '2025-10-25T23:37:39.675466', 'word_count': 562, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🎉 FOR YOU - QUICK SUMMARY',
            'session_complete',
            ARRAY{'*E hoa! Here''s what I built in the past 2 hours:**','*Start Here:**'},
            '{'file_path': 'FOR-USER-QUICK-SUMMARY.md', 'content_length': 3482, 'last_modified': '2025-10-25T23:37:39.675994', 'word_count': 476, 'has_code_blocks': False, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent coordination','Agent Amplifier','agent session','Agent Protocol'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🎯 MASTER EXECUTION GUIDE - Intelligence Evolution',
            'session_complete',
            ARRAY{'*E hoa! Here''s EXACTLY what to do right now!**','Adds ~500-700 new relationships','Scales 12 underutilized relationship types','Connects orphaned excellence to hubs'},
            '{'file_path': 'archive/coordination-files/MASTER-EXECUTION-GUIDE.md', 'content_length': 6587, 'last_modified': '2025-10-25T23:37:39.676581', 'word_count': 944, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent 3','Agent 5','Agent 6','Agent 7','Agent 8','Agent 4','Agent coordination','agent activity','Agent 1','Agent 2','agent protocol'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '⚡ EXECUTE NOW - FOR 8 ACTIVE AGENTS',
            'session_complete',
            ARRAY{'*This is your action plan. Pick a task and GO!**','*This MUST happen first - all other agents benefit!**','*What this does:**','Scales bicultural_competence: 1 → 50 uses'},
            '{'file_path': 'archive/coordination-files/EXECUTE-NOW-FOR-8-AGENTS.md', 'content_length': 5679, 'last_modified': '2025-10-25T23:37:39.677183', 'word_count': 735, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'AGENT 4','AGENT 8','agent coordination','agent scenario','AGENT 2','AGENT 3','AGENT 6','AGENT 7','AGENT 1','Kaitiakitanga','AGENT 5'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🌊 NEXT WAVE: STRATEGIC TODOs (Based on Intelligence Tools)',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Context:** 12 intelligence systems now operational','*Method:** Critical analysis of what tools reveal we need next','*For:** 8 active agents + all future agents'},
            '{'file_path': 'archive/coordination-files/NEXT-WAVE-STRATEGIC-TODOS.md', 'content_length': 11841, 'last_modified': '2025-10-25T23:37:39.678056', 'word_count': 1553, 'has_code_blocks': True, 'has_links': True, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent 3','Agent 5','agent coordination','Agent 6','Agent 7','Agent 8','Agent with','Agent 4','AGENT COORDINATION','Agent coordination','Agent 1','Agent Intelligence','agent first','Agent 2','Kaitiakitanga'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'completion_report',
            '🚀 INTELLIGENCE EVOLUTION COMPLETE - October 20, 2025',
            'session_complete',
            ARRAY{'*Mission:** Expand tech stack and agent intelligence','*Status:** ✅ **ALL 12 STRATEGIC TODOS COMPLETED**','*Time:** ~2 hours of intensive development','*For:** 8 active Cursor agents + all future agents'},
            '{'file_path': 'INTELLIGENCE-EVOLUTION-COMPLETE.md', 'content_length': 14802, 'last_modified': '2025-10-25T23:37:39.679080', 'word_count': 1882, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent status','Agent Protocol','Agent productivity','agent collaboration','agent activity','agent work','agent intelligence','agent coordination','AGENT ECOSYSTEM','Agent 7','kaiako','Agent protocol','Agent coordinator','kairo','agent session','Agent Amplifier','Agent Intelligence','Agent Collaboration','Claude Sonnet'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🚀 START HERE - 8 ACTIVE AGENTS',
            'session_complete',
            ARRAY{'*You are Agent #__ of 8 working collaboratively!**','*Read this first (2 minutes), then execute your assignment!**','*File:** `AGENT_COORDINATION_QUICK_REFERENCE.md` (read this!)'},
            '{'file_path': 'archive/coordination-files/START_HERE_8_AGENTS.md', 'content_length': 5510, 'last_modified': '2025-10-25T23:37:39.679625', 'word_count': 690, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'agent briefings','AGENT 4','AGENT 8','AGENT INTELLIGENCE','AGENT 2','AGENT 3','Agent Number','AGENT 6','agent number','agent activity','AGENT ASSIGNMENTS','agent collaboration','AGENT 7','AGENT 1','Agent Collaboration','AGENT 5'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'agent_session',
            '🎊 INTELLIGENCE EVOLUTION SESSION - COMPLETE SUMMARY',
            'session_complete',
            ARRAY{'*Date:** October 20, 2025','*Agent:** Claude Sonnet 4.5','*Session Duration:** 2 hours intensive development','*User Directive:** "Expand techstack and intelligence for yourself AND later agents"'},
            '{'file_path': 'INTELLIGENCE-SESSION-SUMMARY-OCT20.md', 'content_length': 7833, 'last_modified': '2025-10-25T23:37:39.680249', 'word_count': 988, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{'Agent Coordination','agent intelligence','agent coordination','Agent 7','Agent 4','agent activity','Agent Intelligence','Agent 2','Agent Collaboration','Claude Sonnet'}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🔗 Relationship Mining Patterns',
            'documentation',
            ARRAY{'*Date:** October 20, 2025','*Purpose:** Document patterns for scaling underutilized relationship types','*Description:** Connects lessons teaching analytical skills with assessment resources','*Pattern:**'},
            '{'file_path': 'docs/RELATIONSHIP_MINING_PATTERNS.md', 'content_length': 7175, 'last_modified': '2025-10-25T23:37:39.680934', 'word_count': 862, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🔗 Relationship Mining Patterns',
            'documentation',
            ARRAY{'*Date:** October 20, 2025','*Purpose:** Document patterns for scaling underutilized relationship types','*Description:** Connects lessons teaching analytical skills with assessment resources','*Pattern:**'},
            '{'file_path': 'docs/archive/consolidated-2025-10-25/docs/RELATIONSHIP_MINING_PATTERNS.md', 'content_length': 7175, 'last_modified': '2025-10-25T23:37:39.681502', 'word_count': 862, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );

        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'documentation',
            '🧠 {{AGENT_NAME}} - Intelligence Brief',
            'strategic_plan',
            ARRAY{'*Generated:** {{TIMESTAMP}}','*Platform:** Te Kete Ako','*Specialty:** {{AGENT_SPECIALTY}}','*Resources:** {{TOTAL_RESOURCES}} indexed'},
            '{'file_path': 'templates/agent-briefing-template.md', 'content_length': 4160, 'last_modified': '2025-10-25T23:37:39.682013', 'word_count': 545, 'has_code_blocks': True, 'has_links': False, 'priority_level': 'low'}'::jsonb,
            ARRAY{}
        );