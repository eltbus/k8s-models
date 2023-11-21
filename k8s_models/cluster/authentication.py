from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.authentication_k8s_io import UserInfo, BoundObjectReference


class SelfSubjectReviewStatus(BaseModel):
    userInfo: UserInfo = Field(
        default=None,
        description=r""" User attributes of the user making this request. """,
    )


class TokenRequestSpec(BaseModel):
    audiences: List[str] = Field(
        default=None,
        description=r""" Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. """,
    )
    boundObjectRef: BoundObjectReference = Field(
        default=None,
        description=r""" BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation. """,
    )
    expirationSeconds: int = Field(
        default=None,
        description=r""" ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response. """,
    )


class TokenReviewSpec(BaseModel):
    audiences: List[str] = Field(
        default=None,
        description=r""" Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver. """,
    )
    token: str = Field(
        default=None, description=r""" Token is the opaque bearer token. """
    )
