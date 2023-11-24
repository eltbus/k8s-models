from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.networking_k8s_io.ingress_load_balancer_ingress import IngressLoadBalancerIngress


class IngressLoadBalancerStatus(BaseModel):
    ingress: List[IngressLoadBalancerIngress] = Field(default=None, description=r""" ingress is a list containing ingress points for the load-balancer. """)
