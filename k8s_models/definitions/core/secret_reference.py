from pydantic import BaseModel, Field


class SecretReference(BaseModel):
    name: str = Field(default=None, description=r""" name is unique within a namespace to reference a secret resource. """)
    namespace: str = Field(default=None, description=r""" namespace defines the space within which the secret name must be unique. """)
