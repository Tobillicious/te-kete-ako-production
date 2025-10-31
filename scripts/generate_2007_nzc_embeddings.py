#!/usr/bin/env python3
"""
Generate embeddings specifically for 2007 NZC curriculum content.

This script generates vector embeddings for the 380 newly extracted 2007 NZC
achievement objectives using FREE local sentence-transformers.

This completes our comprehensive curriculum system with full semantic search
across ALL New Zealand curriculum versions (2007-2025).

Usage:
    python generate_2007_nzc_embeddings.py [--dry-run]
"""

import os
import sys
import time
from typing import List, Dict, Any
from datetime import datetime

from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Supabase setup
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY") or os.getenv("SUPABASE_ANON_KEY")

if not supabase_url or not supabase_key:
    print("❌ Missing SUPABASE_URL or SUPABASE_SERVICE_KEY/SUPABASE_ANON_KEY in .env file")
    sys.exit(1)

supabase: Client = create_client(supabase_url, supabase_key)

# Initialize embedding model
print("🧠 INITIALIZING FREE LOCAL EMBEDDINGS...")
print("   📥 Loading sentence-transformers model...")
print("   (This may take a moment on first run)")

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("   ✅ Model loaded: all-MiniLM-L6-v2 (384 dimensions)")
    print("   💰 Cost: FREE! No API keys needed!")
except ImportError:
    print("❌ sentence-transformers not installed!")
    print("   Install with: pip install sentence-transformers")
    sys.exit(1)


def pad_embedding(embedding: List[float], target_dim: int = 1536) -> List[float]:
    """Pad embedding to 1536 dimensions for pgvector compatibility."""
    if len(embedding) >= target_dim:
        return embedding[:target_dim]
    return embedding + [0.0] * (target_dim - len(embedding))


def fetch_2007_nzc_statements() -> List[Dict[str, Any]]:
    """Fetch all 2007 NZC statements that need embeddings."""
    
    print("📥 Fetching 2007 NZC statements without embeddings...")
    
    try:
        response = supabase.table("curriculum_statements") \
            .select("id, curriculum_version, learning_area, level, strand, statement_text") \
            .eq("curriculum_version", "2007_nzc") \
            .is_("embedding", "null") \
            .execute()
        
        statements = response.data
        print(f"   Found {len(statements)} statements to process")
        
        if statements:
            # Show breakdown by subject
            subject_counts = {}
            for stmt in statements:
                subject = stmt['learning_area']
                subject_counts[subject] = subject_counts.get(subject, 0) + 1
            
            print("   📊 Breakdown by subject:")
            for subject, count in sorted(subject_counts.items()):
                print(f"      {subject}: {count} objectives")
        
        return statements
        
    except Exception as e:
        print(f"❌ Error fetching statements: {e}")
        sys.exit(1)


