from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.meta.condition import Condition
from k8s_models.definitions.core.load_balancer_status import LoadBalancerStatus


class ServiceStatus(BaseModel):
    conditions: List[Condition] = Field(default=None, description=r""" Current service state """)
    loadBalancer: LoadBalancerStatus = Field(default=None, description=r""" LoadBalancer contains the current status of the load-balancer, if one is present. """)
