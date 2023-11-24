from pydantic import BaseModel, Field


class ServiceBackendPort(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the port on the Service. This is a mutually exclusive setting with "Number". """)
    number: int = Field(default=None, description=r""" number is the numerical port number (e.g. 80) on the Service. This is a mutually exclusive setting with "Name". """)
