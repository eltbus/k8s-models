from pydantic import BaseModel, Field


class ResourceQuotaSpec(BaseModel):
    hard: dict = Field(default=None, description=r""" hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """)
    scopeSelector: ScopeSelector = Field(default=None, description=r""" scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched. """)
    scopes: List[str] = Field(default=None, description=r""" A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. """)
