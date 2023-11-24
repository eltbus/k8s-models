from pydantic import BaseModel, Field

from k8s_models.definitions.core.local_object_reference import LocalObjectReference


class CSIVolumeSource(BaseModel):
    driver: str = Field(default=None, description=r""" driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. """)
    fsType: str = Field(default=None, description=r""" fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. """)
    nodePublishSecretRef: LocalObjectReference = Field(default=None, description=r""" nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed. """)
    readOnly: bool = Field(default=None, description=r""" readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). """)
    volumeAttributes: dict = Field(default=None, description=r""" volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values. """)
