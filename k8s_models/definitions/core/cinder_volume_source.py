from pydantic import BaseModel, Field


class CinderVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is optional: points to a secret object containing parameters used to connect to OpenStack. """)
    volumeID: str = Field(default=None, description=r""" volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
