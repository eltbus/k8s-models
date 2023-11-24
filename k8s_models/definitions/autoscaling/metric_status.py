from pydantic import BaseModel, Field

from k8s_models.definitions.autoscaling.container_resource_metric_status import ContainerResourceMetricStatus
from k8s_models.definitions.autoscaling.external_metric_status import ExternalMetricStatus
from k8s_models.definitions.autoscaling.object_metric_status import ObjectMetricStatus
from k8s_models.definitions.autoscaling.pods_metric_status import PodsMetricStatus
from k8s_models.definitions.autoscaling.resource_metric_status import ResourceMetricStatus


class MetricStatus(BaseModel):
    containerResource: ContainerResourceMetricStatus = Field(default=None, description=r""" container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    external: ExternalMetricStatus = Field(default=None, description=r""" external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). """)
    object: ObjectMetricStatus = Field(default=None, description=r""" object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). """)
    pods: PodsMetricStatus = Field(default=None, description=r""" pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. """)
    resource: ResourceMetricStatus = Field(default=None, description=r""" resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    type: str = Field(default=None, description=r""" type is the type of metric source.  It will be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each corresponds to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled """)
