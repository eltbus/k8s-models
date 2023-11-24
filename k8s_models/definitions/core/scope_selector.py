from pydantic import BaseModel, Field


class ScopeSelector(BaseModel):
    matchExpressions: List[ScopedResourceSelectorRequirement] = Field(default=None, description=r""" A list of scope selector requirements by scope of the resources. """)
