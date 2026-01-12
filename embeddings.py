# embeddings.py
from sentence_transformers import SentenceTransformer

# all-MiniLM-L6-v2 embed dim = 384
MODEL_NAME = "all-MiniLM-L6-v2"
_model = None

def _load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model

def embed_text(text: str):
    """
    Returns a 1D list/np-array-like vector for `text`.
    """
    model = _load_model()
    vec = model.encode(text, show_progress_bar=False)
    # return as Python list (faiss will accept numpy float32 later)
    return vec.tolist()
