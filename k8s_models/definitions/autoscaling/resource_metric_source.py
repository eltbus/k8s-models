from pydantic import BaseModel, Field

from k8s_models.definitions.autoscaling.metric_target import MetricTarget


class ResourceMetricSource(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)
