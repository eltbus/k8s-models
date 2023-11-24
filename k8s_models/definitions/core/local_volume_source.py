from pydantic import BaseModel, Field


class LocalVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified. """)
    path: str = Field(default=None, description=r""" path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, ...). """)
