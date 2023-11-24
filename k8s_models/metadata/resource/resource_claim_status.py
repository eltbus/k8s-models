from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.resource_k8s_io.allocation_result import AllocationResult
from k8s_models.definitions.resource_k8s_io.resource_claim_consumer_reference import ResourceClaimConsumerReference


class ResourceClaimStatus(BaseModel):
    allocation: AllocationResult = Field(default=None, description=r""" Allocation is set by the resource driver once a resource or set of resources has been allocated successfully. If this is not specified, the resources have not been allocated yet. """)
    deallocationRequested: bool = Field(default=None, description=r""" DeallocationRequested indicates that a ResourceClaim is to be deallocated.  The driver then must deallocate this claim and reset the field together with clearing the Allocation field.  While DeallocationRequested is set, no new consumers may be added to ReservedFor. """)
    driverName: str = Field(default=None, description=r""" DriverName is a copy of the driver name from the ResourceClass at the time when allocation started. """)
    reservedFor: List[ResourceClaimConsumerReference] = Field(default=None, description=r""" ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started.  There can be at most 32 such reservations. This may get increased in the future, but not reduced. """)
