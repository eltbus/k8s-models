from pydantic import BaseModel, Field


class VolumeAttachmentSource(BaseModel):
    inlineVolumeSpec: PersistentVolumeSpec = Field(default=None, description=r""" inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature. """)
    persistentVolumeName: str = Field(default=None, description=r""" persistentVolumeName represents the name of the persistent volume to attach. """)
