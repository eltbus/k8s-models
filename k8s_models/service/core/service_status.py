from pydantic import BaseModel, Field


class ServiceStatus(BaseModel):
    conditions: List[Condition] = Field(default=None, description=r""" Current service state """)
    loadBalancer: LoadBalancerStatus = Field(default=None, description=r""" LoadBalancer contains the current status of the load-balancer, if one is present. """)
