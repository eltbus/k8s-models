from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time


class ReplicaSetCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" The last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
    reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of replica set condition. """)
