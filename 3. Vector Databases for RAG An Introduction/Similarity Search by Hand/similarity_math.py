import math
import numpy as np
import scipy.spatial
import torch
from langchain_chroma.vectorstores import cosine_similarity
from sentence_transformers import SentenceTransformer

documents = [
    'Bugs introduced by the intern had to be squashed by the lead developer.',
    'Bugs found by the quality assurance engineer were difficult to debug.',
    'Bugs are common throughout the warm summer months, according to the entomologist.',
    'Bugs, in particular spiders, are extensively studied by arachnologists.'
]

print("loading embedding model")
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

print("convert the document into a mathematical vector")
embeddings = model.encode(documents)

print(f"Number of documents: {embeddings.shape[0]}")
print(f"Dimensions per vector: {embeddings.shape[1]}")
print(f"Vector Sample: {embeddings[0][:5]}")
print(embeddings.shape)

# Euclidean Distance

def euclidean_distance_fn(vector1, vector2):
    squared_sum = sum((x - y)**2 for x,y in zip(vector1, vector2))
    return math.sqrt(squared_sum)

print("Calculating L2 Distances manually")
num_docs = embeddings.shape[0]

l2_dist_manual = np.zeros([num_docs, num_docs])

for i in range(num_docs):
    for j in range(num_docs):
        l2_dist_manual[i,j] = euclidean_distance_fn(embeddings[i], embeddings[j])

print("L2 Distance Matrix")
np.set_printoptions(precision=4, suppress=True)
print(l2_dist_manual)


# Dot Product Similarity
def dot_product_fn(vector1, vector2):
    return sum(x*y for x,y in zip(vector1, vector2))

print("Calculating Dot Products manually")
dot_product_manual = np.zeros([num_docs, num_docs])

for i in range(num_docs):
    for j in range(num_docs):
        dot_product_manual[i,j] = dot_product_fn(embeddings[i], embeddings[j])

print("Dot Product Matrix (manual)")
print(dot_product_manual)

# faster way: Matrix Multiplication
print("Dot Product Matrix (faster)")
dot_product_fast = embeddings @ embeddings.T
print(dot_product_fast)

# Cosine Similarity
normalized_embeddings = torch.nn.functional.normalize(
    torch.from_numpy(embeddings)
).numpy()

cosine_similarity_matrix = normalized_embeddings @ normalized_embeddings.T

print("Cosine similarity matrix")
print(cosine_similarity_matrix)

print("executing similarity search query")
query = ["Who is responsible for a coding project and fixing others' mistakes?"]

query_embedding = model.encode(query)
normalized_query_embedding = torch.nn.functional.normalize(
    torch.from_numpy(query_embedding)
).numpy()

query_scores = normalized_embeddings @ normalized_query_embedding.T

print(f"Query Scores: {query_scores}")

for idx, score in enumerate(query_scores):
    print(f"Document {idx}: Score = {score[0]:.4f} | Text: {documents[idx]}")

best_match_idx = query_scores.argmax()

print(f"Best match index: {best_match_idx}")
print(f"Best match document: {documents[best_match_idx]}")