from __future__ import annotations

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.cluster.authentication import (
    SelfSubjectReviewStatus,
    TokenRequestSpec,
    TokenReviewSpec,
)
from k8s_models.definitions.unknown import TokenRequestStatus, TokenReviewStatus


class SelfSubjectReview(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="SelfSubjectReview",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    status: SelfSubjectReviewStatus = Field(
        default=None,
        description=r""" Status is filled in by the server with the user attributes. """,
    )


class TokenRequest(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="TokenRequest",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: TokenRequestSpec = Field(
        default=None,
        description=r""" Spec holds information about the request being evaluated """,
    )
    status: TokenRequestStatus = Field(
        default=None,
        description=r""" Status is filled in by the server and indicates whether the token can be authenticated. """,
    )


class TokenReview(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="TokenReview",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: TokenReviewSpec = Field(
        default=None,
        description=r""" Spec holds information about the request being evaluated """,
    )
    status: TokenReviewStatus = Field(
        default=None,
        description=r""" Status is filled in by the server and indicates whether the request can be authenticated. """,
    )
