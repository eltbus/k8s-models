from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.meta import LabelSelector

class AggregationRule(BaseModel):
    clusterRoleSelectors: List[LabelSelector] = Field(default=None, description=r""" ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added """)

class PolicyRule(BaseModel):
    apiGroups: List[str] = Field(default=None, description=r""" APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "*" represents all API groups. """)
    nonResourceURLs: List[str] = Field(default=None, description=r""" NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both. """)
    resourceNames: List[str] = Field(default=None, description=r""" ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. """)
    resources: List[str] = Field(default=None, description=r""" Resources is a list of resources this rule applies to. '\*' represents all resources. """)
    verbs: List[str] = Field(default=None, description=r""" Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '\*' represents all verbs. """)

class RoleRef(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced """)
    kind: str = Field(default="RoleRef", description=r""" Kind is the type of resource being referenced """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)
