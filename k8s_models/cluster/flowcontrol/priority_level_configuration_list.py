from pydantic import Field

from k8s_models.models import KubeModel


class PriorityLevelConfigurationList(KubeModel):
    apiVersion: str = Field(default="v1beta3", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PriorityLevelConfiguration] = Field(default=None, description=r""" `items` is a list of request-priorities. """)
    kind: str = Field(default="PriorityLevelConfigurationList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
