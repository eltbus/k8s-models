from pydantic import BaseModel, Field


class ScopedResourceSelectorRequirement(BaseModel):
    operator: str = Field(default=None, description=r""" Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. """)
    scopeName: str = Field(default=None, description=r""" The name of the scope that the selector applies to. """)
    values: List[str] = Field(default=None, description=r""" An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. """)
