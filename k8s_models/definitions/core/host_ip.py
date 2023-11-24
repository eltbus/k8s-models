from pydantic import BaseModel, Field


class HostIP(BaseModel):
    ip: str = Field(default=None, description=r""" IP is the IP address assigned to the host """)
