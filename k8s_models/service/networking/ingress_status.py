from pydantic import BaseModel, Field


class IngressStatus(BaseModel):
    loadBalancer: IngressLoadBalancerStatus = Field(default=None, description=r""" loadBalancer contains the current status of the load-balancer. """)
