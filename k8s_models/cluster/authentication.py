from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.meta import Time
from k8s_models.definitions.authentication_k8s_io import UserInfo, BoundObjectReference

class SelfSubjectReviewStatus(BaseModel):
	userInfo: UserInfo = Field(default=None, description=r""" User attributes of the user making this request. """)

class TokenRequestSpec(BaseModel):
	audiences: List[str] = Field(default=None, description=r""" Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. """)
	boundObjectRef: BoundObjectReference = Field(default=None, description=r""" BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation. """)
	expirationSeconds: int = Field(default=None, description=r""" ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response. """)

class TokenRequestStatus(BaseModel):
	expirationTimestamp: Time = Field(default=None, description=r""" ExpirationTimestamp is the time of expiration of the returned token. """)
	token: str = Field(default=None, description=r""" Token is the opaque bearer token. """)

class TokenReviewSpec(BaseModel):
	audiences: List[str] = Field(default=None, description=r""" Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver. """)
	token: str = Field(default=None, description=r""" Token is the opaque bearer token. """)

class TokenReviewStatus(BaseModel):
	audiences: List[str] = Field(default=None, description=r""" Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server. """)
	authenticated: bool = Field(default=None, description=r""" Authenticated indicates that the token was associated with a known user. """)
	error: str = Field(default=None, description=r""" Error indicates that the token couldn't be checked """)
	user: UserInfo = Field(default=None, description=r""" User is the UserInfo associated with the provided token. """)
