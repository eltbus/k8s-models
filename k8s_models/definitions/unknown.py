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

class APIServiceStatus(BaseModel):
    pass

class TokenRequestStatus(BaseModel):
    pass

class TokenReviewStatus(BaseModel):
    pass

class SubjectAccessReviewStatus(BaseModel):
    pass

class CertificateSigningRequestStatus(BaseModel):
    pass

class NamespaceStatus(BaseModel):
    pass

class NodeStatus(BaseModel):
    pass

class PersistentVolumeStatus(BaseModel):
    pass

class PersistentVolumeClaimStatus(BaseModel):
    pass

class ResourceQuotaStatus(BaseModel):
    pass

class FlowSchemaStatus(BaseModel):
    pass

class PriorityLevelConfigurationStatus(BaseModel):
    pass

class StorageVersionStatus(BaseModel):
    pass

class VolumeAttachmentStatus(BaseModel):
    pass

class ValidatingAdmissionPolicyStatus(BaseModel):
    pass

class CustomResourceDefinitionStatus(BaseModel):
    pass

class HorizontalPodAutoscalerStatus(BaseModel):
    pass

class PodDisruptionBudgetStatus(BaseModel):
    pass

class PodSchedulingContextStatus(BaseModel):
    pass

class ResourceClaimStatus(BaseModel):
    pass
