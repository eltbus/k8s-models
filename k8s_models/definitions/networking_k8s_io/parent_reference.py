from pydantic import BaseModel, Field


class ParentReference(BaseModel):
    group: str = Field(default=None, description=r""" Group is the group of the object being referenced. """)
    name: str = Field(default=None, description=r""" Name is the name of the object being referenced. """)
    namespace: str = Field(default=None, description=r""" Namespace is the namespace of the object being referenced. """)
    resource: str = Field(default=None, description=r""" Resource is the resource of the object being referenced. """)
    uid: str = Field(default=None, description=r""" UID is the uid of the object being referenced. """)
