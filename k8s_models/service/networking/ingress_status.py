from pydantic import BaseModel, Field

from k8s_models.definitions.networking_k8s_io.ingress_load_balancer_status import IngressLoadBalancerStatus


class IngressStatus(BaseModel):
    loadBalancer: IngressLoadBalancerStatus = Field(default=None, description=r""" loadBalancer contains the current status of the load-balancer. """)
