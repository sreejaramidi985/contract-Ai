from agent_manager import run_agents_parallel, multi_turn_interaction
from pinecone_store import store_result

def main():
    contract_text = """
    Company A hires Developer B for software development.
    Total payment is INR 85,000 split 50/50.
    Duration: 16 weeks.
    Confidentiality is required.
    Termination by 30 days written notice.
    Liability limited to fees paid.
    """

    print("\n--- RUNNING PARALLEL AGENTS ---")
    parallel_results = run_agents_parallel(contract_text)
    print(parallel_results)

    print("\n--- STORING RESULTS IN PINECONE ---")
    for agent, result in parallel_results.items():
        store_result(agent, result)

    print("\n--- MULTI-TURN AGENT INTERACTION ---")
    multi_turn_results = multi_turn_interaction(contract_text)
    print(multi_turn_results)

if __name__ == "__main__":
    main()
