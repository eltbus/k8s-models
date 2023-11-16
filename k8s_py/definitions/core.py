from pydantic import BaseModel

class AWSElasticBlockStoreVolumeSource(BaseModel):
    pass

class Affinity(BaseModel):
    pass

class AttachedVolume(BaseModel):
    pass

class AzureDiskVolumeSource(BaseModel):
    pass

class AzureFilePersistentVolumeSource(BaseModel):
    pass

class AzureFileVolumeSource(BaseModel):
    pass

class CSIPersistentVolumeSource(BaseModel):
    pass

class CSIVolumeSource(BaseModel):
    pass

class Capabilities(BaseModel):
    pass

class CephFSPersistentVolumeSource(BaseModel):
    pass

class CephFSVolumeSource(BaseModel):
    pass

class CinderPersistentVolumeSource(BaseModel):
    pass

class CinderVolumeSource(BaseModel):
    pass

class ClaimSource(BaseModel):
    pass

class ClientIPConfig(BaseModel):
    pass

class ComponentCondition(BaseModel):
    pass

class ConfigMapEnvSource(BaseModel):
    pass

class ConfigMapKeySelector(BaseModel):
    pass

class ConfigMapNodeConfigSource(BaseModel):
    pass

class ConfigMapProjection(BaseModel):
    pass

class ConfigMapVolumeSource(BaseModel):
    pass

class ContainerImage(BaseModel):
    pass

class ContainerPort(BaseModel):
    pass

class ContainerResizePolicy(BaseModel):
    pass

class ContainerState(BaseModel):
    pass

class ContainerStateRunning(BaseModel):
    pass

class ContainerStateTerminated(BaseModel):
    pass

class ContainerStateWaiting(BaseModel):
    pass

class DaemonEndpoint(BaseModel):
    pass

class DownwardAPIProjection(BaseModel):
    pass

class DownwardAPIVolumeFile(BaseModel):
    pass

class DownwardAPIVolumeSource(BaseModel):
    pass

class EmptyDirVolumeSource(BaseModel):
    pass

class EndpointAddress(BaseModel):
    pass

class EndpointPort(BaseModel):
    pass

class EndpointSubset(BaseModel):
    pass

class EnvFromSource(BaseModel):
    pass

class EnvVar(BaseModel):
    pass

class EnvVarSource(BaseModel):
    pass

class EphemeralContainer(BaseModel):
    pass

class EphemeralVolumeSource(BaseModel):
    pass

class EventSource(BaseModel):
    pass

class ExecAction(BaseModel):
    pass

class FCVolumeSource(BaseModel):
    pass

class FlexPersistentVolumeSource(BaseModel):
    pass

class FlexVolumeSource(BaseModel):
    pass

class FlockerVolumeSource(BaseModel):
    pass

class GCEPersistentDiskVolumeSource(BaseModel):
    pass

class GRPCAction(BaseModel):
    pass

class GitRepoVolumeSource(BaseModel):
    pass

class GlusterfsPersistentVolumeSource(BaseModel):
    pass

class GlusterfsVolumeSource(BaseModel):
    pass

class HTTPGetAction(BaseModel):
    pass

class HTTPHeader(BaseModel):
    pass

class HostAlias(BaseModel):
    pass

class HostIP(BaseModel):
    pass

class HostPathVolumeSource(BaseModel):
    pass

class ISCSIPersistentVolumeSource(BaseModel):
    pass

class ISCSIVolumeSource(BaseModel):
    pass

class KeyToPath(BaseModel):
    pass

class Lifecycle(BaseModel):
    pass

class LifecycleHandler(BaseModel):
    pass

class LimitRangeItem(BaseModel):
    pass

class LoadBalancerIngress(BaseModel):
    pass

class LoadBalancerStatus(BaseModel):
    pass

class LocalObjectReference(BaseModel):
    pass

class LocalVolumeSource(BaseModel):
    pass

class NFSVolumeSource(BaseModel):
    pass

class NamespaceCondition(BaseModel):
    pass

class NodeAddress(BaseModel):
    pass

class NodeAffinity(BaseModel):
    pass

class NodeCondition(BaseModel):
    pass

class NodeConfigSource(BaseModel):
    pass

