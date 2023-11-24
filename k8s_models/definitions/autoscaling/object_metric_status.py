from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.autoscaling.metric_value_status import MetricValueStatus
from k8s_models.definitions.autoscaling.cross_version_object_reference import CrossVersionObjectReference
from k8s_models.definitions.autoscaling.metric_identifier import MetricIdentifier


class ObjectMetricStatus(KubeModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    describedObject: CrossVersionObjectReference = Field(default=None, description=r""" DescribedObject specifies the descriptions of a object,such as kind,name apiVersion """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
