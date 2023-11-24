from pydantic import BaseModel, Field


class PodResourceClaim(BaseModel):
    name: str = Field(default=None, description=r""" Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL. """)
    source: ClaimSource = Field(default=None, description=r""" Source describes where to find the ResourceClaim. """)
