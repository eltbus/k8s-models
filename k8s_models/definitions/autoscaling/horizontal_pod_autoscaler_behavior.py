from pydantic import BaseModel, Field


class HorizontalPodAutoscalerBehavior(BaseModel):
    scaleDown: HPAScalingRules = Field(default=None, description=r""" scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used). """)
    scaleUp: HPAScalingRules = Field(default=None, description=r""" scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:   * increase no more than 4 pods per 60 seconds   * double the number of pods per 60 seconds No stabilization is used. """)
