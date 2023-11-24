from pydantic import Field

from k8s_models.models import KubeModel


class ResourceClaim(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ResourceClaim", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata """)
    spec: ResourceClaimSpec = Field(default=None, description=r""" Spec describes the desired attributes of a resource that then needs to be allocated. It can only be set once when creating the ResourceClaim. """)
    status: ResourceClaimStatus = Field(default=None, description=r""" Status describes whether the resource is available and with which attributes. """)
