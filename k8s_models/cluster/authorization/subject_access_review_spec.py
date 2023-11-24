from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.authorization_k8s_io.non_resource_attributes import NonResourceAttributes
from k8s_models.definitions.authorization_k8s_io.resource_attributes import ResourceAttributes


class SubjectAccessReviewSpec(BaseModel):
    extra: dict = Field(default=None, description=r""" Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here. """)
    groups: List[str] = Field(default=None, description=r""" Groups is the groups you're testing for. """)
    nonResourceAttributes: NonResourceAttributes = Field(default=None, description=r""" NonResourceAttributes describes information for a non-resource access request """)
    resourceAttributes: ResourceAttributes = Field(default=None, description=r""" ResourceAuthorizationAttributes describes information for a resource access request """)
    uid: str = Field(default=None, description=r""" UID information about the requesting user. """)
    user: str = Field(default=None, description=r""" User is the user you're testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups """)
