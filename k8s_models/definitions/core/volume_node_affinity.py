from pydantic import BaseModel, Field


class VolumeNodeAffinity(BaseModel):
    required: NodeSelector = Field(default=None, description=r""" required specifies hard node constraints that must be met. """)
