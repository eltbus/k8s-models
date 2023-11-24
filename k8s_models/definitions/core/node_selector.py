from pydantic import BaseModel, Field


class NodeSelector(BaseModel):
    nodeSelectorTerms: List[NodeSelectorTerm] = Field(default=None, description=r""" Required. A list of node selector terms. The terms are ORed. """)
