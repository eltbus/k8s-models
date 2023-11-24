from pydantic import Field

from k8s_models.models import KubeModel


class PodDisruptionBudget(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="PodDisruptionBudget", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: PodDisruptionBudgetSpec = Field(default=None, description=r""" Specification of the desired behavior of the PodDisruptionBudget. """)
    status: PodDisruptionBudgetStatus = Field(default=None, description=r""" Most recently observed status of the PodDisruptionBudget. """)
