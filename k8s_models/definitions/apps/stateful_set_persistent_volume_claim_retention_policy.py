from pydantic import BaseModel, Field


class StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    whenDeleted: str = Field(default=None, description=r""" WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted. """)
    whenScaled: str = Field(default=None, description=r""" WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted. """)