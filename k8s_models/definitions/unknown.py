from pydantic import BaseModel


class RollingUpdateDaemonSet(BaseModel):
    pass


class ScaleSpec(BaseModel):
    pass


class ScaleStatus(BaseModel):
    pass

class DaemonSetStatus(BaseModel):
    pass

class DeploymentStatus(BaseModel):
    pass

class DeploymentStrategy(BaseModel):
    pass

class ReplicaSetStatus(BaseModel):
    pass

class StatefulSetStatus(BaseModel):
    pass

class PodStatus(BaseModel):
    pass

class ReplicationControllerStatus(BaseModel):
    pass

class CronJobStatus(BaseModel):
    pass

class JobStatus(BaseModel):
    pass
