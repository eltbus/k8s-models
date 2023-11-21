from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.meta import ObjectMeta
from k8s_models.definitions.core import (
    Affinity,
    EnvVar,
    EnvFromSource,
    Lifecycle,
    LocalObjectReference,
    HostAlias,
    EphemeralContainer,
    Probe,
    VolumeDevice,
    VolumeMount,
    ContainerState,
    ResourceRequirements,
    ContainerPort,
    ContainerResizePolicy,
    SecurityContext,
    PodDNSConfig,
    PodOS,
    PodReadinessGate,
    PodResourceClaim,
    PodSchedulingGate,
    PodSecurityContext,
    Toleration,
    TopologySpreadConstraint,
)
from k8s_models.definitions.unknown import PodStatus, ReplicationControllerStatus
from k8s_models.config_and_storage.core import Volume
from k8s_models.metadata.core import PodTemplateSpec


class Container(BaseModel):
    args: List[str] = Field(
        default=None,
        description=r""" Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """,
    )
    command: List[str] = Field(
        default=None,
        description=r""" Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """,
    )
    env: List[EnvVar] = Field(
        default=None,
        description=r""" List of environment variables to set in the container. Cannot be updated. """,
    )
    envFrom: List[EnvFromSource] = Field(
        default=None,
        description=r""" List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. """,
    )
    image: str = Field(
        default=None,
        description=r""" Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. """,
    )
    imagePullPolicy: str = Field(
        default=None,
        description=r""" Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images """,
    )
    lifecycle: Lifecycle = Field(
        default=None,
        description=r""" Actions that the management system should take in response to container lifecycle events. Cannot be updated. """,
    )
    livenessProbe: Probe = Field(
        default=None,
        description=r""" Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """,
    )
    name: str = Field(
        default=None,
        description=r""" Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. """,
    )
    ports: List[ContainerPort] = Field(
        default=None,
        description=r""" List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated. """,
    )
    readinessProbe: Probe = Field(
        default=None,
        description=r""" Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """,
    )
    resizePolicy: List[ContainerResizePolicy] = Field(
        default=None, description=r""" Resources resize policy for the container. """
    )
    resources: ResourceRequirements = Field(
        default=None,
        description=r""" Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """,
    )
    restartPolicy: str = Field(
        default=None,
        description=r""" RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed. """,
    )
    securityContext: SecurityContext = Field(
        default=None,
        description=r""" SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/ """,
    )
    startupProbe: Probe = Field(
        default=None,
        description=r""" StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """,
    )
    stdin: bool = Field(
        default=None,
        description=r""" Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. """,
    )
    stdinOnce: bool = Field(
        default=None,
        description=r""" Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false """,
    )
    terminationMessagePath: str = Field(
        default=None,
        description=r""" Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. """,
    )
    terminationMessagePolicy: str = Field(
        default=None,
        description=r""" Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. """,
    )
    tty: bool = Field(
        default=None,
        description=r""" Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. """,
    )
    volumeDevices: List[VolumeDevice] = Field(
        default=None,
        description=r""" volumeDevices is the list of block devices to be used by the container. """,
    )
    volumeMounts: List[VolumeMount] = Field(
        default=None,
        description=r""" Pod volumes to mount into the container's filesystem. Cannot be updated. """,
    )
    workingDir: str = Field(
        default=None,
        description=r""" Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. """,
    )


class ContainerStatus(BaseModel):
    allocatedResources: dict = Field(
        default=None,
        description=r""" AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize. """,
    )
    containerID: str = Field(
        default=None,
        description=r""" ContainerID is the ID of the container in the format '<type>://<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example "containerd"). """,
    )
    image: str = Field(
        default=None,
        description=r""" Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images. """,
    )
    imageID: str = Field(
        default=None,
        description=r""" ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime. """,
    )
    lastState: ContainerState = Field(
        default=None,
        description=r""" LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0. """,
    )
    name: str = Field(
        default=None,
        description=r""" Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated. """,
    )
    ready: bool = Field(
        default=None,
        description=r""" Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).  The value is typically used to determine whether a container is ready to accept traffic. """,
    )
    resources: ResourceRequirements = Field(
        default=None,
        description=r""" Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized. """,
    )
    restartCount: int = Field(
        default=None,
        description=r""" RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative. """,
    )
    started: bool = Field(
        default=None,
        description=r""" Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false. """,
    )
    state: ContainerState = Field(
        default=None,
        description=r""" State holds details about the container's current condition. """,
    )


