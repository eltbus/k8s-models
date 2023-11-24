from pydantic import BaseModel, Field

from k8s_models.definitions.core.object_reference import ObjectReference


class EndpointAddress(BaseModel):
    hostname: str = Field(default=None, description=r""" The Hostname of this endpoint """)
    ip: str = Field(default=None, description=r""" The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16). """)
    nodeName: str = Field(default=None, description=r""" Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. """)
    targetRef: ObjectReference = Field(default=None, description=r""" Reference to object providing the endpoint. """)
