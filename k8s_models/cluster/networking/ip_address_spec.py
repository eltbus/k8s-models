from pydantic import BaseModel, Field

from k8s_models.definitions.networking_k8s_io.parent_reference import ParentReference


class IPAddressSpec(BaseModel):
    parentRef: ParentReference = Field(default=None, description=r""" ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object. """)
