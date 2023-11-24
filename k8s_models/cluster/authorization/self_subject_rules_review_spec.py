from pydantic import BaseModel, Field


class SelfSubjectRulesReviewSpec(BaseModel):
    namespace: str = Field(default=None, description=r""" Namespace to evaluate rules for. Required. """)
