from pydantic import BaseModel, Field


class AllocationResult(BaseModel):
    availableOnNodes: NodeSelector = Field(default=None, description=r""" This field will get set by the resource driver after it has allocated the resource to inform the scheduler where it can schedule Pods using the ResourceClaim.  Setting this field is optional. If null, the resource is available everywhere. """)
    resourceHandles: List[ResourceHandle] = Field(default=None, description=r""" ResourceHandles contain the state associated with an allocation that should be maintained throughout the lifetime of a claim. Each ResourceHandle contains data that should be passed to a specific kubelet plugin once it lands on a node. This data is returned by the driver after a successful allocation and is opaque to Kubernetes. Driver documentation may explain to users how to interpret this data if needed.  Setting this field is optional. It has a maximum size of 32 entries. If null (or empty), it is assumed this allocation will be processed by a single kubelet plugin with no ResourceHandle data attached. The name of the kubelet plugin invoked will match the DriverName set in the ResourceClaimStatus this AllocationResult is embedded in. """)
    shareable: bool = Field(default=None, description=r""" Shareable determines whether the resource supports more than one consumer at a time. """)
