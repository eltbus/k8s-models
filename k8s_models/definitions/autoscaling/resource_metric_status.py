from pydantic import BaseModel, Field

from k8s_models.definitions.autoscaling.metric_value_status import MetricValueStatus


class ResourceMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
