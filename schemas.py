from pydantic import BaseModel, Field
from typing import List, Literal

class ExtractedBusinessRule(BaseModel):
    rule_id: str = Field(description="Unique identifier, e.g., BR-001")
    description: str = Field(description="Clear explanation of the business logic in plain English")
    legacy_condition: str = Field(description="The exact condition in COBOL, e.g., 'WS-CREDIT-SCORE < 600'")
    action_taken: str = Field(description="Action executed when condition is met, e.g., 'Set WS-DECISION to REJECTED'")
    source_lines: str = Field(description="Exact line range from the code, e.g., '0012-0013'")

class MigrationRisk(BaseModel):
    risk_id: str = Field(description="Unique risk identifier, e.g., RSK-001")
    severity: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] = Field(description="Severity rating")
    category: Literal["HARDCODED_LOGIC", "DATA_DEPENDENCY", "MISSING_VALIDATION", "DEPRECATED_SYNTAX"]
    summary: str = Field(description="Short description of the migration risk")
    remediation: str = Field(description="Actionable suggestion for the modern cloud/microservice target")

class ModernizationArtifact(BaseModel):
    program_name: str = Field(description="Name of the legacy program from PROGRAM-ID")
    executive_summary: str = Field(description="High-level explanation of what this program does")
    business_rules: List[ExtractedBusinessRule]
    risks: List[MigrationRisk]