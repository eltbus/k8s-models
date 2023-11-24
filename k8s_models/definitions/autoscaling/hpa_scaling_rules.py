from pydantic import BaseModel, Field


class HPAScalingRules(BaseModel):
    policies: List[HPAScalingPolicy] = Field(default=None, description=r""" policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid """)
    selectPolicy: str = Field(default=None, description=r""" selectPolicy is used to specify which policy should be used. If not set, the default value Max is used. """)
    stabilizationWindowSeconds: int = Field(default=None, description=r""" stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). """)
