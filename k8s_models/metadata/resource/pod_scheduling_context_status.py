from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.resource_k8s_io.resource_claim_scheduling_status import ResourceClaimSchedulingStatus


class PodSchedulingContextStatus(BaseModel):
    resourceClaims: List[ResourceClaimSchedulingStatus] = Field(default=None, description=r""" ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses "WaitForFirstConsumer" allocation mode. """)
