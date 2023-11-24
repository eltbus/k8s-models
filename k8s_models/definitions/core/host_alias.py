from pydantic import BaseModel, Field


class HostAlias(BaseModel):
    hostnames: List[str] = Field(default=None, description=r""" Hostnames for the above IP address. """)
    ip: str = Field(default=None, description=r""" IP address of the host file entry. """)
