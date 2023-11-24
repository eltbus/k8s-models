from pydantic import Field

from k8s_models.models import KubeModel


class PodSchedulingContext(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="PodSchedulingContext", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata """)
    spec: PodSchedulingContextSpec = Field(default=None, description=r""" Spec describes where resources for the Pod are needed. """)
    status: PodSchedulingContextStatus = Field(default=None, description=r""" Status describes where resources for the Pod can be allocated. """)
