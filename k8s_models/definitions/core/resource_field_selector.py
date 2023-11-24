from pydantic import BaseModel, Field


class ResourceFieldSelector(BaseModel):
    containerName: str = Field(default=None, description=r""" Container name: required for volumes, optional for env vars """)
    divisor: Quantity = Field(default=None, description=r""" Specifies the output format of the exposed resources, defaults to "1" """)
    resource: str = Field(default=None, description=r""" Required: resource to select """)
