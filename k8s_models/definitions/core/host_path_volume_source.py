from pydantic import BaseModel, Field


class HostPathVolumeSource(BaseModel):
    path: str = Field(default=None, description=r""" path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)
    type: str = Field(default=None, description=r""" type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)
