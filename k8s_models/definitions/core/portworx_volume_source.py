from pydantic import BaseModel, Field


class PortworxVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. """)
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    volumeID: str = Field(default=None, description=r""" volumeID uniquely identifies a Portworx volume """)
