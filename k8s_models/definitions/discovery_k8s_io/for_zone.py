from pydantic import BaseModel, Field


class ForZone(BaseModel):
    name: str = Field(default=None, description=r""" name represents the name of the zone. """)
