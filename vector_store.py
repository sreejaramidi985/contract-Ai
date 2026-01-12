# vector_store.py
import numpy as np
import faiss
from embeddings import embed_text

class VectorStore:
    """
    Simple FAISS-based vector store for contract chunks.
    """
    def __init__(self, dim=384):
        self.dim = dim
        self.index = faiss.IndexFlatL2(self.dim)
        self.texts = []

    def add_document(self, text: str):
        vec = np.array(embed_text(text), dtype="float32").reshape(1, self.dim)
        self.index.add(vec)
        self.texts.append(text)

    def search(self, query: str, k: int = 3):
        qvec = np.array(embed_text(query), dtype="float32").reshape(1, self.dim)
        distances, indices = self.index.search(qvec, k)

        results = []
        for idx in indices[0]:
            if idx != -1 and idx < len(self.texts):
                results.append(self.texts[idx])
        return results

# singleton instance
vector_store = VectorStore()
