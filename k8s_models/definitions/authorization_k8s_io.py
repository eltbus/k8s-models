from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

class NonResourceAttributes(BaseModel):
	path: str = Field(default=None, description=r""" Path is the URL path of the request """)
	verb: str = Field(default=None, description=r""" Verb is the standard HTTP verb """)

class NonResourceRule(BaseModel):
	nonResourceURLs: List[str] = Field(default=None, description=r""" NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all. """)
	verbs: List[str] = Field(default=None, description=r""" Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all. """)

class ResourceAttributes(BaseModel):
	group: str = Field(default=None, description=r""" Group is the API Group of the Resource.  "*" means all. """)
	name: str = Field(default=None, description=r""" Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all. """)
	namespace: str = Field(default=None, description=r""" Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview """)
	resource: str = Field(default=None, description=r""" Resource is one of the existing resource types.  "*" means all. """)
	subresource: str = Field(default=None, description=r""" Subresource is one of the existing resource types.  "" means none. """)
	verb: str = Field(default=None, description=r""" Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all. """)
	version: str = Field(default=None, description=r""" Version is the API Version of the Resource.  "*" means all. """)

class ResourceRule(BaseModel):
	apiGroups: List[str] = Field(default=None, description=r""" APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  "*" means all. """)
	resourceNames: List[str] = Field(default=None, description=r""" ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  "*" means all. """)
	resources: List[str] = Field(default=None, description=r""" Resources is a list of resources this rule applies to.  "*" means all in the specified apiGroups.  "*/foo" represents the subresource 'foo' for all resources in the specified apiGroups. """)
	verbs: List[str] = Field(default=None, description=r""" Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  "*" means all. """)

class SubjectRulesReviewStatus(BaseModel):
	evaluationError: str = Field(default=None, description=r""" EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. """)
	incomplete: bool = Field(default=None, description=r""" Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation. """)
	nonResourceRules: List[NonResourceRule] = Field(default=None, description=r""" NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete. """)
	resourceRules: List[ResourceRule] = Field(default=None, description=r""" ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete. """)
