#!/usr/bin/env ts-node
/**
 * Kaitiaki Aronui Memory System - The Hippocampus of Te Kete Ako
 * 
 * This is the episodic memory system that catalogs and indexes every artifact
 * created by our AI agents. It's like having a photographic memory of everything
 * that's been built for Mangakōtukutuku College.
 * 
 * The system learns from patterns: which resources work, what teachers modify,
 * how students respond. This becomes the foundation for increasingly intelligent
 * content generation.
 */

import * as fs from 'fs';
import * as path from 'path';
import * as crypto from 'crypto';
import fg from 'fast-glob';
import pdfParse from 'pdf-parse';
import * as cheerio from 'cheerio';
import frontMatter from 'front-matter';
import { createClient } from '@supabase/supabase-js';
import axios from 'axios';
import * as dotenv from 'dotenv';

dotenv.config();

// Configuration - The nervous system of our indexer
const config = {
  supabase: {
    url: process.env.SUPABASE_URL!,
    key: process.env.SUPABASE_SERVICE_KEY!
  },
  ai: {
    deepseekKey: process.env.DEEPSEEK_API_KEY || 'sk-103cb83572a346e2aef89e2d2a4f7f89',
    openaiKey: process.env.OPENAI_API_KEY || '',
    embeddingModel: 'text-embedding-3-large',
    embeddingDim: 1536
  },
  patterns: [
    '**/*.md', '**/*.markdown', '**/*.html', '**/*.htm', 
    '**/*.pdf', '**/*.txt', '**/*.json', '**/*.py', '**/*.js', '**/*.ts'
  ],
  cultural: {
    maoriWords: ['māori', 'iwi', 'hapū', 'whānau', 'kaiako', 'ākonga', 'kōrero', 'whakatōhea', 'manaakitanga', 'ako'],
    culturalConcepts: ['te ao māori', 'tikanga', 'kaupapa', 'whakapapa', 'taonga', 'mauri']
  }
};

if (!config.supabase.url || !config.supabase.key) {
  console.error('❌ Missing Supabase credentials. Set SUPABASE_URL and SUPABASE_SERVICE_KEY');
  process.exit(1);
}

const supabase = createClient(config.supabase.url, config.supabase.key);

// ========================================
// MEMORY ENCODING FUNCTIONS
// ========================================

function sha256(content: Buffer | string): string {
  return crypto.createHash('sha256').update(content).digest('hex');
}

async function embedWithOpenAI(text: string): Promise<number[]> {
  if (!config.ai.openaiKey) {
    console.warn('⚠️  No OpenAI key - using random vector (NOT for production)');
    return Array.from({ length: config.ai.embeddingDim }, () => Math.random() - 0.5);
  }
  
  try {
    const response = await axios.post('https://api.openai.com/v1/embeddings', {
      model: config.ai.embeddingModel,
      input: text.slice(0, 8000) // Truncate for API limits
    }, {
      headers: { Authorization: `Bearer ${config.ai.openaiKey}` }
    });
    return response.data.data[0].embedding;
  } catch (error) {
    console.warn('⚠️  Embedding failed, using random vector:', error);
    return Array.from({ length: config.ai.embeddingDim }, () => Math.random() - 0.5);
  }
}

function extractCulturalContext(text: string): { tags: string[], significance: string } {
  const lowerText = text.toLowerCase();
  const foundWords = config.cultural.maoriWords.filter((word: string) => lowerText.includes(word));
  const foundConcepts = config.cultural.culturalConcepts.filter((concept: string) => lowerText.includes(concept));
  
  const tags = [...foundWords, ...foundConcepts];
  const significance = tags.length > 0 ? 'Contains Māori cultural elements' : 'General educational content';
  
  return { tags: Array.from(new Set(tags)), significance };
}

function extractKeywords(text: string, maxKeywords = 10): string[] {
  if (!text) return [];
  
  // Simple keyword extraction - focuses on educational terms
  const words = text
    .toLowerCase()
    .replace(/[^\w\s]/g, ' ')
    .split(/\s+/)
    .filter(word => 
      word.length > 3 && 
      !['this', 'that', 'with', 'have', 'will', 'been', 'from', 'they', 'were', 'said', 'each', 'which', 'your', 'what', 'their', 'time', 'about'].includes(word)
    );
    
  const frequency: Record<string, number> = {};
  words.forEach((word: string) => frequency[word] = (frequency[word] || 0) + 1);
  
  return Object.entries(frequency)
    .sort(([,a], [,b]) => b - a)
    .slice(0, maxKeywords)
    .map(([word]) => word);
}

// ========================================
// CONTENT EXTRACTORS
// ========================================

