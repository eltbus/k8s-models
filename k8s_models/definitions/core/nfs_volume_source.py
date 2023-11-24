from pydantic import BaseModel, Field


class NFSVolumeSource(BaseModel):
    path: str = Field(default=None, description=r""" path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
    server: str = Field(default=None, description=r""" server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
