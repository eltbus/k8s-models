from pydantic import Field

from k8s_models.models import KubeModel


class ObjectMetricSource(KubeModel):
    describedObject: CrossVersionObjectReference = Field(default=None, description=r""" describedObject specifies the descriptions of a object,such as kind,name apiVersion """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)
