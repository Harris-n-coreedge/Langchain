from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

document = [
    "The capital of India is New Delhi.",
    "The capital of France is Paris.",  
    "The capital of Germany is Berlin."
    "The capital of pakistan is Islamabad"
]
query = "Tell me about the capital of Pakistan"

doc_embeddings = embeddings.embed_documents(document)

query_embedding = embeddings.embed_query(query)

similarities = cosine_similarity([query_embedding], doc_embeddings)

print("Document Similarities:", similarities)

