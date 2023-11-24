from pydantic import BaseModel, Field


class TokenRequestStatus(BaseModel):
    expirationTimestamp: Time = Field(default=None, description=r""" ExpirationTimestamp is the time of expiration of the returned token. """)
    token: str = Field(default=None, description=r""" Token is the opaque bearer token. """)
