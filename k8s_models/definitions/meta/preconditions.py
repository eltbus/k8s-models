from pydantic import BaseModel, Field


class Preconditions(BaseModel):
    resourceVersion: str = Field(default=None, description=r""" Specifies the target ResourceVersion """)
    uid: str = Field(default=None, description=r""" Specifies the target UID. """)
