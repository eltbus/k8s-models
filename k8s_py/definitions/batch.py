from pydantic import BaseModel

class JobCondition(BaseModel):
    pass

class JobTemplateSpec(BaseModel):
    pass

class PodFailurePolicy(BaseModel):
    pass

class PodFailurePolicyOnExitCodesRequirement(BaseModel):
    pass

class PodFailurePolicyOnPodConditionsPattern(BaseModel):
    pass

class PodFailurePolicyRule(BaseModel):
    pass

class UncountedTerminatedPods(BaseModel):
    pass
