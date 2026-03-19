from fastapi import APIRouter
from app.schemas.company import Company
from app.services.retriever import retrieve_policies
from app.services.policy_matcher import match_policies
from app.services.report_generator import generate_report

router = APIRouter()

@router.post("/match")
def match(company: Company):
    policies = retrieve_policies(company)
    matched = match_policies(company, policies)
    report = generate_report(company, matched)
    return report