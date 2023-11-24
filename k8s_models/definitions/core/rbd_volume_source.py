from pydantic import BaseModel, Field


class RBDVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd """)
    image: str = Field(default=None, description=r""" image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    keyring: str = Field(default=None, description=r""" keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    monitors: List[str] = Field(default=None, description=r""" monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    pool: str = Field(default=None, description=r""" pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    user: str = Field(default=None, description=r""" user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
