from pydantic import Field

from k8s_models.models import KubeModel


class PriorityClass(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    description: str = Field(default=None, description=r""" description is an arbitrary string that usually provides guidelines on when this priority class should be used. """)
    globalDefault: bool = Field(default=None, description=r""" globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority. """)
    kind: str = Field(default="PriorityClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    preemptionPolicy: str = Field(default=None, description=r""" preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. """)
    value: int = Field(default=None, description=r""" value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec. """)
