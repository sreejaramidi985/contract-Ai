def multi_turn_interaction(agent_outputs):
    """
    Simulates multi-turn interaction between agents
    """

    conversation = []

    # Turn 1: Finance → Legal
    if "finance" in agent_outputs:
        finance_summary = agent_outputs["finance"]["summary"]
        conversation.append({
            "from": "Finance",
            "to": "Legal",
            "message": f"Financial risk detected: {finance_summary}"
        })

    # Turn 2: Legal → Compliance
    if "legal" in agent_outputs:
        legal_summary = agent_outputs["legal"]["summary"]
        conversation.append({
            "from": "Legal",
            "to": "Compliance",
            "message": f"Legal clause impact: {legal_summary}"
        })

    return conversation
