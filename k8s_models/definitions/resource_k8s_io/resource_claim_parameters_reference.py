from pydantic import BaseModel, Field


class ResourceClaimParametersReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """)
    kind: str = Field(default="ResourceClaimParametersReference", description=r""" Kind is the type of resource being referenced. This is the same value as in the parameter object's metadata, for example "ConfigMap". """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced. """)
