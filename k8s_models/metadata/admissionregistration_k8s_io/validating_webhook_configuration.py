from typing import List

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta.object_meta import ObjectMeta
from k8s_models.definitions.admissionregistration_k8s_io.validating_webhook import ValidatingWebhook


class ValidatingWebhookConfiguration(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ValidatingWebhookConfiguration", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """)
    webhooks: List[ValidatingWebhook] = Field(default=None, description=r""" Webhooks is a list of webhooks and the affected resources and operations. """)
