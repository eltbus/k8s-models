from pydantic import BaseModel, Field


class CephFSVolumeSource(BaseModel):
    monitors: List[str] = Field(default=None, description=r""" monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    path: str = Field(default=None, description=r""" path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    secretFile: str = Field(default=None, description=r""" secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    user: str = Field(default=None, description=r""" user is optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
