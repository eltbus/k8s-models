from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.internal_apiserver_k8s_io.server_storage_version import ServerStorageVersion
from k8s_models.definitions.internal_apiserver_k8s_io.storage_version_condition import StorageVersionCondition


class StorageVersionStatus(BaseModel):
    commonEncodingVersion: str = Field(default=None, description=r""" If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality. """)
    conditions: List[StorageVersionCondition] = Field(default=None, description=r""" The latest available observations of the storageVersion's state. """)
    storageVersions: List[ServerStorageVersion] = Field(default=None, description=r""" The reported versions per API server instance. """)
