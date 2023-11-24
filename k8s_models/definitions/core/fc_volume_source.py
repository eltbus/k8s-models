from pydantic import BaseModel, Field


class FCVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    lun: int = Field(default=None, description=r""" lun is Optional: FC target lun number """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    targetWWNs: List[str] = Field(default=None, description=r""" targetWWNs is Optional: FC target worldwide names (WWNs) """)
    wwids: List[str] = Field(default=None, description=r""" wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. """)