def generate_embeddings_batch(statements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Generate embeddings for a batch of statements."""
    
    if not statements:
        return []
    
    # Extract texts for batch processing
    texts = [stmt['statement_text'] for stmt in statements]
    
    print(f"   🧠 Generating embeddings for {len(texts)} statements...")
    start_time = time.time()
    
    try:
        # Generate embeddings in batch (much faster than one-by-one)
        embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
        
        # Pad to 1536 dimensions and convert to lists
        padded_embeddings = [pad_embedding(emb.tolist(), 1536) for emb in embeddings]
        
        # Combine with statement data
        updates = []
        for i, stmt in enumerate(statements):
            updates.append({
                'id': stmt['id'],
                'embedding': padded_embeddings[i]
            })
        
        elapsed = time.time() - start_time
        print(f"   ✅ Generated {len(embeddings)} embeddings in {elapsed:.1f}s")
        print(f"   📏 Dimensions: {len(padded_embeddings[0])} (padded to pgvector format)")
        
        return updates
        
    except Exception as e:
        print(f"❌ Error generating embeddings: {e}")
        raise


def update_embeddings_in_database(updates: List[Dict[str, Any]]) -> None:
    """Update the database with generated embeddings."""
    
    if not updates:
        print("No updates to apply")
        return
    
    print(f"📤 Updating {len(updates)} statements in database...")
    
    batch_size = 50
    total_updated = 0
    
    for i in range(0, len(updates), batch_size):
        batch = updates[i:i + batch_size]
        
        try:
            # Update each statement with its embedding
            for update in batch:
                supabase.table("curriculum_statements") \
                    .update({"embedding": update["embedding"]}) \
                    .eq("id", update["id"]) \
                    .execute()
            
            total_updated += len(batch)
            print(f"   ✅ Updated batch {i // batch_size + 1} ({len(batch)} statements) - Total: {total_updated}")
            
            # Brief pause to be respectful to database
            time.sleep(0.1)
            
        except Exception as e:
            print(f"❌ Error updating batch {i // batch_size + 1}: {e}")
            raise
    
    print(f"🎉 Successfully updated {total_updated} statements with embeddings!")


def verify_embeddings() -> None:
    """Verify that all 2007 NZC statements now have embeddings."""
    
    print("🔍 Verifying embedding generation...")
    
    try:
        # Check remaining statements without embeddings
        remaining = supabase.table("curriculum_statements") \
            .select("id", count="exact") \
            .eq("curriculum_version", "2007_nzc") \
            .is_("embedding", "null") \
            .execute()
        
        # Check statements with embeddings
        with_embeddings = supabase.table("curriculum_statements") \
            .select("id", count="exact") \
            .eq("curriculum_version", "2007_nzc") \
            .not_.is_("embedding", "null") \
            .execute()
        
        print(f"   2007 NZC statements WITHOUT embeddings: {remaining.count}")
        print(f"   2007 NZC statements WITH embeddings: {with_embeddings.count}")
        
        if remaining.count == 0:
            print("   ✅ All 2007 NZC statements now have embeddings!")
        else:
            print(f"   ⚠️  {remaining.count} statements still need embeddings")
        
        # Check total system status
        total_without = supabase.table("curriculum_statements") \
            .select("id", count="exact") \
            .is_("embedding", "null") \
            .execute()
        
        total_with = supabase.table("curriculum_statements") \
            .select("id", count="exact") \
            .not_.is_("embedding", "null") \
            .execute()
        
        print(f"\\n📊 COMPLETE SYSTEM STATUS:")
        print(f"   Total statements WITH embeddings: {total_with.count}")
        print(f"   Total statements WITHOUT embeddings: {total_without.count}")
        
        if total_without.count == 0:
            print("   🎉 COMPLETE! All curriculum statements have embeddings!")
        
    except Exception as e:
        print(f"❌ Error during verification: {e}")


def main():
    """Main execution function."""
    
    import argparse
    parser = argparse.ArgumentParser(description="Generate embeddings for 2007 NZC curriculum")
    parser.add_argument("--dry-run", action="store_true", help="Preview without updating database")
    args = parser.parse_args()
    
    print("🏔️ 2007 NZC EMBEDDING GENERATOR")
    print("=" * 60)
    print("Generating FREE local embeddings for complete curriculum coverage")
    print("=" * 60)
    
    # Fetch statements to process
    statements = fetch_2007_nzc_statements()
    
    if not statements:
        print("✅ No 2007 NZC statements need embeddings - already complete!")
        verify_embeddings()
        return
    
    if args.dry_run:
        print(f"🔍 DRY RUN: Would generate embeddings for {len(statements)} statements")
        return
    
    # Generate embeddings
    try:
        updates = generate_embeddings_batch(statements)
        
        # Update database
        update_embeddings_in_database(updates)
        
        # Verify completion
        verify_embeddings()
        
        print(f"\\n🚀 SUCCESS! Next steps:")
        print(f"1. Test semantic search: python scripts/test_semantic_search.py")
        print(f"2. Search across ALL curriculum versions (2007-2025)!")
        print(f"3. Generate curriculum-aligned content with full integration!")
        print(f"\\n🧺 Te Kete Ako now has the most comprehensive NZ curriculum")
        print(f"   database with complete semantic search capabilities! ✨")
        
    except Exception as e:
        print(f"❌ Error during embedding generation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()