from pydantic import BaseModel, Field


class VolumeAttachmentSpec(BaseModel):
    attacher: str = Field(default=None, description=r""" attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName(). """)
    nodeName: str = Field(default=None, description=r""" nodeName represents the node that the volume should be attached to. """)
    source: VolumeAttachmentSource = Field(default=None, description=r""" source represents the volume that should be attached. """)
