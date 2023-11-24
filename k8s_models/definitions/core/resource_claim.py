from pydantic import BaseModel, Field


class ResourceClaim(BaseModel):
    name: str = Field(default=None, description=r""" Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. """)
