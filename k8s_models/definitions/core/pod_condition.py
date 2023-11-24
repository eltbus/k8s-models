from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time


class PodCondition(BaseModel):
    lastProbeTime: Time = Field(default=None, description=r""" Last time we probed the condition. """)
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" Human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" Unique, one-word, CamelCase reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """)
    type: str = Field(default=None, description=r""" Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """)
