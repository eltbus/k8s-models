from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.models import KubeModel
from k8s_models.definitions.core import Quantity
from k8s_models.definitions.meta import Time, LabelSelector, ObjectMeta
from k8s_models.definitions.unknown import ScaleSpec, ScaleStatus

class ContainerResourceMetricSource(BaseModel):
    container: str = Field(default=None, description=r""" container is the name of the container in the pods of the scaling target """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)

class ContainerResourceMetricStatus(BaseModel):
    container: str = Field(default=None, description=r""" container is the name of the container in the pods of the scaling target """)
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)

class CrossVersionObjectReference(KubeModel):
    apiVersion: str = Field(default="v2", description=r""" apiVersion is the API version of the referent """)
    kind: str = Field(default="CrossVersionObjectReference", description=r""" kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)

class ExternalMetricSource(BaseModel):
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)

class ExternalMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)

class HPAScalingPolicy(BaseModel):
    periodSeconds: int = Field(default=None, description=r""" periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). """)
    type: str = Field(default=None, description=r""" type is used to specify the scaling policy. """)
    value: int = Field(default=None, description=r""" value contains the amount of change which is permitted by the policy. It must be greater than zero """)

class HPAScalingRules(BaseModel):
    policies: List[HPAScalingPolicy] = Field(default=None, description=r""" policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid """)
    selectPolicy: str = Field(default=None, description=r""" selectPolicy is used to specify which policy should be used. If not set, the default value Max is used. """)
    stabilizationWindowSeconds: int = Field(default=None, description=r""" stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). """)

class HorizontalPodAutoscalerBehavior(BaseModel):
    scaleDown: HPAScalingRules = Field(default=None, description=r""" scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used). """)
    scaleUp: HPAScalingRules = Field(default=None, description=r""" scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:   * increase no more than 4 pods per 60 seconds   * double the number of pods per 60 seconds No stabilization is used. """)

class HorizontalPodAutoscalerCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the last time the condition transitioned from one status to another """)
    message: str = Field(default=None, description=r""" message is a human-readable explanation containing details about the transition """)
    reason: str = Field(default=None, description=r""" reason is the reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" status is the status of the condition (True, False, Unknown) """)
    type: str = Field(default=None, description=r""" type describes the current condition """)

class MetricIdentifier(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the given metric """)
    selector: LabelSelector = Field(default=None, description=r""" selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics. """)

class MetricSpec(BaseModel):
    containerResource: ContainerResourceMetricSource = Field(default=None, description=r""" containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag. """)
    external: ExternalMetricSource = Field(default=None, description=r""" external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). """)
    object: ObjectMetricSource = Field(default=None, description=r""" object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). """)
    pods: PodsMetricSource = Field(default=None, description=r""" pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. """)
    resource: ResourceMetricSource = Field(default=None, description=r""" resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    type: str = Field(default=None, description=r""" type is the type of metric source.  It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled """)

class MetricStatus(BaseModel):
    containerResource: ContainerResourceMetricStatus = Field(default=None, description=r""" container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    external: ExternalMetricStatus = Field(default=None, description=r""" external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). """)
    object: ObjectMetricStatus = Field(default=None, description=r""" object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). """)
    pods: PodsMetricStatus = Field(default=None, description=r""" pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. """)
    resource: ResourceMetricStatus = Field(default=None, description=r""" resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    type: str = Field(default=None, description=r""" type is the type of metric source.  It will be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each corresponds to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled """)

class MetricTarget(BaseModel):
    averageUtilization: int = Field(default=None, description=r""" averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type """)
    averageValue: Quantity = Field(default=None, description=r""" averageValue is the target value of the average of the metric across all relevant pods (as a quantity) """)
    type: str = Field(default=None, description=r""" type represents whether the metric type is Utilization, Value, or AverageValue """)
    value: Quantity = Field(default=None, description=r""" value is the target value of the metric (as a quantity). """)

class MetricValueStatus(BaseModel):
    averageUtilization: int = Field(default=None, description=r""" currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. """)
    averageValue: Quantity = Field(default=None, description=r""" averageValue is the current value of the average of the metric across all relevant pods (as a quantity) """)
    value: Quantity = Field(default=None, description=r""" value is the current value of the metric (as a quantity). """)

class ObjectMetricSource(BaseModel):
    describedObject: CrossVersionObjectReference = Field(default=None, description=r""" describedObject specifies the descriptions of a object,such as kind,name apiVersion """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)

class ObjectMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    describedObject: CrossVersionObjectReference = Field(default=None, description=r""" DescribedObject specifies the descriptions of a object,such as kind,name apiVersion """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)

class PodsMetricSource(BaseModel):
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)

class PodsMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)

class ResourceMetricSource(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)

class ResourceMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)

class Scale(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Scale", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """)
    spec: ScaleSpec = Field(default=None, description=r""" spec defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. """)
    status: ScaleStatus = Field(default=None, description=r""" status is the current status of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. Read-only. """)
