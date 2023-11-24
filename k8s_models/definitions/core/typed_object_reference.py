from pydantic import BaseModel, Field


class TypedObjectReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
    kind: str = Field(default="TypedObjectReference", description=r""" Kind is the type of resource being referenced """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)
    namespace: str = Field(default=None, description=r""" Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. """)
