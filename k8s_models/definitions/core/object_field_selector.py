from pydantic import BaseModel, Field


class ObjectFieldSelector(BaseModel):
    apiVersion: str = Field(default="v1", description=r""" Version of the schema the FieldPath is written in terms of, defaults to "v1". """)
    fieldPath: str = Field(default=None, description=r""" Path of the field to select in the specified API version. """)
