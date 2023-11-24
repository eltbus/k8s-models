from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.networking_k8s_io.ingress_port_status import IngressPortStatus


class IngressLoadBalancerIngress(BaseModel):
    hostname: str = Field(default=None, description=r""" hostname is set for load-balancer ingress points that are DNS based. """)
    ip: str = Field(default=None, description=r""" ip is set for load-balancer ingress points that are IP based. """)
    ports: List[IngressPortStatus] = Field(default=None, description=r""" ports provides information about the ports exposed by this LoadBalancer. """)
