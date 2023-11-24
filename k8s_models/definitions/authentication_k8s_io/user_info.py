from typing import List

from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    extra: dict = Field(default=None, description=r""" Any additional information provided by the authenticator. """)
    groups: List[str] = Field(default=None, description=r""" The names of groups this user is a part of. """)
    uid: str = Field(default=None, description=r""" A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. """)
    username: str = Field(default=None, description=r""" The name that uniquely identifies this user among all active users. """)
