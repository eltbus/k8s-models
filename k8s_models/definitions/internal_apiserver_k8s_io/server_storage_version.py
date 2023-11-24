from pydantic import BaseModel, Field


class ServerStorageVersion(BaseModel):
    apiServerID: str = Field(default=None, description=r""" The ID of the reporting API server. """)
    decodableVersions: List[str] = Field(default=None, description=r""" The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. """)
    encodingVersion: str = Field(default=None, description=r""" The API server encodes the object to this version when persisting it in the backend (e.g., etcd). """)
    servedVersions: List[str] = Field(default=None, description=r""" The API server can serve these versions. DecodableVersions must include all ServedVersions. """)
