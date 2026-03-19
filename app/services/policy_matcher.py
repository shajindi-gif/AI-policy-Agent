def match_policies(company, policies):
    results = []

    for p in policies:
        score = 0

        if p["city"] in ["全国", company.city]:
            score += 1

        if "科技" in company.industry:
            score += 1

        results.append({
            "policy": p,
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results