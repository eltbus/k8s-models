from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.core import NodeSelector


class AllocationResult(BaseModel):
    availableOnNodes: NodeSelector = Field(
        default=None,
        description=r""" This field will get set by the resource driver after it has allocated the resource to inform the scheduler where it can schedule Pods using the ResourceClaim.  Setting this field is optional. If null, the resource is available everywhere. """,
    )
    resourceHandles: List[ResourceHandle] = Field(
        default=None,
        description=r""" ResourceHandles contain the state associated with an allocation that should be maintained throughout the lifetime of a claim. Each ResourceHandle contains data that should be passed to a specific kubelet plugin once it lands on a node. This data is returned by the driver after a successful allocation and is opaque to Kubernetes. Driver documentation may explain to users how to interpret this data if needed.  Setting this field is optional. It has a maximum size of 32 entries. If null (or empty), it is assumed this allocation will be processed by a single kubelet plugin with no ResourceHandle data attached. The name of the kubelet plugin invoked will match the DriverName set in the ResourceClaimStatus this AllocationResult is embedded in. """,
    )
    shareable: bool = Field(
        default=None,
        description=r""" Shareable determines whether the resource supports more than one consumer at a time. """,
    )


class ResourceClaimConsumerReference(BaseModel):
    apiGroup: str = Field(
        default=None,
        description=r""" APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """,
    )
    name: str = Field(
        default=None,
        description=r""" Name is the name of resource being referenced. """,
    )
    resource: str = Field(
        default=None,
        description=r""" Resource is the type of resource being referenced, for example "pods". """,
    )
    uid: str = Field(
        default=None,
        description=r""" UID identifies exactly one incarnation of the resource. """,
    )


class ResourceClaimParametersReference(BaseModel):
    apiGroup: str = Field(
        default=None,
        description=r""" APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """,
    )
    kind: str = Field(
        default="ResourceClaimParametersReference",
        description=r""" Kind is the type of resource being referenced. This is the same value as in the parameter object's metadata, for example "ConfigMap". """,
    )
    name: str = Field(
        default=None,
        description=r""" Name is the name of resource being referenced. """,
    )


class ResourceClaimSchedulingStatus(BaseModel):
    name: str = Field(
        default=None,
        description=r""" Name matches the pod.spec.resourceClaims[*].Name field. """,
    )
    unsuitableNodes: List[str] = Field(
        default=None,
        description=r""" UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced. """,
    )


class ResourceClassParametersReference(BaseModel):
    apiGroup: str = Field(
        default=None,
        description=r""" APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """,
    )
    kind: str = Field(
        default="ResourceClassParametersReference",
        description=r""" Kind is the type of resource being referenced. This is the same value as in the parameter object's metadata. """,
    )
    name: str = Field(
        default=None,
        description=r""" Name is the name of resource being referenced. """,
    )
    namespace: str = Field(
        default=None,
        description=r""" Namespace that contains the referenced resource. Must be empty for cluster-scoped resources and non-empty for namespaced resources. """,
    )


class ResourceHandle(BaseModel):
    data: str = Field(
        default=None,
        description=r""" Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced. """,
    )
    driverName: str = Field(
        default=None,
        description=r""" DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle's data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in. """,
    )
