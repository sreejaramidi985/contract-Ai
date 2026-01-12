from .prompt_templates import compliance_prompt

def compliance_agent(contract):
    return {
        "agent": "Compliance",
        "risk_type": "Compliance",
        "analysis": "Confidentiality and regulatory obligations detected"
    }
