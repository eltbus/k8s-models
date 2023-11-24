from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time


class HorizontalPodAutoscalerCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the last time the condition transitioned from one status to another """)
    message: str = Field(default=None, description=r""" message is a human-readable explanation containing details about the transition """)
    reason: str = Field(default=None, description=r""" reason is the reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" status is the status of the condition (True, False, Unknown) """)
    type: str = Field(default=None, description=r""" type describes the current condition """)
