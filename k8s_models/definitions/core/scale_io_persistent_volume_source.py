from pydantic import BaseModel, Field


class ScaleIOPersistentVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs" """)
    gateway: str = Field(default=None, description=r""" gateway is the host address of the ScaleIO API Gateway. """)
    protectionDomain: str = Field(default=None, description=r""" protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. """)
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. """)
    sslEnabled: bool = Field(default=None, description=r""" sslEnabled is the flag to enable/disable SSL communication with Gateway, default false """)
    storageMode: str = Field(default=None, description=r""" storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. """)
    storagePool: str = Field(default=None, description=r""" storagePool is the ScaleIO Storage Pool associated with the protection domain. """)
    system: str = Field(default=None, description=r""" system is the name of the storage system as configured in ScaleIO. """)
    volumeName: str = Field(default=None, description=r""" volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. """)
