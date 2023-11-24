from pydantic import BaseModel, Field


class TopologySelectorTerm(BaseModel):
    matchLabelExpressions: List[TopologySelectorLabelRequirement] = Field(default=None, description=r""" A list of topology selector requirements by labels. """)
