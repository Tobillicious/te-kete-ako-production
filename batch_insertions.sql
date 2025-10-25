INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'session_complete',
            'Kaitiaki Aronui V3.0 Complete Session Oct 19 2025',
            'session_summary',
            ARRAY['Platform transformation complete', 'All critical blockers resolved', 'Beta launch ready'],
            '{"file_path": "kaitiaki-aronui-session-oct19.md", "content_length": 2500, "quality_score": 95}'::jsonb,
            ARRAY['Kaitiaki Aronui V3', 'Agent Infrastructure Specialist']
        );
INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'platform_audit',
            'MASTER-PLATFORM-AUDIT-SYNTHESIS.md',
            'audit_report',
            ARRAY['Site is 85-90% functional', 'GraphRAG has 740 pages in /public/', 'Critical missing CSS includes'],
            '{"file_path": "MASTER-PLATFORM-AUDIT-SYNTHESIS.md", "content_length": 5000, "quality_score": 98}'::jsonb,
            ARRAY['Kaitiaki Aronui V3', 'All Agents']
        );
INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            'deployment_ready',
            'BETA LAUNCH PREPARATION COMPLETE - TE KETE AKO READY',
            'deployment_summary',
            ARRAY['Platform 99.5% ready for launch', '6-email recruitment campaign prepared', '4-tier support system designed'],
            '{"file_path": "BETA-LAUNCH-PREPARATION.md", "content_length": 3000, "quality_score": 92}'::jsonb,
            ARRAY['Production Readiness Specialist', 'Launch Coordinator']
        );