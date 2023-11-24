from pydantic import BaseModel, Field


class ConfigMapKeySelector(BaseModel):
    key: str = Field(default=None, description=r""" The key to select. """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" Specify whether the ConfigMap or its key must be defined """)
