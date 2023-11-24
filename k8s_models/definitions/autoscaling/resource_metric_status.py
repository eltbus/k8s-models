from pydantic import BaseModel, Field


class ResourceMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
