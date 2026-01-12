import re

AGENT_KEYWORDS = {
    "Compliance": [
         "gdpr", "regulation", "regulatory", "compliance", "audit", "policy",
        "law", "legal requirement", "data protection", "privacy",
        "iso", "sox", "hipaa", "pci", "standards", "governance",
        "breach", "violation", "penalty", "monitoring", "reporting"
    ],
    "Legal": [
         "contract", "agreement", "terminate", "termination",
        "liability", "liable", "clause", "indemnity",
        "confidentiality", "intellectual property", "ip rights",
        "jurisdiction", "governing law", "breach",
        "dispute", "arbitration", "notice", "warranty", "obligation"
    
    ],
    "Finance": [
        "cost", "price", "pricing", "revenue", "fee", "fees", "payment",
        "invoice", "billing", "charges", "expenses", "penalty",
        "late payment", "tax", "taxes", "budget", "financial",
        "compensation", "refund", "credit", "discount"
    ],
    "Operations": [
         "process", "implement", "implementation", "update", "execute",
        "execution", "timeline", "schedule", "delivery", "milestone",
        "scope", "responsibility", "roles", "service level",
        "sla", "maintenance", "support", "workflow",
        "operational", "resources", "deployment"
    ]
}


def analyze_contract(contract_text: str):
    sentences = re.split(r'(?<=[.!?])\s+', contract_text)

    result = {
        "Compliance": [],
        "Legal": [],
        "Finance": [],
        "Operations": []
    }

    for sentence in sentences:
        sentence_lower = sentence.lower()

        for domain, keywords in AGENT_KEYWORDS.items():
            if any(keyword in sentence_lower for keyword in keywords):
                clean_sentence = sentence.strip()
                if clean_sentence and clean_sentence not in result[domain]:
                    result[domain].append(clean_sentence)

    return result
