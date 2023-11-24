from pydantic import BaseModel, Field


class IngressLoadBalancerStatus(BaseModel):
    ingress: List[IngressLoadBalancerIngress] = Field(default=None, description=r""" ingress is a list containing ingress points for the load-balancer. """)
