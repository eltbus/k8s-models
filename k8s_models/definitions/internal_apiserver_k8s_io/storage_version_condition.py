from pydantic import BaseModel, Field


class StorageVersionCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
    observedGeneration: int = Field(default=None, description=r""" If set, this represents the .metadata.generation that the condition was set based upon. """)
    reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of the condition. """)
