from .prompt_templates import legal_prompt

def legal_agent(contract):
    return {
        "agent": "Legal",
        "risk_type": "Legal",
        "analysis": "Termination clause and liability limits detected"
    }
