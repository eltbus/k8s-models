from pydantic import BaseModel, Field


class AzureFilePersistentVolumeSource(BaseModel):
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretName: str = Field(default=None, description=r""" secretName is the name of secret that contains Azure Storage Account Name and Key """)
    secretNamespace: str = Field(default=None, description=r""" secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod """)
    shareName: str = Field(default=None, description=r""" shareName is the azure Share Name """)
