from pydantic import BaseModel, Field


class PodSchedulingContextStatus(BaseModel):
    resourceClaims: List[ResourceClaimSchedulingStatus] = Field(default=None, description=r""" ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses "WaitForFirstConsumer" allocation mode. """)
