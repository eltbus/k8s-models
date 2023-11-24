from pydantic import BaseModel, Field


class ResourceClaimConsumerReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced. """)
    resource: str = Field(default=None, description=r""" Resource is the type of resource being referenced, for example "pods". """)
    uid: str = Field(default=None, description=r""" UID identifies exactly one incarnation of the resource. """)
