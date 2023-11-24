from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.scoped_resource_selector_requirement import ScopedResourceSelectorRequirement


class ScopeSelector(BaseModel):
    matchExpressions: List[ScopedResourceSelectorRequirement] = Field(default=None, description=r""" A list of scope selector requirements by scope of the resources. """)
