// 🧠 AI-Enhanced GraphRAG Intelligence
// Uses Claude API to make GraphRAG searches semantic and intelligent

const Anthropic = require('@anthropic-ai/sdk');
const { createClient } = require('@supabase/supabase-js');

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY // Set in Netlify environment variables
});

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_ANON_KEY
);

exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  try {
    const { query, mode } = JSON.parse(event.body);

    switch(mode) {
      case 'semantic_search':
        return await semanticSearch(query);
      
      case 'infer_relationships':
        return await inferRelationships(query);
      
      case 'quality_score':
        return await scoreQuality(query);
      
      case 'teacher_assistant':
        return await teacherAssistant(query);
      
      default:
        return await semanticSearch(query);
    }
  } catch (error) {
    console.error('AI GraphRAG Error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};

// 🔍 SEMANTIC SEARCH - Understand teacher intent, find perfect resources
async function semanticSearch(teacherQuery) {
  console.log('🔍 Semantic search for:', teacherQuery);

  // Step 1: Get GraphRAG context (top resources)
  const { data: resources } = await supabase
    .from('resources')
    .select('*')
    .eq('is_active', true)
    .limit(100);

  // Step 2: Ask Claude to find best matches based on intent
  const message = await anthropic.messages.create({
    model: "claude-3-5-sonnet-20241022",
    max_tokens: 2048,
    messages: [{
      role: "user",
      content: `You are helping a NZ teacher find educational resources.

Teacher query: "${teacherQuery}"

Available resources (sample):
${resources.slice(0, 20).map(r => `- ${r.title} (${r.subject}, ${r.level}): ${r.description}`).join('\n')}

Analyze the teacher's intent and return:
1. Top 5 most relevant resource IDs
2. Why each is relevant
3. Suggested teaching sequence
4. Cultural integration opportunities

Format as JSON.`
    }]
  });

  const aiAnalysis = message.content[0].text;

  return {
    statusCode: 200,
    body: JSON.stringify({
      query: teacherQuery,
      ai_analysis: aiAnalysis,
      resources: resources
    })
  };
}

// 🔗 INFER RELATIONSHIPS - Auto-discover connections between resources
async function inferRelationships(resourceId) {
  console.log('🔗 Inferring relationships for:', resourceId);

  // Get the resource
  const { data: resource } = await supabase
    .from('resources')
    .select('*')
    .eq('id', resourceId)
    .single();

  // Get potential related resources
  const { data: candidates } = await supabase
    .from('resources')
    .select('*')
    .eq('subject', resource.subject)
    .neq('id', resourceId)
    .limit(50);

  // Ask Claude to analyze relationships
  const message = await anthropic.messages.create({
    model: "claude-3-5-sonnet-20241022",
    max_tokens: 2048,
    messages: [{
      role: "user",
      content: `Analyze relationships between resources.

SOURCE: ${resource.title}
Description: ${resource.description}
Subject: ${resource.subject}, Level: ${resource.level}

CANDIDATES:
${candidates.map(c => `${c.id}: ${c.title} (${c.level})`).join('\n')}

For each candidate, determine:
1. Relationship type (prerequisite, follows_from, enriches, alternative_approach, cultural_extension)
2. Confidence (0.0-1.0)
3. Reasoning

Return top 10 relationships as JSON array:
[{"target_id": "...", "type": "...", "confidence": 0.95, "reason": "..."}]`
    }]
  });

  const relationships = JSON.parse(message.content[0].text);

  // Insert into GraphRAG
  for (const rel of relationships) {
    await supabase.from('graphrag_relationships').insert({
      source_path: resource.path,
      target_path: candidates.find(c => c.id === rel.target_id)?.path,
      relationship_type: rel.type,
      confidence: rel.confidence,
      metadata: { ai_inferred: true, reasoning: rel.reason }
    });
  }

  return {
    statusCode: 200,
    body: JSON.stringify({
      resource: resource.title,
      relationships_found: relationships.length,
      relationships
    })
  };
}

// 📊 QUALITY SCORE - AI-powered quality assessment
async function scoreQuality(resourceId) {
  console.log('📊 Scoring quality for:', resourceId);

  const { data: resource } = await supabase
    .from('resources')
    .select('*')
    .eq('id', resourceId)
    .single();

  // Fetch actual content if available
  const contentPreview = resource.description || '';

  const message = await anthropic.messages.create({
    model: "claude-3-5-sonnet-20241022",
    max_tokens: 1024,
    messages: [{
      role: "user",
      content: `Rate this NZ educational resource (0-100 scale):

Title: ${resource.title}
Subject: ${resource.subject}
Level: ${resource.level}
Description: ${contentPreview}

Evaluate:
1. Cultural Integration (0-100): Does it incorporate Māori concepts, Te Reo, tikanga?
2. Pedagogical Quality (0-100): Teaching effectiveness, engagement, differentiation
3. NZ Curriculum Alignment (0-100): How well does it match NZ curriculum standards?
4. Practical Usability (0-100): Can a teacher use this tomorrow with minimal prep?

Return JSON:
{
  "cultural_integration": 85,
  "pedagogical_quality": 90,
  "curriculum_alignment": 95,
  "practical_usability": 88,
  "overall_score": 89,
  "strengths": ["...", "..."],
  "improvements": ["...", "..."]
}`
    }]
  });

  const scores = JSON.parse(message.content[0].text);

  // Update resource with AI scores
  await supabase
    .from('resources')
    .update({
      cultural_elements: {
        ...resource.cultural_elements,
        ai_cultural_score: scores.cultural_integration,
        ai_overall_score: scores.overall_score,
        ai_strengths: scores.strengths,
        ai_improvements: scores.improvements,
        scored_at: new Date().toISOString()
      }
    })
    .eq('id', resourceId);

  return {
    statusCode: 200,
    body: JSON.stringify({
      resource: resource.title,
      scores
    })
  };
}

// 🧑‍🏫 TEACHER ASSISTANT - Answer questions using GraphRAG context
async function teacherAssistant(question) {
  console.log('🧑‍🏫 Teacher assistant question:', question);

  // Get relevant GraphRAG context
  const { data: resources } = await supabase
    .from('resources')
    .select('*')
    .eq('is_active', true)
    .order('featured', { ascending: false })
    .limit(50);

  // Get relationships
  const { data: relationships } = await supabase
    .from('graphrag_relationships')
    .select('*')
    .limit(100);

  // Get synthesis wisdom
  const { data: wisdom } = await supabase
    .from('agent_knowledge')
    .select('*')
    .order('created_at', { ascending: false })
    .limit(10);

  const message = await anthropic.messages.create({
    model: "claude-3-5-sonnet-20241022",
    max_tokens: 2048,
    system: `You are a helpful teaching assistant for Te Kete Ako, a NZ educational platform.
You have access to GraphRAG knowledge including:
- 3,500+ educational resources (lessons, units, handouts, games)
- Relationships between resources (progressions, prerequisites, enrichments)
- Platform wisdom (best practices, cultural integration patterns)

Always:
- Provide specific resource recommendations with paths
- Suggest teaching sequences based on relationships
- Highlight cultural integration opportunities
- Be practical and actionable`,
    messages: [{
      role: "user",
      content: `Teacher question: "${question}"

Available resources:
${resources.slice(0, 20).map(r => `${r.path}: ${r.title} (${r.subject}, ${r.level})`).join('\n')}

Platform wisdom:
${wisdom.map(w => w.source_name + ': ' + w.key_insights?.slice(0, 2).join('; ')).join('\n')}

Provide a helpful, specific answer with resource recommendations.`
    }]
  });

  return {
    statusCode: 200,
    body: JSON.stringify({
      question,
      answer: message.content[0].text
    })
  };
}

