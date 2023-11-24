from pydantic import BaseModel, Field

from k8s_models.definitions.autoscaling.metric_identifier import MetricIdentifier
from k8s_models.definitions.autoscaling.metric_target import MetricTarget


class ExternalMetricSource(BaseModel):
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)
