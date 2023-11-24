from pydantic import BaseModel, Field


class PolicyRule(BaseModel):
    apiGroups: List[str] = Field(default=None, description=r""" APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "*" represents all API groups. """)
    nonResourceURLs: List[str] = Field(default=None, description=r""" NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both. """)
    resourceNames: List[str] = Field(default=None, description=r""" ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. """)
    resources: List[str] = Field(default=None, description=r""" Resources is a list of resources this rule applies to. '\*' represents all resources. """)
    verbs: List[str] = Field(default=None, description=r""" Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '\*' represents all verbs. """)
