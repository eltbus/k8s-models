from pydantic import BaseModel, Field


class LoadBalancerStatus(BaseModel):
    ingress: List[LoadBalancerIngress] = Field(default=None, description=r""" Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. """)
