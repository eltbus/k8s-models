from typing import List

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.metadata.admissionregistration_k8s_io.validating_webhook_configuration import ValidatingWebhookConfiguration
from k8s_models.definitions.meta.list_meta import ListMeta


class ValidatingWebhookConfigurationList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ValidatingWebhookConfiguration] = Field(default=None, description=r""" List of ValidatingWebhookConfiguration. """)
    kind: str = Field(default="ValidatingWebhookConfigurationList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
