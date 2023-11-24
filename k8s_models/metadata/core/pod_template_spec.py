from pydantic import BaseModel, Field

from k8s_models.definitions.meta.object_meta import ObjectMeta
from k8s_models.workloads.core.pod_spec import PodSpec


class PodTemplateSpec(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: PodSpec = Field(default=None, description=r""" Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
