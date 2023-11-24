from pydantic import Field

from k8s_models.models import KubeModel


class CrossVersionObjectReference(KubeModel):
    apiVersion: str = Field(default="v2", description=r""" apiVersion is the API version of the referent """)
    kind: str = Field(default="CrossVersionObjectReference", description=r""" kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
