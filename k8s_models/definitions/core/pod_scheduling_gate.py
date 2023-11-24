from pydantic import BaseModel, Field


class PodSchedulingGate(BaseModel):
    name: str = Field(default=None, description=r""" Name of the scheduling gate. Each scheduling gate must have a unique name field. """)
