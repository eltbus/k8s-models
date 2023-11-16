from pydantic import BaseModel

class DaemonSetCondition(BaseModel):
    pass

class DaemonSetUpdateStrategy(BaseModel):
    pass

class DeploymentCondition(BaseModel):
    pass

class ReplicaSetCondition(BaseModel):
    pass

class RollingUpdateStatefulSetStrategy(BaseModel):
    pass

class StatefulSetCondition(BaseModel):
    pass

class StatefulSetOrdinals(BaseModel):
    pass

class StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    pass

class StatefulSetUpdateStrategy(BaseModel):
    pass
