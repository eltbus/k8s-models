from pydantic import BaseModel, Field


class PreferredSchedulingTerm(BaseModel):
    preference: NodeSelectorTerm = Field(default=None, description=r""" A node selector term, associated with the corresponding weight. """)
    weight: int = Field(default=None, description=r""" Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. """)
