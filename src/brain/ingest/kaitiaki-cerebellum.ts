/**
 * Kaitiaki Aronui Cerebellum - Coordination & Motor Learning
 * 
 * This is our coordination center - orchestrating smooth collaboration between
 * all AI agents and managing the complex workflow of transforming raw PDFs
 * and documents into living, connected knowledge graphs.
 * 
 * Like the cerebellum in the human brain, this system:
 * - Coordinates precise movements between AI agents
 * - Learns from experience to improve performance
 * - Maintains balance between different processing tasks
 * - Ensures smooth, automatic execution of complex workflows
 */

import * as fs from 'fs';
import * as path from 'path';
import pdfParse from 'pdf-parse';
import axios from 'axios';
import { createClient } from '@supabase/supabase-js';
import { v4 as uuidv4 } from 'uuid';
import * as dotenv from 'dotenv';
import retry from 'async-retry';

dotenv.config();

// ========================================
// NEURAL COORDINATION CONFIG
// ========================================

const config = {
  services: {
    extractorUrl: process.env.EXTRACTOR_URL || 'http://localhost:3001/extract',
    extractorBatchUrl: process.env.EXTRACTOR_BATCH_URL || 'http://localhost:3001/extract-batch',
  },
  ai: {
    deepseekKey: process.env.DEEPSEEK_API_KEY || '',
    openaiKey: process.env.OPENAI_API_KEY || '',
    embeddingModel: 'text-embedding-3-large',
    embeddingDim: 1536
  },
  supabase: {
    url: process.env.SUPABASE_URL!,
    key: process.env.SUPABASE_SERVICE_KEY!
  },
  processing: {
    chunkSize: 4000,
    chunkOverlap: 200,
    maxRetries: 3,
    retryDelay: 2000,
    batchSize: 5,
    qualityThreshold: 0.7
  }
};

if (!config.supabase.url || !config.supabase.key) {
  console.error('❌ Missing Supabase credentials');
  process.exit(1);
}

const supabase = createClient(config.supabase.url, config.supabase.key);

// ========================================
// COORDINATION FUNCTIONS
// ========================================

interface ProcessingContext {
  documentId: string;
  sourceTitle: string;
  sourceUrl?: string;
  metadata: any;
  startTime: number;
}

/**
 * Extract text from PDF with metadata extraction
 */
async function extractPDFContent(buffer: Buffer): Promise<{ text: string, metadata: any }> {
  try {
    const data = await pdfParse(buffer, {
      max: 50, // limit to first 50 pages for performance
    });
    
    const metadata = {
      pages: data.numpages,
      info: data.info,
      textLength: data.text.length,
      extractedAt: new Date().toISOString()
    };
    
    return { text: data.text, metadata };
  } catch (error: any) {
    throw new Error(`PDF parsing failed: ${error.message}`);
  }
}

/**
 * Intelligent text chunking that respects document structure
 */
function chunkTextIntelligently(text: string, maxChunkSize = config.processing.chunkSize): string[] {
  const chunks: string[] = [];
  let currentChunk = '';
  
  // Split by paragraphs first, then by sentences if needed
  const paragraphs = text.split(/\n\s*\n/);
  
  for (const paragraph of paragraphs) {
    // If paragraph is small enough, add to current chunk
    if (currentChunk.length + paragraph.length < maxChunkSize) {
      currentChunk += (currentChunk ? '\n\n' : '') + paragraph;
    } else {
      // Save current chunk if it exists
      if (currentChunk) {
        chunks.push(currentChunk.trim());
      }
      
      // If paragraph is still too long, split by sentences
      if (paragraph.length > maxChunkSize) {
        const sentences = paragraph.split(/(?<=[.!?])\s+/);
        currentChunk = '';
        
        for (const sentence of sentences) {
          if (currentChunk.length + sentence.length < maxChunkSize) {
            currentChunk += (currentChunk ? ' ' : '') + sentence;
          } else {
            if (currentChunk) chunks.push(currentChunk.trim());
            currentChunk = sentence;
          }
        }
      } else {
        currentChunk = paragraph;
      }
    }
  }
  
  // Add final chunk
  if (currentChunk) {
    chunks.push(currentChunk.trim());
  }
  
  return chunks.filter(chunk => chunk.length > 100); // Filter very short chunks
}

/**
 * Generate embeddings using OpenAI or fallback
 */
async function generateEmbedding(text: string): Promise<number[]> {
  if (!config.ai.openaiKey) {
    console.warn('⚠️  No OpenAI key - using zero vector (NOT for production)');
    return Array.from({ length: config.ai.embeddingDim }, () => 0);
  }
  
  try {
    const response = await axios.post('https://api.openai.com/v1/embeddings', {
      model: config.ai.embeddingModel,
      input: text.slice(0, 8000) // Respect API limits
    }, {
      headers: { 
        Authorization: `Bearer ${config.ai.openaiKey}`,
        'Content-Type': 'application/json'
      },
      timeout: 30000
    });
    
    return response.data.data[0].embedding;
  } catch (error: any) {
    console.warn(`⚠️  Embedding failed for text: ${error.message}`);
    return Array.from({ length: config.ai.embeddingDim }, () => Math.random() - 0.5);
  }
}

