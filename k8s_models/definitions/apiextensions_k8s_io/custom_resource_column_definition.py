from pydantic import BaseModel, Field


class CustomResourceColumnDefinition(BaseModel):
    description: str = Field(default=None, description=r""" description is a human readable description of this column. """)
    format: str = Field(default=None, description=r""" format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. """)
    jsonPath: str = Field(default=None, description=r""" jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column. """)
    name: str = Field(default=None, description=r""" name is a human readable name for the column. """)
    priority: int = Field(default=None, description=r""" priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0. """)
    type: str = Field(default=None, description=r""" type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. """)
