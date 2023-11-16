from pydantic import BaseModel

class EnvVar(BaseModel):
    pass

class EnvFromSource(BaseModel):
    pass

class Lifecycle(BaseModel):
    pass

class Probe(BaseModel):
    pass

class ContainerPort(BaseModel):
    pass

class ResourceRequirements(BaseModel):
    pass

class SecurityContext(BaseModel):
    pass

class VolumeDevice(BaseModel):
    pass

class VolumeMount(BaseModel):
    pass

class DaemonSetSpec(BaseModel):
    pass

class DaemonSetStatus(BaseModel):
    pass

class JobTemplateSpec(BaseModel):
    pass

class ObjectMeta(BaseModel):
    pass

class DeploymentSpec(BaseModel):
    pass

class DeploymentStatus(BaseModel):
    pass

class JobSpec(BaseModel):
    pass

class JobStatus(BaseModel):
    pass

class PodSpec(BaseModel):
    pass

class PodStatus(BaseModel):
    pass

class ReplicaSetSpec(BaseModel):
    pass

class ReplicaSetStatus(BaseModel):
    pass

class ReplicationControllerSpec(BaseModel):
    pass

class ReplicationControllerStatus(BaseModel):
    pass
