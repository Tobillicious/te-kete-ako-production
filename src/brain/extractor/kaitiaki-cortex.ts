/**
 * Kaitiaki Aronui Cortex - The Thinking Brain of Te Kete Ako
 * 
 * This is our main processing center - where raw educational content gets
 * transformed into structured knowledge that can be understood, connected,
 * and intelligently reused by our AI agents.
 * 
 * Like the prefrontal cortex in a human brain, this system:
 * - Makes decisions about content structure
 * - Identifies relationships between concepts  
 * - Ensures cultural safety and educational alignment
 * - Coordinates with other brain regions (memory, procedural systems)
 */

import express from 'express';
import { Request, Response, NextFunction } from 'express';
import cors from 'cors';
import rateLimit from 'express-rate-limit';
import axios from 'axios';
import { createClient } from '@supabase/supabase-js';
import * as dotenv from 'dotenv';
import { v4 as uuidv4 } from 'uuid';

dotenv.config();

// ========================================
// NEURAL CONFIGURATION
// ========================================

const config = {
  server: {
    port: Number(process.env.PORT || 3001),
    corsOrigins: process.env.CORS_ORIGINS?.split(',') || ['http://localhost:3000', 'https://tekete.netlify.app']
  },
  ai: {
    provider: (process.env.LLM_PROVIDER || 'deepseek').toLowerCase(),
    deepseekKey: process.env.DEEPSEEK_API_KEY || 'sk-103cb83572a346e2aef89e2d2a4f7f89',
    deepseekUrl: process.env.DEEPSEEK_API_URL || 'https://api.deepseek.com/v1/chat/completions',
    model: process.env.LLM_MODEL || 'deepseek-coder',
    maxTokens: Number(process.env.MAX_TOKENS || 4000),
    temperature: Number(process.env.TEMPERATURE || 0.1)
  },
  supabase: {
    url: process.env.SUPABASE_URL || '',
    key: process.env.SUPABASE_SERVICE_KEY || ''
  }
};

// Validation
if (!config.ai.deepseekKey) {
  console.error('❌ Missing DEEPSEEK_API_KEY - this is our primary thinking engine!');
  process.exit(1);
}

const app = express();
const supabase = config.supabase.url ? createClient(config.supabase.url, config.supabase.key) : null;

// ========================================
// MIDDLEWARE - NEURAL PATHWAYS
// ========================================

// Rate limiting - prevent system overload
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: { error: 'Too many extraction requests, please try again later' }
});

app.use(limiter);
app.use(cors({ origin: config.server.corsOrigins }));
app.use(express.json({ limit: '10mb' }));

