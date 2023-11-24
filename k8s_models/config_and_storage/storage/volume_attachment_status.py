from pydantic import BaseModel, Field

from k8s_models.definitions.storage_k8s_io.volume_error import VolumeError


class VolumeAttachmentStatus(BaseModel):
    attachError: VolumeError = Field(default=None, description=r""" attachError represents the last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. """)
    attached: bool = Field(default=None, description=r""" attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. """)
    attachmentMetadata: dict = Field(default=None, description=r""" attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. """)
    detachError: VolumeError = Field(default=None, description=r""" detachError represents the last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher. """)
