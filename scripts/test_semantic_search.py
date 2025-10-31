#!/usr/bin/env python3
"""
Test semantic search on curriculum statements.

This script works with both local and Gemini embeddings.

Usage:
    python test_semantic_search.py [--provider local|gemini]

Requirements:
    pip install sentence-transformers supabase python-dotenv
"""

import os
import sys
import argparse
from typing import List, Dict, Any
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Determine provider
PROVIDER = os.getenv("EMBEDDING_PROVIDER", "local").lower()
embedding_model = None


def initialize_embedder(provider: str):
    """Initialize the embedding model based on provider."""
    global embedding_model
    
    print(f"🔧 Initializing {provider.upper()} embeddings...")
    
    if provider == "local":
        from sentence_transformers import SentenceTransformer
        print("   📥 Loading model...")
        embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        print("   ✅ Local embeddings ready!")
        
    elif provider == "gemini":
        import google.generativeai as genai
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ GEMINI_API_KEY not found in .env file")
            sys.exit(1)
        genai.configure(api_key=api_key)
        embedding_model = genai
        print("   ✅ Gemini embeddings ready!")
    else:
        print(f"❌ Unknown provider: {provider}")
        sys.exit(1)


def pad_embedding(embedding: List[float], target_dim: int = 1536) -> List[float]:
    """Pad embedding to target dimensions with zeros."""
    if len(embedding) >= target_dim:
        return embedding[:target_dim]
    return embedding + [0.0] * (target_dim - len(embedding))


# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY") or os.getenv("SUPABASE_ANON_KEY")
supabase: Client = create_client(supabase_url, supabase_key)


def generate_query_embedding(query: str, provider: str) -> List[float]:
    """Generate embedding for a search query."""
    if provider == "local":
        embedding = embedding_model.encode(query, convert_to_numpy=True)
        return pad_embedding(embedding.tolist(), 1536)
    
    elif provider == "gemini":
        result = embedding_model.embed_content(
            model="models/embedding-001",
            content=query,
            task_type="retrieval_query"
        )
        return pad_embedding(result['embedding'], 1536)


def semantic_search(
    query: str,
    provider: str,
    limit: int = 10,
    learning_area: str = None,
    phase: str = None
) -> List[Dict[str, Any]]:
    """
    Perform semantic search on curriculum statements.
    
    Args:
        query: Natural language search query
        provider: Embedding provider (local or gemini)
        limit: Maximum number of results to return
        learning_area: Optional filter by learning area
        phase: Optional filter by phase
    
    Returns:
        List of matching curriculum statements with similarity scores
    """
    # Generate embedding for the query
    query_embedding = generate_query_embedding(query, provider)
    
    # Build filter conditions for SQL
    filters = []
    if learning_area:
        filters.append(f"learning_area = '{learning_area}'")
    if phase:
        filters.append(f"phase = '{phase}'")
    
    where_clause = " AND " + " AND ".join(filters) if filters else ""
    
    # Use Supabase vector similarity search
    # Note: Using raw SQL through execute since RPC might not be available
    try:
        # Try using the search function if it exists
        params = {
            'query_embedding': query_embedding,
            'match_threshold': 0.3,  # Lower threshold for better recall
            'match_count': limit,
            'filter_learning_area': learning_area,
            'filter_phase': phase
        }
        
        response = supabase.rpc('search_curriculum_statements', params).execute()
        return response.data
        
    except Exception as e:
        # Fallback to direct SQL query
        print(f"   (Using direct SQL query)")
        
        # Convert embedding list to PostgreSQL array format
        embedding_str = '[' + ','.join(map(str, query_embedding)) + ']'
        
        sql = f"""
        SELECT 
            id,
            curriculum_version,
            learning_area,
            phase,
            year_levels,
            strand,
            sub_strand,
            element,
            statement_text,
            context,
            tahurangi_url,
            1 - (embedding <=> '{embedding_str}'::vector) as similarity
        FROM curriculum_statements
        WHERE embedding IS NOT NULL{where_clause}
        ORDER BY embedding <=> '{embedding_str}'::vector
        LIMIT {limit};
        """
        
        response = supabase.rpc('exec_sql', {'query': sql}).execute()
        return response.data if hasattr(response, 'data') else []


