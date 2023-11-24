from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.discovery_k8s_io.for_zone import ForZone


class EndpointHints(BaseModel):
    forZones: List[ForZone] = Field(default=None, description=r""" forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing. """)
