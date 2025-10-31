#!/usr/bin/env python3
"""
Generate embeddings for all curriculum statements in Supabase.

This script supports multiple embedding providers:
1. LOCAL (FREE) - sentence-transformers (RECOMMENDED)
2. GEMINI - Google Gemini embeddings (if you have GEMINI_API_KEY)

Usage:
    python generate_embeddings.py [--provider local|gemini]

Requirements:
    pip install sentence-transformers supabase python-dotenv tqdm
"""

import os
import sys
import time
import argparse
from typing import List, Dict, Any
from dotenv import load_dotenv
from supabase import create_client, Client
import numpy as np

# Load environment variables
load_dotenv()

# Determine which provider to use
PROVIDER = os.getenv("EMBEDDING_PROVIDER", "local").lower()

# Initialize embedding model based on provider
embedding_model = None
EMBEDDING_DIMENSIONS = 1536  # Will be updated based on model

def initialize_embedder(provider: str):
    """Initialize the embedding model based on provider."""
    global embedding_model, EMBEDDING_DIMENSIONS
    
    print(f"🔧 Initializing {provider.upper()} embeddings...")
    
    if provider == "local":
        # FREE local embeddings using sentence-transformers
        from sentence_transformers import SentenceTransformer
        print("   📥 Loading sentence-transformers model...")
        print("   (First run will download ~400MB model - subsequent runs are instant)")
        
        # Use a high-quality model that outputs 768 dimensions
        # We'll pad it to 1536 to match pgvector setup
        embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        EMBEDDING_DIMENSIONS = 384  # This model outputs 384 dims
        print(f"   ✅ Model loaded: all-MiniLM-L6-v2 ({EMBEDDING_DIMENSIONS} dimensions)")
        print("   💰 Cost: FREE! No API key needed!")
        
    elif provider == "gemini":
        # Google Gemini embeddings
        import google.generativeai as genai
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ GEMINI_API_KEY not found in .env file")
            sys.exit(1)
        
        genai.configure(api_key=api_key)
        embedding_model = genai
        EMBEDDING_DIMENSIONS = 768  # Gemini embedding dimensions
        print(f"   ✅ Gemini configured ({EMBEDDING_DIMENSIONS} dimensions)")
        print("   💰 Cost: Very low (~$0.01 for all 3,445 statements)")
        
    else:
        print(f"❌ Unknown provider: {provider}")
        print("   Supported providers: local, gemini")
        sys.exit(1)

# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

if not supabase_url or not supabase_key:
    print("❌ Missing Supabase credentials!")
    print("   Please set SUPABASE_URL and SUPABASE_SERVICE_KEY in .env")
    sys.exit(1)

supabase: Client = create_client(supabase_url, supabase_key)

# Configuration
BATCH_SIZE = 100  # Process in batches
DELAY_BETWEEN_BATCHES = 0.5  # seconds


def pad_embedding(embedding: List[float], target_dim: int = 1536) -> List[float]:
    """Pad embedding to target dimensions with zeros."""
    if len(embedding) >= target_dim:
        return embedding[:target_dim]
    return embedding + [0.0] * (target_dim - len(embedding))


def fetch_statements_without_embeddings() -> List[Dict[str, Any]]:
    """Fetch all curriculum statements that don't have embeddings yet."""
    print("📥 Fetching statements without embeddings...")
    
    response = supabase.table("curriculum_statements") \
        .select("id, statement_text, learning_area, phase") \
        .is_("embedding", "null") \
        .execute()
    
    print(f"✅ Found {len(response.data)} statements needing embeddings")
    return response.data


def generate_embedding_local(text: str) -> List[float]:
    """Generate embedding using local sentence-transformers model."""
    embedding = embedding_model.encode(text, convert_to_numpy=True)
    # Pad to 1536 dimensions for compatibility with pgvector index
    return pad_embedding(embedding.tolist(), 1536)


def generate_embedding_gemini(text: str) -> List[float]:
    """Generate embedding using Google Gemini."""
    result = embedding_model.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    embedding = result['embedding']
    # Pad to 1536 dimensions
    return pad_embedding(embedding, 1536)


def generate_embeddings_batch(texts: List[str], provider: str) -> List[List[float]]:
    """Generate embeddings for a batch of texts."""
    if provider == "local":
        # Batch encoding is much faster
        embeddings = embedding_model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
        return [pad_embedding(emb.tolist(), 1536) for emb in embeddings]
    
    elif provider == "gemini":
        # Gemini batch processing
        return [generate_embedding_gemini(text) for text in texts]
    
    else:
        raise ValueError(f"Unknown provider: {provider}")


def update_statement_embedding(statement_id: int, embedding: List[float]) -> None:
    """Update a single statement with its embedding."""
    supabase.table("curriculum_statements") \
        .update({"embedding": embedding}) \
        .eq("id", statement_id) \
        .execute()


