from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time

class NamespaceCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None)
    message: str = Field(default=None)
    reason: str = Field(default=None)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of namespace controller condition. """)
