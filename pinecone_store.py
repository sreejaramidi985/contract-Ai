import os
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# Load embedding model (CPU-friendly)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Pinecone init
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "contract-risk-index"

# Create index if not exists
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)


def store_result(agent_name, result):
    """
    Stores agent analysis in Pinecone after embedding
    """
    text = result["analysis"]

    # 🔑 Convert text → vector
    vector = model.encode(text).tolist()

    index.upsert([
        {
            "id": agent_name,
            "values": vector,
            "metadata": {
                "agent": result["agent"],
                "risk_type": result["risk_type"],
                "analysis": text
            }
        }
    ])
