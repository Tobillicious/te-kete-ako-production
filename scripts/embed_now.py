#!/usr/bin/env python3
"""Quick and dirty embedding generation - just DO IT!"""

import sys
import time
from sentence_transformers import SentenceTransformer

# Load model
print("🔧 Loading sentence-transformers model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Model loaded!")

def pad_embedding(embedding, target_dim=1536):
    """Pad to 1536 dimensions"""
    emb_list = embedding.tolist()
    if len(emb_list) >= target_dim:
        return emb_list[:target_dim]
    return emb_list + [0.0] * (target_dim - len(emb_list))

# Read statement text from stdin
if __name__ == "__main__":
    text = sys.stdin.read().strip()
    if not text:
        print("ERROR: No input", file=sys.stderr)
        sys.exit(1)
    
    # Generate embedding
    embedding = model.encode(text, convert_to_numpy=True)
    padded = pad_embedding(embedding, 1536)
    
    # Output as comma-separated values
    print(','.join(map(str, padded)))

