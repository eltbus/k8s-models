from pydantic import BaseModel, Field

from k8s_models.definitions.autoscaling.metric_value_status import MetricValueStatus
from k8s_models.definitions.autoscaling.metric_identifier import MetricIdentifier


class PodsMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
