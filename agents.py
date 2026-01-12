# agents.py
from transformers import pipeline

# Load Hugging Face model ONCE (important for performance)
# You can change model name later if needed
hf_model = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200,
    temperature=0.3
)


def ask_huggingface(prompt: str):
    """
    Calls Hugging Face model safely via transformers pipeline.
    """
    try:
        response = hf_model(prompt)
        return response[0]["generated_text"]

    except Exception as e:
        return f"[ERROR calling Hugging Face model] {str(e)}"


def analyze(role: str, text: str):
    """
    Optimized domain-specific prompt for Hugging Face models.
    """
    prompt = f"""
You are a {role} expert.

Analyze the following contract text and provide
clear bullet-point insights focusing ONLY on {role} aspects.

Contract Text:
{text}

Return short, precise bullet points.
"""

    return ask_huggingface(prompt)
