from pydantic import Field

from k8s_models.models import KubeModel


class BoundObjectReference(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" API version of the referent. """)
    kind: str = Field(default="BoundObjectReference", description=r""" Kind of the referent. Valid kinds are 'Pod' and 'Secret'. """)
    name: str = Field(default=None, description=r""" Name of the referent. """)
    uid: str = Field(default=None, description=r""" UID of the referent. """)
