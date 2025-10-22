# 🚦 Lighthouse Audit Checklist - Te Kete Ako

**Date:** Oct 21, 2025  
**Purpose:** Automated performance, accessibility, SEO, and best practices audit

---

## 📊 Lighthouse Score Targets

| Category | Minimum Score | Target Score | Weight |
|----------|---------------|--------------|--------|
| **Performance** | 80 | 90+ | High Priority |
| **Accessibility** | 90 | 95+ | Critical |
| **Best Practices** | 85 | 90+ | Medium Priority |
| **SEO** | 85 | 90+ | Medium Priority |
| **PWA** | N/A | N/A | Optional |

---

## 🔧 Setup Lighthouse

### Option 1: Chrome DevTools (Easiest)
1. Open Chrome
2. Navigate to page to audit
3. Open DevTools (F12 or Ctrl+Shift+I)
4. Click "Lighthouse" tab
5. Select categories to audit
6. Click "Analyze page load"

### Option 2: Lighthouse CLI (Best for automation)
```bash
# Install globally
npm install -g lighthouse

# Run audit for a single page
lighthouse http://localhost:8000/ --output html --output-path ./audits/homepage-audit.html --view

# Run with mobile simulation
lighthouse http://localhost:8000/ --preset mobile --output html --output-path ./audits/homepage-mobile.html

# Run with desktop simulation
lighthouse http://localhost:8000/ --preset desktop --output html --output-path ./audits/homepage-desktop.html
```

### Option 3: PageSpeed Insights (After Deployment)
1. Go to https://pagespeed.web.dev/
2. Enter your deployed URL
3. View results for mobile and desktop

---

## 📋 Pages to Audit

### Critical Pages (MUST Audit)

1. **Homepage** `/`
   - [ ] Desktop audit completed
   - [ ] Mobile audit completed
   - Performance: ___
   - Accessibility: ___
   - Best Practices: ___
   - SEO: ___
   - **Issues:** _________________

2. **Lessons Browse** `/lessons.html`
   - [ ] Desktop audit completed
   - [ ] Mobile audit completed
   - Performance: ___
   - Accessibility: ___
   - Best Practices: ___
   - SEO: ___
   - **Issues:** _________________

3. **Sample Lesson** `/lessons/y9-science-climate-change-action.html`
   - [ ] Desktop audit completed
   - [ ] Mobile audit completed
   - Performance: ___
   - Accessibility: ___
   - Best Practices: ___
   - SEO: ___
   - **Issues:** _________________

4. **Handouts Browse** `/handouts.html`
   - [ ] Desktop audit completed
   - [ ] Mobile audit completed
   - Performance: ___
   - Accessibility: ___
   - Best Practices: ___
   - SEO: ___
   - **Issues:** _________________

5. **Unit Plans Browse** `/unit-plans.html`
   - [ ] Desktop audit completed
   - [ ] Mobile audit completed
   - Performance: ___
   - Accessibility: ___
   - Best Practices: ___
   - SEO: ___
   - **Issues:** _________________

### High-Priority Pages

6. **Cultural Hub** `/cultural-hub.html`
   - [ ] Audit completed
   - Scores: P___ A___ BP___ SEO___
   
7. **Discovery Tools** `/discovery-tools.html`
   - [ ] Audit completed
   - Scores: P___ A___ BP___ SEO___

8. **Teacher Dashboard** `/teacher-dashboard-unified.html`
   - [ ] Audit completed
   - Scores: P___ A___ BP___ SEO___

9. **Login Page** `/login.html`
   - [ ] Audit completed
   - Scores: P___ A___ BP___ SEO___

10. **Register Page** `/register-simple.html`
    - [ ] Audit completed
    - Scores: P___ A___ BP___ SEO___

---

## 🎯 Core Web Vitals

These metrics are critical for user experience and SEO:

### Largest Contentful Paint (LCP)
- **Target:** < 2.5 seconds
- **Measures:** Loading performance
- **Common Issues:**
  - Large images not optimized
  - Render-blocking resources
  - Slow server response times

### First Input Delay (FID)
- **Target:** < 100 milliseconds
- **Measures:** Interactivity
- **Common Issues:**
  - Long JavaScript execution
  - Heavy third-party scripts
  - Main thread blocking

### Cumulative Layout Shift (CLS)
- **Target:** < 0.1
- **Measures:** Visual stability
- **Common Issues:**
  - Images without dimensions
  - Ads/embeds without reserved space
  - Web fonts causing layout shifts

---

## 🔍 Common Issues & Fixes

### Performance Issues

| Issue | Fix | Priority |
|-------|-----|----------|
| **Large images** | Compress with ImageOptim/TinyPNG, use WebP | High |
| **Render-blocking CSS** | Inline critical CSS, defer non-critical | High |
| **Render-blocking JS** | Add `defer` or `async` to script tags | High |
| **No text compression** | Enable gzip/brotli on server | Medium |
| **No browser caching** | Set Cache-Control headers | Medium |
| **Large bundle sizes** | Code splitting, tree shaking | Medium |
| **Too many requests** | Bundle files, use sprite sheets | Low |

### Accessibility Issues

| Issue | Fix | Priority |
|-------|-----|----------|
| **Missing alt text** | Add descriptive alt attributes to `<img>` | Critical |
| **Low color contrast** | Adjust colors to meet WCAG 2.1 AA (4.5:1) | High |
| **Missing form labels** | Add `<label>` tags or `aria-label` | High |
| **Non-semantic HTML** | Use `<nav>`, `<main>`, `<article>` etc. | Medium |
| **Missing ARIA** | Add ARIA labels to interactive elements | Medium |
| **Keyboard navigation** | Ensure all interactive elements are focusable | High |
| **Missing page lang** | Add `<html lang="en">` or `lang="mi"` | Medium |

