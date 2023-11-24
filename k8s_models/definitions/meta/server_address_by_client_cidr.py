from pydantic import BaseModel, Field


class ServerAddressByClientCIDR(BaseModel):
    clientCIDR: str = Field(default=None, description=r""" The CIDR with which clients can match their IP to figure out the server address that they should use. """)
    serverAddress: str = Field(default=None, description=r""" Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port. """)
