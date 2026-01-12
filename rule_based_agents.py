def compliance_agent(clause):
    return {
        "agent": "Compliance",
        "risk": "high" if "must" in clause.lower() else "medium",
        "analysis": f"Regulatory obligation identified: {clause}"
    }


def finance_agent(clause):
    return {
        "agent": "Finance",
        "exposure": "monetary",
        "analysis": f"Financial impact detected: {clause}"
    }


def legal_agent(clause):
    return {
        "agent": "Legal",
        "obligation": True,
        "analysis": f"Contractual/legal clause detected: {clause}"
    }


def operations_agent(clause):
    return {
        "agent": "Operations",
        "action_required": True,
        "analysis": f"Operational task identified: {clause}"
    }
