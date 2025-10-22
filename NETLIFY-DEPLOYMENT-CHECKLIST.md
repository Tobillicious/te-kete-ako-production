# 🚀 Netlify Deployment Checklist

**Date:** Oct 21, 2025  
**Purpose:** Ensure smooth deployment to Netlify production

---

## ✅ Pre-Deployment Checks

### 1. Code Quality
- [ ] All placeholder text removed from active files
- [ ] Content duplication issues resolved
- [ ] No broken links in navigation
- [ ] All CSS/JS files properly linked
- [ ] No syntax errors in HTML/CSS/JS
- [ ] Visual audit completed (see `VISUAL-AUDIT-CHECKLIST.md`)

### 2. Configuration Files
- [ ] `netlify.toml` exists and is configured correctly
- [ ] `_redirects` file configured (if needed)
- [ ] `_headers` file configured for security/CORS
- [ ] Environment variables set in Netlify dashboard (if needed)

### 3. Content Verification
- [ ] All critical pages load correctly locally
- [ ] Forms work (beta feedback, login, register)
- [ ] Search functionality works
- [ ] GraphRAG integration tested
- [ ] Supabase connection works
- [ ] Authentication flows tested

### 4. Performance Optimization
- [ ] Images optimized (compressed, appropriate sizes)
- [ ] CSS/JS minified (if applicable)
- [ ] Lazy loading implemented for images
- [ ] Service worker configured for caching
- [ ] No console errors on key pages

### 5. SEO & Accessibility
- [ ] Meta descriptions present on key pages
- [ ] Open Graph tags for social sharing
- [ ] Proper heading hierarchy (h1 → h2 → h3)
- [ ] Alt text on all images
- [ ] ARIA labels on interactive elements
- [ ] Color contrast meets WCAG 2.1 AA standards

### 6. Cultural Integrity
- [ ] Te reo Māori macrons display correctly (ā, ē, ī, ō, ū)
- [ ] Cultural content reviewed for accuracy
- [ ] Whakataukī displayed correctly
- [ ] Cultural safety guidelines followed

---

## 🔧 Netlify Configuration

### Required Files

#### `netlify.toml`
```toml
[build]
  publish = "public"
  command = "echo 'No build required - static site'"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

#### `_headers` (in `/public/`)
```
/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  
/css/*
  Cache-Control: public, max-age=31536000, immutable
  
/js/*
  Cache-Control: public, max-age=31536000, immutable
  
/images/*
  Cache-Control: public, max-age=31536000, immutable
```

---

## 📦 Deployment Steps

### Step 1: Connect Repository to Netlify
1. Log in to Netlify dashboard
2. Click "Add new site" → "Import an existing project"
3. Choose Git provider (GitHub/GitLab/Bitbucket)
4. Select repository: `te-kete-ako-clean`
5. Configure build settings:
   - **Build command:** (leave blank or use echo)
   - **Publish directory:** `public`
   - **Branch:** `main` or `master`

### Step 2: Configure Environment Variables (if needed)
1. Go to Site settings → Environment variables
2. Add required variables:
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - (Add others as needed)

### Step 3: Configure Custom Domain (Optional)
1. Go to Domain settings
2. Add custom domain
3. Configure DNS records:
   - A record: `185.199.108.153`
   - CNAME: `[your-site].netlify.app`
4. Enable HTTPS (automatic with Netlify)

### Step 4: Deploy
1. Click "Deploy site"
2. Monitor build logs for errors
3. Once deployed, test the live site

### Step 5: Post-Deployment Verification
- [ ] Home page loads correctly
- [ ] Navigation works across all pages
- [ ] Forms submit successfully
- [ ] Search functionality works
- [ ] Authentication works
- [ ] Supabase queries work
- [ ] No 404 errors on known pages
- [ ] HTTPS certificate is active

---

## 🧪 Testing After Deployment

### Smoke Test Checklist
1. **Home Page** (`/`)
   - [ ] Loads without errors
   - [ ] Hero section displays
   - [ ] Navigation works
   
2. **Lessons Page** (`/lessons.html`)
   - [ ] Lesson cards display
   - [ ] Filters work
   - [ ] Lesson links open correctly
   
3. **Login/Register** (`/login.html`, `/register-simple.html`)
   - [ ] Forms display correctly
   - [ ] Submit buttons work
   - [ ] Authentication redirects work
   
4. **Search** (Test on any page)
   - [ ] Search bar appears
   - [ ] Search returns results
   - [ ] Results link to correct pages
   
5. **Mobile Experience**
   - [ ] Test on actual mobile device or browser dev tools
   - [ ] Mobile navigation works
   - [ ] Pages are responsive
   - [ ] No horizontal scroll

---

## 📊 Monitoring & Analytics

### Post-Deployment Monitoring
- [ ] Set up Netlify Analytics (optional paid feature)
- [ ] Monitor Netlify build/deploy logs
- [ ] Check Supabase logs for errors
- [ ] Review PostHog analytics (if configured)
- [ ] Set up uptime monitoring (e.g., UptimeRobot)

### Performance Metrics to Track
- **Lighthouse Scores:**
  - Performance: > 90
  - Accessibility: > 95
  - Best Practices: > 90
  - SEO: > 90
  
- **Core Web Vitals:**
  - LCP (Largest Contentful Paint): < 2.5s
  - FID (First Input Delay): < 100ms
  - CLS (Cumulative Layout Shift): < 0.1

---

## 🐛 Troubleshooting Common Deployment Issues

| Issue | Solution |
|-------|----------|
| Build fails | Check build logs; verify `netlify.toml` syntax |
| 404 errors | Check `_redirects` file; verify file paths are correct |
| CSS/JS not loading | Check file paths; verify files exist in `public/` |
| Forms not working | Check Netlify Forms settings; add `netlify` attribute to forms |
| CORS errors | Update `_headers` file with CORS headers |
| Supabase connection fails | Verify environment variables are set correctly |
| Images don't load | Check image paths; ensure images are in `public/images/` |

---

## 🎯 Rollback Plan

If deployment causes critical issues:
1. Go to Netlify dashboard → Deploys
2. Find last working deploy
3. Click "Publish deploy" on that version
4. Fix issues locally
5. Redeploy when ready

---

## ✅ Final Checklist Before Going Live

- [ ] All critical bugs fixed
- [ ] Visual audit passed
- [ ] Browser testing completed
- [ ] Lighthouse audit scores acceptable
- [ ] Mobile experience tested
- [ ] Authentication flows tested
- [ ] Forms tested
- [ ] SEO meta tags present
- [ ] Analytics configured
- [ ] Monitoring set up
- [ ] Team notified of deployment
- [ ] Documentation updated

---

## 📝 Deployment Log

| Date | Deployed By | Version/Commit | Status | Notes |
|------|-------------|----------------|--------|-------|
| Oct 21, 2025 | Agent 9a4dd0d0 | [commit-hash] | 🟢 Success | Initial deployment |
| | | | | |

---

**🎉 Ready to Deploy!**

Once all checkboxes are ticked, proceed with confidence to Netlify deployment.

