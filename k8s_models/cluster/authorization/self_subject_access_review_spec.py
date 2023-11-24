from pydantic import BaseModel, Field


class SelfSubjectAccessReviewSpec(BaseModel):
    nonResourceAttributes: NonResourceAttributes = Field(default=None, description=r""" NonResourceAttributes describes information for a non-resource access request """)
    resourceAttributes: ResourceAttributes = Field(default=None, description=r""" ResourceAuthorizationAttributes describes information for a resource access request """)
