from pydantic import BaseModel, Field


class ResourceMetricSource(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)
