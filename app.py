from agent_manager import run_all_agents
from vector_store import vector_store
import os

CONTRACT_PATH = "sample_docs/sample_contract.txt"

def load_contract():
    with open(CONTRACT_PATH, "r") as f:
        return f.read()

def split_to_chunks(text, max_len=600):
    return [text[i:i+max_len] for i in range(0, len(text), max_len)]

def main():
    contract = load_contract()
    chunks = split_to_chunks(contract)

    for chunk in chunks:
        result = run_all_agents(chunk)

        print("\n===== FINAL STRUCTURED OUTPUT =====")
        print(result)

if __name__ == "__main__":
    main()