async function extractFromPDF(buffer: Buffer): Promise<{ text: string, title: string }> {
  try {
    const data = await pdfParse(buffer);
    const text = data.text || '';
    const title = text.split('\n').find((line: string) => line.trim().length > 0)?.slice(0, 100) || 'Untitled PDF';
    return { text, title };
  } catch (error) {
    console.warn('PDF parsing failed:', error);
    return { text: '', title: 'PDF (parsing failed)' };
  }
}

function extractFromHTML(html: string): { text: string, title: string, headings: string[] } {
  try {
    const $ = cheerio.load(html);
    const title = $('title').text() || $('h1').first().text() || 'Untitled HTML';
    const headings: string[] = [];
    $('h1, h2, h3, h4').each((_, elem) => {
      const heading = $(elem).text().trim();
      if (heading) headings.push(heading);
    });
    const text = $('body').text().replace(/\s+/g, ' ').trim();
    return { text, title, headings };
  } catch (error) {
    console.warn('HTML parsing failed:', error);
    return { text: html, title: 'HTML (parsing failed)', headings: [] };
  }
}

function extractFromMarkdown(content: string): { text: string, title: string, metadata: any } {
  try {
    const parsed = frontMatter(content);
    const metadata = parsed.attributes as any || {};
    const text = String(parsed.body || content);
    const title = metadata.title || text.split('\n').find((line: string) => line.startsWith('#'))?.replace(/^#+\s*/, '') || 'Untitled';
    return { text, title, metadata };
  } catch (error) {
    return { text: content, title: 'Markdown (parsing failed)', metadata: {} };
  }
}

// ========================================
// ARTIFACT PROCESSING
// ========================================

async function processArtifact(filePath: string, rootDir: string): Promise<void> {
  try {
    const relPath = path.relative(rootDir, filePath);
    const ext = path.extname(filePath).toLowerCase();
    const stat = fs.statSync(filePath);
    const buffer = fs.readFileSync(filePath);
    const contentHash = sha256(buffer);
    
    // Check if already processed with same hash
    const { data: existing } = await supabase
      .from('artifact_catalog')
      .select('content_hash')
      .eq('file_path', relPath)
      .single();
      
    if (existing?.content_hash === contentHash) {
      console.log(`⏭️  Skipping ${relPath} (unchanged)`);
      return;
    }
    
    let title = path.basename(filePath, ext);
    let description = '';
    let keywords: string[] = [];
    let yearLevels: number[] = [];
    let subjects: string[] = [];
    let metadata: any = {};
    let agent_creator = 'unknown';
    
    // Extract content based on file type
    try {
      if (ext === '.pdf') {
        const { text, title: pdfTitle } = await extractFromPDF(buffer);
        title = pdfTitle;
        description = text.slice(0, 500).replace(/\s+/g, ' ').trim() + (text.length > 500 ? '...' : '');
        keywords = extractKeywords(text);
      } else if (['.html', '.htm'].includes(ext)) {
        const { text, title: htmlTitle, headings } = extractFromHTML(buffer.toString('utf8'));
        title = htmlTitle;
        description = text.slice(0, 500).replace(/\s+/g, ' ').trim() + (text.length > 500 ? '...' : '');
        keywords = extractKeywords([...headings, text].join(' '));
      } else if (['.md', '.markdown'].includes(ext)) {
        const { text, title: mdTitle, metadata: mdMeta } = extractFromMarkdown(buffer.toString('utf8'));
        title = mdTitle;
        description = mdMeta.description || text.slice(0, 500).replace(/\s+/g, ' ').trim() + (text.length > 500 ? '...' : '');
        keywords = mdMeta.tags || extractKeywords(text);
        yearLevels = mdMeta.year_levels || mdMeta.yearLevels || [];
        subjects = mdMeta.subjects || [];
        metadata = mdMeta;
        agent_creator = mdMeta.agent || mdMeta.created_by || 'unknown';
      } else if (['.js', '.ts', '.py'].includes(ext)) {
        const code = buffer.toString('utf8');
        // Extract title from first comment or filename
        const firstComment = code.match(/\/\*\*([\s\S]*?)\*\/|"""([\s\S]*?)"""|'''([\s\S]*?)'''/);
        title = firstComment ? firstComment[1]?.split('\n')[0]?.trim() || title : title;
        description = `Code file: ${ext.slice(1)} script`;
        keywords = extractKeywords(code);
      } else {
        const text = buffer.toString('utf8');
        description = text.slice(0, 500).replace(/\s+/g, ' ').trim() + (text.length > 500 ? '...' : '');
        keywords = extractKeywords(text);
      }
    } catch (parseError) {
      console.warn(`⚠️  Parse error for ${relPath}:`, parseError);
      description = `File processing error: ${parseError}`;
    }
    
    // Analyze cultural context
    const fullText = [title, description, keywords.join(' ')].join(' ');
    const { tags: culturalTags, significance } = extractCulturalContext(fullText);
    
    // Generate embedding
    const embedding = await embedWithOpenAI(fullText);
    
    // Determine file type category
    let fileType = 'unknown';
    if (['lesson', 'unit', 'handout', 'activity', 'game'].some(t => relPath.toLowerCase().includes(t))) {
      fileType = 'educational_resource';
    } else if (['script', 'py', 'js', 'ts'].some(t => relPath.toLowerCase().includes(t) || ext === `.${t}`)) {
      fileType = 'script';
    } else if (['doc', 'md', 'readme', 'guide'].some(t => relPath.toLowerCase().includes(t))) {
      fileType = 'documentation';
    } else if (ext === '.pdf') {
      fileType = 'pdf_resource';
    }
    
    // Calculate quality score (basic heuristic)
    let qualityScore = 0.5; // baseline
    if (title && title !== path.basename(filePath, ext)) qualityScore += 0.2; // has meaningful title
    if (description.length > 100) qualityScore += 0.2; // substantial description
    if (keywords.length >= 3) qualityScore += 0.1; // good keywords
    if (culturalTags.length > 0) qualityScore += 0.2; // cultural integration
    qualityScore = Math.min(1.0, qualityScore);
    
    // Upsert to catalog
    const artifact = {
      file_path: relPath,
      file_name: path.basename(filePath),
      file_type: fileType,
      file_size_bytes: stat.size,
      content_hash: contentHash,
      title: title.slice(0, 300),
      description: description.slice(0, 1000),
      keywords,
      year_levels: yearLevels,
      subjects,
      cultural_tags: culturalTags,
      agent_creator,
      quality_score: qualityScore,
      embedding,
      metadata,
      created_at: stat.birthtime?.toISOString() || new Date().toISOString(),
      updated_at: new Date().toISOString()
    };
    
    const { error } = await supabase
      .from('artifact_catalog')
      .upsert(artifact, { onConflict: 'file_path' });
      
    if (error) throw error;
    
    console.log(`✅ Indexed: ${relPath} (${fileType}, quality: ${qualityScore.toFixed(2)})`);
    
  } catch (error) {
    console.error(`❌ Failed to process ${filePath}:`, error);
  }
}

// ========================================
// MAIN INDEXING FUNCTION
// ========================================

async function indexTeKeteAko(rootDir: string): Promise<void> {
  console.log('🧠 Kaitiaki Aronui Memory System - Indexing Te Kete Ako');
  console.log('📁 Scanning directory:', rootDir);
  
  try {
    const files = await fg(config.patterns, { 
      cwd: rootDir, 
      absolute: true, 
      dot: true,
      ignore: ['**/node_modules/**', '**/.*/**', '**/*.log', '**/backups/**']
    });
    
    console.log(`📊 Found ${files.length} artifacts to catalog`);
    
    let processed = 0;
    for (const file of files) {
      await processArtifact(file, rootDir);
      processed++;
      if (processed % 10 === 0) {
        console.log(`📈 Progress: ${processed}/${files.length} (${Math.round(processed/files.length*100)}%)`);
      }
    }
    
    // Generate summary
    const { data: stats } = await supabase
      .from('artifact_catalog')
      .select('file_type');
      
    console.log('\n🎯 Indexing Complete!');
    console.log('📊 Summary:');
    if (stats && Array.isArray(stats)) {
      const summary = stats.reduce((acc: Record<string, number>, item: any) => {
        acc[item.file_type] = (acc[item.file_type] || 0) + 1;
        return acc;
      }, {});
      
      Object.entries(summary).forEach(([fileType, count]) => {
        console.log(`   ${fileType}: ${count} artifacts`);
      });
    }
    
    console.log('\n🧺 "Whaowhia te kete mātauranga" - The basket of knowledge is now indexed!');
    
  } catch (error) {
    console.error('❌ Indexing failed:', error);
    throw error;
  }
}

// ========================================
// CLI INTERFACE
// ========================================

async function main() {
  const targetDir = process.argv[2] || './te-kete-ako-clean';
  const resolvedDir = path.resolve(targetDir);
  
  if (!fs.existsSync(resolvedDir)) {
    console.error(`❌ Directory not found: ${resolvedDir}`);
    process.exit(1);
  }
  
  console.log(`🚀 Starting memory indexing for: ${resolvedDir}`);
  
  try {
    await indexTeKeteAko(resolvedDir);
    console.log('✨ Memory indexing completed successfully!');
  } catch (error) {
    console.error('💥 Memory indexing failed:', error);
    process.exit(1);
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

export { indexTeKeteAko, processArtifact };