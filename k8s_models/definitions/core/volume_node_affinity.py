from pydantic import BaseModel, Field

from k8s_models.definitions.core.node_selector import  NodeSelector


class VolumeNodeAffinity(BaseModel):
    required: NodeSelector = Field(default=None, description=r""" required specifies hard node constraints that must be met. """)
