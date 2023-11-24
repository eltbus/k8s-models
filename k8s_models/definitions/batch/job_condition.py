from pydantic import BaseModel, Field


class JobCondition(BaseModel):
    lastProbeTime: Time = Field(default=None, description=r""" Last time the condition was checked. """)
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transit from one status to another. """)
    message: str = Field(default=None, description=r""" Human readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" (brief) reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of job condition, Complete or Failed. """)