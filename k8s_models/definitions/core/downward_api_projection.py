from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.downward_api_volume_file import DownwardAPIVolumeFile


class DownwardAPIProjection(BaseModel):
    items: List[DownwardAPIVolumeFile] = Field(default=None, description=r""" Items is a list of DownwardAPIVolume file """)
