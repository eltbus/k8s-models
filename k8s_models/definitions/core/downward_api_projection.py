from pydantic import BaseModel, Field


class DownwardAPIProjection(BaseModel):
    items: List[DownwardAPIVolumeFile] = Field(default=None, description=r""" Items is a list of DownwardAPIVolume file """)
