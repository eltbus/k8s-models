from __future__ import annotations

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import MicroTime


class LeaseSpec(BaseModel):
    acquireTime: MicroTime = Field(
        default=None,
        description=r""" acquireTime is a time when the current lease was acquired. """,
    )
    holderIdentity: str = Field(
        default=None,
        description=r""" holderIdentity contains the identity of the holder of a current lease. """,
    )
    leaseDurationSeconds: int = Field(
        default=None,
        description=r""" leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed renewTime. """,
    )
    leaseTransitions: int = Field(
        default=None,
        description=r""" leaseTransitions is the number of transitions of a lease between holders. """,
    )
    renewTime: MicroTime = Field(
        default=None,
        description=r""" renewTime is a time when the current holder of a lease has last updated the lease. """,
    )
