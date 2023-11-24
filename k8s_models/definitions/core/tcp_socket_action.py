from pydantic import BaseModel, Field


class TCPSocketAction(BaseModel):
    host: str = Field(default=None, description=r""" Optional: Host name to connect to, defaults to the pod IP. """)
    port: Any = Field(default=None, description=r""" Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. """)