/**
 * Call the extraction service with retry logic
 */
async function extractWithRetry(chunkText: string, sourceTitle: string, sourceUrl?: string): Promise<any> {
  return retry(async (bail, attempt) => {
    try {
      console.log(`🧠 Extracting knowledge (attempt ${attempt})...`);
      
      const response = await axios.post(config.services.extractorUrl, {
        chunkText,
        sourceTitle,
        sourceUrl
      }, {
        timeout: 120000, // 2 minutes
        headers: { 'Content-Type': 'application/json' }
      });
      
      if (!response.data.success) {
        throw new Error(`Extractor returned error: ${response.data.error}`);
      }
      
      return response.data.extracted;
    } catch (error: any) {
      if (error.response?.status === 400) {
        // Bad request - don't retry
        bail(new Error(`Bad request: ${error.response.data.error}`));
        return;
      }
      
      console.warn(`⚠️  Extraction attempt ${attempt} failed: ${error.message}`);
      throw error;
    }
  }, {
    retries: config.processing.maxRetries,
    minTimeout: config.processing.retryDelay,
    maxTimeout: config.processing.retryDelay * 3
  });
}

/**
 * Store knowledge nodes in Supabase with conflict resolution
 */
async function storeKnowledgeNodes(nodes: any[], context: ProcessingContext): Promise<Map<string, string>> {
  const idMapping = new Map<string, string>();
  
  for (const node of nodes) {
    try {
      const nodeId = uuidv4();
      
      // Generate embedding for the node content
      const nodeText = [node.title, node.content_summary, ...(node.keywords || [])].join(' ');
      const embedding = await generateEmbedding(nodeText);
      
      // Store in knowledge_nodes table
      const { error } = await supabase.from('knowledge_nodes').insert({
        id: nodeId,
        node_type: node.type,
        title: node.title?.slice(0, 300) || 'Untitled',
        content_body: node.content_summary?.slice(0, 5000),
        year_levels: node.year_levels || [],
        subjects: node.subjects || [],
        cultural_context: node.cultural_context ? { context: node.cultural_context } : null,
        difficulty_level: node.difficulty_level || 0.5,
        learning_objectives: node.learning_objectives || [],
        success_criteria: node.success_criteria || [],
        embedding,
        metadata: {
          provenance: node.provenance,
          nzc_alignment: node.nzc_alignment,
          cultural_safety_check: node.cultural_safety_check,
          confidence: node.confidence,
          source_document: context.documentId,
          extracted_at: new Date().toISOString()
        },
        created_by: 'kaitiaki_cerebellum',
        created_at: new Date().toISOString(),
        last_modified: new Date().toISOString()
      });
      
      if (error) {
        console.error(`❌ Failed to store node ${node.id_hint}:`, error);
        continue;
      }
      
      idMapping.set(node.id_hint, nodeId);
      console.log(`✅ Stored node: ${node.title} (${nodeId})`);
      
    } catch (error: any) {
      console.error(`❌ Error storing node ${node.id_hint}:`, error.message);
    }
  }
  
  return idMapping;
}

/**
 * Store knowledge edges with proper node resolution
 */
async function storeKnowledgeEdges(edges: any[], nodeMapping: Map<string, string>, context: ProcessingContext): Promise<void> {
  for (const edge of edges) {
    try {
      const sourceId = nodeMapping.get(edge.source_hint);
      const targetId = nodeMapping.get(edge.target_hint);
      
      if (!sourceId || !targetId) {
        console.warn(`⚠️  Skipping edge ${edge.source_hint} -> ${edge.target_hint} (nodes not found)`);
        continue;
      }
      
      const { error } = await supabase.from('knowledge_edges').insert({
        id: uuidv4(),
        source_node: sourceId,
        target_node: targetId,
        relationship_type: edge.relationship,
        strength: edge.strength || 0.8,
        evidence_text: edge.evidence?.slice(0, 500),
        cultural_significance: edge.cultural_significance?.slice(0, 500),
        created_by: 'kaitiaki_cerebellum',
        confidence: edge.confidence || 0.8,
        created_at: new Date().toISOString()
      });
      
      if (error) {
        console.error(`❌ Failed to store edge:`, error);
        continue;
      }
      
      console.log(`✅ Stored edge: ${edge.source_hint} --[${edge.relationship}]--> ${edge.target_hint}`);
      
    } catch (error: any) {
      console.error(`❌ Error storing edge:`, error.message);
    }
  }
}

