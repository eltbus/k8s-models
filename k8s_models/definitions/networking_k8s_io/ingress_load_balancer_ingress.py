from pydantic import BaseModel, Field


class IngressLoadBalancerIngress(BaseModel):
    hostname: str = Field(default=None, description=r""" hostname is set for load-balancer ingress points that are DNS based. """)
    ip: str = Field(default=None, description=r""" ip is set for load-balancer ingress points that are IP based. """)
    ports: List[IngressPortStatus] = Field(default=None, description=r""" ports provides information about the ports exposed by this LoadBalancer. """)
