AGENT_KEYWORDS = {
    "Compliance": [
        "gdpr", "regulation", "regulatory", "compliance", "audit", "policy",
        "law", "legal requirement", "data protection", "privacy",
        "iso", "sox", "hipaa", "pci", "standards", "governance",
        "breach", "violation", "penalty", "monitoring", "reporting"
    ],

    "Finance": [
        "cost", "price", "pricing", "revenue", "fee", "fees", "payment",
        "invoice", "billing", "charges", "expenses", "penalty",
        "late payment", "tax", "taxes", "budget", "financial",
        "compensation", "refund", "credit", "discount"
    ],

    "Legal": [
        "contract", "agreement", "terminate", "termination",
        "liability", "liable", "clause", "indemnity",
        "confidentiality", "intellectual property", "ip rights",
        "jurisdiction", "governing law", "breach",
        "dispute", "arbitration", "notice", "warranty", "obligation"
    ],

    "Operations": [
        "process", "implement", "implementation", "update", "execute",
        "execution", "timeline", "schedule", "delivery", "milestone",
        "scope", "responsibility", "roles", "service level",
        "sla", "maintenance", "support", "workflow",
        "operational", "resources", "deployment"
    ]
}


def classify_clause(clause: str):
    clause_lower = clause.lower()
    matched_agents = []

    for agent, keywords in AGENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in clause_lower:
                matched_agents.append(agent)
                break  # Avoid duplicate matches per agent

    return matched_agents
