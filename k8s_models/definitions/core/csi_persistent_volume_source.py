from pydantic import BaseModel, Field

from k8s_models.definitions.core.secret_reference import SecretReference


class CSIPersistentVolumeSource(BaseModel):
    controllerExpandSecretRef: SecretReference = Field(default=None, description=r""" controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    controllerPublishSecretRef: SecretReference = Field(default=None, description=r""" controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    driver: str = Field(default=None, description=r""" driver is the name of the driver to use for this volume. Required. """)
    fsType: str = Field(default=None, description=r""" fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". """)
    nodeExpandSecretRef: SecretReference = Field(default=None, description=r""" nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This is a beta field which is enabled default by CSINodeExpandSecret feature gate. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    nodePublishSecretRef: SecretReference = Field(default=None, description=r""" nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    nodeStageSecretRef: SecretReference = Field(default=None, description=r""" nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    readOnly: bool = Field(default=None, description=r""" readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). """)
    volumeAttributes: dict = Field(default=None, description=r""" volumeAttributes of the volume to publish. """)
    volumeHandle: str = Field(default=None, description=r""" volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. """)
