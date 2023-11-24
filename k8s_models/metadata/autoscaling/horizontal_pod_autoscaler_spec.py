from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.autoscaling.horizontal_pod_autoscaler_behavior import HorizontalPodAutoscalerBehavior
from k8s_models.definitions.autoscaling.metric_spec import MetricSpec
from k8s_models.definitions.autoscaling.cross_version_object_reference import CrossVersionObjectReference


class HorizontalPodAutoscalerSpec(BaseModel):
    behavior: HorizontalPodAutoscalerBehavior = Field(default=None, description=r""" behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default HPAScalingRules for scale up and scale down are used. """)
    maxReplicas: int = Field(default=None, description=r""" maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas. """)
    metrics: List[MetricSpec] = Field(default=None, description=r""" metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization. """)
    minReplicas: int = Field(default=None, description=r""" minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available. """)
    scaleTargetRef: CrossVersionObjectReference = Field(default=None, description=r""" scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count. """)
