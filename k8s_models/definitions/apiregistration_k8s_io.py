from __future__ import annotations

from pydantic import BaseModel, Field
from k8s_py.definitions.meta import Time


class APIServiceCondition(BaseModel):
    lastTransitionTime: Time = Field(
        default=None,
        description=r""" Last time the condition transitioned from one status to another. """,
    )
    message: str = Field(
        default=None,
        description=r""" Human-readable message indicating details about last transition. """,
    )
    reason: str = Field(
        default=None,
        description=r""" Unique, one-word, CamelCase reason for the condition's last transition. """,
    )
    status: str = Field(
        default=None,
        description=r""" Status is the status of the condition. Can be True, False, Unknown. """,
    )
    type: str = Field(
        default=None, description=r""" Type is the type of the condition. """
    )
