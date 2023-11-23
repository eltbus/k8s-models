from __future__ import annotations

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.cluster.authorization import (
    SubjectAccessReviewSpec,
    SelfSubjectAccessReviewSpec,
    SelfSubjectRulesReviewSpec,
)
from k8s_models.definitions.authorization_k8s_io import SubjectRulesReviewStatus
from k8s_models.cluster.authorization import SubjectAccessReviewStatus

class LocalSubjectAccessReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="LocalSubjectAccessReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: SubjectAccessReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated.  spec.namespace must be equal to the namespace you made the request against.  If empty, it is defaulted. """)
    status: SubjectAccessReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates whether the request is allowed or not """)

class SelfSubjectAccessReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="SelfSubjectAccessReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: SelfSubjectAccessReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated.  user and groups must be empty """)
    status: SubjectAccessReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates whether the request is allowed or not """)

class SelfSubjectRulesReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="SelfSubjectRulesReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: SelfSubjectRulesReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated. """)
    status: SubjectRulesReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates the set of actions a user can perform. """)

class SubjectAccessReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="SubjectAccessReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: SubjectAccessReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated """)
    status: SubjectAccessReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates whether the request is allowed or not """)
