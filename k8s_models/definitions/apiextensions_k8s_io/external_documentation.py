from pydantic import BaseModel, Field


class ExternalDocumentation(BaseModel):
    description: str = Field(default=None)
    url: str = Field(default=None)
