from pydantic import BaseModel, Field


class NamespaceCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None)
    message: str = Field(default=None)
    reason: str = Field(default=None)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of namespace controller condition. """)
