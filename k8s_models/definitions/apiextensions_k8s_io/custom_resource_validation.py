from pydantic import BaseModel, Field

from k8s_models.definitions.apiextensions_k8s_io.json_schema_props import JSONSchemaProps


class CustomResourceValidation(BaseModel):
    openAPIV3Schema: JSONSchemaProps = Field(default=None, description=r""" openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning. """)
