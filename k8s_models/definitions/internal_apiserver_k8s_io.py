from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import Time


class ServerStorageVersion(BaseModel):
    apiServerID: str = Field(
        default=None, description=r""" The ID of the reporting API server. """
    )
    decodableVersions: List[str] = Field(
        default=None,
        description=r""" The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. """,
    )
    encodingVersion: str = Field(
        default=None,
        description=r""" The API server encodes the object to this version when persisting it in the backend (e.g., etcd). """,
    )
    servedVersions: List[str] = Field(
        default=None,
        description=r""" The API server can serve these versions. DecodableVersions must include all ServedVersions. """,
    )


class StorageVersionCondition(BaseModel):
    lastTransitionTime: Time = Field(
        default=None,
        description=r""" Last time the condition transitioned from one status to another. """,
    )
    message: str = Field(
        default=None,
        description=r""" A human readable message indicating details about the transition. """,
    )
    observedGeneration: int = Field(
        default=None,
        description=r""" If set, this represents the .metadata.generation that the condition was set based upon. """,
    )
    reason: str = Field(
        default=None,
        description=r""" The reason for the condition's last transition. """,
    )
    status: str = Field(
        default=None,
        description=r""" Status of the condition, one of True, False, Unknown. """,
    )
    type: str = Field(default=None, description=r""" Type of the condition. """)
