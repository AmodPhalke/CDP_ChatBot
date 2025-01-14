from sentence_transformers import SentenceTransformer
import numpy as np

# Load cleaned documentation
with open('Segment_Docs.txt', 'r', encoding='utf-8') as f:
    segment_docs = f.read().splitlines()

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for the documents
document_embeddings = model.encode(segment_docs)

# Save embeddings for later use
np.save('document_embeddings.npy', document_embeddings)