def print_search_results(query: str, results: List[Dict[str, Any]]) -> None:
    """Pretty print search results."""
    print("\n" + "=" * 80)
    print(f"🔍 Query: \"{query}\"")
    print("=" * 80)
    
    if not results:
        print("❌ No results found")
        return
    
    for i, result in enumerate(results, 1):
        similarity = result.get('similarity', 0) * 100
        
        print(f"\n📄 Result {i} - Similarity: {similarity:.1f}%")
        print(f"   Learning Area: {result['learning_area']}")
        print(f"   Phase: {result['phase']}")
        if result.get('strand'):
            print(f"   Strand: {result['strand']}")
        if result.get('element'):
            print(f"   Element: {result['element']}")
        print(f"\n   Statement:")
        statement_text = result['statement_text']
        if len(statement_text) > 200:
            print(f"   {statement_text[:200]}...")
        else:
            print(f"   {statement_text}")
        print(f"\n   URL: {result['tahurangi_url']}")
        print("-" * 80)


def run_example_searches(provider: str):
    """Run a series of example semantic searches."""
    
    print("=" * 80)
    print("🧠 CURRICULUM SEMANTIC SEARCH DEMO")
    print(f"   Provider: {provider.upper()}")
    print("=" * 80)
    
    # Example 1: Cross-curriculum concept search
    print("\n\n🎯 EXAMPLE 1: Cross-Curriculum Concept Search")
    query1 = "critical thinking and analyzing information"
    results1 = semantic_search(query1, provider, limit=5)
    print_search_results(query1, results1)
    
    # Example 2: Cultural concept search
    print("\n\n🎯 EXAMPLE 2: Cultural Concept Search")
    query2 = "identity, belonging, and whakapapa"
    results2 = semantic_search(query2, provider, limit=5)
    print_search_results(query2, results2)
    
    # Example 3: Specific learning area query
    print("\n\n🎯 EXAMPLE 3: Science-specific Query")
    query3 = "environmental sustainability and conservation"
    results3 = semantic_search(query3, provider, limit=5, learning_area="Science")
    print_search_results(query3, results3)
    
    # Example 4: Phase-specific query
    print("\n\n🎯 EXAMPLE 4: Phase 3 (Years 7-8) Query")
    query4 = "data analysis and statistics"
    results4 = semantic_search(query4, provider, limit=5, phase="Phase 3")
    print_search_results(query4, results4)
    
    # Example 5: Digital technology
    print("\n\n🎯 EXAMPLE 5: Digital Technology")
    query5 = "digital citizenship and online safety"
    results5 = semantic_search(query5, provider, limit=5)
    print_search_results(query5, results5)
    
    print("\n\n" + "=" * 80)
    print("✅ Demo complete! Semantic search is working!")
    print("=" * 80)


def interactive_search(provider: str):
    """Run interactive search session."""
    print("\n" + "=" * 80)
    print("🔍 INTERACTIVE SEMANTIC SEARCH")
    print("=" * 80)
    print("Enter your search queries (or 'quit' to exit)")
    print("=" * 80)
    
    while True:
        query = input("\n🔍 Search query: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not query:
            continue
        
        # Ask for filters
        learning_area = input("   Filter by learning area (optional): ").strip() or None
        phase = input("   Filter by phase (optional): ").strip() or None
        
        # Perform search
        results = semantic_search(query, provider, limit=5, learning_area=learning_area, phase=phase)
        print_search_results(query, results)


def main():
    """Main execution function."""
    # Parse arguments
    parser = argparse.ArgumentParser(description="Test curriculum semantic search")
    parser.add_argument(
        "--provider",
        choices=["local", "gemini"],
        default="local",
        help="Embedding provider (default: local)"
    )
    args = parser.parse_args()
    
    provider = args.provider
    
    # Initialize embedding model
    initialize_embedder(provider)
    
    # Check if embeddings exist
    response = supabase.table("curriculum_statements") \
        .select("id", count="exact") \
        .not_.is_("embedding", "null") \
        .execute()
    
    embeddings_count = response.count
    
    if embeddings_count == 0:
        print("\n❌ No embeddings found in database!")
        print("   Please run generate_embeddings.py first")
        return
    
    print(f"\n✅ Found {embeddings_count} curriculum statements with embeddings")
    
    # Run example searches
    run_example_searches(provider)
    
    # Offer interactive mode
    response = input("\n🤔 Would you like to try interactive search? (yes/no): ")
    if response.lower() == "yes":
        interactive_search(provider)


if __name__ == "__main__":
    main()
