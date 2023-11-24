from pydantic import BaseModel, Field


class AzureFileVolumeSource(BaseModel):
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretName: str = Field(default=None, description=r""" secretName is the  name of secret that contains Azure Storage Account Name and Key """)
    shareName: str = Field(default=None, description=r""" shareName is the azure share Name """)
