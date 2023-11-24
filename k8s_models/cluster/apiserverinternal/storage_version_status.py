from pydantic import BaseModel, Field


class StorageVersionStatus(BaseModel):
    commonEncodingVersion: str = Field(default=None, description=r""" If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality. """)
    conditions: List[StorageVersionCondition] = Field(default=None, description=r""" The latest available observations of the storageVersion's state. """)
    storageVersions: List[ServerStorageVersion] = Field(default=None, description=r""" The reported versions per API server instance. """)
