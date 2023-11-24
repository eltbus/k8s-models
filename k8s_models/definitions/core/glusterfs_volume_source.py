from pydantic import BaseModel, Field


class GlusterfsVolumeSource(BaseModel):
    endpoints: str = Field(default=None, description=r""" endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
    path: str = Field(default=None, description=r""" path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
