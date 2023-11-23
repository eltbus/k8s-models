from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.authorization_k8s_io import (
    NonResourceAttributes,
    ResourceAttributes,
)

class SelfSubjectAccessReviewSpec(BaseModel):
	nonResourceAttributes: NonResourceAttributes = Field(default=None, description=r""" NonResourceAttributes describes information for a non-resource access request """)
	resourceAttributes: ResourceAttributes = Field(default=None, description=r""" ResourceAuthorizationAttributes describes information for a resource access request """)

class SelfSubjectRulesReviewSpec(BaseModel):
	namespace: str = Field(default=None, description=r""" Namespace to evaluate rules for. Required. """)

class SubjectAccessReviewSpec(BaseModel):
	extra: dict = Field(default=None, description=r""" Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here. """)
	groups: List[str] = Field(default=None, description=r""" Groups is the groups you're testing for. """)
	nonResourceAttributes: NonResourceAttributes = Field(default=None, description=r""" NonResourceAttributes describes information for a non-resource access request """)
	resourceAttributes: ResourceAttributes = Field(default=None, description=r""" ResourceAuthorizationAttributes describes information for a resource access request """)
	uid: str = Field(default=None, description=r""" UID information about the requesting user. """)
	user: str = Field(default=None, description=r""" User is the user you're testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups """)

class SubjectAccessReviewStatus(BaseModel):
	allowed: bool = Field(default=None, description=r""" Allowed is required. True if the action would be allowed, false otherwise. """)
	denied: bool = Field(default=None, description=r""" Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true. """)
	evaluationError: str = Field(default=None, description=r""" EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request. """)
	reason: str = Field(default=None, description=r""" Reason is optional.  It indicates why a request was allowed or denied. """)
