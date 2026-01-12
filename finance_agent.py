from .prompt_templates import finance_prompt

def finance_agent(contract):
    return {
        "agent": "Finance",
        "risk_type": "Financial",
        "analysis": "Payment split, penalty risk, cost exposure detected"
    }
