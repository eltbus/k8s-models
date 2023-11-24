from pydantic import BaseModel, Field


class EndpointHints(BaseModel):
    forZones: List[ForZone] = Field(default=None, description=r""" forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing. """)
