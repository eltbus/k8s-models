from pydantic import BaseModel, Field


class DaemonEndpoint(BaseModel):
    Port: int = Field(default=None, description=r""" Port number of the given endpoint. """)
