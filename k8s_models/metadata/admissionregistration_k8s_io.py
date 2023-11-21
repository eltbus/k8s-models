from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.definitions.admissionregistration_k8s_io import (
    MutatingWebhook,
    ValidatingWebhook,
)
from k8s_models.metadata.admissionregistration import (
    ValidatingAdmissionPolicySpec,
    ValidatingAdmissionPolicyBindingSpec,
)
from k8s_models.definitions.unknown import ValidatingAdmissionPolicyStatus


class MutatingWebhookConfiguration(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="MutatingWebhookConfiguration",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """,
    )
    webhooks: List[MutatingWebhook] = Field(
        default=None,
        description=r""" Webhooks is a list of webhooks and the affected resources and operations. """,
    )


class ValidatingWebhookConfiguration(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="ValidatingWebhookConfiguration",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """,
    )
    webhooks: List[ValidatingWebhook] = Field(
        default=None,
        description=r""" Webhooks is a list of webhooks and the affected resources and operations. """,
    )


class ValidatingAdmissionPolicy(BaseModel):
    apiVersion: str = Field(
        default="v1beta1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="ValidatingAdmissionPolicy",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """,
    )
    spec: ValidatingAdmissionPolicySpec = Field(
        default=None,
        description=r""" Specification of the desired behavior of the ValidatingAdmissionPolicy. """,
    )
    status: ValidatingAdmissionPolicyStatus = Field(
        default=None,
        description=r""" The status of the ValidatingAdmissionPolicy, including warnings that are useful to determine if the policy behaves in the expected way. Populated by the system. Read-only. """,
    )


class ValidatingAdmissionPolicyBinding(BaseModel):
    apiVersion: str = Field(
        default="v1beta1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="ValidatingAdmissionPolicyBinding",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """,
    )
    spec: ValidatingAdmissionPolicyBindingSpec = Field(
        default=None,
        description=r""" Specification of the desired behavior of the ValidatingAdmissionPolicyBinding. """,
    )
