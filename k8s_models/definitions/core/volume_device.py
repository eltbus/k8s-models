from pydantic import BaseModel, Field


class VolumeDevice(BaseModel):
    devicePath: str = Field(default=None, description=r""" devicePath is the path inside of the container that the device will be mapped to. """)
    name: str = Field(default=None, description=r""" name must match the name of a persistentVolumeClaim in the pod """)