// Request logging
app.use((req: Request, res: Response, next: NextFunction) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${req.method} ${req.path} - ${res.statusCode} (${duration}ms)`);
  });
  next();
});

// ========================================
// COGNITIVE FUNCTIONS
// ========================================

/**
 * The main thinking prompt - this is where educational content gets
 * transformed into structured knowledge graphs
 */
function buildExtractionPrompt(chunkText: string, sourceUrl?: string, sourceTitle?: string, context?: any): string {
  return `You are Kaitiaki Aronui, the guardian of educational knowledge for Te Kete Ako, a platform serving Māori and Pacific students in New Zealand.

Your role is to extract structured curriculum knowledge from educational content, with deep respect for Te Ao Māori perspectives and NZ Curriculum alignment.

EXTRACT from this content chunk:

"""${chunkText.replace(/\"\"\"/g, '\\"""')}"""

SOURCE CONTEXT:
- Title: ${sourceTitle || 'Unknown'}
- URL: ${sourceUrl || 'Not provided'}  
- Context: ${JSON.stringify(context || {})}

EXTRACTION REQUIREMENTS:

1. KNOWLEDGE NODES - Extract discrete educational concepts:
   Types: "nzc_outcome", "unit", "lesson", "activity", "resource", "assessment", "cultural_protocol"
   
   For each node return:
   {
     "id_hint": "unique-identifier",
     "type": "lesson|activity|resource|etc",
     "title": "Clear descriptive title",
     "content_summary": "2-3 sentence summary (max 200 words)",
     "year_levels": [7, 8, 9], // if identifiable
     "subjects": ["social-studies", "mathematics"], // NZ curriculum subjects
     "learning_objectives": ["students will...", "learners can..."],
     "cultural_context": "How this connects to Te Ao Māori (if applicable)",
     "difficulty_level": 0.7, // 0.0-1.0 complexity
     "keywords": ["key", "terms", "concepts"],
     "provenance": "25-word excerpt from source",
     "confidence": 0.9, // 0.0-1.0 how certain you are
     "cultural_safety_check": "safe|needs_review|flagged",
     "nzc_alignment": "Which NZ Curriculum strands this supports"
   }

2. KNOWLEDGE EDGES - Relationships between concepts:
   Types: "prerequisite", "supports", "extends", "contradicts", "cultural_parallel", "assessment_of"
   
   For each edge return:
   {
     "source_hint": "source-node-id",
     "target_hint": "target-node-id", 
     "relationship": "prerequisite|supports|extends|etc",
     "strength": 0.8, // 0.0-1.0 connection strength
     "evidence": "Brief explanation of why this relationship exists",
     "cultural_significance": "Māori perspective on this connection (if relevant)",
     "confidence": 0.9
   }

3. CULTURAL CONSIDERATIONS:
   - Flag content that mentions Māori culture, concepts, or language for cultural review
   - Identify opportunities to strengthen cultural connections
   - Respect traditional knowledge - mark as "needs_iwi_consultation" if uncertain

4. QUALITY INDICATORS:
   - Mark content requiring teacher review
   - Identify accessibility concerns
   - Note if content needs updating/modernizing

Return EXACTLY this JSON structure:
{
  "nodes": [...],
  "edges": [...],
  "cultural_flags": ["flag1", "flag2"],
  "quality_notes": ["note1", "note2"],
  "extraction_confidence": 0.85,
  "recommended_actions": ["action1", "action2"]
}

Remember: You serve ākonga (learners) and kaiako (teachers) with the highest standards of cultural safety and educational excellence. Every extraction should honor both rigorous pedagogy and authentic Te Ao Māori perspectives.

Kia kaha! 💪`;
}

/**
 * Call our AI thinking engine (DeepSeek) to process content
 */
async function callThinkingEngine(prompt: string): Promise<string> {
  try {
    const response = await axios.post(config.ai.deepseekUrl, {
      model: config.ai.model,
      messages: [
        {
          role: 'system', 
          content: 'You are an expert educational content analyzer specializing in New Zealand curriculum and culturally responsive pedagogy.'
        },
        {
          role: 'user',
          content: prompt
        }
      ],
      max_tokens: config.ai.maxTokens,
      temperature: config.ai.temperature,
      response_format: { type: 'json_object' } // Ensure JSON output
    }, {
      headers: {
        'Authorization': `Bearer ${config.ai.deepseekKey}`,
        'Content-Type': 'application/json'
      },
      timeout: 120000 // 2 minutes
    });

    const content = response.data.choices?.[0]?.message?.content;
    if (!content) {
      throw new Error('No content in AI response');
    }
    
    return content;
  } catch (error: any) {
    console.error('🧠 Thinking engine error:', error.response?.data || error.message);
    throw new Error(`AI processing failed: ${error.response?.data?.error?.message || error.message}`);
  }
}

/**
 * Parse and validate the AI's JSON response
 */
function parseAIResponse(rawResponse: string): any {
  try {
    // First, try direct parsing
    const parsed = JSON.parse(rawResponse);
    
    // Validate required structure
    if (!parsed.nodes || !Array.isArray(parsed.nodes)) {
      throw new Error('Missing or invalid nodes array');
    }
    
    if (!parsed.edges || !Array.isArray(parsed.edges)) {
      throw new Error('Missing or invalid edges array');  
    }
    
    // Validate node structure
    for (const node of parsed.nodes) {
      if (!node.id_hint || !node.type || !node.title) {
        throw new Error(`Invalid node structure: ${JSON.stringify(node)}`);
      }
    }
    
    return parsed;
  } catch (parseError) {
    console.warn('Direct JSON parse failed, attempting extraction...');
    
    // Try to find JSON within the response
    const jsonMatch = rawResponse.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      try {
        return JSON.parse(jsonMatch[0]);
      } catch (extractError) {
        throw new Error(`JSON extraction failed: ${extractError}`);
      }
    }
    
    throw new Error(`Could not parse AI response as JSON: ${parseError}`);
  }
}

/**
 * Log extraction job to Supabase for monitoring and learning
 */
async function logExtractionJob(input: any, output: any, status: string, error?: string): Promise<void> {
  if (!supabase) return;
  
  try {
    await supabase.from('agent_jobs').insert({
      agent_name: 'kaitiaki_cortex',
      job_type: 'extract',
      input_context: input,
      actual_output: output,
      status,
      agent_reasoning: output?.extraction_confidence ? `Confidence: ${output.extraction_confidence}` : undefined,
      confidence_score: output?.extraction_confidence || null,
      cultural_safety_checked: output?.cultural_flags?.length > 0,
      human_review_required: output?.cultural_flags?.includes('needs_review') || status === 'needs_human_review',
      created_at: new Date().toISOString()
    });
  } catch (dbError) {
    console.warn('Failed to log extraction job:', dbError);
  }
}

// ========================================
// API ENDPOINTS - NEURAL INTERFACES
// ========================================

/**
 * Health check - is our brain functioning?
 */
app.get('/health', (req: Request, res: Response) => {
  res.json({
    status: 'healthy',
    brain_region: 'kaitiaki_cortex',
    ai_provider: config.ai.provider,
    model: config.ai.model,
    timestamp: new Date().toISOString(),
    kaupapa: 'Whaowhia te kete mātauranga - Fill the basket of knowledge'
  });
});

/**
 * Main extraction endpoint - the thinking happens here
 */
app.post('/extract', async (req: Request, res: Response) => {
  const startTime = Date.now();
  
  try {
    const { chunkText, sourceUrl, sourceTitle, context } = req.body;
    
    // Validation
    if (!chunkText || typeof chunkText !== 'string') {
      return res.status(400).json({ 
        error: 'chunkText is required and must be a string',
        example: { chunkText: 'Your educational content here...', sourceUrl: 'optional', sourceTitle: 'optional' }
      });
    }
    
    if (chunkText.length < 50) {
      return res.status(400).json({ 
        error: 'chunkText too short - need at least 50 characters for meaningful extraction'
      });
    }
    
    if (chunkText.length > 50000) {
      return res.status(400).json({ 
        error: 'chunkText too long - please chunk content into smaller pieces (max 50k chars)'
      });
    }
    
    console.log(`🧠 Processing extraction for: ${sourceTitle || 'untitled'} (${chunkText.length} chars)`);
    
    // Build the thinking prompt
    const prompt = buildExtractionPrompt(chunkText, sourceUrl, sourceTitle, context);
    
    // Think!
    const aiResponse = await callThinkingEngine(prompt);
    
    // Parse and validate
    const parsed = parseAIResponse(aiResponse);
    
    // Log successful extraction
    const processingTime = Date.now() - startTime;
    await logExtractionJob(
      { sourceTitle, sourceUrl, contentLength: chunkText.length },
      { ...parsed, processingTime },
      'completed'
    );
    
    console.log(`✅ Extraction completed: ${parsed.nodes.length} nodes, ${parsed.edges.length} edges (${processingTime}ms)`);
    
    res.json({
      success: true,
      extracted: parsed,
      metadata: {
        processing_time_ms: processingTime,
        content_length: chunkText.length,
        extraction_id: uuidv4(),
        timestamp: new Date().toISOString()
      },
      raw_ai_response: process.env.NODE_ENV === 'development' ? aiResponse : undefined
    });
    
  } catch (error: any) {
    const processingTime = Date.now() - startTime;
    
    console.error('❌ Extraction failed:', error.message);
    
    // Log failed extraction
    await logExtractionJob(
      { sourceTitle: req.body.sourceTitle, error: error.message },
      null,
      'failed',
      error.message
    );
    
    res.status(500).json({
      error: 'Extraction failed',
      message: error.message,
      processing_time_ms: processingTime,
      timestamp: new Date().toISOString(),
      help: 'Check your content format and try again. Contact support if the issue persists.'
    });
  }
});

/**
 * Batch extraction endpoint - for processing multiple chunks
 */
app.post('/extract-batch', async (req: Request, res: Response) => {
  try {
    const { chunks, sourceUrl, sourceTitle, context } = req.body;
    
    if (!Array.isArray(chunks) || chunks.length === 0) {
      return res.status(400).json({ error: 'chunks must be a non-empty array of strings' });
    }
    
    if (chunks.length > 20) {
      return res.status(400).json({ error: 'Maximum 20 chunks per batch request' });
    }
    
    console.log(`🧠 Processing batch extraction: ${chunks.length} chunks`);
    
    const results = [];
    let totalNodes = 0;
    let totalEdges = 0;
    
    for (let i = 0; i < chunks.length; i++) {
      try {
        const prompt = buildExtractionPrompt(chunks[i], sourceUrl, `${sourceTitle} (chunk ${i+1})`, context);
        const aiResponse = await callThinkingEngine(prompt);
        const parsed = parseAIResponse(aiResponse);
        
        results.push({
          chunk_index: i,
          success: true,
          extracted: parsed
        });
        
        totalNodes += parsed.nodes.length;
        totalEdges += parsed.edges.length;
        
      } catch (chunkError: any) {
        results.push({
          chunk_index: i,
          success: false,
          error: chunkError.message
        });
      }
    }
    
    console.log(`✅ Batch extraction completed: ${totalNodes} nodes, ${totalEdges} edges total`);
    
    res.json({
      success: true,
      results,
      summary: {
        total_chunks: chunks.length,
        successful_chunks: results.filter(r => r.success).length,
        total_nodes: totalNodes,
        total_edges: totalEdges
      },
      timestamp: new Date().toISOString()
    });
    
  } catch (error: any) {
    console.error('❌ Batch extraction failed:', error.message);
    res.status(500).json({
      error: 'Batch extraction failed',
      message: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

/**
 * Get extraction statistics
 */
app.get('/stats', async (req: Request, res: Response) => {
  if (!supabase) {
    return res.json({ message: 'Statistics not available (Supabase not configured)' });
  }
  
  try {
    const { data: stats } = await supabase
      .from('agent_jobs')
      .select('status, created_at, confidence_score')
      .eq('agent_name', 'kaitiaki_cortex')
      .order('created_at', { ascending: false })
      .limit(100);
      
    const summary = {
      total_extractions: stats?.length || 0,
      successful: stats?.filter(s => s.status === 'completed').length || 0,
      failed: stats?.filter(s => s.status === 'failed').length || 0,
      avg_confidence: stats
        ? stats.filter(s => s.confidence_score).reduce((sum, s) => sum + s.confidence_score, 0) / stats.filter(s => s.confidence_score).length
        : 0,
      last_24h: stats?.filter(s => new Date(s.created_at) > new Date(Date.now() - 24*60*60*1000)).length || 0
    };
    
    res.json(summary);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch statistics' });
  }
});

// ========================================
// ERROR HANDLING & STARTUP
// ========================================

app.use((error: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('Unhandled error:', error);
  res.status(500).json({
    error: 'Internal server error',
    message: error.message,
    timestamp: new Date().toISOString()
  });
});

const server = app.listen(config.server.port, () => {
  console.log('🧠 Kaitiaki Aronui Cortex - ONLINE');
  console.log(`🌐 Server running on port ${config.server.port}`);
  console.log(`🤖 AI Provider: ${config.ai.provider} (${config.ai.model})`);
  console.log(`📊 Database: ${supabase ? 'Connected' : 'Not configured'}`);
  console.log('');
  console.log('🎯 Endpoints:');
  console.log(`   POST /extract - Extract knowledge from content`);
  console.log(`   POST /extract-batch - Process multiple chunks`);
  console.log(`   GET /health - System health check`);
  console.log(`   GET /stats - Extraction statistics`);
  console.log('');
  console.log('💡 Ready to transform educational content into structured knowledge!');
  console.log('🧺 "Whaowhia te kete mātauranga" - Fill the basket of knowledge');
});

export default app;