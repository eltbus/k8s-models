from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.models import KubeModel
from k8s_models.cluster.coordination_k8s_io import Lease
from k8s_models.definitions.meta import MicroTime, ListMeta

class LeaseSpec(BaseModel):
    acquireTime: MicroTime = Field(default=None, description=r""" acquireTime is a time when the current lease was acquired. """)
    holderIdentity: str = Field(default=None, description=r""" holderIdentity contains the identity of the holder of a current lease. """)
    leaseDurationSeconds: int = Field(default=None, description=r""" leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed renewTime. """)
    leaseTransitions: int = Field(default=None, description=r""" leaseTransitions is the number of transitions of a lease between holders. """)
    renewTime: MicroTime = Field(default=None, description=r""" renewTime is a time when the current holder of a lease has last updated the lease. """)

class LeaseList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Lease] = Field(default=None, description=r""" items is a list of schema objects. """)
    kind: str = Field(default="LeaseList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
