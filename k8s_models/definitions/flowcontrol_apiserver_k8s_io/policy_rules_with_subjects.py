from pydantic import BaseModel, Field


class PolicyRulesWithSubjects(BaseModel):
    nonResourceRules: List[NonResourcePolicyRule] = Field(default=None, description=r""" `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL. """)
    resourceRules: List[ResourcePolicyRule] = Field(default=None, description=r""" `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty. """)
    subjects: List[Subject] = Field(default=None, description=r""" subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required. """)
