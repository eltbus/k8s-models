from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta, ListMeta
from k8s_models.definitions.resource_k8s_io import ResourceClaimParametersReference
from k8s_models.metadata.resource_k8s_io import ResourceClass


class PodSchedulingContextSpec(BaseModel):
    potentialNodes: List[str] = Field(
        default=None,
        description=r""" PotentialNodes lists nodes where the Pod might be able to run.  The size of this field is limited to 128. This is large enough for many clusters. Larger clusters may need more attempts to find a node that suits all pending resources. This may get increased in the future, but not reduced. """,
    )
    selectedNode: str = Field(
        default=None,
        description=r""" SelectedNode is the node for which allocation of ResourceClaims that are referenced by the Pod and that use "WaitForFirstConsumer" allocation is to be attempted. """,
    )


class ResourceClaimSpec(BaseModel):
    allocationMode: str = Field(
        default=None,
        description=r""" Allocation can start immediately or when a Pod wants to use the resource. "WaitForFirstConsumer" is the default. """,
    )
    parametersRef: ResourceClaimParametersReference = Field(
        default=None,
        description=r""" ParametersRef references a separate object with arbitrary parameters that will be used by the driver when allocating a resource for the claim.  The object must be in the same namespace as the ResourceClaim. """,
    )
    resourceClassName: str = Field(
        default=None,
        description=r""" ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment. """,
    )


class ResourceClaimTemplateSpec(BaseModel):
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" ObjectMeta may contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """,
    )
    spec: ResourceClaimSpec = Field(
        default=None,
        description=r""" Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that gets created from this template. The same fields as in a ResourceClaim are also valid here. """,
    )


class ResourceClassList(BaseModel):
    apiVersion: str = Field(
        default="v1alpha2",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    items: List[ResourceClass] = Field(
        default=None, description=r""" Items is the list of resource classes. """
    )
    kind: str = Field(
        default="ResourceClassList",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ListMeta = Field(
        default=None, description=r""" Standard list metadata """
    )
