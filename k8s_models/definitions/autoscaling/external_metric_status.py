from pydantic import BaseModel, Field


class ExternalMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
