from pydantic import Field

from k8s_models.models import KubeModel


class OwnerReference(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" API version of the referent. """)
    blockOwnerDeletion: bool = Field(default=None, description=r""" If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned. """)
    controller: bool = Field(default=None, description=r""" If true, this reference points to the managing controller. """)
    kind: str = Field(default="OwnerReference", description=r""" Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names """)
    uid: str = Field(default=None, description=r""" UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids """)
