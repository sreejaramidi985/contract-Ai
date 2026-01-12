def generate_report(analysis_result, tone, focus):
    report = ""

    if tone == "Executive":
        report += "Executive Summary\n"
        report += analysis_result["summary"] + "\n\n"

    elif tone == "Technical":
        report += "Technical Analysis Report\n\n"

    elif tone == "Compliance-Focused":
        report += "Compliance Risk Assessment\n\n"

    for domain in focus:
        if domain in analysis_result["domains"]:
            report += f"{domain} Findings:\n"
            for issue in analysis_result["domains"][domain]["issues"]:
                report += f"- {issue}\n"
            report += "\n"

    return report
