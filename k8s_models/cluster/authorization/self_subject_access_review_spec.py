from pydantic import BaseModel, Field

from k8s_models.definitions.authorization_k8s_io.non_resource_attributes import NonResourceAttributes
from k8s_models.definitions.authorization_k8s_io.resource_attributes import ResourceAttributes


class SelfSubjectAccessReviewSpec(BaseModel):
    nonResourceAttributes: NonResourceAttributes = Field(default=None, description=r""" NonResourceAttributes describes information for a non-resource access request """)
    resourceAttributes: ResourceAttributes = Field(default=None, description=r""" ResourceAuthorizationAttributes describes information for a resource access request """)
