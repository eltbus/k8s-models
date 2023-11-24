from typing import List

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.workloads.core.pod import Pod
from k8s_models.definitions.meta.list_meta import ListMeta


class PodList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Pod] = Field(default=None, description=r""" List of pods. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md """)
    kind: str = Field(default="PodList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
