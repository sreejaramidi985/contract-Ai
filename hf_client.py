from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    device=-1  # CPU
)

def ask_model(prompt: str) -> str:
    result = generator(
        prompt,
        max_new_tokens=180,
        temperature=0.2,
        do_sample=False
    )
    return result[0]["generated_text"]
