from pydantic import BaseModel, Field


class ComponentCondition(BaseModel):
    error: str = Field(default=None, description=r""" Condition error code for a component. For example, a health check error code. """)
    message: str = Field(default=None, description=r""" Message about the condition for a component. For example, information about a health check. """)
    status: str = Field(default=None, description=r""" Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown". """)
    type: str = Field(default=None, description=r""" Type of condition for a component. Valid value: "Healthy" """)
