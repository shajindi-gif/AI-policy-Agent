def generate_report(company, matched):
    results = []

    for m in matched:
        policy = m["policy"]
        score = m["score"]

        if score >= 2:
            reason = "地区和行业均较匹配"
        elif score == 1:
            reason = "部分条件匹配"
        else:
            reason = "匹配度较低，建议人工复核"

        results.append({
            "policy": policy["title"],
            "score": score,
            "reason": reason,
            "content": policy["content"]
        })

    return {
        "company": company.name,
        "city": company.city,
        "industry": company.industry,
        "stage": company.stage,
        "results": results
    }