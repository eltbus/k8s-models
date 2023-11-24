from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.port_status import PortStatus


class LoadBalancerIngress(BaseModel):
    hostname: str = Field(default=None, description=r""" Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers) """)
    ip: str = Field(default=None, description=r""" IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers) """)
    ports: List[PortStatus] = Field(default=None, description=r""" Ports is a list of records of service ports If used, every port defined in the service should have an entry in it """)
