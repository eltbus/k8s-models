from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time


class FlowSchemaCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" `lastTransitionTime` is the last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" `message` is a human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" `reason` is a unique, one-word, CamelCase reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" `status` is the status of the condition. Can be True, False, Unknown. Required. """)
    type: str = Field(default=None, description=r""" `type` is the type of the condition. Required. """)
