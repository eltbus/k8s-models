from pydantic import BaseModel, Field


class ResourceRule(BaseModel):
    apiGroups: List[str] = Field(default=None, description=r""" APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  "*" means all. """)
    resourceNames: List[str] = Field(default=None, description=r""" ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  "*" means all. """)
    resources: List[str] = Field(default=None, description=r""" Resources is a list of resources this rule applies to.  "*" means all in the specified apiGroups.  "*/foo" represents the subresource 'foo' for all resources in the specified apiGroups. """)
    verbs: List[str] = Field(default=None, description=r""" Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  "*" means all. """)
