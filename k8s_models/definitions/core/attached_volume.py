from pydantic import BaseModel, Field


class AttachedVolume(BaseModel):
    devicePath: str = Field(default=None, description=r""" DevicePath represents the device path where the volume should be available """)
    name: str = Field(default=None, description=r""" Name of the attached volume """)
