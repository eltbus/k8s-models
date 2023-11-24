from pydantic import BaseModel, Field

from k8s_models.definitions.autoscaling.metric_target import MetricTarget


class ContainerResourceMetricSource(BaseModel):
    container: str = Field(default=None, description=r""" container is the name of the container in the pods of the scaling target """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)
