from rule_based_agents import (
    finance_agent as rb_finance,
    legal_agent as rb_legal,
    compliance_agent as rb_compliance,
    operations_agent as rb_operations
)

from agent_manager import run_agents_parallel


def run_hybrid_agents(contract_text):
    """
    Step 1: Rule-based agents (fast classification)
    Step 2: LLM-based agents (deep analysis)
    Step 3: Merge results
    """

    rule_based_results = {
        "finance": rb_finance(contract_text),
        "legal": rb_legal(contract_text),
        "compliance": rb_compliance(contract_text),
        "operations": rb_operations(contract_text),
    }

    llm_results = run_agents_parallel(contract_text)

    return {
        "rule_based_analysis": rule_based_results,
        "llm_based_analysis": llm_results
    }
