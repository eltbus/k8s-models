from pydantic import BaseModel, Field


class NodeSelectorTerm(BaseModel):
    matchExpressions: List[NodeSelectorRequirement] = Field(default=None, description=r""" A list of node selector requirements by node's labels. """)
    matchFields: List[NodeSelectorRequirement] = Field(default=None, description=r""" A list of node selector requirements by node's fields. """)
