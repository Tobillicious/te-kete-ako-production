const { chromium } = require('playwright');
const { Eyes, Target, ClassicRunner, BatchInfo } = require('@applitools/eyes-playwright');

(async () => {
    const runner = new ClassicRunner();
    const eyes = new Eyes(runner);
    
    eyes.setApiKey(process.env.APPLITOOLS_API_KEY);
    
    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        // Start visual test
        await eyes.open(page, 'Te Kete Ako', 'Homepage GraphRAG Issue Check', { width: 1920, height: 1080 });
        
        console.log('📸 Loading localhost:8888...');
        await page.goto('http://localhost:8888');
        
        // Wait for page to load
        await page.waitForTimeout(3000);
        
        // Take screenshot of full page
        console.log('📸 Taking full page screenshot...');
        await eyes.check('Homepage - Full Page', Target.window().fully());
        
        // Scroll down to see content
        await page.evaluate(() => window.scrollTo(0, 500));
        await page.waitForTimeout(1000);
        await eyes.check('Homepage - Scrolled', Target.window().fully());
        
        // Check navigation dropdowns
        console.log('📸 Checking navigation...');
        const intelligenceNav = await page.$('a[href="/intelligence-hub.html"]');
        if (intelligenceNav) {
            console.log('⚠️  FOUND: Intelligence Hub link in navigation!');
            await intelligenceNav.hover();
            await page.waitForTimeout(1000);
            await eyes.check('Navigation - Intelligence Dropdown', Target.window().fully());
        }
        
        const brainNav = await page.$('a[href="/graphrag-brain-hub.html"]');
        if (brainNav) {
            console.log('⚠️  FOUND: Brain Hub link in navigation!');
        }
        
        const discoveryNav = await page.$('a[href="/discovery-tools.html"]');
        if (discoveryNav) {
            console.log('⚠️  FOUND: Discovery Tools link in navigation!');
        }
        
        // Check for GraphRAG links
        const graphragLinks = await page.$$('a[href*="graphrag"]');
        console.log(`⚠️  FOUND: ${graphragLinks.length} links containing "graphrag"`);
        
        // Check console for errors
        page.on('console', msg => console.log('CONSOLE:', msg.text()));
        
        await eyes.close();
        
    } catch (error) {
        console.error('❌ Test error:', error);
        await eyes.abortIfNotClosed();
    } finally {
        await browser.close();
        const results = await runner.getAllTestResults();
        console.log('✅ Visual test complete!');
        console.log('🔗 View results:', results.getAllResults()[0].getAppUrls().getBatch());
    }
})();

