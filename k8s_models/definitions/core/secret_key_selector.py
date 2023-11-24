from pydantic import BaseModel, Field


class SecretKeySelector(BaseModel):
    key: str = Field(default=None, description=r""" The key of the secret to select from.  Must be a valid secret key. """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" Specify whether the Secret or its key must be defined """)
