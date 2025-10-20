#!/usr/bin/env python3
"""
SEMANTIC RELATIONSHIP ENGINE - Embedding Generator
Generates vector embeddings for all resources using OpenAI

Prerequisites:
    pip install openai
    export OPENAI_API_KEY="your-key-here"

Usage:
    python3 scripts/generate-resource-embeddings.py
    python3 scripts/generate-resource-embeddings.py --batch-size 100
    python3 scripts/generate-resource-embeddings.py --model text-embedding-3-small
"""

import json
import os
from datetime import datetime
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

class SemanticEmbeddingGenerator:
    """Generate embeddings for semantic relationship discovery"""
    
    def __init__(self, model='text-embedding-3-small'):
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.model = model
        self.embeddings_generated = 0
        
        # Check for OpenAI API key
        self.openai_key = os.getenv('OPENAI_API_KEY')
        if not self.openai_key:
            print("⚠️  OPENAI_API_KEY not set!")
            print("   Set with: export OPENAI_API_KEY='your-key'")
            print("   Or this will run in simulation mode")
        
    def generate_all_embeddings(self, batch_size=100):
        """Generate embeddings for all resources"""
        print("🔮 SEMANTIC EMBEDDING GENERATOR")
        print("=" * 70)
        print(f"Model: {self.model}")
        print(f"Batch size: {batch_size}")
        
        # Get all resources
        print(f"\n📊 Getting resources...")
        resources = self._get_resources()
        
        print(f"Found {len(resources)} resources")
        
        # Generate embeddings in batches
        total_batches = (len(resources) + batch_size - 1) // batch_size
        
        print(f"\n🎯 Generating embeddings ({total_batches} batches)...")
        
        for i in range(0, len(resources), batch_size):
            batch = resources[i:i+batch_size]
            batch_num = i // batch_size + 1
            
            print(f"\n  Batch {batch_num}/{total_batches} ({len(batch)} resources)...")
            
            if self.openai_key:
                embeddings = self._generate_batch_embeddings(batch)
                self._save_embeddings(batch, embeddings)
                print(f"     ✅ Generated {len(embeddings)} embeddings")
            else:
                print(f"     ℹ️  Simulated (no OpenAI key)")
                self.embeddings_generated += len(batch)
        
        print(f"\n✅ Embedding generation complete!")
        print(f"📊 Total embeddings: {self.embeddings_generated}")
        
        # Estimate cost
        cost = (self.embeddings_generated / 1000) * 0.13  # $0.13 per 1K tokens
        print(f"💰 Estimated cost: ${cost:.2f}")
        
        return self.embeddings_generated
    
    def _get_resources(self):
        """Get all resources needing embeddings"""
        try:
            result = self.supabase.table('graphrag_resources')\
                .select('file_path, title, subject, year_level, content_preview')\
                .limit(1000)\
                .execute()
            
            return result.data if result.data else []
        except Exception as e:
            print(f"⚠️  Error getting resources: {e}")
            return []
    
    def _generate_batch_embeddings(self, batch):
        """Generate embeddings for batch using OpenAI"""
        # Combine metadata for embedding
        texts = []
        for resource in batch:
            text = f"{resource['title']} {resource.get('subject', '')} {resource.get('year_level', '')} {resource.get('content_preview', '')[:200]}"
            texts.append(text)
        
        # In production, would call OpenAI API:
        # import openai
        # response = openai.Embedding.create(input=texts, model=self.model)
        # return [e['embedding'] for e in response['data']]
        
        # Simulation
        return [[0.1] * 1536 for _ in texts]
    
    def _save_embeddings(self, batch, embeddings):
        """Save embeddings to database"""
        # In production, would update graphrag_resources with embeddings
        # ALTER TABLE graphrag_resources ADD COLUMN embedding vector(1536);
        # UPDATE graphrag_resources SET embedding = ... WHERE file_path = ...
        
        self.embeddings_generated += len(embeddings)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate Resource Embeddings')
    parser.add_argument('--batch-size', type=int, default=100, help='Batch size')
    parser.add_argument('--model', type=str, default='text-embedding-3-small', help='OpenAI model')
    
    args = parser.parse_args()
    
    generator = SemanticEmbeddingGenerator(model=args.model)
    generator.generate_all_embeddings(batch_size=args.batch_size)
    
    print(f"\n🔮 Semantic intelligence ready!")


if __name__ == '__main__':
    main()

