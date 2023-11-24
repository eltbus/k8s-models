from pydantic import BaseModel, Field


class EnvFromSource(BaseModel):
    configMapRef: ConfigMapEnvSource = Field(default=None, description=r""" The ConfigMap to select from """)
    prefix: str = Field(default=None, description=r""" An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER. """)
    secretRef: SecretEnvSource = Field(default=None, description=r""" The Secret to select from """)
