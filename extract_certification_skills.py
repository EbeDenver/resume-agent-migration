"""Utility to query and extract job-targeted certifications and skills from the repository.

Usage:
    python3 extract_certification_skills.py "data analytics python pandas"
    python3 extract_certification_skills.py "generative ai llm agentic"
    python3 extract_certification_skills.py "ai governance ethics compliance"
    python3 extract_certification_skills.py "cost optimization prompt caching"
"""
import sys
import json
from pathlib import Path

REPO_PATH = Path(__file__).parent / "data" / "certifications_repository.json"

def load_repository():
    with open(REPO_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def match_certifications(query_terms):
    repo = load_repository()
    query_lower = [t.lower().strip() for t in query_terms if t.strip()]
    
    matches = []
    for cert in repo.get("certificates", []):
        score = 0
        matched_reasons = []
        
        # Check domains
        for domain in cert.get("domains", []):
            for term in query_lower:
                if term in domain.lower():
                    score += 3
                    matched_reasons.append(f"Domain: {domain}")
                    
        # Check verified skills
        for skill in cert.get("verified_skills_and_tools", []):
            for term in query_lower:
                if term in skill.lower():
                    score += 2
                    matched_reasons.append(f"Skill: {skill}")
                    
        # Check target roles
        for role in cert.get("target_roles", []):
            for term in query_lower:
                if term in role.lower():
                    score += 2
                    matched_reasons.append(f"Role: {role}")
                    
        # Check title
        for term in query_lower:
            if term in cert.get("title", "").lower():
                score += 3
                matched_reasons.append(f"Title: {cert.get('title')}")

        if score > 0:
            matches.append({
                "score": score,
                "cert": cert,
                "reasons": list(set(matched_reasons))
            })
            
    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches

def display_matches(query, matches):
    print(f"\n=======================================================")
    print(f"CERTIFICATION SKILL EXTRACTION FOR: '{query}'")
    print(f"=======================================================")
    if not matches:
        print("No direct certificate matches found. Showing general credentials.")
        return
        
    for idx, m in enumerate(matches, 1):
        c = m["cert"]
        print(f"\n[{idx}] {c['title']} (Score: {m['score']})")
        print(f"    • Issuing Body: {c['issuing_organization']}")
        print(f"    • Display Format: {c['resume_display_format']}")
        if c.get("credential_id"):
            print(f"    • Credential ID / CeDiD: {c['credential_id']}")
        if c.get("verification_url"):
            print(f"    • Verification URL: {c['verification_url']}")
        print(f"    • Matched Proofs: {', '.join(m['reasons'][:4])}")
        print(f"    • Verified Skills/Tools to inject: {', '.join(c['verified_skills_and_tools'][:6])}")
        print(f"    • Recommended Bullet:")
        bullets = c.get("extractable_resume_bullets", [])
        if bullets:
            print(f"      \"{bullets[0]}\"")
        if c.get("guardrails"):
            print(f"    ⚠️ Guardrail: {c['guardrails'][0]}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "data analytics python prompt caching governance"
        
    terms = query.split()
    results = match_certifications(terms)
    display_matches(query, results)
