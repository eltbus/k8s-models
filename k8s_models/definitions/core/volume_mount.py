from pydantic import BaseModel, Field


class VolumeMount(BaseModel):
    mountPath: str = Field(default=None, description=r""" Path within the container at which the volume should be mounted.  Must not contain ':'. """)
    mountPropagation: str = Field(default=None, description=r""" mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. """)
    name: str = Field(default=None, description=r""" This must match the Name of a Volume. """)
    readOnly: bool = Field(default=None, description=r""" Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. """)
    subPath: str = Field(default=None, description=r""" Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root). """)
    subPathExpr: str = Field(default=None, description=r""" Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive. """)
