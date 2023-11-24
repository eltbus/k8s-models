from pydantic import BaseModel, Field

from k8s_models.definitions.core.claim_source import ClaimSource


class PodResourceClaim(BaseModel):
    name: str = Field(default=None, description=r""" Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL. """)
    source: ClaimSource = Field(default=None, description=r""" Source describes where to find the ResourceClaim. """)
