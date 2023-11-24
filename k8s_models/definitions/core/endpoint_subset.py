from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.endpoint_address import EndpointAddress
from k8s_models.definitions.core.endpoint_port import EndpointPort


class EndpointSubset(BaseModel):
    addresses: List[EndpointAddress] = Field(default=None, description=r""" IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize. """)
    notReadyAddresses: List[EndpointAddress] = Field(default=None, description=r""" IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check. """)
    ports: List[EndpointPort] = Field(default=None, description=r""" Port numbers available on the related IP addresses. """)
