from concurrent.futures import ThreadPoolExecutor
from agents import (
    finance_agent,
    legal_agent,
    compliance_agent,
    operations_agent
)

# -------- PARALLEL EXECUTION --------
def run_agents_parallel(contract):
    results = {}

    with ThreadPoolExecutor(max_workers=4) as executor:
        tasks = {
            "finance": executor.submit(finance_agent, contract),
            "legal": executor.submit(legal_agent, contract),
            "compliance": executor.submit(compliance_agent, contract),
            "operations": executor.submit(operations_agent, contract)
        }

        for key, task in tasks.items():
            results[key] = task.result()

    return results


# -------- MULTI-TURN INTERACTION --------
def multi_turn_interaction(contract):
    finance = finance_agent(contract)

    legal = legal_agent(
        f"{contract}\nFinance findings: {finance}"
    )

    compliance = compliance_agent(
        f"{contract}\nFinance: {finance}\nLegal: {legal}"
    )

    return {
        "finance": finance,
        "legal": legal,
        "compliance": compliance
    }
