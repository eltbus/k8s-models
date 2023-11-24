from pydantic import BaseModel, Field


class TypedLocalObjectReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
    kind: str = Field(default="TypedLocalObjectReference", description=r""" Kind is the type of resource being referenced """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)
