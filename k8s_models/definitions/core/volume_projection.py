from pydantic import BaseModel, Field


class VolumeProjection(BaseModel):
    configMap: ConfigMapProjection = Field(default=None, description=r""" configMap information about the configMap data to project """)
    downwardAPI: DownwardAPIProjection = Field(default=None, description=r""" downwardAPI information about the downwardAPI data to project """)
    secret: SecretProjection = Field(default=None, description=r""" secret information about the secret data to project """)
    serviceAccountToken: ServiceAccountTokenProjection = Field(default=None, description=r""" serviceAccountToken is information about the serviceAccountToken data to project """)
