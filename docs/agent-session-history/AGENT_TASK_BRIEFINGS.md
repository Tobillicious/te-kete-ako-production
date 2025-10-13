# Agent Task Briefings - Phase 2 Content Integration

**Generated:** October 13, 2025  
**Mission:** Transform Te Kete Ako into New Zealand's most comprehensive educational platform

---

## Agent-4: Navigation & Handouts Integration Specialist

### Current Tasks
1. **Check for broken navigation links across the site** (Priority: High)
2. **Integrate 2,257 discovered handouts into the site** (Priority: Critical)

### Success Criteria
- Navigation audit complete with <5 broken links remaining
- All handouts integrated with proper CSS styling
- Handout index page functional with filtering capabilities
- Breadcrumb navigation working on all handout pages

### Tools Available
- Content integration engine: `node scripts/content-integration-engine.cjs handouts`
- Quality validation: `python3 scripts/automated-quality-validation.py validate orphan-integration [location]`
- Link checker: Use workflow validator for navigation checks

### Next Steps
1. Run navigation audit using workflow validator
2. Fix any critical broken links
3. Process handouts in batches of 100 using integration engine
4. Validate each batch before proceeding

---

## Agent-6: Lessons Integration Specialist

### Current Task
- **Integrate 2,753 discovered lessons into the site** (Priority: Critical)

### Success Criteria
- All lessons integrated with proper CSS styling
- Lesson index page functional with subject/year filtering
- Breadcrumb navigation working on all lesson pages
- Lessons properly categorized by subject and year level

### Tools Available
- Content integration engine: `node scripts/content-integration-engine.cjs lessons`
- Quality validation: `python3 scripts/automated-quality-validation.py validate orphan-integration [location]`
- Content prioritization: Focus on Phase 1 high-priority lessons first

### Next Steps
1. Start with Phase 1 high-priority lessons (quality score ≥80)
2. Process lessons in batches of 100 using integration engine
3. Validate each batch before proceeding
4. Update lesson index with new content

---

## Agent-7: Cultural Validation Specialist

### Current Task
- **Validate cultural authenticity of 1,223 high cultural value resources** (Priority: Critical)

### Success Criteria
- All high cultural value content reviewed for authenticity
- Cultural protocols properly observed in all content
- Māori language usage validated where present
- Cultural sensitivity issues identified and addressed

### Validation Criteria
1. **Mātauranga Māori Accuracy**: Is the cultural knowledge correct and appropriately presented?
2. **Language Authenticity**: Is te reo Māori used correctly with proper diacritics?
3. **Cultural Protocols**: Are appropriate cultural protocols observed?
4. **Context Appropriateness**: Is the cultural content presented in appropriate educational context?

### Tools Available
- Cultural content filter: `python3 scripts/content-treasure-hunter.py cultural-filter`
- Quality validation: `python3 scripts/automated-quality-validation.py validate content-enhancement [location]`
- Content prioritization: Focus on high cultural value items first

### Next Steps
1. Begin with Phase 1 high cultural value items
2. Validate in batches of 50 items
3. Document any issues found
4. Work with content creators to address concerns

---

## Agent-10: Coordination & Authentication Specialist

### Current Tasks
1. **Implement role-based authentication system** (Priority: High)
2. **Create deployment workflow with testing** (Priority: Medium)

### Success Criteria
- Teacher vs student views properly differentiated
- Authentication system functional and secure
- Deployment pipeline with automated testing
- All deployments validated before going live

### Tools Available
- Authentication template: `public/auth-test.html`
- Deployment pipeline: `python3 scripts/deployment-pipeline.py`
- Validation pipeline: `python3 scripts/validation-deployment-pipeline.py`

### Next Steps
1. Review authentication requirements
2. Implement basic role differentiation
3. Set up deployment workflow with testing
4. Validate deployment process

---

## Agent-5: Quality Assurance Specialist

### Current Task
- **Set up automated quality checks** (Priority: High)

### Success Criteria
- Automated quality validation system operational
- All content meets minimum quality standards (score ≥70)
- Accessibility compliance verified (WCAG 2.1 AA)
- Performance benchmarks met

### Tools Available
- Quality validation system: `python3 scripts/automated-quality-validation.py`
- Workflow validator: `python3 scripts/workflow-pipeline-validator.py`
- Performance monitoring: Built into validation system

### Next Steps
1. Enhance quality validation system
2. Set up automated checks for new content
3. Implement accessibility validation
4. Monitor performance metrics

---

## Coordination Protocol

### Daily Check-ins
Each agent should update progress in `progress-log.md` using this format:
```
[HH:MM] Agent-X: TASK_NAME - Progress description (Status: IN_PROGRESS/COMPLETED/BLOCKED)
```

### Weekly Status Reports
Every Friday, agents should provide:
1. Tasks completed this week
2. Tasks planned for next week
3. Any blockers or challenges
4. Support needed from other agents

### Quality Gates
No content should be considered complete until:
1. Automated quality validation passes (score ≥70)
2. Cultural validation completed (for relevant content)
3. Navigation links verified
4. Accessibility compliance checked

### Communication Channels
- **Progress Log**: For daily updates and status tracking
- **MCP Server**: For real-time coordination (when available)
- **Issues**: For blockers requiring immediate attention

---

## Mission Critical Timeline

### Week 1 (Current)
- Complete Phase 1 integration validation
- Begin Phase 2 task execution
- Set up enhanced progress tracking

### Week 2
- Complete Agent-4 navigation audit and handout integration (first 500)
- Complete Agent-6 lessons integration (first 500)
- Begin Agent-7 cultural validation (first 200)

### Week 3
- Continue Phase 2 integration at scale
- Implement Agent-10 authentication system
- Complete Agent-5 quality checks setup

### Week 4
- Complete Phase 2 integration
- Validate all integrated content
- Deploy Phase 2 changes

---

Remember: We're not just building a website - we're creating New Zealand's most comprehensive educational platform that honors mātauranga Māori while serving the diverse needs of all learners. Every task contributes to this important mission!
