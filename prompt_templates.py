def finance_prompt(contract):
    return f"""
You are a Finance agent.
Extract payment terms, penalties, and financial risks.

Contract:
{contract}

Return clear finance risks.
"""

def legal_prompt(contract):
    return f"""
You are a Legal agent.
Extract termination, liability, and contractual obligations.

Contract:
{contract}

Return legal risks.
"""

def compliance_prompt(contract):
    return f"""
You are a Compliance agent.
Extract regulatory, policy, and compliance risks.

Contract:
{contract}

Return compliance risks.
"""

def operations_prompt(contract):
    return f"""
You are an Operations agent.
Extract timelines, execution tasks, and operational risks.

Contract:
{contract}

Return operational risks.
"""
