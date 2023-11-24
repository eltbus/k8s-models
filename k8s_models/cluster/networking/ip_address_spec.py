from pydantic import BaseModel, Field


class IPAddressSpec(BaseModel):
    parentRef: ParentReference = Field(default=None, description=r""" ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object. """)
