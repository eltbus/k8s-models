from pydantic import BaseModel, Field


class PodDNSConfigOption(BaseModel):
    name: str = Field(default=None, description=r""" Required. """)
    value: str = Field(default=None)
