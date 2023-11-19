from __future__ import annotations

from pydantic import BaseModel, Field
from k8s_py.definitions.meta import Time


class CertificateSigningRequestCondition(BaseModel):
    lastTransitionTime: Time = Field(
        default=None,
        description=r""" lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition's status is changed, the server defaults this to the current time. """,
    )
    lastUpdateTime: Time = Field(
        default=None,
        description=r""" lastUpdateTime is the time of the last update to this condition """,
    )
    message: str = Field(
        default=None,
        description=r""" message contains a human readable message with details about the request state """,
    )
    reason: str = Field(
        default=None,
        description=r""" reason indicates a brief reason for the request state """,
    )
    status: str = Field(
        default=None,
        description=r""" status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be "False" or "Unknown". """,
    )
    type: str = Field(
        default=None,
        description=r""" type of the condition. Known conditions are "Approved", "Denied", and "Failed".  An "Approved" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.  A "Denied" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.  A "Failed" condition is added via the /status subresource, indicating the signer failed to issue the certificate.  Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.  Only one condition of a given type is allowed. """,
    )
