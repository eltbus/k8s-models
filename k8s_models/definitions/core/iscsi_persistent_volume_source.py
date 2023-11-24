from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.secret_reference import SecretReference


class ISCSIPersistentVolumeSource(BaseModel):
    chapAuthDiscovery: bool = Field(default=None, description=r""" chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication """)
    chapAuthSession: bool = Field(default=None, description=r""" chapAuthSession defines whether support iSCSI Session CHAP authentication """)
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi """)
    initiatorName: str = Field(default=None, description=r""" initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection. """)
    iqn: str = Field(default=None, description=r""" iqn is Target iSCSI Qualified Name. """)
    iscsiInterface: str = Field(default=None, description=r""" iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). """)
    lun: int = Field(default=None, description=r""" lun is iSCSI Target Lun number. """)
    portals: List[str] = Field(default=None, description=r""" portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef is the CHAP Secret for iSCSI target and initiator authentication """)
    targetPortal: str = Field(default=None, description=r""" targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)
