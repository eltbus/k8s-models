from pydantic import BaseModel, Field


class TokenReviewSpec(BaseModel):
    audiences: List[str] = Field(default=None, description=r""" Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver. """)
    token: str = Field(default=None, description=r""" Token is the opaque bearer token. """)
