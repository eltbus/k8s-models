from pydantic import BaseModel, Field


class HorizontalPodAutoscalerStatus(BaseModel):
    conditions: List[HorizontalPodAutoscalerCondition] = Field(default=None, description=r""" conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met. """)
    currentMetrics: List[MetricStatus] = Field(default=None, description=r""" currentMetrics is the last read state of the metrics used by this autoscaler. """)
    currentReplicas: int = Field(default=None, description=r""" currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler. """)
    desiredReplicas: int = Field(default=None, description=r""" desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler. """)
    lastScaleTime: Time = Field(default=None, description=r""" lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed. """)
    observedGeneration: int = Field(default=None, description=r""" observedGeneration is the most recent generation observed by this autoscaler. """)
