from pydantic import BaseModel, Field


class DownwardAPIVolumeFile(BaseModel):
    fieldRef: ObjectFieldSelector = Field(default=None, description=r""" Required: Selects a field of the pod: only annotations, labels, name and namespace are supported. """)
    mode: int = Field(default=None, description=r""" Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
    path: str = Field(default=None, description=r""" Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' """)
    resourceFieldRef: ResourceFieldSelector = Field(default=None, description=r""" Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. """)
