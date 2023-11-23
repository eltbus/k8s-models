from __future__ import annotations
from typing import List

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.cluster.node_k8s_io import RuntimeClass
from k8s_models.definitions.meta import ListMeta

class RuntimeClassList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[RuntimeClass] = Field(default=None, description=r""" items is a list of schema objects. """)
    kind: str = Field(default="RuntimeClassList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
