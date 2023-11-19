from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field


class BoundObjectReference(BaseModel):
    apiVersion: str = Field(
        default=None, description=r""" API version of the referent. """
    )
    kind: str = Field(
        default=None,
        description=r""" Kind of the referent. Valid kinds are 'Pod' and 'Secret'. """,
    )
    name: str = Field(default=None, description=r""" Name of the referent. """)
    uid: str = Field(default=None, description=r""" UID of the referent. """)


class UserInfo(BaseModel):
    extra: dict = Field(
        default=None,
        description=r""" Any additional information provided by the authenticator. """,
    )
    groups: List[str] = Field(
        default=None, description=r""" The names of groups this user is a part of. """
    )
    uid: str = Field(
        default=None,
        description=r""" A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. """,
    )
    username: str = Field(
        default=None,
        description=r""" The name that uniquely identifies this user among all active users. """,
    )
