from pydantic import BaseModel, Field


class LocalObjectReference(BaseModel):
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
