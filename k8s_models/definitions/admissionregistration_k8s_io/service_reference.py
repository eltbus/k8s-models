from pydantic import BaseModel, Field


class ServiceReference(BaseModel):
    name: str = Field(default=None, description=r""" `name` is the name of the service. Required """)
    namespace: str = Field(default=None, description=r""" `namespace` is the namespace of the service. Required """)
    path: str = Field(default=None, description=r""" `path` is an optional URL path which will be sent in any request to this service. """)
    port: int = Field(default=None, description=r""" If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive). """)
