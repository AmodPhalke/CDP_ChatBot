from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the cleaned documentation from the file
with open('Segment_Docs.txt', 'r', encoding='utf-8') as f:
    segment_docs = f.read().splitlines()  # Read each line as a separate document

# Load the saved embeddings
document_embeddings = np.load('document_embeddings.npy')

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def preprocess_query(query):
    # Implement any necessary preprocessing steps (e.g., lowercasing, removing punctuation)
    return query.strip().lower()

def query_bot(user_query, top_n=5):
    # Preprocess the user query
    preprocessed_query = preprocess_query(user_query)

    # Convert the query to an embedding
    query_embedding = model.encode([preprocessed_query])

    # Calculate cosine similarity between the query embedding and document embeddings
    similarities = cosine_similarity(query_embedding, document_embeddings)

    # Get the indices of the top N most similar documents
    top_indices = np.argsort(similarities[0])[-top_n:][::-1]  # Get top N indices

    # Retrieve the corresponding documents from segment_docs
    results = [segment_docs[i] for i in top_indices]

    return results

# Example usage
user_query = "What are the key features of Lytics?"
results = query_bot(user_query)
for result in results:
    print(result)