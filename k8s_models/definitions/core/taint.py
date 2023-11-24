from pydantic import BaseModel, Field


class Taint(BaseModel):
    effect: str = Field(default=None, description=r""" Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. """)
    key: str = Field(default=None, description=r""" Required. The taint key to be applied to a node. """)
    timeAdded: Time = Field(default=None, description=r""" TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. """)
    value: str = Field(default=None, description=r""" The taint value corresponding to the taint key. """)