/**
 * Log processing job for monitoring and improvement
 */
async function logProcessingJob(context: ProcessingContext, result: any, status: string): Promise<void> {
  try {
    await supabase.from('agent_jobs').insert({
      id: context.documentId,
      agent_name: 'kaitiaki_cerebellum',
      job_type: 'ingest_document',
      input_context: {
        source_title: context.sourceTitle,
        source_url: context.sourceUrl,
        metadata: context.metadata
      },
      actual_output: result,
      status,
      confidence_score: result?.avg_confidence || null,
      cultural_safety_checked: result?.cultural_flags?.length > 0,
      human_review_required: result?.needs_review || false,
      created_at: new Date().toISOString(),
      completed_at: new Date().toISOString()
    });
  } catch (error) {
    console.warn('Failed to log processing job:', error);
  }
}

// ========================================
// MAIN ORCHESTRATION FUNCTIONS
// ========================================

/**
 * Process a single PDF document through the complete pipeline
 */
export async function ingestDocument(filePath: string, options: {
  sourceTitle?: string;
  sourceUrl?: string;
  metadata?: any;
} = {}): Promise<{ 
  success: boolean; 
  documentId: string;
  nodesCreated: number;
  edgesCreated: number;
  processingTime: number;
  culturalFlags: string[];
}> {
  const startTime = Date.now();
  const documentId = uuidv4();
  
  const context: ProcessingContext = {
    documentId,
    sourceTitle: options.sourceTitle || path.basename(filePath),
    sourceUrl: options.sourceUrl,
    metadata: options.metadata || {},
    startTime
  };
  
  try {
    console.log(`🚀 Starting document ingestion: ${context.sourceTitle}`);
    
    // 1. Extract PDF content
    console.log('📄 Extracting PDF content...');
    const buffer = fs.readFileSync(filePath);
    const { text, metadata: pdfMetadata } = await extractPDFContent(buffer);
    
    if (!text || text.length < 200) {
      throw new Error('PDF contains insufficient text content');
    }
    
    context.metadata = { ...context.metadata, ...pdfMetadata };
    
    // 2. Intelligent chunking
    console.log('✂️  Chunking content intelligently...');
    const chunks = chunkTextIntelligently(text);
    console.log(`📊 Created ${chunks.length} chunks from ${text.length} characters`);
    
    // 3. Process chunks in batches
    let allNodes: any[] = [];
    let allEdges: any[] = [];
    let allCulturalFlags: string[] = [];
    
    for (let i = 0; i < chunks.length; i += config.processing.batchSize) {
      const batch = chunks.slice(i, i + config.processing.batchSize);
      console.log(`🔄 Processing batch ${Math.floor(i / config.processing.batchSize) + 1} (chunks ${i + 1}-${Math.min(i + batch.length, chunks.length)})`);
      
      const batchPromises = batch.map(async (chunk, batchIndex) => {
        try {
          const chunkTitle = `${context.sourceTitle} (chunk ${i + batchIndex + 1})`;
          const extracted = await extractWithRetry(chunk, chunkTitle, context.sourceUrl);
          
          return {
            success: true,
            nodes: extracted.nodes || [],
            edges: extracted.edges || [],
            cultural_flags: extracted.cultural_flags || [],
            quality_notes: extracted.quality_notes || []
          };
        } catch (error: any) {
          console.error(`❌ Failed to process chunk ${i + batchIndex + 1}:`, error.message);
          return {
            success: false,
            error: error.message,
            nodes: [],
            edges: [],
            cultural_flags: [],
            quality_notes: []
          };
        }
      });
      
      const batchResults = await Promise.all(batchPromises);
      
      // Aggregate results
      batchResults.forEach(result => {
        if (result.success) {
          allNodes.push(...result.nodes);
          allEdges.push(...result.edges);
          allCulturalFlags.push(...result.cultural_flags);
        }
      });
      
      // Brief pause between batches to avoid overwhelming services
      if (i + config.processing.batchSize < chunks.length) {
        await new Promise(resolve => setTimeout(resolve, 1000));
      }
    }
    
    // 4. Quality filtering
    const highQualityNodes = allNodes.filter(node => 
      (node.confidence || 0) >= config.processing.qualityThreshold &&
      node.title && node.title.length > 3
    );
    
    console.log(`🎯 Quality filtering: ${highQualityNodes.length}/${allNodes.length} nodes passed threshold`);
    
    // 5. Store in knowledge graph
    console.log('💾 Storing knowledge nodes...');
    const nodeMapping = await storeKnowledgeNodes(highQualityNodes, context);
    
    console.log('🔗 Storing knowledge edges...');
    await storeKnowledgeEdges(allEdges, nodeMapping, context);
    
    // 6. Summary and logging
    const processingTime = Date.now() - startTime;
    const result = {
      success: true,
      documentId,
      nodesCreated: nodeMapping.size,
      edgesCreated: allEdges.length,
      processingTime,
      culturalFlags: Array.from(new Set(allCulturalFlags)),
      chunks_processed: chunks.length,
      avg_confidence: allNodes.reduce((sum, n) => sum + (n.confidence || 0), 0) / Math.max(allNodes.length, 1)
    };
    
    await logProcessingJob(context, result, 'completed');
    
    console.log('🎉 Document ingestion completed successfully!');
    console.log(`📊 Results: ${result.nodesCreated} nodes, ${result.edgesCreated} edges`);
    console.log(`⏱️  Processing time: ${(processingTime / 1000).toFixed(1)}s`);
    console.log(`🛡️  Cultural flags: ${result.culturalFlags.join(', ') || 'none'}`);
    
    return result;
    
  } catch (error: any) {
    const processingTime = Date.now() - startTime;
    console.error(`❌ Document ingestion failed: ${error.message}`);
    
    const result = {
      success: false,
      documentId,
      nodesCreated: 0,
      edgesCreated: 0,
      processingTime,
      culturalFlags: [],
      error: error.message
    };
    
    await logProcessingJob(context, result, 'failed');
    
    return result;
  }
}

