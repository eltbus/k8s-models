from pydantic import BaseModel, Field


class TopologySelectorLabelRequirement(BaseModel):
    key: str = Field(default=None, description=r""" The label key that the selector applies to. """)
    values: List[str] = Field(default=None, description=r""" An array of string values. One value must match the label to be selected. Each entry in Values is ORed. """)
