from pydantic import BaseModel, Field


class ResourceClaimTemplateSpec(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" ObjectMeta may contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """)
    spec: ResourceClaimSpec = Field(default=None, description=r""" Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that gets created from this template. The same fields as in a ResourceClaim are also valid here. """)