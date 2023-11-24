from pydantic import BaseModel, Field


class PodFailurePolicyOnPodConditionsPattern(BaseModel):
    status: str = Field(default=None, description=r""" Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True. """)
    type: str = Field(default=None, description=r""" Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type. """)
