"""Structured Pydantic schema for the candidate Master Resume.

Represents Ebenezer J. Rolston's authoritative resume sections, verified claims,
education, technical proficiencies, AI portfolio, and explicit anti-hallucination guardrails.
"""
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Dict, Optional

class ContactInfo(BaseModel):
    name: str = "Ebenezer J. Rolston"
    title: str = "AI-First Transformation Analyst - Program Analyst · Strategy Consultant"
    email: str = "eberolston@yahoo.com"
    phone: str = "501-307-3237"
    location: str = "Denver, CO"
    work_preference: str = "Open to Hybrid / Relocation"
    linkedin_url: Optional[str] = "https://www.linkedin.com/in/ebenezer-rolston/"
    ai_guardians_portal_url: str = "https://portal.aiguardiansllc.us/"

class AIPortfolioItem(BaseModel):
    title: str
    organization: str = "University of Denver / AI Guardians LLC"
    description: str
    context_label: str = "graduate_portfolio"  # graduate_portfolio | personal_project | company_product

class WorkExperience(BaseModel):
    role_title: str
    company_or_agency: str
    location: str = "Denver, CO"
    dates: str
    is_gs_level: bool = False
    gs_level: Optional[str] = None
    bullets: List[str]

class EducationCredential(BaseModel):
    degree_or_cert: str
    institution: str
    display_format: str  # Rule: No expected/graduation dates for DU
    credential_id: Optional[str] = None
    verification_url: Optional[str] = None
    domains: List[str] = Field(default_factory=list)

class CertificationItem(BaseModel):
    id: str
    title: str
    issuing_organization: str
    credential_type: str
    domains: List[str] = Field(default_factory=list)
    target_roles: List[str] = Field(default_factory=list)
    verified_skills_and_tools: List[str] = Field(default_factory=list)
    extractable_resume_bullets: List[str] = Field(default_factory=list)
    resume_display_format: str
    credential_id: Optional[str] = None
    verification_url: Optional[str] = None
    guardrails: List[str] = Field(default_factory=list)

class TechnicalProficiencies(BaseModel):
    generative_ai_llms: List[str] = Field(default_factory=list)
    data_analytics: List[str] = Field(default_factory=list)
    programming_languages: List[str] = Field(default_factory=list)
    databases: List[str] = Field(default_factory=list)
    enterprise_systems: List[str] = Field(default_factory=list)

class AntiHallucinationGuardrails(BaseModel):
    """Explicit negative constraints — facts the candidate CANNOT claim."""
    do_not_claim: List[str] = Field(default_factory=lambda: [
        "UiPath or UiPath RPA skills",
        "Power Apps, Power Automate, Power Platform, Dataverse, DAX",
        "Appian or low-code platform experience",
        "External client production deployment of AI Guardians tools or Gumloop agents",
        "AWS Bedrock live deployment",
        "Enterprise cloud administration (AWS/GCP/Azure admin)",
        "Formal people management / supervisory authority (claim project/team leadership)",
        "VA employment or VA contractor experience",
        "Digital-health AI client production deployments"
    ])

class MasterResumeModel(BaseModel):
    """Authoritative Pydantic model for Ebenezer J. Rolston's Master Resume."""
    contact_info: ContactInfo = Field(default_factory=ContactInfo)
    professional_summary: str
    core_competencies: List[str] = Field(default_factory=list)
    ai_portfolio: List[AIPortfolioItem] = Field(default_factory=list)
    work_experience: List[WorkExperience] = Field(default_factory=list)
    education: List[EducationCredential] = Field(default_factory=list)
    technical_proficiencies: TechnicalProficiencies = Field(default_factory=TechnicalProficiencies)
    verified_evidence_bank: Dict[str, List[str]] = Field(default_factory=dict)
    guardrails: AntiHallucinationGuardrails = Field(default_factory=AntiHallucinationGuardrails)

    def to_full_markdown(self) -> str:
        """Render complete formatted markdown representation of the master resume."""
        lines = [
            f"# {self.contact_info.name} — Master Resume",
            f"**{self.contact_info.title}**",
            f"{self.contact_info.email} | {self.contact_info.phone} | {self.contact_info.location} | {self.contact_info.work_preference}",
            f"Portal: {self.contact_info.ai_guardians_portal_url}\n",
            "## PROFESSIONAL SUMMARY",
            self.professional_summary,
            "\n## CORE COMPETENCIES",
            ", ".join(self.core_competencies),
            "\n## AI STRATEGY & TRANSFORMATION PORTFOLIO",
        ]
        for p in self.ai_portfolio:
            lines.append(f"- **{p.title}** ({p.organization}): {p.description}")

        lines.append("\n## PROFESSIONAL EXPERIENCE")
        for w in self.work_experience:
            lines.append(f"\n### {w.role_title} | {w.company_or_agency} ({w.dates})")
            for b in w.bullets:
                lines.append(f"- {b}")

        lines.append("\n## EDUCATION & CREDENTIALS")
        for ed in self.education:
            lines.append(f"- {ed.display_format}")

        lines.append("\n## EXPLICIT NOT SUPPORTED (DO NOT CLAIM)")
        for g in self.guardrails.do_not_claim:
            lines.append(f"- {g}")

        return "\n".join(lines)
