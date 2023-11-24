from pydantic import BaseModel, Field


class PersistentVolumeClaimCondition(BaseModel):
    lastProbeTime: Time = Field(default=None, description=r""" lastProbeTime is the time we probed the condition. """)
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" message is the human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized. """)
    status: str = Field(default=None)
    type: str = Field(default=None)
