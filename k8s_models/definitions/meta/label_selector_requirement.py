from pydantic import BaseModel, Field


class LabelSelectorRequirement(BaseModel):
    key: str = Field(default=None, description=r""" key is the label key that the selector applies to. """)
    operator: str = Field(default=None, description=r""" operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. """)
    values: List[str] = Field(default=None, description=r""" values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. """)
