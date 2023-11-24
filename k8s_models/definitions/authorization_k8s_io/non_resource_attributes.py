from pydantic import BaseModel, Field


class NonResourceAttributes(BaseModel):
    path: str = Field(default=None, description=r""" Path is the URL path of the request """)
    verb: str = Field(default=None, description=r""" Verb is the standard HTTP verb """)