### Best Practices Issues

| Issue | Fix | Priority |
|-------|-----|----------|
| **HTTP not HTTPS** | Deploy with SSL certificate (Netlify auto) | Critical |
| **Mixed content** | Ensure all resources use HTTPS | High |
| **No meta viewport** | Add `<meta name="viewport" content="width=device-width, initial-scale=1.0">` | High |
| **Console errors** | Fix JavaScript errors | High |
| **Deprecated APIs** | Update to modern alternatives | Medium |
| **Insecure libraries** | Update vulnerable dependencies | High |

### SEO Issues

| Issue | Fix | Priority |
|-------|-----|----------|
| **Missing title** | Add unique `<title>` to each page | Critical |
| **Missing meta description** | Add `<meta name="description" content="...">` | High |
| **No structured data** | Add JSON-LD schema for lessons/resources | Medium |
| **Links not crawlable** | Use `<a href="...">` not `<div onclick="...">` | High |
| **Images missing alt** | Add descriptive alt text | High |
| **No robots.txt** | Create `robots.txt` in public root | Low |
| **No sitemap** | Generate and submit `sitemap.xml` | Medium |

---

## 📝 Audit Script (Batch Processing)

Create a script to audit multiple pages at once:

```bash
#!/bin/bash
# audit-all.sh - Run Lighthouse on all critical pages

mkdir -p audits

pages=(
  "/"
  "/lessons.html"
  "/handouts.html"
  "/unit-plans.html"
  "/games.html"
  "/cultural-hub.html"
  "/discovery-tools.html"
  "/login.html"
)

for page in "${pages[@]}"; do
  filename=$(echo $page | tr '/' '-' | sed 's/^-//' | sed 's/\.html//')
  echo "Auditing: $page"
  lighthouse "http://localhost:8000$page" \
    --output html \
    --output json \
    --output-path "./audits/$filename" \
    --preset desktop \
    --chrome-flags="--headless"
done

echo "✅ All audits complete! Check ./audits/ folder"
```

Run it:
```bash
chmod +x audit-all.sh
./audit-all.sh
```

---

## 📊 Audit Results Tracker

### Overall Summary

| Page | Performance | Accessibility | Best Practices | SEO | Status |
|------|-------------|---------------|----------------|-----|--------|
| Homepage | ___ | ___ | ___ | ___ | ⏳ |
| Lessons | ___ | ___ | ___ | ___ | ⏳ |
| Handouts | ___ | ___ | ___ | ___ | ⏳ |
| Units | ___ | ___ | ___ | ___ | ⏳ |
| Games | ___ | ___ | ___ | ___ | ⏳ |
| Cultural Hub | ___ | ___ | ___ | ___ | ⏳ |
| Discovery Tools | ___ | ___ | ___ | ___ | ⏳ |
| Login | ___ | ___ | ___ | ___ | ⏳ |

**Average Scores:**
- Performance: ___
- Accessibility: ___
- Best Practices: ___
- SEO: ___

---

## 🎯 Priority Fixes

After running audits, list the top issues to fix:

### P0 - Critical (Fix before deployment)
1. _______________________
2. _______________________
3. _______________________

### P1 - High (Fix within 1 week)
1. _______________________
2. _______________________
3. _______________________

### P2 - Medium (Fix within 1 month)
1. _______________________
2. _______________________

### P3 - Low (Nice to have)
1. _______________________
2. _______________________

---

## 🚀 Performance Optimization Checklist

### Images
- [ ] All images compressed
- [ ] Using appropriate formats (WebP where supported)
- [ ] Images have width/height attributes
- [ ] Lazy loading implemented for below-fold images
- [ ] Responsive images with `srcset`

### CSS
- [ ] Critical CSS inlined
- [ ] Non-critical CSS deferred
- [ ] CSS minified
- [ ] Unused CSS removed
- [ ] No CSS @import statements

### JavaScript
- [ ] Scripts have `defer` or `async`
- [ ] JavaScript minified
- [ ] Unused JavaScript removed
- [ ] Large libraries lazy-loaded
- [ ] No long-running scripts blocking main thread

### Fonts
- [ ] Fonts preloaded: `<link rel="preload" as="font">`
- [ ] Font-display: swap used
- [ ] Only necessary font weights loaded
- [ ] WOFF2 format used (smaller)

### Server
- [ ] Gzip/Brotli compression enabled
- [ ] Cache-Control headers set
- [ ] CDN used for static assets (Netlify handles this)
- [ ] HTTP/2 enabled (Netlify default)

---

## ✅ Lighthouse Sign-Off

Once all audits are complete and critical issues fixed:

```
LIGHTHOUSE AUDIT SIGN-OFF
Date: _______________
Auditor: _______________

Average Scores:
- Performance: ___ / 100 (Target: 90+)
- Accessibility: ___ / 100 (Target: 95+)
- Best Practices: ___ / 100 (Target: 90+)
- SEO: ___ / 100 (Target: 90+)

Critical Issues Fixed: ✅ All resolved
High-Priority Issues: ___ remaining

Recommendation:
[ ] ✅ Ready for deployment - All targets met
[ ] ⚠️ Deploy with monitoring - Minor issues remain
[ ] ❌ Hold deployment - Critical issues need fixing
```

---

## 📚 Additional Resources

- [Lighthouse Documentation](https://developer.chrome.com/docs/lighthouse/)
- [Web.dev Performance Guide](https://web.dev/performance/)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Chrome DevTools Performance](https://developer.chrome.com/docs/devtools/performance/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

**Next Step:** After passing Lighthouse audits, proceed with Netlify deployment!

