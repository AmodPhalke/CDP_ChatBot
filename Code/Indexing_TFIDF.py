from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle

# Load cleaned documentation
with open('Segment_Docs.txt', 'r', encoding='utf-8') as f:
    segment_docs = f.read().splitlines()

with open('mParticle_Docs.txt', 'r', encoding='utf-8') as f:
    mp_docs = f.read().splitlines()

with open('Lytics_Docs.txt', 'r', encoding='utf-8') as f:
    lytics_docs = f.read().splitlines()

with open('Zeotap_Docs.txt', 'r', encoding='utf-8') as f:
    zeotap_docs = f.read().splitlines()

# Combine all documents into a single list
all_docs = segment_docs + mp_docs + lytics_docs + zeotap_docs # Add other platforms similarly

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_docs)

# Save the vectorizer and matrix for later use
np.save('tfidf_matrix.npy', tfidf_matrix.toarray())
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)