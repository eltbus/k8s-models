from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.meta import ListMeta
from k8s_models.definitions.internal_apiserver_k8s_io import StorageVersionCondition, ServerStorageVersion
from k8s_models.cluster.internal_apiserver_k8s_io import StorageVersion

class StorageVersionSpec(BaseModel):
	pass


class StorageVersionStatus(BaseModel):
	commonEncodingVersion: str = Field(default=None, description=r""" If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality. """)
	conditions: List[StorageVersionCondition] = Field(default=None, description=r""" The latest available observations of the storageVersion's state. """)
	storageVersions: List[ServerStorageVersion] = Field(default=None, description=r""" The reported versions per API server instance. """)

class StorageVersionList(BaseModel):
	apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[StorageVersion] = Field(default=None, description=r""" Items holds a list of StorageVersion """)
	kind: str = Field(default="StorageVersionList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
