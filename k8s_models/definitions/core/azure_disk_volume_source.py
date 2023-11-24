from pydantic import BaseModel, Field


class AzureDiskVolumeSource(BaseModel):
    cachingMode: str = Field(default=None, description=r""" cachingMode is the Host Caching mode: None, Read Only, Read Write. """)
    diskName: str = Field(default=None, description=r""" diskName is the Name of the data disk in the blob storage """)
    diskURI: str = Field(default=None, description=r""" diskURI is the URI of data disk in the blob storage """)
    fsType: str = Field(default=None, description=r""" fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    kind: str = Field(default="AzureDiskVolumeSource", description=r""" kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared """)
    readOnly: bool = Field(default=None, description=r""" readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
