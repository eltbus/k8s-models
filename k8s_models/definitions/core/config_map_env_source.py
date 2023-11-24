from pydantic import BaseModel, Field


class ConfigMapEnvSource(BaseModel):
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" Specify whether the ConfigMap must be defined """)