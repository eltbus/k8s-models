from pydantic import BaseModel, Field


class NodeAddress(BaseModel):
    address: str = Field(default=None, description=r""" The node address. """)
    type: str = Field(default=None, description=r""" Node address type, one of Hostname, ExternalIP or InternalIP. """)
