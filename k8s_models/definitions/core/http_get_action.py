from pydantic import BaseModel, Field


class HTTPGetAction(BaseModel):
    host: str = Field(default=None, description=r""" Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. """)
    httpHeaders: List[HTTPHeader] = Field(default=None, description=r""" Custom headers to set in the request. HTTP allows repeated headers. """)
    path: str = Field(default=None, description=r""" Path to access on the HTTP server. """)
    port: Any = Field(default=None, description=r""" Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. """)
    scheme: str = Field(default=None, description=r""" Scheme to use for connecting to the host. Defaults to HTTP. """)
