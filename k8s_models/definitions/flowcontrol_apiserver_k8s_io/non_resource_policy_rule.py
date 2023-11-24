from pydantic import BaseModel, Field


class NonResourcePolicyRule(BaseModel):
    nonResourceURLs: List[str] = Field(default=None, description=r""" `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:   - "/healthz" is legal   - "/hea*" is illegal   - "/hea" is legal but matches nothing   - "/hea/*" also matches nothing   - "/healthz/*" matches all per-component health checks. "*" matches all non-resource urls. if it is present, it must be the only entry. Required. """)
    verbs: List[str] = Field(default=None, description=r""" `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs. If it is present, it must be the only entry. Required. """)
