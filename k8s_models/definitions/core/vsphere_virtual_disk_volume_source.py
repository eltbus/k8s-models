from pydantic import BaseModel, Field


class VsphereVirtualDiskVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    storagePolicyID: str = Field(default=None, description=r""" storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. """)
    storagePolicyName: str = Field(default=None, description=r""" storagePolicyName is the storage Policy Based Management (SPBM) profile name. """)
    volumePath: str = Field(default=None, description=r""" volumePath is the path that identifies vSphere volume vmdk """)
