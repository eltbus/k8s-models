from pydantic import BaseModel, Field


class IngressClassParametersReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
    kind: str = Field(default="IngressClassParametersReference", description=r""" kind is the type of resource being referenced. """)
    name: str = Field(default=None, description=r""" name is the name of resource being referenced. """)
    namespace: str = Field(default=None, description=r""" namespace is the namespace of the resource being referenced. This field is required when scope is set to "Namespace" and must be unset when scope is set to "Cluster". """)
    scope: str = Field(default=None, description=r""" scope represents if this refers to a cluster or namespace scoped resource. This may be set to "Cluster" (default) or "Namespace". """)
