from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.definitions.autoscaling import HorizontalPodAutoscalerBehavior, MetricSpec, CrossVersionObjectReference
from k8s_models.definitions.unknown import HorizontalPodAutoscalerStatus

class HorizontalPodAutoscaler(BaseModel):
	apiVersion: str = Field(default="v2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="HorizontalPodAutoscaler", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: HorizontalPodAutoscalerSpec = Field(default=None, description=r""" spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. """)
	status: HorizontalPodAutoscalerStatus = Field(default=None, description=r""" status is the current information about the autoscaler. """)

class HorizontalPodAutoscalerSpec(BaseModel):
	behavior: HorizontalPodAutoscalerBehavior = Field(default=None, description=r""" behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default HPAScalingRules for scale up and scale down are used. """)
	maxReplicas: int = Field(default=None, description=r""" maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas. """)
	metrics: List[MetricSpec] = Field(default=None, description=r""" metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization. """)
	minReplicas: int = Field(default=None, description=r""" minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available. """)
	scaleTargetRef: CrossVersionObjectReference = Field(default=None, description=r""" scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count. """)
