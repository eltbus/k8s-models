from pydantic import BaseModel, Field


class HPAScalingPolicy(BaseModel):
    periodSeconds: int = Field(default=None, description=r""" periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). """)
    type: str = Field(default=None, description=r""" type is used to specify the scaling policy. """)
    value: int = Field(default=None, description=r""" value contains the amount of change which is permitted by the policy. It must be greater than zero """)
