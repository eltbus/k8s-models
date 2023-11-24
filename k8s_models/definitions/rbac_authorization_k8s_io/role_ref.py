from pydantic import BaseModel, Field


class RoleRef(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced """)
    kind: str = Field(default="RoleRef", description=r""" Kind is the type of resource being referenced """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)
