from pydantic import BaseModel, Field


class HTTPHeader(BaseModel):
    name: str = Field(default=None, description=r""" The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. """)
    value: str = Field(default=None, description=r""" The header field value """)
