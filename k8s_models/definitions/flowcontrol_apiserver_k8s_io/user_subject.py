from pydantic import BaseModel, Field


class UserSubject(BaseModel):
    name: str = Field(default=None, description=r""" `name` is the username that matches, or "*" to match all usernames. Required. """)