def process_statements_in_batches(statements: List[Dict[str, Any]], provider: str) -> None:
    """Process all statements in batches to generate and store embeddings."""
    total = len(statements)
    processed = 0
    errors = 0
    
    print(f"\n🚀 Starting embedding generation for {total} statements...")
    print(f"📊 Processing in batches of {BATCH_SIZE}")
    print(f"🔧 Provider: {provider.upper()}")
    print("=" * 60)
    
    start_time = time.time()
    
    for i in range(0, total, BATCH_SIZE):
        batch = statements[i:i + BATCH_SIZE]
        batch_num = (i // BATCH_SIZE) + 1
        total_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
        
        print(f"\n📦 Batch {batch_num}/{total_batches} ({len(batch)} statements)")
        
        try:
            # Extract texts for batch processing
            texts = [stmt["statement_text"] for stmt in batch]
            
            # Generate embeddings for the entire batch
            print(f"   🤖 Generating embeddings...")
            embeddings = generate_embeddings_batch(texts, provider)
            
            # Update database with embeddings
            print(f"   💾 Updating database...")
            for stmt, embedding in zip(batch, embeddings):
                update_statement_embedding(stmt["id"], embedding)
                processed += 1
            
            # Progress update
            progress_pct = (processed / total) * 100
            elapsed = time.time() - start_time
            rate = processed / elapsed if elapsed > 0 else 0
            remaining = (total - processed) / rate if rate > 0 else 0
            
            print(f"   ✅ Progress: {processed}/{total} ({progress_pct:.1f}%)")
            print(f"   ⏱️  Rate: {rate:.1f} statements/sec")
            print(f"   🕐 Est. remaining: {remaining/60:.1f} minutes")
            
            # Rate limiting delay (except for last batch)
            if i + BATCH_SIZE < total:
                time.sleep(DELAY_BETWEEN_BATCHES)
                
        except Exception as e:
            errors += 1
            print(f"   ❌ Error processing batch: {e}")
            print(f"   ⏭️  Skipping to next batch...")
            continue
    
    # Final summary
    elapsed_total = time.time() - start_time
    print("\n" + "=" * 60)
    print("🎉 EMBEDDING GENERATION COMPLETE!")
    print("=" * 60)
    print(f"✅ Successfully processed: {processed}/{total} statements")
    print(f"❌ Errors: {errors} batches")
    print(f"⏱️  Total time: {elapsed_total/60:.1f} minutes")
    
    if provider == "local":
        print(f"💰 Cost: $0.00 (FREE!)")
    elif provider == "gemini":
        print(f"💰 Estimated cost: ${(processed * 0.000003):.4f}")
    
    print("=" * 60)


def verify_embeddings() -> None:
    """Verify that all statements now have embeddings."""
    print("\n🔍 Verifying embeddings...")
    
    response = supabase.table("curriculum_statements") \
        .select("id", count="exact") \
        .is_("embedding", "null") \
        .execute()
    
    remaining = response.count
    
    if remaining == 0:
        print("✅ Perfect! All statements now have embeddings!")
    else:
        print(f"⚠️  Warning: {remaining} statements still missing embeddings")


def main():
    """Main execution function."""
    # Parse arguments
    parser = argparse.ArgumentParser(description="Generate curriculum embeddings")
    parser.add_argument(
        "--provider",
        choices=["local", "gemini"],
        default="local",
        help="Embedding provider (default: local - FREE!)"
    )
    args = parser.parse_args()
    
    provider = args.provider
    
    print("=" * 60)
    print("🧠 CURRICULUM EMBEDDING GENERATION")
    print("=" * 60)
    
    # Initialize embedding model
    initialize_embedder(provider)
    
    print("=" * 60)
    
    # Fetch statements
    statements = fetch_statements_without_embeddings()
    
    if not statements:
        print("\n✅ No statements need embeddings. All done!")
        return
    
    # Estimate
    if provider == "local":
        print(f"\n💰 Cost: FREE! (No API key needed)")
        print(f"⏱️  Estimated time: {len(statements) / 100:.1f} minutes")
    elif provider == "gemini":
        estimated_cost = len(statements) * 0.000003  # Very rough estimate
        print(f"\n💰 Estimated cost: ${estimated_cost:.4f}")
        print(f"⏱️  Estimated time: {len(statements) / 50:.1f} minutes")
    
    # Confirm before proceeding
    response = input("\n🚀 Ready to generate embeddings? (yes/no): ")
    if response.lower() != "yes":
        print("❌ Cancelled by user")
        return
    
    # Process all statements
    process_statements_in_batches(statements, provider)
    
    # Verify completion
    verify_embeddings()
    
    print("\n🎯 Next steps:")
    print("   1. Test semantic search: python test_semantic_search.py")
    print("   2. Integrate into your application")
    print("   3. Build curriculum-aligned features!")


if __name__ == "__main__":
    main()
