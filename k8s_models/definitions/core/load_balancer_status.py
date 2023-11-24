from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.load_balancer_ingress import LoadBalancerIngress


class LoadBalancerStatus(BaseModel):
    ingress: List[LoadBalancerIngress] = Field(default=None, description=r""" Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. """)
