from pydantic import BaseModel, Field


class ResourceClaimSchedulingStatus(BaseModel):
    name: str = Field(default=None, description=r""" Name matches the pod.spec.resourceClaims[*].Name field. """)
    unsuitableNodes: List[str] = Field(default=None, description=r""" UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced. """)
