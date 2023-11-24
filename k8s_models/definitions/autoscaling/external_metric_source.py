from pydantic import BaseModel, Field


class ExternalMetricSource(BaseModel):
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)
