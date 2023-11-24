from typing import List

from pydantic import BaseModel, Field


class APIResource(BaseModel):
    categories: List[str] = Field(default=None, description=r""" categories is a list of the grouped resources this resource belongs to (e.g. 'all') """)
    group: str = Field(default=None, description=r""" group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale". """)
    kind: str = Field(default="APIResource", description=r""" kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo') """)
    name: str = Field(default=None, description=r""" name is the plural name of the resource. """)
    namespaced: bool = Field(default=None, description=r""" namespaced indicates if a resource is namespaced or not. """)
    shortNames: List[str] = Field(default=None, description=r""" shortNames is a list of suggested short names of the resource. """)
    singularName: str = Field(default=None, description=r""" singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface. """)
    storageVersionHash: str = Field(default=None, description=r""" The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates. """)
    verbs: List[str] = Field(default=None, description=r""" verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy) """)
    version: str = Field(default=None, description=r""" version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)". """)