class Pod(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="Pod",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: PodSpec = Field(
        default=None,
        description=r""" Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """,
    )
    status: PodStatus = Field(
        default=None,
        description=r""" Most recently observed status of the pod. This data may not be up to date. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """,
    )


class PodSpec(BaseModel):
    activeDeadlineSeconds: int = Field(
        default=None,
        description=r""" Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer. """,
    )
    affinity: Affinity = Field(
        default=None,
        description=r""" If specified, the pod's scheduling constraints """,
    )
    automountServiceAccountToken: bool = Field(
        default=None,
        description=r""" AutomountServiceAccountToken indicates whether a service account token should be automatically mounted. """,
    )
    containers: List[Container] = Field(
        default=None,
        description=r""" List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. """,
    )
    dnsConfig: PodDNSConfig = Field(
        default=None,
        description=r""" Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy. """,
    )
    dnsPolicy: str = Field(
        default=None,
        description=r""" Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'. """,
    )
    enableServiceLinks: bool = Field(
        default=None,
        description=r""" EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true. """,
    )
    ephemeralContainers: List[EphemeralContainer] = Field(
        default=None,
        description=r""" List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. """,
    )
    hostAliases: List[HostAlias] = Field(
        default=None,
        description=r""" HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods. """,
    )
    hostIPC: bool = Field(
        default=None,
        description=r""" Use the host's ipc namespace. Optional: Default to false. """,
    )
    hostNetwork: bool = Field(
        default=None,
        description=r""" Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false. """,
    )
    hostPID: bool = Field(
        default=None,
        description=r""" Use the host's pid namespace. Optional: Default to false. """,
    )
    hostUsers: bool = Field(
        default=None,
        description=r""" Use the host's user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature. """,
    )
    hostname: str = Field(
        default=None,
        description=r""" Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value. """,
    )
    imagePullSecrets: List[LocalObjectReference] = Field(
        default=None,
        description=r""" ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod """,
    )
    initContainers: List[Container] = Field(
        default=None,
        description=r""" List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ """,
    )
    nodeName: str = Field(
        default=None,
        description=r""" NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements. """,
    )
    nodeSelector: dict = Field(
        default=None,
        description=r""" NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ """,
    )
    os: PodOS = Field(
        default=None,
        description=r""" Specifies the OS of the containers in the pod. Some pod and container fields are restricted if this is set.  If the OS field is set to linux, the following fields must be unset: -securityContext.windowsOptions  If the OS field is set to windows, following fields must be unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.containers[*].securityContext.seLinuxOptions - spec.containers[*].securityContext.seccompProfile - spec.containers[*].securityContext.capabilities - spec.containers[*].securityContext.readOnlyRootFilesystem - spec.containers[*].securityContext.privileged - spec.containers[*].securityContext.allowPrivilegeEscalation - spec.containers[*].securityContext.procMount - spec.containers[*].securityContext.runAsUser - spec.containers[*].securityContext.runAsGroup """,
    )
    overhead: dict = Field(
        default=None,
        description=r""" Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md """,
    )
    preemptionPolicy: str = Field(
        default=None,
        description=r""" PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. """,
    )
    priority: int = Field(
        default=None,
        description=r""" The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority. """,
    )
    priorityClassName: str = Field(
        default=None,
        description=r""" If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default. """,
    )
    readinessGates: List[PodReadinessGate] = Field(
        default=None,
        description=r""" If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates """,
    )
    resourceClaims: List[PodResourceClaim] = Field(
        default=None,
        description=r""" ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. """,
    )
    restartPolicy: str = Field(
        default=None,
        description=r""" Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy """,
    )
    runtimeClassName: str = Field(
        default=None,
        description=r""" RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class """,
    )
    schedulerName: str = Field(
        default=None,
        description=r""" If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler. """,
    )
    schedulingGates: List[PodSchedulingGate] = Field(
        default=None,
        description=r""" SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.  SchedulingGates can only be set at pod creation time, and be removed only afterwards.  This is a beta feature enabled by the PodSchedulingReadiness feature gate. """,
    )
    securityContext: PodSecurityContext = Field(
        default=None,
        description=r""" SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field. """,
    )
    serviceAccount: str = Field(
        default=None,
        description=r""" DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead. """,
    )
    serviceAccountName: str = Field(
        default=None,
        description=r""" ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ """,
    )
    setHostnameAsFQDN: bool = Field(
        default=None,
        description=r""" If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false. """,
    )
    shareProcessNamespace: bool = Field(
        default=None,
        description=r""" Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false. """,
    )
    subdomain: str = Field(
        default=None,
        description=r""" If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all. """,
    )
    terminationGracePeriodSeconds: int = Field(
        default=None,
        description=r""" Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds. """,
    )
    tolerations: List[Toleration] = Field(
        default=None, description=r""" If specified, the pod's tolerations. """
    )
    topologySpreadConstraints: List[TopologySpreadConstraint] = Field(
        default=None,
        description=r""" TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed. """,
    )
    volumes: List[Volume] = Field(
        default=None,
        description=r""" List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes """,
    )


class ReplicationController(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="ReplicationController",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: ReplicationControllerSpec = Field(
        default=None,
        description=r""" Spec defines the specification of the desired behavior of the replication controller. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """,
    )
    status: ReplicationControllerStatus = Field(
        default=None,
        description=r""" Status is the most recently observed status of the replication controller. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """,
    )


class ReplicationControllerSpec(BaseModel):
    minReadySeconds: int = Field(
        default=None,
        description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """,
    )
    replicas: int = Field(
        default=None,
        description=r""" Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller """,
    )
    selector: dict = Field(
        default=None,
        description=r""" Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """,
    )
    template: PodTemplateSpec = Field(
        default=None,
        description=r""" Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """,
    )
