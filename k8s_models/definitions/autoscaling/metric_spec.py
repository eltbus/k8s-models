from pydantic import BaseModel, Field

from k8s_models.definitions.autoscaling.container_resource_metric_source import ContainerResourceMetricSource
from k8s_models.definitions.autoscaling.external_metric_source import ExternalMetricSource
from k8s_models.definitions.autoscaling.object_metric_source import ObjectMetricSource
from k8s_models.definitions.autoscaling.pods_metric_source import PodsMetricSource
from k8s_models.definitions.autoscaling.resource_metric_source import ResourceMetricSource


class MetricSpec(BaseModel):
    containerResource: ContainerResourceMetricSource = Field(default=None, description=r""" containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag. """)
    external: ExternalMetricSource = Field(default=None, description=r""" external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). """)
    object: ObjectMetricSource = Field(default=None, description=r""" object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). """)
    pods: PodsMetricSource = Field(default=None, description=r""" pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. """)
    resource: ResourceMetricSource = Field(default=None, description=r""" resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    type: str = Field(default=None, description=r""" type is the type of metric source.  It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled """)
