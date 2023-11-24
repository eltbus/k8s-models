from pydantic import BaseModel, Field


class ResourceAttributes(BaseModel):
    group: str = Field(default=None, description=r""" Group is the API Group of the Resource.  "*" means all. """)
    name: str = Field(default=None, description=r""" Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all. """)
    namespace: str = Field(default=None, description=r""" Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview """)
    resource: str = Field(default=None, description=r""" Resource is one of the existing resource types.  "*" means all. """)
    subresource: str = Field(default=None, description=r""" Subresource is one of the existing resource types.  "" means none. """)
    verb: str = Field(default=None, description=r""" Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all. """)
    version: str = Field(default=None, description=r""" Version is the API Version of the Resource.  "*" means all. """)
