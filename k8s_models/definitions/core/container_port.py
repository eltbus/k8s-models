from pydantic import BaseModel, Field


class ContainerPort(BaseModel):
    containerPort: int = Field(default=None, description=r""" Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. """)
    hostIP: str = Field(default=None, description=r""" What host IP to bind the external port to. """)
    hostPort: int = Field(default=None, description=r""" Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. """)
    name: str = Field(default=None, description=r""" If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. """)
    protocol: str = Field(default=None, description=r""" Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". """)