/**
 * Batch process multiple documents
 */
export async function ingestDocumentBatch(filePaths: string[], options: {
  baseUrl?: string;
  metadata?: any;
  concurrent?: number;
} = {}): Promise<any[]> {
  const concurrent = options.concurrent || 2; // Process 2 docs at a time to avoid overload
  const results: any[] = [];
  
  console.log(`🔄 Starting batch ingestion: ${filePaths.length} documents (${concurrent} concurrent)`);
  
  for (let i = 0; i < filePaths.length; i += concurrent) {
    const batch = filePaths.slice(i, i + concurrent);
    
    const batchPromises = batch.map(async (filePath) => {
      const sourceTitle = path.basename(filePath, path.extname(filePath));
      const sourceUrl = options.baseUrl ? `${options.baseUrl}/${sourceTitle}` : undefined;
      
      return ingestDocument(filePath, {
        sourceTitle,
        sourceUrl,
        metadata: options.metadata
      });
    });
    
    const batchResults = await Promise.all(batchPromises);
    results.push(...batchResults);
    
    console.log(`✅ Completed batch ${Math.floor(i / concurrent) + 1}/${Math.ceil(filePaths.length / concurrent)}`);
  }
  
  const successful = results.filter(r => r.success).length;
  const totalNodes = results.reduce((sum, r) => sum + r.nodesCreated, 0);
  const totalEdges = results.reduce((sum, r) => sum + r.edgesCreated, 0);
  
  console.log('🎊 Batch ingestion completed!');
  console.log(`📊 Results: ${successful}/${filePaths.length} documents successful`);
  console.log(`🧠 Knowledge created: ${totalNodes} nodes, ${totalEdges} edges`);
  
  return results;
}

// ========================================
// CLI INTERFACE
// ========================================

async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log('🧠 Kaitiaki Aronui Cerebellum - Document Ingestion System');
    console.log('');
    console.log('Usage:');
    console.log('  Single document: node kaitiaki-cerebellum.ts <pdf-file> [title]');
    console.log('  Batch process:   node kaitiaki-cerebellum.ts --batch <directory>');
    console.log('');
    console.log('Examples:');
    console.log('  node kaitiaki-cerebellum.ts unit-plan.pdf "Year 8 Social Studies"');
    console.log('  node kaitiaki-cerebellum.ts --batch ./curriculum-docs/');
    console.log('');
    console.log('🧺 "Whaowhia te kete mātauranga" - Fill the basket of knowledge');
    process.exit(0);
  }
  
  if (args[0] === '--batch') {
    const directory = args[1];
    if (!directory || !fs.existsSync(directory)) {
      console.error('❌ Directory not found:', directory);
      process.exit(1);
    }
    
    const pdfFiles = fs.readdirSync(directory)
      .filter(file => file.endsWith('.pdf'))
      .map(file => path.join(directory, file));
      
    if (pdfFiles.length === 0) {
      console.error('❌ No PDF files found in directory:', directory);
      process.exit(1);
    }
    
    await ingestDocumentBatch(pdfFiles);
  } else {
    const filePath = args[0];
    const sourceTitle = args[1];
    
    if (!fs.existsSync(filePath)) {
      console.error('❌ File not found:', filePath);
      process.exit(1);
    }
    
    await ingestDocument(filePath, { sourceTitle });
  }
}

// Run if called directly
if (require.main === module) {
  main().catch(error => {
    console.error('💥 Fatal error:', error);
    process.exit(1);
  });
}