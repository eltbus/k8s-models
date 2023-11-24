from pydantic import BaseModel, Field

from k8s_models.definitions.core.secret_reference import SecretReference


class FlexPersistentVolumeSource(BaseModel):
    driver: str = Field(default=None, description=r""" driver is the name of the driver to use for this volume. """)
    fsType: str = Field(default=None, description=r""" fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. """)
    options: dict = Field(default=None, description=r""" options is Optional: this field holds extra command options if any. """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef is Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. """)
