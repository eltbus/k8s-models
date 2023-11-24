from pydantic import BaseModel, Field


class PhotonPersistentDiskVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    pdID: str = Field(default=None, description=r""" pdID is the ID that identifies Photon Controller persistent disk """)
