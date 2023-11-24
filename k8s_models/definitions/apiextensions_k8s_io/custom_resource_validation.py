from pydantic import BaseModel, Field


class CustomResourceValidation(BaseModel):
    openAPIV3Schema: JSONSchemaProps = Field(default=None, description=r""" openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning. """)
