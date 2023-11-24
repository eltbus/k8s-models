from typing import List

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.metadata.autoscaling.horizontal_pod_autoscaler import HorizontalPodAutoscaler
from k8s_models.definitions.meta.list_meta import ListMeta


class HorizontalPodAutoscalerList(KubeModel):
    apiVersion: str = Field(default="v2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[HorizontalPodAutoscaler] = Field(default=None, description=r""" items is the list of horizontal pod autoscaler objects. """)
    kind: str = Field(default="HorizontalPodAutoscalerList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" metadata is the standard list metadata. """)