class NodeConfigStatus(BaseModel):
    pass

class NodeDaemonEndpoints(BaseModel):
    pass

class NodeSelector(BaseModel):
    pass

class NodeSelectorRequirement(BaseModel):
    pass

class NodeSelectorTerm(BaseModel):
    pass

class NodeSystemInfo(BaseModel):
    pass

class ObjectFieldSelector(BaseModel):
    pass

class ObjectReference(BaseModel):
    pass

class PersistentVolumeClaimCondition(BaseModel):
    pass

class PersistentVolumeClaimTemplate(BaseModel):
    pass

class PersistentVolumeClaimVolumeSource(BaseModel):
    pass

class PhotonPersistentDiskVolumeSource(BaseModel):
    pass

class PodAffinity(BaseModel):
    pass

class PodAffinityTerm(BaseModel):
    pass

class PodAntiAffinity(BaseModel):
    pass

class PodCondition(BaseModel):
    pass

class PodDNSConfig(BaseModel):
    pass

class PodDNSConfigOption(BaseModel):
    pass

class PodIP(BaseModel):
    pass

class PodOS(BaseModel):
    pass

class PodReadinessGate(BaseModel):
    pass

class PodResourceClaim(BaseModel):
    pass

class PodSchedulingGate(BaseModel):
    pass

class PodSecurityContext(BaseModel):
    pass

class PortStatus(BaseModel):
    pass

class PortworxVolumeSource(BaseModel):
    pass

class PreferredSchedulingTerm(BaseModel):
    pass

class Probe(BaseModel):
    pass

class ProjectedVolumeSource(BaseModel):
    pass

class Quantity(BaseModel):
    pass

class QuobyteVolumeSource(BaseModel):
    pass

class RBDPersistentVolumeSource(BaseModel):
    pass

class RBDVolumeSource(BaseModel):
    pass

class ReplicationControllerCondition(BaseModel):
    pass

class ResourceClaim(BaseModel):
    pass

class ResourceFieldSelector(BaseModel):
    pass

class ResourceRequirements(BaseModel):
    pass

class SELinuxOptions(BaseModel):
    pass

class ScaleIOPersistentVolumeSource(BaseModel):
    pass

class ScaleIOVolumeSource(BaseModel):
    pass

class ScopeSelector(BaseModel):
    pass

class ScopedResourceSelectorRequirement(BaseModel):
    pass

class SeccompProfile(BaseModel):
    pass

class SecretEnvSource(BaseModel):
    pass

class SecretKeySelector(BaseModel):
    pass

class SecretProjection(BaseModel):
    pass

class SecretReference(BaseModel):
    pass

class SecretVolumeSource(BaseModel):
    pass

class SecurityContext(BaseModel):
    pass

class ServiceAccountTokenProjection(BaseModel):
    pass

class ServicePort(BaseModel):
    pass

class SessionAffinityConfig(BaseModel):
    pass

class StorageOSPersistentVolumeSource(BaseModel):
    pass

class StorageOSVolumeSource(BaseModel):
    pass

class Sysctl(BaseModel):
    pass

class TCPSocketAction(BaseModel):
    pass

class Taint(BaseModel):
    pass

class Toleration(BaseModel):
    pass

class TopologySelectorLabelRequirement(BaseModel):
    pass

class TopologySelectorTerm(BaseModel):
    pass

class TopologySpreadConstraint(BaseModel):
    pass

class TypedLocalObjectReference(BaseModel):
    pass

class TypedObjectReference(BaseModel):
    pass

class VolumeDevice(BaseModel):
    pass

class VolumeMount(BaseModel):
    pass

class VolumeNodeAffinity(BaseModel):
    pass

class VolumeProjection(BaseModel):
    pass

class VsphereVirtualDiskVolumeSource(BaseModel):
    pass

class WeightedPodAffinityTerm(BaseModel):
    pass

class WindowsSecurityContextOptions(BaseModel):
    pass

##--------------------------------------------------
##--------------------------------------------------
class DaemonSetSpec(BaseModel):
    pass

class DaemonSetStatus(BaseModel):
    pass

class JobTemplateSpec(BaseModel):
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

class StatefulSetSpec(BaseModel):
    pass

class StatefulSetStatus(BaseModel):
    pass
