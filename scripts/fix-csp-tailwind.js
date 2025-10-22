#!/usr/bin/env node

/**
 * BATCH FIX: Add cdn.tailwindcss.com to CSP headers
 * Fixes console error: "Refused to load script 'https://cdn.tailwindcss.com/'"
 */

const fs = require('fs');
const path = require('path');
const { glob } = require('glob');

// Configuration
const TARGET_DIR = path.join(__dirname, '../public/dist-handouts');
const DRY_RUN = process.argv.includes('--dry-run');

// CSP patterns
const OLD_CSP_PATTERN = /(<meta http-equiv="Content-Security-Policy" content="[^"]*script-src\s+'self'\s+'unsafe-inline'(?:\s+'unsafe-eval')?\s+https:\/\/cdn\.jsdelivr\.net\s+https:\/\/unpkg\.com\s+https:\/\/supabase\.com)/g;

const REPLACEMENT = (match) => {
  // Check if cdn.tailwindcss.com is already there
  if (match.includes('cdn.tailwindcss.com')) {
    return match; // Already fixed
  }
  
  // Add cdn.tailwindcss.com and ensure 'unsafe-eval' is present
  let updated = match;
  
  // Ensure 'unsafe-eval' is present
  if (!updated.includes("'unsafe-eval'")) {
    updated = updated.replace("'unsafe-inline'", "'unsafe-inline' 'unsafe-eval'");
  }
  
  // Add cdn.tailwindcss.com after cdn.jsdelivr.net
  updated = updated.replace(
    'https://cdn.jsdelivr.net',
    'https://cdn.jsdelivr.net https://cdn.tailwindcss.com'
  );
  
  return updated;
};

async function fixFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    
    // Check if file has Tailwind script
    if (!content.includes('cdn.tailwindcss.com')) {
      return { skipped: true, reason: 'No Tailwind CDN usage' };
    }
    
    // Check if already fixed
    const cspMatch = content.match(OLD_CSP_PATTERN);
    if (!cspMatch) {
      // Check if it has CSP with Tailwind already
      if (content.includes('script-src') && content.includes('cdn.tailwindcss.com')) {
        return { skipped: true, reason: 'Already fixed' };
      }
      return { skipped: true, reason: 'No CSP or different pattern' };
    }
    
    // Apply fix
    const updated = content.replace(OLD_CSP_PATTERN, REPLACEMENT);
    
    if (updated === content) {
      return { skipped: true, reason: 'No changes needed' };
    }
    
    if (!DRY_RUN) {
      fs.writeFileSync(filePath, updated, 'utf8');
    }
    
    return { fixed: true };
  } catch (error) {
    return { error: error.message };
  }
}

async function main() {
  console.log('🔧 CSP Tailwind CDN Batch Fix\n');
  console.log(`Mode: ${DRY_RUN ? '🔍 DRY RUN' : '✍️  LIVE FIX'}\n`);
  
  // Find all HTML files
  const pattern = path.join(TARGET_DIR, '*.html').replace(/\\/g, '/');
  const files = await glob(pattern, { ignore: ['**/*.bak'] });
  
  console.log(`Found ${files.length} HTML files\n`);
  
  let fixed = 0;
  let skipped = 0;
  let errors = 0;
  
  for (const file of files) {
    const result = await fixFile(file);
    const fileName = path.basename(file);
    
    if (result.fixed) {
      console.log(`✅ ${fileName}`);
      fixed++;
    } else if (result.error) {
      console.log(`❌ ${fileName}: ${result.error}`);
      errors++;
    } else if (result.skipped) {
      // Don't log every skip, just count
      skipped++;
    }
  }
  
  console.log(`\n📊 Summary:`);
  console.log(`   Fixed: ${fixed}`);
  console.log(`   Skipped: ${skipped}`);
  console.log(`   Errors: ${errors}`);
  console.log(`   Total: ${files.length}`);
  
  if (DRY_RUN) {
    console.log(`\n💡 Run without --dry-run to apply changes`);
  } else {
    console.log(`\n✨ CSP headers updated successfully!`);
  }
}

main().catch(console.error);

