from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta import ObjectMeta, ListMeta
from k8s_models.definitions.resource_k8s_io import ResourceClaimParametersReference, ResourceClaimSchedulingStatus, AllocationResult, ResourceClaimConsumerReference
from k8s_models.metadata.resource_k8s_io import ResourceClass, PodSchedulingContext, ResourceClaimTemplate, ResourceClaim

class PodSchedulingContextSpec(BaseModel):
	potentialNodes: List[str] = Field(default=None, description=r""" PotentialNodes lists nodes where the Pod might be able to run.  The size of this field is limited to 128. This is large enough for many clusters. Larger clusters may need more attempts to find a node that suits all pending resources. This may get increased in the future, but not reduced. """)
	selectedNode: str = Field(default=None, description=r""" SelectedNode is the node for which allocation of ResourceClaims that are referenced by the Pod and that use "WaitForFirstConsumer" allocation is to be attempted. """)

class PodSchedulingContextStatus(BaseModel):
	resourceClaims: List[ResourceClaimSchedulingStatus] = Field(default=None, description=r""" ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses "WaitForFirstConsumer" allocation mode. """)

class PodSchedulingContextList(KubeModel):
	apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[PodSchedulingContext] = Field(default=None, description=r""" Items is the list of PodSchedulingContext objects. """)
	kind: str = Field(default="PodSchedulingContextList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)

class ResourceClaimSpec(BaseModel):
	allocationMode: str = Field(default=None, description=r""" Allocation can start immediately or when a Pod wants to use the resource. "WaitForFirstConsumer" is the default. """)
	parametersRef: ResourceClaimParametersReference = Field(default=None, description=r""" ParametersRef references a separate object with arbitrary parameters that will be used by the driver when allocating a resource for the claim.  The object must be in the same namespace as the ResourceClaim. """)
	resourceClassName: str = Field(default=None, description=r""" ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment. """)

class ResourceClaimStatus(BaseModel):
	allocation: AllocationResult = Field(default=None, description=r""" Allocation is set by the resource driver once a resource or set of resources has been allocated successfully. If this is not specified, the resources have not been allocated yet. """)
	deallocationRequested: bool = Field(default=None, description=r""" DeallocationRequested indicates that a ResourceClaim is to be deallocated.  The driver then must deallocate this claim and reset the field together with clearing the Allocation field.  While DeallocationRequested is set, no new consumers may be added to ReservedFor. """)
	driverName: str = Field(default=None, description=r""" DriverName is a copy of the driver name from the ResourceClass at the time when allocation started. """)
	reservedFor: List[ResourceClaimConsumerReference] = Field(default=None, description=r""" ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started.  There can be at most 32 such reservations. This may get increased in the future, but not reduced. """)

class ResourceClaimList(KubeModel):
	apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ResourceClaim] = Field(default=None, description=r""" Items is the list of resource claims. """)
	kind: str = Field(default="ResourceClaimList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)

class ResourceClaimTemplateSpec(BaseModel):
	metadata: ObjectMeta = Field(default=None, description=r""" ObjectMeta may contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """)
	spec: ResourceClaimSpec = Field(default=None, description=r""" Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that gets created from this template. The same fields as in a ResourceClaim are also valid here. """)

class ResourceClaimTemplateList(KubeModel):
	apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ResourceClaimTemplate] = Field(default=None, description=r""" Items is the list of resource claim templates. """)
	kind: str = Field(default="ResourceClaimTemplateList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)

class ResourceClassList(KubeModel):
	apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ResourceClass] = Field(default=None, description=r""" Items is the list of resource classes. """)
	kind: str = Field(default="ResourceClassList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)
