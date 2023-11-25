from __future__ import annotations
from typing import Any, List

from pydantic import BaseModel, Field
from yaml import safe_dump


class KubeModel(BaseModel):
    def model_to_yaml(self):
        model_data = self.model_dump(by_alias=True, exclude_none=True)
        return safe_dump(
            data=model_data,
            sort_keys=False,
            default_flow_style=False,
            indent=2,
            allow_unicode=True,
            explicit_start=True
        )


ScaleSpec = Any
ScaleStatus = Any
PodResourceClaimStatus = Any


class Container(BaseModel):
    args: List[str] = Field(default=None, description=r""" Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """)
    command: List[str] = Field(default=None, description=r""" Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """)
    env: List[EnvVar] = Field(default=None, description=r""" List of environment variables to set in the container. Cannot be updated. """)
    envFrom: List[EnvFromSource] = Field(default=None, description=r""" List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. """)
    image: str = Field(default=None, description=r""" Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. """)
    imagePullPolicy: str = Field(default=None, description=r""" Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images """)
    lifecycle: Lifecycle = Field(default=None, description=r""" Actions that the management system should take in response to container lifecycle events. Cannot be updated. """)
    livenessProbe: Probe = Field(default=None, description=r""" Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)
    name: str = Field(default=None, description=r""" Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. """)
    ports: List[ContainerPort] = Field(default=None, description=r""" List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated. """)
    readinessProbe: Probe = Field(default=None, description=r""" Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)
    resizePolicy: List[ContainerResizePolicy] = Field(default=None, description=r""" Resources resize policy for the container. """)
    resources: ResourceRequirements = Field(default=None, description=r""" Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """)
    restartPolicy: str = Field(default=None, description=r""" RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed. """)
    securityContext: SecurityContext = Field(default=None, description=r""" SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/ """)
    startupProbe: Probe = Field(default=None, description=r""" StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)
    stdin: bool = Field(default=None, description=r""" Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. """)
    stdinOnce: bool = Field(default=None, description=r""" Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false """)
    terminationMessagePath: str = Field(default=None, description=r""" Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. """)
    terminationMessagePolicy: str = Field(default=None, description=r""" Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. """)
    tty: bool = Field(default=None, description=r""" Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. """)
    volumeDevices: List[VolumeDevice] = Field(default=None, description=r""" volumeDevices is the list of block devices to be used by the container. """)
    volumeMounts: List[VolumeMount] = Field(default=None, description=r""" Pod volumes to mount into the container's filesystem. Cannot be updated. """)
    workingDir: str = Field(default=None, description=r""" Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. """)


class ContainerStatus(BaseModel):
    allocatedResources: dict = Field(default=None, description=r""" AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize. """)
    containerID: str = Field(default=None, description=r""" ContainerID is the ID of the container in the format '<type>://<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example "containerd"). """)
    image: str = Field(default=None, description=r""" Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images. """)
    imageID: str = Field(default=None, description=r""" ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime. """)
    lastState: ContainerState = Field(default=None, description=r""" LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0. """)
    name: str = Field(default=None, description=r""" Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated. """)
    ready: bool = Field(default=None, description=r""" Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).  The value is typically used to determine whether a container is ready to accept traffic. """)
    resources: ResourceRequirements = Field(default=None, description=r""" Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized. """)
    restartCount: int = Field(default=None, description=r""" RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative. """)
    started: bool = Field(default=None, description=r""" Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false. """)
    state: ContainerState = Field(default=None, description=r""" State holds details about the container's current condition. """)


class CronJob(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="CronJob", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: CronJobSpec = Field(default=None, description=r""" Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: CronJobStatus = Field(default=None, description=r""" Current status of a cron job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class CronJobSpec(BaseModel):
    concurrencyPolicy: str = Field(default=None, description=r""" Specifies how to treat concurrent executions of a Job. Valid values are:  - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - "Replace": cancels currently running job and replaces it with a new one """)
    failedJobsHistoryLimit: int = Field(default=None, description=r""" The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1. """)
    jobTemplate: JobTemplateSpec = Field(default=None, description=r""" Specifies the job that will be created when executing a CronJob. """)
    schedule: str = Field(default=None, description=r""" The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron. """)
    startingDeadlineSeconds: int = Field(default=None, description=r""" Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones. """)
    successfulJobsHistoryLimit: int = Field(default=None, description=r""" The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3. """)
    suspend: bool = Field(default=None, description=r""" This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false. """)
    timeZone: str = Field(default=None, description=r""" The time zone name for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones """)


class CronJobStatus(BaseModel):
    active: List[ObjectReference] = Field(default=None, description=r""" A list of pointers to currently running jobs. """)
    lastScheduleTime: Time = Field(default=None, description=r""" Information when was the last time the job was successfully scheduled. """)
    lastSuccessfulTime: Time = Field(default=None, description=r""" Information when was the last time the job successfully completed. """)


class CronJobList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[CronJob] = Field(default=None, description=r""" items is the list of CronJobs. """)
    kind: str = Field(default="CronJobList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class DaemonSet(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="DaemonSet", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: DaemonSetSpec = Field(default=None, description=r""" The desired behavior of this daemon set. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: DaemonSetStatus = Field(default=None, description=r""" The current status of this daemon set. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class DaemonSetSpec(BaseModel):
    minReadySeconds: int = Field(default=None, description=r""" The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready). """)
    revisionHistoryLimit: int = Field(default=None, description=r""" The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. """)
    selector: LabelSelector = Field(default=None, description=r""" A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """)
    template: PodTemplateSpec = Field(default=None, description=r""" An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """)
    updateStrategy: DaemonSetUpdateStrategy = Field(default=None, description=r""" An update strategy to replace existing DaemonSet pods with new pods. """)


class DaemonSetStatus(BaseModel):
    collisionCount: int = Field(default=None, description=r""" Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. """)
    conditions: List[DaemonSetCondition] = Field(default=None, description=r""" Represents the latest available observations of a DaemonSet's current state. """)
    currentNumberScheduled: int = Field(default=None, description=r""" The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """)
    desiredNumberScheduled: int = Field(default=None, description=r""" The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """)
    numberAvailable: int = Field(default=None, description=r""" The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds) """)
    numberMisscheduled: int = Field(default=None, description=r""" The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """)
    numberReady: int = Field(default=None, description=r""" numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition. """)
    numberUnavailable: int = Field(default=None, description=r""" The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds) """)
    observedGeneration: int = Field(default=None, description=r""" The most recent generation observed by the daemon set controller. """)
    updatedNumberScheduled: int = Field(default=None, description=r""" The total number of nodes that are running updated daemon pod """)


class DaemonSetList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[DaemonSet] = Field(default=None, description=r""" A list of daemon sets. """)
    kind: str = Field(default="DaemonSetList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class RollingUpdateDaemonSet(BaseModel):
    maxSurge: Any = Field(default=None, description=r""" The maximum number of nodes with an existing available DaemonSet pod that can have an updated DaemonSet pod during during an update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up to a minimum of 1. Default value is 0. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their a new pod created before the old pod is marked as deleted. The update starts by launching new pods on 30% of nodes. Once an updated pod is available (Ready for at least minReadySeconds) the old DaemonSet pod on that node is marked deleted. If the old pod becomes unavailable for any reason (Ready transitions to false, is evicted, or is drained) an updated pod is immediatedly created on that node without considering surge limits. Allowing surge implies the possibility that the resources consumed by the daemonset on any given node can double if the readiness check fails, and so resource intensive daemonsets should take into account that they may cause evictions during disruption. """)
    maxUnavailable: Any = Field(default=None, description=r""" The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0 if MaxSurge is 0 Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update. """)


class Deployment(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Deployment", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: DeploymentSpec = Field(default=None, description=r""" Specification of the desired behavior of the Deployment. """)
    status: DeploymentStatus = Field(default=None, description=r""" Most recently observed status of the Deployment. """)


class DeploymentSpec(BaseModel):
    minReadySeconds: int = Field(default=None, description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """)
    paused: bool = Field(default=None, description=r""" Indicates that the deployment is paused. """)
    progressDeadlineSeconds: int = Field(default=None, description=r""" The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. """)
    replicas: int = Field(default=None, description=r""" Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. """)
    revisionHistoryLimit: int = Field(default=None, description=r""" The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. """)
    selector: LabelSelector = Field(default=None, description=r""" Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels. """)
    strategy: DeploymentStrategy = Field(default=None, description=r""" The deployment strategy to use to replace existing pods with new ones. """)
    template: PodTemplateSpec = Field(default=None, description=r""" Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always". """)


class DeploymentStatus(BaseModel):
    availableReplicas: int = Field(default=None, description=r""" Total number of available pods (ready for at least minReadySeconds) targeted by this deployment. """)
    collisionCount: int = Field(default=None, description=r""" Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet. """)
    conditions: List[DeploymentCondition] = Field(default=None, description=r""" Represents the latest available observations of a deployment's current state. """)
    observedGeneration: int = Field(default=None, description=r""" The generation observed by the deployment controller. """)
    readyReplicas: int = Field(default=None, description=r""" readyReplicas is the number of pods targeted by this Deployment with a Ready Condition. """)
    replicas: int = Field(default=None, description=r""" Total number of non-terminated pods targeted by this deployment (their labels match the selector). """)
    unavailableReplicas: int = Field(default=None, description=r""" Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created. """)
    updatedReplicas: int = Field(default=None, description=r""" Total number of non-terminated pods targeted by this deployment that have the desired template spec. """)


class DeploymentList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Deployment] = Field(default=None, description=r""" Items is the list of Deployments. """)
    kind: str = Field(default="DeploymentList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. """)


class DeploymentStrategy(BaseModel):
    rollingUpdate: RollingUpdateDeployment = Field(default=None, description=r""" Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate. """)
    type: str = Field(default=None, description=r""" Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate. """)


class RollingUpdateDeployment(BaseModel):
    maxSurge: Any = Field(default=None, description=r""" The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. """)
    maxUnavailable: Any = Field(default=None, description=r""" The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. """)


class Job(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Job", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: JobSpec = Field(default=None, description=r""" Specification of the desired behavior of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: JobStatus = Field(default=None, description=r""" Current status of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class JobSpec(BaseModel):
    activeDeadlineSeconds: int = Field(default=None, description=r""" Specifies the duration in seconds relative to the startTime that the job may be continuously active before the system tries to terminate it; value must be positive integer. If a Job is suspended (at creation or through an update), this timer will effectively be stopped and reset when the Job is resumed again. """)
    backoffLimit: int = Field(default=None, description=r""" Specifies the number of retries before marking this job failed. Defaults to 6 """)
    backoffLimitPerIndex: int = Field(default=None, description=r""" Specifies the limit for the number of retries within an index before marking this index as failed. When enabled the number of failures per index is kept in the pod's batch.kubernetes.io/job-index-failure-count annotation. It can only be set when Job's completionMode=Indexed, and the Pod's restart policy is Never. The field is immutable. This field is alpha-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (disabled by default). """)
    completionMode: str = Field(default=None, description=r""" completionMode specifies how Pod completions are tracked. It can be `NonIndexed` (default) or `Indexed`.  `NonIndexed` means that the Job is considered complete when there have been .spec.completions successfully completed Pods. Each Pod completion is homologous to each other.  `Indexed` means that the Pods of a Job get an associated completion index from 0 to (.spec.completions - 1), available in the annotation batch.kubernetes.io/job-completion-index. The Job is considered complete when there is one successfully completed Pod for each index. When value is `Indexed`, .spec.completions must be specified and `.spec.parallelism` must be less than or equal to 10^5. In addition, The Pod name takes the form `$(job-name)-$(index)-$(random-string)`, the Pod hostname takes the form `$(job-name)-$(index)`.  More completion modes can be added in the future. If the Job controller observes a mode that it doesn't recognize, which is possible during upgrades due to version skew, the controller skips updates for the Job. """)
    completions: int = Field(default=None, description=r""" Specifies the desired number of successfully finished pods the job should be run with.  Setting to null means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ """)
    manualSelector: bool = Field(default=None, description=r""" manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector """)
    maxFailedIndexes: int = Field(default=None, description=r""" Specifies the maximal number of failed indexes before marking the Job as failed, when backoffLimitPerIndex is set. Once the number of failed indexes exceeds this number the entire Job is marked as Failed and its execution is terminated. When left as null the job continues execution of all of its indexes and is marked with the `Complete` Job condition. It can only be specified when backoffLimitPerIndex is set. It can be null or up to completions. It is required and must be less than or equal to 10^4 when is completions greater than 10^5. This field is alpha-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (disabled by default). """)
    parallelism: int = Field(default=None, description=r""" Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ """)
    podFailurePolicy: PodFailurePolicy = Field(default=None, description=r""" Specifies the policy of handling failed pods. In particular, it allows to specify the set of actions and conditions which need to be satisfied to take the associated action. If empty, the default behaviour applies - the counter of failed pods, represented by the jobs's .status.failed field, is incremented and it is checked against the backoffLimit. This field cannot be used in combination with restartPolicy=OnFailure.  This field is beta-level. It can be used when the `JobPodFailurePolicy` feature gate is enabled (enabled by default). """)
    podReplacementPolicy: str = Field(default=None, description=r""" podReplacementPolicy specifies when to create replacement Pods. Possible values are: - TerminatingOrFailed means that we recreate pods   when they are terminating (has a metadata.deletionTimestamp) or failed. - Failed means to wait until a previously created Pod is fully terminated (has phase   Failed or Succeeded) before creating a replacement Pod.  When using podFailurePolicy, Failed is the the only allowed value. TerminatingOrFailed and Failed are allowed values when podFailurePolicy is not in use. This is an alpha field. Enable JobPodReplacementPolicy to be able to use this field. """)
    selector: LabelSelector = Field(default=None, description=r""" A label query over pods that should match the pod count. Normally, the system sets this field for you. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """)
    suspend: bool = Field(default=None, description=r""" suspend specifies whether the Job controller should create Pods or not. If a Job is created with suspend set to true, no Pods are created by the Job controller. If a Job is suspended after creation (i.e. the flag goes from false to true), the Job controller will delete all active Pods associated with this Job. Users must design their workload to gracefully handle this. Suspending a Job will reset the StartTime field of the Job, effectively resetting the ActiveDeadlineSeconds timer too. Defaults to false. """)
    template: PodTemplateSpec = Field(default=None, description=r""" Describes the pod that will be created when executing a job. The only allowed template.spec.restartPolicy values are "Never" or "OnFailure". More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ """)
    ttlSecondsAfterFinished: int = Field(default=None, description=r""" ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. """)


class JobStatus(BaseModel):
    active: int = Field(default=None, description=r""" The number of pending and running pods. """)
    completedIndexes: str = Field(default=None, description=r""" completedIndexes holds the completed indexes when .spec.completionMode = "Indexed" in a text format. The indexes are represented as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as "1,3-5,7". """)
    completionTime: Time = Field(default=None, description=r""" Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. The completion time is only set when the job finishes successfully. """)
    conditions: List[JobCondition] = Field(default=None, description=r""" The latest available observations of an object's current state. When a Job fails, one of the conditions will have type "Failed" and status true. When a Job is suspended, one of the conditions will have type "Suspended" and status true; when the Job is resumed, the status of this condition will become false. When a Job is completed, one of the conditions will have type "Complete" and status true. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ """)
    failed: int = Field(default=None, description=r""" The number of pods which reached phase Failed. """)
    failedIndexes: str = Field(default=None, description=r""" FailedIndexes holds the failed indexes when backoffLimitPerIndex=true. The indexes are represented in the text format analogous as for the `completedIndexes` field, ie. they are kept as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the failed indexes are 1, 3, 4, 5 and 7, they are represented as "1,3-5,7". This field is alpha-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (disabled by default). """)
    ready: int = Field(default=None, description=r""" The number of pods which have a Ready condition.  This field is beta-level. The job controller populates the field when the feature gate JobReadyPods is enabled (enabled by default). """)
    startTime: Time = Field(default=None, description=r""" Represents time when the job controller started processing a job. When a Job is created in the suspended state, this field is not set until the first time it is resumed. This field is reset every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC. """)
    succeeded: int = Field(default=None, description=r""" The number of pods which reached phase Succeeded. """)
    terminating: int = Field(default=None, description=r""" The number of pods which are terminating (in phase Pending or Running and have a deletionTimestamp).  This field is alpha-level. The job controller populates the field when the feature gate JobPodReplacementPolicy is enabled (disabled by default). """)
    uncountedTerminatedPods: UncountedTerminatedPods = Field(default=None, description=r""" uncountedTerminatedPods holds the UIDs of Pods that have terminated but the job controller hasn't yet accounted for in the status counters.  The job controller creates pods with a finalizer. When a pod terminates (succeeded or failed), the controller does three steps to account for it in the job status:  1. Add the pod UID to the arrays in this field. 2. Remove the pod finalizer. 3. Remove the pod UID from the arrays while increasing the corresponding     counter.  Old jobs might not be tracked using this field, in which case the field remains null. """)


class JobList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Job] = Field(default=None, description=r""" items is the list of Jobs. """)
    kind: str = Field(default="JobList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class Pod(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Pod", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: PodSpec = Field(default=None, description=r""" Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: PodStatus = Field(default=None, description=r""" Most recently observed status of the pod. This data may not be up to date. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class PodSpec(BaseModel):
    activeDeadlineSeconds: int = Field(default=None, description=r""" Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer. """)
    affinity: Affinity = Field(default=None, description=r""" If specified, the pod's scheduling constraints """)
    automountServiceAccountToken: bool = Field(default=None, description=r""" AutomountServiceAccountToken indicates whether a service account token should be automatically mounted. """)
    containers: List[Container] = Field(default=None, description=r""" List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. """)
    dnsConfig: PodDNSConfig = Field(default=None, description=r""" Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy. """)
    dnsPolicy: str = Field(default=None, description=r""" Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'. """)
    enableServiceLinks: bool = Field(default=None, description=r""" EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true. """)
    ephemeralContainers: List[EphemeralContainer] = Field(default=None, description=r""" List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. """)
    hostAliases: List[HostAlias] = Field(default=None, description=r""" HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods. """)
    hostIPC: bool = Field(default=None, description=r""" Use the host's ipc namespace. Optional: Default to false. """)
    hostNetwork: bool = Field(default=None, description=r""" Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false. """)
    hostPID: bool = Field(default=None, description=r""" Use the host's pid namespace. Optional: Default to false. """)
    hostUsers: bool = Field(default=None, description=r""" Use the host's user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature. """)
    hostname: str = Field(default=None, description=r""" Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value. """)
    imagePullSecrets: List[LocalObjectReference] = Field(default=None, description=r""" ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod """)
    initContainers: List[Container] = Field(default=None, description=r""" List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ """)
    nodeName: str = Field(default=None, description=r""" NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements. """)
    nodeSelector: dict = Field(default=None, description=r""" NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ """)
    os: PodOS = Field(default=None, description=r""" Specifies the OS of the containers in the pod. Some pod and container fields are restricted if this is set.  If the OS field is set to linux, the following fields must be unset: -securityContext.windowsOptions  If the OS field is set to windows, following fields must be unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.containers[*].securityContext.seLinuxOptions - spec.containers[*].securityContext.seccompProfile - spec.containers[*].securityContext.capabilities - spec.containers[*].securityContext.readOnlyRootFilesystem - spec.containers[*].securityContext.privileged - spec.containers[*].securityContext.allowPrivilegeEscalation - spec.containers[*].securityContext.procMount - spec.containers[*].securityContext.runAsUser - spec.containers[*].securityContext.runAsGroup """)
    overhead: dict = Field(default=None, description=r""" Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md """)
    preemptionPolicy: str = Field(default=None, description=r""" PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. """)
    priority: int = Field(default=None, description=r""" The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority. """)
    priorityClassName: str = Field(default=None, description=r""" If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default. """)
    readinessGates: List[PodReadinessGate] = Field(default=None, description=r""" If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates """)
    resourceClaims: List[PodResourceClaim] = Field(default=None, description=r""" ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. """)
    restartPolicy: str = Field(default=None, description=r""" Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy """)
    runtimeClassName: str = Field(default=None, description=r""" RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class """)
    schedulerName: str = Field(default=None, description=r""" If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler. """)
    schedulingGates: List[PodSchedulingGate] = Field(default=None, description=r""" SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.  SchedulingGates can only be set at pod creation time, and be removed only afterwards.  This is a beta feature enabled by the PodSchedulingReadiness feature gate. """)
    securityContext: PodSecurityContext = Field(default=None, description=r""" SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field. """)
    serviceAccount: str = Field(default=None, description=r""" DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead. """)
    serviceAccountName: str = Field(default=None, description=r""" ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ """)
    setHostnameAsFQDN: bool = Field(default=None, description=r""" If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false. """)
    shareProcessNamespace: bool = Field(default=None, description=r""" Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false. """)
    subdomain: str = Field(default=None, description=r""" If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all. """)
    terminationGracePeriodSeconds: int = Field(default=None, description=r""" Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds. """)
    tolerations: List[Toleration] = Field(default=None, description=r""" If specified, the pod's tolerations. """)
    topologySpreadConstraints: List[TopologySpreadConstraint] = Field(default=None, description=r""" TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed. """)
    volumes: List[Volume] = Field(default=None, description=r""" List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes """)


class PodStatus(BaseModel):
    conditions: List[PodCondition] = Field(default=None, description=r""" Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """)
    containerStatuses: List[ContainerStatus] = Field(default=None, description=r""" The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status """)
    ephemeralContainerStatuses: List[ContainerStatus] = Field(default=None, description=r""" Status for any ephemeral containers that have run in this pod. """)
    hostIP: str = Field(default=None, description=r""" hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean that HostIP will not be updated even if there is a node is assigned to pod """)
    hostIPs: List[HostIP] = Field(default=None, description=r""" hostIPs holds the IP addresses allocated to the host. If this field is specified, the first entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be updated even if there is a node is assigned to this pod. """)
    initContainerStatuses: List[ContainerStatus] = Field(default=None, description=r""" The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about why the pod is in this condition. """)
    nominatedNodeName: str = Field(default=None, description=r""" nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled. """)
    phase: str = Field(default=None, description=r""" The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase """)
    podIP: str = Field(default=None, description=r""" podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated. """)
    podIPs: List[PodIP] = Field(default=None, description=r""" podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet. """)
    qosClass: str = Field(default=None, description=r""" The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes """)
    reason: str = Field(default=None, description=r""" A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted' """)
    resize: str = Field(default=None, description=r""" Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to "Proposed" """)
    resourceClaimStatuses: List[PodResourceClaimStatus] = Field(default=None, description=r""" Status of resource claims. """)
    startTime: Time = Field(default=None, description=r""" RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod. """)


class PodList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Pod] = Field(default=None, description=r""" List of pods. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md """)
    kind: str = Field(default="PodList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class ReplicaSet(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ReplicaSet", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: ReplicaSetSpec = Field(default=None, description=r""" Spec defines the specification of the desired behavior of the ReplicaSet. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: ReplicaSetStatus = Field(default=None, description=r""" Status is the most recently observed status of the ReplicaSet. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class ReplicaSetSpec(BaseModel):
    minReadySeconds: int = Field(default=None, description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """)
    replicas: int = Field(default=None, description=r""" Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller """)
    selector: LabelSelector = Field(default=None, description=r""" Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """)
    template: PodTemplateSpec = Field(default=None, description=r""" Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """)


class ReplicaSetStatus(BaseModel):
    availableReplicas: int = Field(default=None, description=r""" The number of available replicas (ready for at least minReadySeconds) for this replica set. """)
    conditions: List[ReplicaSetCondition] = Field(default=None, description=r""" Represents the latest available observations of a replica set's current state. """)
    fullyLabeledReplicas: int = Field(default=None, description=r""" The number of pods that have labels matching the labels of the pod template of the replicaset. """)
    observedGeneration: int = Field(default=None, description=r""" ObservedGeneration reflects the generation of the most recently observed ReplicaSet. """)
    readyReplicas: int = Field(default=None, description=r""" readyReplicas is the number of pods targeted by this ReplicaSet with a Ready Condition. """)
    replicas: int = Field(default=None, description=r""" Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller """)


class ReplicaSetList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ReplicaSet] = Field(default=None, description=r""" List of ReplicaSets. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller """)
    kind: str = Field(default="ReplicaSetList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class ReplicationController(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ReplicationController", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: ReplicationControllerSpec = Field(default=None, description=r""" Spec defines the specification of the desired behavior of the replication controller. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: ReplicationControllerStatus = Field(default=None, description=r""" Status is the most recently observed status of the replication controller. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class ReplicationControllerSpec(BaseModel):
    minReadySeconds: int = Field(default=None, description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """)
    replicas: int = Field(default=None, description=r""" Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller """)
    selector: dict = Field(default=None, description=r""" Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """)
    template: PodTemplateSpec = Field(default=None, description=r""" Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """)


class ReplicationControllerStatus(BaseModel):
    availableReplicas: int = Field(default=None, description=r""" The number of available replicas (ready for at least minReadySeconds) for this replication controller. """)
    conditions: List[ReplicationControllerCondition] = Field(default=None, description=r""" Represents the latest available observations of a replication controller's current state. """)
    fullyLabeledReplicas: int = Field(default=None, description=r""" The number of pods that have labels matching the labels of the pod template of the replication controller. """)
    observedGeneration: int = Field(default=None, description=r""" ObservedGeneration reflects the generation of the most recently observed replication controller. """)
    readyReplicas: int = Field(default=None, description=r""" The number of ready replicas for this replication controller. """)
    replicas: int = Field(default=None, description=r""" Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller """)


class ReplicationControllerList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ReplicationController] = Field(default=None, description=r""" List of replication controllers. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller """)
    kind: str = Field(default="ReplicationControllerList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class StatefulSet(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="StatefulSet", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: StatefulSetSpec = Field(default=None, description=r""" Spec defines the desired identities of pods in this set. """)
    status: StatefulSetStatus = Field(default=None, description=r""" Status is the current status of Pods in this StatefulSet. This data may be out of date by some window of time. """)


class StatefulSetSpec(BaseModel):
    minReadySeconds: int = Field(default=None, description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """)
    ordinals: StatefulSetOrdinals = Field(default=None, description=r""" ordinals controls the numbering of replica indices in a StatefulSet. The default ordinals behavior assigns a "0" index to the first replica and increments the index by one for each additional replica requested. Using the ordinals field requires the StatefulSetStartOrdinal feature gate to be enabled, which is beta. """)
    persistentVolumeClaimRetentionPolicy: StatefulSetPersistentVolumeClaimRetentionPolicy = Field(default=None, description=r""" persistentVolumeClaimRetentionPolicy describes the lifecycle of persistent volume claims created from volumeClaimTemplates. By default, all persistent volume claims are created as needed and retained until manually deleted. This policy allows the lifecycle to be altered, for example by deleting persistent volume claims when their stateful set is deleted, or when their pod is scaled down. This requires the StatefulSetAutoDeletePVC feature gate to be enabled, which is alpha.  +optional """)
    podManagementPolicy: str = Field(default=None, description=r""" podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once. """)
    replicas: int = Field(default=None, description=r""" replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1. """)
    revisionHistoryLimit: int = Field(default=None, description=r""" revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10. """)
    selector: LabelSelector = Field(default=None, description=r""" selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """)
    serviceName: str = Field(default=None, description=r""" serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller. """)
    template: PodTemplateSpec = Field(default=None, description=r""" template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet. Each pod will be named with the format <statefulsetname>-<podindex>. For example, a pod in a StatefulSet named "web" with index number "3" would be named "web-3". The only allowed template.spec.restartPolicy value is "Always". """)
    updateStrategy: StatefulSetUpdateStrategy = Field(default=None, description=r""" updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template. """)
    volumeClaimTemplates: List[PersistentVolumeClaim] = Field(default=None, description=r""" volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name. """)


class StatefulSetStatus(BaseModel):
    availableReplicas: int = Field(default=None, description=r""" Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset. """)
    collisionCount: int = Field(default=None, description=r""" collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. """)
    conditions: List[StatefulSetCondition] = Field(default=None, description=r""" Represents the latest available observations of a statefulset's current state. """)
    currentReplicas: int = Field(default=None, description=r""" currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision. """)
    currentRevision: str = Field(default=None, description=r""" currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas). """)
    observedGeneration: int = Field(default=None, description=r""" observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server. """)
    readyReplicas: int = Field(default=None, description=r""" readyReplicas is the number of pods created for this StatefulSet with a Ready Condition. """)
    replicas: int = Field(default=None, description=r""" replicas is the number of Pods created by the StatefulSet controller. """)
    updateRevision: str = Field(default=None, description=r""" updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas) """)
    updatedReplicas: int = Field(default=None, description=r""" updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision. """)


class StatefulSetList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[StatefulSet] = Field(default=None, description=r""" Items is the list of stateful sets. """)
    kind: str = Field(default="StatefulSetList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class Endpoints(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Endpoints", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    subsets: List[EndpointSubset] = Field(default=None, description=r""" The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service. """)


class EndpointsList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Endpoints] = Field(default=None, description=r""" List of endpoints. """)
    kind: str = Field(default="EndpointsList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class EndpointSlice(KubeModel):
    addressType: str = Field(default=None, description=r""" addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name. """)
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    endpoints: List[Endpoint] = Field(default=None, description=r""" endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints. """)
    kind: str = Field(default="EndpointSlice", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. """)
    ports: List[EndpointPort] = Field(default=None, description=r""" ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports. """)


class EndpointSliceList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[EndpointSlice] = Field(default=None, description=r""" items is the list of endpoint slices """)
    kind: str = Field(default="EndpointSliceList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. """)


class ClusterCIDR(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ClusterCIDR", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: ClusterCIDRSpec = Field(default=None, description=r""" spec is the desired state of the ClusterCIDR. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class ClusterCIDRSpec(BaseModel):
    ipv4: str = Field(default=None, description=r""" ipv4 defines an IPv4 IP block in CIDR notation(e.g. "10.0.0.0/8"). At least one of ipv4 and ipv6 must be specified. This field is immutable. """)
    ipv6: str = Field(default=None, description=r""" ipv6 defines an IPv6 IP block in CIDR notation(e.g. "2001:db8::/64"). At least one of ipv4 and ipv6 must be specified. This field is immutable. """)
    nodeSelector: NodeSelector = Field(default=None, description=r""" nodeSelector defines which nodes the config is applicable to. An empty or nil nodeSelector selects all nodes. This field is immutable. """)
    perNodeHostBits: int = Field(default=None, description=r""" perNodeHostBits defines the number of host bits to be configured per node. A subnet mask determines how much of the address is used for network bits and host bits. For example an IPv4 address of 192.168.0.0/24, splits the address into 24 bits for the network portion and 8 bits for the host portion. To allocate 256 IPs, set this field to 8 (a /24 mask for IPv4 or a /120 for IPv6). Minimum value is 4 (16 IPs). This field is immutable. """)


class ClusterCIDRList(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ClusterCIDR] = Field(default=None, description=r""" items is the list of ClusterCIDRs. """)
    kind: str = Field(default="ClusterCIDRList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class Ingress(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Ingress", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: IngressSpec = Field(default=None, description=r""" spec is the desired state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: IngressStatus = Field(default=None, description=r""" status is the current state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class IngressSpec(BaseModel):
    defaultBackend: IngressBackend = Field(default=None, description=r""" defaultBackend is the backend that should handle requests that don't match any rule. If Rules are not specified, DefaultBackend must be specified. If DefaultBackend is not set, the handling of requests that do not match any of the rules will be up to the Ingress controller. """)
    ingressClassName: str = Field(default=None, description=r""" ingressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the `kubernetes.io/ingress.class` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present. """)
    rules: List[IngressRule] = Field(default=None, description=r""" rules is a list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend. """)
    tls: List[IngressTLS] = Field(default=None, description=r""" tls represents the TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI. """)


class IngressStatus(BaseModel):
    loadBalancer: IngressLoadBalancerStatus = Field(default=None, description=r""" loadBalancer contains the current status of the load-balancer. """)


class IngressList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Ingress] = Field(default=None, description=r""" items is the list of Ingress. """)
    kind: str = Field(default="IngressList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class IngressClass(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="IngressClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: IngressClassSpec = Field(default=None, description=r""" spec is the desired state of the IngressClass. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class IngressClassSpec(BaseModel):
    controller: str = Field(default=None, description=r""" controller refers to the name of the controller that should handle this class. This allows for different "flavors" that are controlled by the same controller. For example, you may have different parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. "acme.io/ingress-controller". This field is immutable. """)
    parameters: IngressClassParametersReference = Field(default=None, description=r""" parameters is a link to a custom resource containing additional configuration for the controller. This is optional if the controller does not require extra parameters. """)


class IngressClassList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[IngressClass] = Field(default=None, description=r""" items is the list of IngressClasses. """)
    kind: str = Field(default="IngressClassList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. """)


class Service(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Service", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: ServiceSpec = Field(default=None, description=r""" Spec defines the behavior of a service. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: ServiceStatus = Field(default=None, description=r""" Most recently observed status of the service. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class ServiceSpec(BaseModel):
    allocateLoadBalancerNodePorts: bool = Field(default=None, description=r""" allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer.  Default is "true". It may be set to "false" if the cluster load-balancer does not rely on NodePorts.  If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type. """)
    clusterIP: str = Field(default=None, description=r""" clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address. Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies """)
    clusterIPs: List[str] = Field(default=None, description=r""" ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly.  If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address.  Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName.  If this field is not specified, it will be initialized from the clusterIP field.  If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.  This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies """)
    externalIPs: List[str] = Field(default=None, description=r""" externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system. """)
    externalName: str = Field(default=None, description=r""" externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved.  Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires `type` to be "ExternalName". """)
    externalTrafficPolicy: str = Field(default=None, description=r""" externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the Service's "externally-facing" addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to "Local", the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, "Cluster", uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get "Cluster" semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node. """)
    healthCheckNodePort: int = Field(default=None, description=r""" healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used.  If not specified, a value will be automatically allocated.  External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type). This field cannot be updated once set. """)
    internalTrafficPolicy: str = Field(default=None, description=r""" InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to "Local", the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, "Cluster", uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). """)
    ipFamilies: List[str] = Field(default=None, description=r""" IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service. Valid values are "IPv4" and "IPv6".  This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to "headless" services. This field will be wiped when updating a Service to type ExternalName.  This field may hold a maximum of two entries (dual-stack families, in either order).  These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. """)
    ipFamilyPolicy: str = Field(default=None, description=r""" IPFamilyPolicy represents the dual-stack-ness requested or required by this Service. If there is no value provided, then this field will be set to SingleStack. Services can be "SingleStack" (a single IP family), "PreferDualStack" (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or "RequireDualStack" (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName. """)
    loadBalancerClass: str = Field(default=None, description=r""" loadBalancerClass is the class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. "internal-vip" or "example.com/internal-vip". Unprefixed names are reserved for end-users. This field can only be set when the Service type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a Service to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type. """)
    loadBalancerIP: str = Field(default=None, description=r""" Only applies to Service Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations. Using it is non-portable and it may not support dual-stack. Users are encouraged to use implementation-specific annotations when available. """)
    loadBalancerSourceRanges: List[str] = Field(default=None, description=r""" If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature." More info: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/ """)
    ports: List[ServicePort] = Field(default=None, description=r""" The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies """)
    publishNotReadyAddresses: bool = Field(default=None, description=r""" publishNotReadyAddresses indicates that any agent which deals with endpoints for this Service should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless Service to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered "ready" even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior. """)
    selector: dict = Field(default=None, description=r""" Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/ """)
    sessionAffinity: str = Field(default=None, description=r""" Supports "ClientIP" and "None". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies """)
    sessionAffinityConfig: SessionAffinityConfig = Field(default=None, description=r""" sessionAffinityConfig contains the configurations of session affinity. """)
    type: str = Field(default=None, description=r""" type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. "ClusterIP" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is "None", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. "NodePort" builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. "LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. "ExternalName" aliases this service to the specified externalName. Several other fields do not apply to ExternalName services. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types """)


class ServiceStatus(BaseModel):
    conditions: List[Condition] = Field(default=None, description=r""" Current service state """)
    loadBalancer: LoadBalancerStatus = Field(default=None, description=r""" LoadBalancer contains the current status of the load-balancer, if one is present. """)


class ServiceList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Service] = Field(default=None, description=r""" List of services """)
    kind: str = Field(default="ServiceList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class ConfigMap(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    binaryData: dict = Field(default=None, description=r""" BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet. """)
    data: dict = Field(default=None, description=r""" Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. """)
    immutable: bool = Field(default=None, description=r""" Immutable, if set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. """)
    kind: str = Field(default="ConfigMap", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class ConfigMapList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ConfigMap] = Field(default=None, description=r""" Items is the list of ConfigMaps. """)
    kind: str = Field(default="ConfigMapList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class CSIDriver(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="CSIDriver", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata. metadata.Name indicates the name of the CSI driver that this object refers to; it MUST be the same name returned by the CSI GetPluginName() call for that driver. The driver name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics between. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: CSIDriverSpec = Field(default=None, description=r""" spec represents the specification of the CSI Driver. """)


class CSIDriverSpec(BaseModel):
    attachRequired: bool = Field(default=None, description=r""" attachRequired indicates this CSI volume driver requires an attach operation (because it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach controller should call the attach volume interface which checks the volumeattachment status and waits until the volume is attached before proceeding to mounting. The CSI external-attacher coordinates with CSI volume driver and updates the volumeattachment status when the attach operation is complete. If the CSIDriverRegistry feature gate is enabled and the value is specified to false, the attach operation will be skipped. Otherwise the attach operation will be called.  This field is immutable. """)
    fsGroupPolicy: str = Field(default=None, description=r""" fsGroupPolicy defines if the underlying volume supports changing ownership and permission of the volume before being mounted. Refer to the specific FSGroupPolicy values for additional details.  This field is immutable.  Defaults to ReadWriteOnceWithFSType, which will examine each volume to determine if Kubernetes should modify ownership and permissions of the volume. With the default policy the defined fsGroup will only be applied if a fstype is defined and the volume's access mode contains ReadWriteOnce. """)
    podInfoOnMount: bool = Field(default=None, description=r""" podInfoOnMount indicates this CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations, if set to true. If set to false, pod information will not be passed on mount. Default is false.  The CSI driver specifies podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and validating the information passed in as VolumeContext.  The following VolumeConext will be passed if podInfoOnMount is set to true. This list might grow, but the prefix will be used. "csi.storage.k8s.io/pod.name": pod.Name "csi.storage.k8s.io/pod.namespace": pod.Namespace "csi.storage.k8s.io/pod.uid": string(pod.UID) "csi.storage.k8s.io/ephemeral": "true" if the volume is an ephemeral inline volume                                 defined by a CSIVolumeSource, otherwise "false"  "csi.storage.k8s.io/ephemeral" is a new feature in Kubernetes 1.16. It is only required for drivers which support both the "Persistent" and "Ephemeral" VolumeLifecycleMode. Other drivers can leave pod info disabled and/or ignore this field. As Kubernetes 1.15 doesn't support this field, drivers can only support one mode when deployed on such a cluster and the deployment determines which mode that is, for example via a command line parameter of the driver.  This field is immutable. """)
    requiresRepublish: bool = Field(default=None, description=r""" requiresRepublish indicates the CSI driver wants `NodePublishVolume` being periodically called to reflect any possible change in the mounted volume. This field defaults to false.  Note: After a successful initial NodePublishVolume call, subsequent calls to NodePublishVolume should only update the contents of the volume. New mount points will not be seen by a running container. """)
    seLinuxMount: bool = Field(default=None, description=r""" seLinuxMount specifies if the CSI driver supports "-o context" mount option.  When "true", the CSI driver must ensure that all volumes provided by this CSI driver can be mounted separately with different `-o context` options. This is typical for storage backends that provide volumes as filesystems on block devices or as independent shared volumes. Kubernetes will call NodeStage / NodePublish with "-o context=xyz" mount option when mounting a ReadWriteOncePod volume used in Pod that has explicitly set SELinux context. In the future, it may be expanded to other volume AccessModes. In any case, Kubernetes will ensure that the volume is mounted only with a single SELinux context.  When "false", Kubernetes won't pass any special SELinux mount options to the driver. This is typical for volumes that represent subdirectories of a bigger shared filesystem.  Default is "false". """)
    storageCapacity: bool = Field(default=None, description=r""" storageCapacity indicates that the CSI volume driver wants pod scheduling to consider the storage capacity that the driver deployment will report by creating CSIStorageCapacity objects with capacity information, if set to true.  The check can be enabled immediately when deploying a driver. In that case, provisioning new volumes with late binding will pause until the driver deployment has published some suitable CSIStorageCapacity object.  Alternatively, the driver can be deployed with the field unset or false and it can be flipped later when storage capacity information has been published.  This field was immutable in Kubernetes <= 1.22 and now is mutable. """)
    tokenRequests: List[TokenRequest] = Field(default=None, description=r""" tokenRequests indicates the CSI driver needs pods' service account tokens it is mounting volume for to do necessary authentication. Kubelet will pass the tokens in VolumeContext in the CSI NodePublishVolume calls. The CSI driver should parse and validate the following VolumeContext: "csi.storage.k8s.io/serviceAccount.tokens": {   "<audience>": {     "token": <token>,     "expirationTimestamp": <expiration timestamp in RFC3339>,   },   ... }  Note: Audience in each TokenRequest should be different and at most one token is empty string. To receive a new token after expiry, RequiresRepublish can be used to trigger NodePublishVolume periodically. """)
    volumeLifecycleModes: List[str] = Field(default=None, description=r""" volumeLifecycleModes defines what kind of volumes this CSI volume driver supports. The default if the list is empty is "Persistent", which is the usage defined by the CSI specification and implemented in Kubernetes via the usual PV/PVC mechanism.  The other mode is "Ephemeral". In this mode, volumes are defined inline inside the pod spec with CSIVolumeSource and their lifecycle is tied to the lifecycle of that pod. A driver has to be aware of this because it is only going to get a NodePublishVolume call for such a volume.  For more information about implementing this mode, see https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html A driver can support one or more of these modes and more modes may be added in the future.  This field is beta. This field is immutable. """)


class CSIDriverList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[CSIDriver] = Field(default=None, description=r""" items is the list of CSIDriver """)
    kind: str = Field(default="CSIDriverList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class CSINode(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="CSINode", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. metadata.name must be the Kubernetes node name. """)
    spec: CSINodeSpec = Field(default=None, description=r""" spec is the specification of CSINode """)


class CSINodeSpec(BaseModel):
    drivers: List[CSINodeDriver] = Field(default=None, description=r""" drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty. """)


class CSINodeList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[CSINode] = Field(default=None, description=r""" items is the list of CSINode """)
    kind: str = Field(default="CSINodeList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class Secret(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    data: dict = Field(default=None, description=r""" Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4 """)
    immutable: bool = Field(default=None, description=r""" Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. """)
    kind: str = Field(default="Secret", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    stringData: dict = Field(default=None, description=r""" stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API. """)
    type: str = Field(default=None, description=r""" Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types """)


class SecretList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Secret] = Field(default=None, description=r""" Items is a list of secret objects. More info: https://kubernetes.io/docs/concepts/configuration/secret """)
    kind: str = Field(default="SecretList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class PersistentVolumeClaim(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="PersistentVolumeClaim", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: PersistentVolumeClaimSpec = Field(default=None, description=r""" spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
    status: PersistentVolumeClaimStatus = Field(default=None, description=r""" status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)


class PersistentVolumeClaimSpec(BaseModel):
    accessModes: List[str] = Field(default=None, description=r""" accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 """)
    dataSource: TypedLocalObjectReference = Field(default=None, description=r""" dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource. """)
    dataSourceRef: TypedObjectReference = Field(default=None, description=r""" dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef   allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef   preserves all values, and generates an error if a disallowed value is   specified. * While dataSource only allows local objects, dataSourceRef allows objects   in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled. """)
    resources: ResourceRequirements = Field(default=None, description=r""" resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources """)
    selector: LabelSelector = Field(default=None, description=r""" selector is a label query over volumes to consider for binding. """)
    storageClassName: str = Field(default=None, description=r""" storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 """)
    volumeMode: str = Field(default=None, description=r""" volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. """)
    volumeName: str = Field(default=None, description=r""" volumeName is the binding reference to the PersistentVolume backing this claim. """)


class PersistentVolumeClaimStatus(BaseModel):
    accessModes: List[str] = Field(default=None, description=r""" accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 """)
    allocatedResourceStatuses: dict = Field(default=None, description=r""" allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either: 	* Un-prefixed keys: 		- storage - the capacity of the volume. 	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states: 	- ControllerResizeInProgress: 		State set when resize controller starts resizing the volume in control-plane. 	- ControllerResizeFailed: 		State set when resize has failed in resize controller with a terminal error. 	- NodeResizePending: 		State set when resize controller has finished resizing the volume but further resizing of 		volume is needed on the node. 	- NodeResizeInProgress: 		State set when kubelet starts resizing the volume. 	- NodeResizeFailed: 		State set when resizing has failed in kubelet with a terminal error. Transient errors don't set 		NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states: 	- pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress"      - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed"      - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending"      - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress"      - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature. """)
    allocatedResources: dict = Field(default=None, description=r""" allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either: 	* Un-prefixed keys: 		- storage - the capacity of the volume. 	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature. """)
    capacity: dict = Field(default=None, description=r""" capacity represents the actual resources of the underlying volume. """)
    conditions: List[PersistentVolumeClaimCondition] = Field(default=None, description=r""" conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'. """)
    phase: str = Field(default=None, description=r""" phase represents the current phase of PersistentVolumeClaim. """)


class PersistentVolumeClaimList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PersistentVolumeClaim] = Field(default=None, description=r""" items is a list of persistent volume claims. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
    kind: str = Field(default="PersistentVolumeClaimList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class StorageClass(KubeModel):
    allowVolumeExpansion: bool = Field(default=None, description=r""" allowVolumeExpansion shows whether the storage class allow volume expand. """)
    allowedTopologies: List[TopologySelectorTerm] = Field(default=None, description=r""" allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature. """)
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="StorageClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    mountOptions: List[str] = Field(default=None, description=r""" mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid. """)
    parameters: dict = Field(default=None, description=r""" parameters holds the parameters for the provisioner that should create volumes of this storage class. """)
    provisioner: str = Field(default=None, description=r""" provisioner indicates the type of the provisioner. """)
    reclaimPolicy: str = Field(default=None, description=r""" reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete. """)
    volumeBindingMode: str = Field(default=None, description=r""" volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature. """)


class StorageClassList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[StorageClass] = Field(default=None, description=r""" items is the list of StorageClasses """)
    kind: str = Field(default="StorageClassList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class CSIStorageCapacity(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    capacity: Quantity = Field(default=None, description=r""" capacity is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  The semantic is currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be used to provision volumes. If not set, that information is currently unavailable. """)
    kind: str = Field(default="CSIStorageCapacity", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    maximumVolumeSize: Quantity = Field(default=None, description=r""" maximumVolumeSize is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  This is defined since CSI spec 1.4.0 as the largest size that may be used in a CreateVolumeRequest.capacity_range.required_bytes field to create a volume with the same parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is ResourceRequirements.Requests in a volume claim. """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. The name has no particular meaning. It must be a DNS subdomain (dots allowed, 253 characters). To ensure that there are no conflicts with other CSI drivers on the cluster, the recommendation is to use csisc-<uuid>, a generated name, or a reverse-domain name which ends with the unique CSI driver name.  Objects are namespaced.  More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    nodeTopology: LabelSelector = Field(default=None, description=r""" nodeTopology defines which nodes have access to the storage for which capacity was reported. If not set, the storage is not accessible from any node in the cluster. If empty, the storage is accessible from all nodes. This field is immutable. """)
    storageClassName: str = Field(default=None, description=r""" storageClassName represents the name of the StorageClass that the reported capacity applies to. It must meet the same requirements as the name of a StorageClass object (non-empty, DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and should be removed by its creator. This field is immutable. """)


class CSIStorageCapacityList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[CSIStorageCapacity] = Field(default=None, description=r""" items is the list of CSIStorageCapacity objects. """)
    kind: str = Field(default="CSIStorageCapacityList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class Volume(BaseModel):
    awsElasticBlockStore: AWSElasticBlockStoreVolumeSource = Field(default=None, description=r""" awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)
    azureDisk: AzureDiskVolumeSource = Field(default=None, description=r""" azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. """)
    azureFile: AzureFileVolumeSource = Field(default=None, description=r""" azureFile represents an Azure File Service mount on the host and bind mount to the pod. """)
    cephfs: CephFSVolumeSource = Field(default=None, description=r""" cephFS represents a Ceph FS mount on the host that shares a pod's lifetime """)
    cinder: CinderVolumeSource = Field(default=None, description=r""" cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
    configMap: ConfigMapVolumeSource = Field(default=None, description=r""" configMap represents a configMap that should populate this volume """)
    csi: CSIVolumeSource = Field(default=None, description=r""" csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers (Beta feature). """)
    downwardAPI: DownwardAPIVolumeSource = Field(default=None, description=r""" downwardAPI represents downward API about the pod that should populate this volume """)
    emptyDir: EmptyDirVolumeSource = Field(default=None, description=r""" emptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """)
    ephemeral: EphemeralVolumeSource = Field(default=None, description=r""" ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.  Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity    tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through    a PersistentVolumeClaim (see EphemeralVolumeSource for more    information on the connection between this volume type    and PersistentVolumeClaim).  Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.  Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.  A pod can use both types of ephemeral volumes and persistent volumes at the same time. """)
    fc: FCVolumeSource = Field(default=None, description=r""" fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod. """)
    flexVolume: FlexVolumeSource = Field(default=None, description=r""" flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. """)
    flocker: FlockerVolumeSource = Field(default=None, description=r""" flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running """)
    gcePersistentDisk: GCEPersistentDiskVolumeSource = Field(default=None, description=r""" gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
    gitRepo: GitRepoVolumeSource = Field(default=None, description=r""" gitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container. """)
    glusterfs: GlusterfsVolumeSource = Field(default=None, description=r""" glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md """)
    hostPath: HostPathVolumeSource = Field(default=None, description=r""" hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)
    iscsi: ISCSIVolumeSource = Field(default=None, description=r""" iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md """)
    name: str = Field(default=None, description=r""" name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    nfs: NFSVolumeSource = Field(default=None, description=r""" nfs represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
    persistentVolumeClaim: PersistentVolumeClaimVolumeSource = Field(default=None, description=r""" persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
    photonPersistentDisk: PhotonPersistentDiskVolumeSource = Field(default=None, description=r""" photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine """)
    portworxVolume: PortworxVolumeSource = Field(default=None, description=r""" portworxVolume represents a portworx volume attached and mounted on kubelets host machine """)
    projected: ProjectedVolumeSource = Field(default=None, description=r""" projected items for all in one resources secrets, configmaps, and downward API """)
    quobyte: QuobyteVolumeSource = Field(default=None, description=r""" quobyte represents a Quobyte mount on the host that shares a pod's lifetime """)
    rbd: RBDVolumeSource = Field(default=None, description=r""" rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md """)
    scaleIO: ScaleIOVolumeSource = Field(default=None, description=r""" scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. """)
    secret: SecretVolumeSource = Field(default=None, description=r""" secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret """)
    storageos: StorageOSVolumeSource = Field(default=None, description=r""" storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. """)
    vsphereVolume: VsphereVirtualDiskVolumeSource = Field(default=None, description=r""" vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine """)


class VolumeAttachment(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="VolumeAttachment", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: VolumeAttachmentSpec = Field(default=None, description=r""" spec represents specification of the desired attach/detach volume behavior. Populated by the Kubernetes system. """)
    status: VolumeAttachmentStatus = Field(default=None, description=r""" status represents status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher. """)


class VolumeAttachmentSpec(BaseModel):
    attacher: str = Field(default=None, description=r""" attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName(). """)
    nodeName: str = Field(default=None, description=r""" nodeName represents the node that the volume should be attached to. """)
    source: VolumeAttachmentSource = Field(default=None, description=r""" source represents the volume that should be attached. """)


class VolumeAttachmentStatus(BaseModel):
    attachError: VolumeError = Field(default=None, description=r""" attachError represents the last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. """)
    attached: bool = Field(default=None, description=r""" attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. """)
    attachmentMetadata: dict = Field(default=None, description=r""" attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. """)
    detachError: VolumeError = Field(default=None, description=r""" detachError represents the last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher. """)


class VolumeAttachmentList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[VolumeAttachment] = Field(default=None, description=r""" items is the list of VolumeAttachments """)
    kind: str = Field(default="VolumeAttachmentList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class ClusterTrustBundle(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ClusterTrustBundle", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" metadata contains the object metadata. """)
    spec: ClusterTrustBundleSpec = Field(default=None, description=r""" spec contains the signer (if any) and trust anchors. """)


class ClusterTrustBundleSpec(BaseModel):
    signerName: str = Field(default=None, description=r""" signerName indicates the associated signer, if any.  In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.  If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`, valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.  If signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.  List/watch requests for ClusterTrustBundles can filter on this field using a `spec.signerName=NAME` field selector. """)
    trustBundle: str = Field(default=None, description=r""" trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.  The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.  Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data. """)


class ClusterTrustBundleList(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ClusterTrustBundle] = Field(default=None, description=r""" items is a collection of ClusterTrustBundle objects """)
    kind: str = Field(default="ClusterTrustBundleList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" metadata contains the list metadata. """)


class ControllerRevision(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    data: Any = Field(default=None, description=r""" Data is the serialized representation of the state. """)
    kind: str = Field(default="ControllerRevision", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    revision: int = Field(default=None, description=r""" Revision indicates the revision of the state represented by Data. """)


class ControllerRevisionList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ControllerRevision] = Field(default=None, description=r""" Items is the list of ControllerRevisions """)
    kind: str = Field(default="ControllerRevisionList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class CustomResourceDefinition(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="CustomResourceDefinition", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: CustomResourceDefinitionSpec = Field(default=None, description=r""" spec describes how the user wants the resources to appear """)
    status: CustomResourceDefinitionStatus = Field(default=None, description=r""" status indicates the actual state of the CustomResourceDefinition """)


class CustomResourceDefinitionSpec(KubeModel):
    conversion: CustomResourceConversion = Field(default=None, description=r""" conversion defines conversion settings for the CRD. """)
    group: str = Field(default=None, description=r""" group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). """)
    names: CustomResourceDefinitionNames = Field(default=None, description=r""" names specify the resource and kind names for the custom resource. """)
    preserveUnknownFields: bool = Field(default=None, description=r""" preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. This field is deprecated in favor of setting `x-preserve-unknown-fields` to true in `spec.versions[*].schema.openAPIV3Schema`. See https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#field-pruning for details. """)
    scope: str = Field(default=None, description=r""" scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`. """)
    versions: List[CustomResourceDefinitionVersion] = Field(default=None, description=r""" versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10. """)


class CustomResourceDefinitionStatus(BaseModel):
    acceptedNames: CustomResourceDefinitionNames = Field(default=None, description=r""" acceptedNames are the names that are actually being used to serve discovery. They may be different than the names in spec. """)
    conditions: List[CustomResourceDefinitionCondition] = Field(default=None, description=r""" conditions indicate state for particular aspects of a CustomResourceDefinition """)
    storedVersions: List[str] = Field(default=None, description=r""" storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list. """)


class CustomResourceDefinitionList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[CustomResourceDefinition] = Field(default=None, description=r""" items list individual CustomResourceDefinition objects """)
    kind: str = Field(default="CustomResourceDefinitionList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class Event(KubeModel):
    action: str = Field(default=None, description=r""" action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters. """)
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    deprecatedCount: int = Field(default=None, description=r""" deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type. """)
    deprecatedFirstTimestamp: Time = Field(default=None, description=r""" deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. """)
    deprecatedLastTimestamp: Time = Field(default=None, description=r""" deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. """)
    deprecatedSource: EventSource = Field(default=None, description=r""" deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type. """)
    eventTime: MicroTime = Field(default=None, description=r""" eventTime is the time when this Event was first observed. It is required. """)
    kind: str = Field(default="Event", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    note: str = Field(default=None, description=r""" note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB. """)
    reason: str = Field(default=None, description=r""" reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters. """)
    regarding: ObjectReference = Field(default=None, description=r""" regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object. """)
    related: ObjectReference = Field(default=None, description=r""" related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object. """)
    reportingController: str = Field(default=None, description=r""" reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events. """)
    reportingInstance: str = Field(default=None, description=r""" reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters. """)
    series: EventSeries = Field(default=None, description=r""" series is data about the Event series this event represents or nil if it's a singleton Event. """)
    type: str = Field(default=None, description=r""" type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events. """)


class EventList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Event] = Field(default=None, description=r""" items is a list of schema objects. """)
    kind: str = Field(default="EventList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class LimitRange(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="LimitRange", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: LimitRangeSpec = Field(default=None, description=r""" Spec defines the limits enforced. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class LimitRangeSpec(BaseModel):
    limits: List[LimitRangeItem] = Field(default=None, description=r""" Limits is the list of LimitRangeItem objects that are enforced. """)


class LimitRangeList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[LimitRange] = Field(default=None, description=r""" Items is a list of LimitRange objects. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """)
    kind: str = Field(default="LimitRangeList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class HorizontalPodAutoscaler(KubeModel):
    apiVersion: str = Field(default="v2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="HorizontalPodAutoscaler", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: HorizontalPodAutoscalerSpec = Field(default=None, description=r""" spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. """)
    status: HorizontalPodAutoscalerStatus = Field(default=None, description=r""" status is the current information about the autoscaler. """)


class HorizontalPodAutoscalerSpec(BaseModel):
    behavior: HorizontalPodAutoscalerBehavior = Field(default=None, description=r""" behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default HPAScalingRules for scale up and scale down are used. """)
    maxReplicas: int = Field(default=None, description=r""" maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas. """)
    metrics: List[MetricSpec] = Field(default=None, description=r""" metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization. """)
    minReplicas: int = Field(default=None, description=r""" minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available. """)
    scaleTargetRef: CrossVersionObjectReference = Field(default=None, description=r""" scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count. """)


class HorizontalPodAutoscalerStatus(BaseModel):
    conditions: List[HorizontalPodAutoscalerCondition] = Field(default=None, description=r""" conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met. """)
    currentMetrics: List[MetricStatus] = Field(default=None, description=r""" currentMetrics is the last read state of the metrics used by this autoscaler. """)
    currentReplicas: int = Field(default=None, description=r""" currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler. """)
    desiredReplicas: int = Field(default=None, description=r""" desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler. """)
    lastScaleTime: Time = Field(default=None, description=r""" lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed. """)
    observedGeneration: int = Field(default=None, description=r""" observedGeneration is the most recent generation observed by this autoscaler. """)


class HorizontalPodAutoscalerList(KubeModel):
    apiVersion: str = Field(default="v2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[HorizontalPodAutoscaler] = Field(default=None, description=r""" items is the list of horizontal pod autoscaler objects. """)
    kind: str = Field(default="HorizontalPodAutoscalerList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" metadata is the standard list metadata. """)


class MutatingWebhookConfiguration(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="MutatingWebhookConfiguration", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """)
    webhooks: List[MutatingWebhook] = Field(default=None, description=r""" Webhooks is a list of webhooks and the affected resources and operations. """)


class MutatingWebhookConfigurationList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[MutatingWebhookConfiguration] = Field(default=None, description=r""" List of MutatingWebhookConfiguration. """)
    kind: str = Field(default="MutatingWebhookConfigurationList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class ValidatingWebhookConfiguration(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ValidatingWebhookConfiguration", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """)
    webhooks: List[ValidatingWebhook] = Field(default=None, description=r""" Webhooks is a list of webhooks and the affected resources and operations. """)


class ValidatingWebhookConfigurationList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ValidatingWebhookConfiguration] = Field(default=None, description=r""" List of ValidatingWebhookConfiguration. """)
    kind: str = Field(default="ValidatingWebhookConfigurationList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class PodSchedulingContext(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="PodSchedulingContext", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata """)
    spec: PodSchedulingContextSpec = Field(default=None, description=r""" Spec describes where resources for the Pod are needed. """)
    status: PodSchedulingContextStatus = Field(default=None, description=r""" Status describes where resources for the Pod can be allocated. """)


class PodSchedulingContextSpec(BaseModel):
    potentialNodes: List[str] = Field(default=None, description=r""" PotentialNodes lists nodes where the Pod might be able to run.  The size of this field is limited to 128. This is large enough for many clusters. Larger clusters may need more attempts to find a node that suits all pending resources. This may get increased in the future, but not reduced. """)
    selectedNode: str = Field(default=None, description=r""" SelectedNode is the node for which allocation of ResourceClaims that are referenced by the Pod and that use "WaitForFirstConsumer" allocation is to be attempted. """)


class PodSchedulingContextStatus(BaseModel):
    resourceClaims: List[ResourceClaimSchedulingStatus] = Field(default=None, description=r""" ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses "WaitForFirstConsumer" allocation mode. """)


class PodSchedulingContextList(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PodSchedulingContext] = Field(default=None, description=r""" Items is the list of PodSchedulingContext objects. """)
    kind: str = Field(default="PodSchedulingContextList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)


class PodTemplate(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="PodTemplate", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    template: PodTemplateSpec = Field(default=None, description=r""" Template defines the pods that will be created from this pod template. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class PodTemplateSpec(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: PodSpec = Field(default=None, description=r""" Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class PodTemplateList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PodTemplate] = Field(default=None, description=r""" List of pod templates """)
    kind: str = Field(default="PodTemplateList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class PodDisruptionBudget(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="PodDisruptionBudget", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: PodDisruptionBudgetSpec = Field(default=None, description=r""" Specification of the desired behavior of the PodDisruptionBudget. """)
    status: PodDisruptionBudgetStatus = Field(default=None, description=r""" Most recently observed status of the PodDisruptionBudget. """)


class PodDisruptionBudgetSpec(BaseModel):
    maxUnavailable: Any = Field(default=None, description=r""" An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable". """)
    minAvailable: Any = Field(default=None, description=r""" An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%". """)
    selector: LabelSelector = Field(default=None, description=r""" Label query over pods whose evictions are managed by the disruption budget. A null selector will match no pods, while an empty ({}) selector will select all pods within the namespace. """)
    unhealthyPodEvictionPolicy: str = Field(default=None, description=r""" UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods should be considered for eviction. Current implementation considers healthy pods, as pods that have status.conditions item with type="Ready",status="True".  Valid policies are IfHealthyBudget and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds to the IfHealthyBudget policy.  IfHealthyBudget policy means that running pods (status.phase="Running"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction.  AlwaysAllow policy means that all running pods (status.phase="Running"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction.  Additional policies may be added in the future. Clients making eviction decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in this field.  This field is beta-level. The eviction API uses this field when the feature gate PDBUnhealthyPodEvictionPolicy is enabled (enabled by default). """)


class PodDisruptionBudgetStatus(BaseModel):
    conditions: List[Condition] = Field(default=None, description=r""" Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn't able to compute               the number of allowed disruptions. Therefore no disruptions are               allowed and the status of the condition will be False. - InsufficientPods: The number of pods are either at or below the number                     required by the PodDisruptionBudget. No disruptions are                     allowed and the status of the condition will be False. - SufficientPods: There are more pods than required by the PodDisruptionBudget.                   The condition will be True, and the number of allowed                   disruptions are provided by the disruptionsAllowed property. """)
    currentHealthy: int = Field(default=None, description=r""" current number of healthy pods """)
    desiredHealthy: int = Field(default=None, description=r""" minimum desired number of healthy pods """)
    disruptedPods: dict = Field(default=None, description=r""" DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions. """)
    disruptionsAllowed: int = Field(default=None, description=r""" Number of pod disruptions that are currently allowed. """)
    expectedPods: int = Field(default=None, description=r""" total number of pods counted by this disruption budget """)
    observedGeneration: int = Field(default=None, description=r""" Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation. """)


class PodDisruptionBudgetList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PodDisruptionBudget] = Field(default=None, description=r""" Items is a list of PodDisruptionBudgets """)
    kind: str = Field(default="PodDisruptionBudgetList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class PriorityClass(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    description: str = Field(default=None, description=r""" description is an arbitrary string that usually provides guidelines on when this priority class should be used. """)
    globalDefault: bool = Field(default=None, description=r""" globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority. """)
    kind: str = Field(default="PriorityClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    preemptionPolicy: str = Field(default=None, description=r""" preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. """)
    value: int = Field(default=None, description=r""" value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec. """)


class PriorityClassList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PriorityClass] = Field(default=None, description=r""" items is the list of PriorityClasses """)
    kind: str = Field(default="PriorityClassList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class ResourceClaim(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ResourceClaim", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata """)
    spec: ResourceClaimSpec = Field(default=None, description=r""" Spec describes the desired attributes of a resource that then needs to be allocated. It can only be set once when creating the ResourceClaim. """)
    status: ResourceClaimStatus = Field(default=None, description=r""" Status describes whether the resource is available and with which attributes. """)


class ResourceClaimSpec(BaseModel):
    allocationMode: str = Field(default=None, description=r""" Allocation can start immediately or when a Pod wants to use the resource. "WaitForFirstConsumer" is the default. """)
    parametersRef: ResourceClaimParametersReference = Field(default=None, description=r""" ParametersRef references a separate object with arbitrary parameters that will be used by the driver when allocating a resource for the claim.  The object must be in the same namespace as the ResourceClaim. """)
    resourceClassName: str = Field(default=None, description=r""" ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment. """)


class ResourceClaimStatus(BaseModel):
    allocation: AllocationResult = Field(default=None, description=r""" Allocation is set by the resource driver once a resource or set of resources has been allocated successfully. If this is not specified, the resources have not been allocated yet. """)
    deallocationRequested: bool = Field(default=None, description=r""" DeallocationRequested indicates that a ResourceClaim is to be deallocated.  The driver then must deallocate this claim and reset the field together with clearing the Allocation field.  While DeallocationRequested is set, no new consumers may be added to ReservedFor. """)
    driverName: str = Field(default=None, description=r""" DriverName is a copy of the driver name from the ResourceClass at the time when allocation started. """)
    reservedFor: List[ResourceClaimConsumerReference] = Field(default=None, description=r""" ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started.  There can be at most 32 such reservations. This may get increased in the future, but not reduced. """)


class ResourceClaimList(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ResourceClaim] = Field(default=None, description=r""" Items is the list of resource claims. """)
    kind: str = Field(default="ResourceClaimList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)


class ResourceClaimTemplate(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ResourceClaimTemplate", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata """)
    spec: ResourceClaimTemplateSpec = Field(default=None, description=r""" Describes the ResourceClaim that is to be generated.  This field is immutable. A ResourceClaim will get created by the control plane for a Pod when needed and then not get updated anymore. """)


class ResourceClaimTemplateSpec(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" ObjectMeta may contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """)
    spec: ResourceClaimSpec = Field(default=None, description=r""" Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that gets created from this template. The same fields as in a ResourceClaim are also valid here. """)


class ResourceClaimTemplateList(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ResourceClaimTemplate] = Field(default=None, description=r""" Items is the list of resource claim templates. """)
    kind: str = Field(default="ResourceClaimTemplateList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)


class ResourceClass(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    driverName: str = Field(default=None, description=r""" DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.  Resource drivers have a unique name in forward domain order (acme.example.com). """)
    kind: str = Field(default="ResourceClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata """)
    parametersRef: ResourceClassParametersReference = Field(default=None, description=r""" ParametersRef references an arbitrary separate object that may hold parameters that will be used by the driver when allocating a resource that uses this class. A dynamic resource driver can distinguish between parameters stored here and and those stored in ResourceClaimSpec. """)
    suitableNodes: NodeSelector = Field(default=None, description=r""" Only nodes matching the selector will be considered by the scheduler when trying to find a Node that fits a Pod when that Pod uses a ResourceClaim that has not been allocated yet.  Setting this field is optional. If null, all nodes are candidates. """)


class ResourceClassList(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ResourceClass] = Field(default=None, description=r""" Items is the list of resource classes. """)
    kind: str = Field(default="ResourceClassList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)


class ValidatingAdmissionPolicy(KubeModel):
    apiVersion: str = Field(default="v1beta1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ValidatingAdmissionPolicy", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """)
    spec: ValidatingAdmissionPolicySpec = Field(default=None, description=r""" Specification of the desired behavior of the ValidatingAdmissionPolicy. """)
    status: ValidatingAdmissionPolicyStatus = Field(default=None, description=r""" The status of the ValidatingAdmissionPolicy, including warnings that are useful to determine if the policy behaves in the expected way. Populated by the system. Read-only. """)


class ValidatingAdmissionPolicySpec(BaseModel):
    auditAnnotations: List[AuditAnnotation] = Field(default=None, description=r""" auditAnnotations contains CEL expressions which are used to produce audit annotations for the audit event of the API request. validations and auditAnnotations may not both be empty; a least one of validations or auditAnnotations is required. """)
    failurePolicy: str = Field(default=None, description=r""" failurePolicy defines how to handle failures for the admission policy. Failures can occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-configured policy definitions or bindings.  A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource.  failurePolicy does not define how validations that evaluate to false are handled.  When failurePolicy is set to Fail, ValidatingAdmissionPolicyBinding validationActions define how failures are enforced.  Allowed values are Ignore or Fail. Defaults to Fail. """)
    matchConditions: List[MatchCondition] = Field(default=None, description=r""" MatchConditions is a list of conditions that must be met for a request to be validated. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  If a parameter object is provided, it can be accessed via the `params` handle in the same manner as validation expressions.  The exact matching logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the policy is skipped.   2. If ALL matchConditions evaluate to TRUE, the policy is evaluated.   3. If any matchCondition evaluates to an error (but none are FALSE):      - If failurePolicy=Fail, reject the request      - If failurePolicy=Ignore, the policy is skipped """)
    matchConstraints: MatchResources = Field(default=None, description=r""" MatchConstraints specifies what resources this policy is designed to validate. The AdmissionPolicy cares about a request if it matches _all_ Constraints. However, in order to prevent clusters from being put into an unstable state that cannot be recovered from via the API ValidatingAdmissionPolicy cannot match ValidatingAdmissionPolicy and ValidatingAdmissionPolicyBinding. Required. """)
    paramKind: ParamKind = Field(default=None, description=r""" ParamKind specifies the kind of resources used to parameterize this policy. If absent, there are no parameters for this policy and the param CEL variable will not be provided to validation expressions. If ParamKind refers to a non-existent kind, this policy definition is mis-configured and the FailurePolicy is applied. If paramKind is specified but paramRef is unset in ValidatingAdmissionPolicyBinding, the params variable will be null. """)
    validations: List[Validation] = Field(default=None, description=r""" Validations contain CEL expressions which is used to apply the validation. Validations and AuditAnnotations may not both be empty; a minimum of one Validations or AuditAnnotations is required. """)
    variables: List[Variable] = Field(default=None, description=r""" Variables contain definitions of variables that can be used in composition of other expressions. Each variable is defined as a named CEL expression. The variables defined here will be available under `variables` in other expressions of the policy except MatchConditions because MatchConditions are evaluated before the rest of the policy.  The expression of a variable can refer to other variables defined earlier in the list but not those after. Thus, Variables must be sorted by the order of first appearance and acyclic. """)


class ValidatingAdmissionPolicyStatus(BaseModel):
    conditions: List[Condition] = Field(default=None, description=r""" The conditions represent the latest available observations of a policy's current state. """)
    observedGeneration: int = Field(default=None, description=r""" The generation observed by the controller. """)
    typeChecking: TypeChecking = Field(default=None, description=r""" The results of type checking for each expression. Presence of this field indicates the completion of the type checking. """)


class ValidatingAdmissionPolicyList(KubeModel):
    apiVersion: str = Field(default="v1beta1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ValidatingAdmissionPolicy] = Field(default=None, description=r""" List of ValidatingAdmissionPolicy. """)
    kind: str = Field(default="ValidatingAdmissionPolicyList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class ValidatingAdmissionPolicyBinding(KubeModel):
    apiVersion: str = Field(default="v1beta1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ValidatingAdmissionPolicyBinding", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """)
    spec: ValidatingAdmissionPolicyBindingSpec = Field(default=None, description=r""" Specification of the desired behavior of the ValidatingAdmissionPolicyBinding. """)


class ValidatingAdmissionPolicyBindingSpec(BaseModel):
    matchResources: MatchResources = Field(default=None, description=r""" MatchResources declares what resources match this binding and will be validated by it. Note that this is intersected with the policy's matchConstraints, so only requests that are matched by the policy can be selected by this. If this is unset, all resources matched by the policy are validated by this binding When resourceRules is unset, it does not constrain resource matching. If a resource is matched by the other fields of this object, it will be validated. Note that this is differs from ValidatingAdmissionPolicy matchConstraints, where resourceRules are required. """)
    paramRef: ParamRef = Field(default=None, description=r""" paramRef specifies the parameter resource used to configure the admission control policy. It should point to a resource of the type specified in ParamKind of the bound ValidatingAdmissionPolicy. If the policy specifies a ParamKind and the resource referred to by ParamRef does not exist, this binding is considered mis-configured and the FailurePolicy of the ValidatingAdmissionPolicy applied. If the policy does not specify a ParamKind then this field is ignored, and the rules are evaluated without a param. """)
    policyName: str = Field(default=None, description=r""" PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required. """)
    validationActions: List[str] = Field(default=None, description=r""" validationActions declares how Validations of the referenced ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced according to these actions.  Failures defined by the ValidatingAdmissionPolicy's FailurePolicy are enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the failures are ignored. This includes compilation errors, runtime errors and misconfigurations of the policy.  validationActions is declared as a set of action values. Order does not matter. validationActions may not contain duplicates of the same action.  The supported actions values are:  "Deny" specifies that a validation failure results in a denied request.  "Warn" specifies that a validation failure is reported to the request client in HTTP Warning headers, with a warning code of 299. Warnings can be sent both for allowed or denied admission responses.  "Audit" specifies that a validation failure is included in the published audit event for the request. The audit event will contain a `validation.policy.admission.k8s.io/validation_failure` audit annotation with a value containing the details of the validation failures, formatted as a JSON list of objects, each with the following fields: - message: The validation failure message string - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation failure Example audit annotation: `"validation.policy.admission.k8s.io/validation_failure": "[{"message": "Invalid value", {"policy": "policy.example.com", {"binding": "policybinding.example.com", {"expressionIndex": "1", {"validationActions": ["Audit"]}]"`  Clients should expect to handle additional values by ignoring any values not recognized.  "Deny" and "Warn" may not be used together since this combination needlessly duplicates the validation failure both in the API response body and the HTTP warning headers.  Required. """)


class ValidatingAdmissionPolicyBindingList(KubeModel):
    apiVersion: str = Field(default="v1beta1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ValidatingAdmissionPolicyBinding] = Field(default=None, description=r""" List of PolicyBinding. """)
    kind: str = Field(default="ValidatingAdmissionPolicyBindingList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class APIService(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="APIService", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: APIServiceSpec = Field(default=None, description=r""" Spec contains information for locating and communicating with a server """)
    status: APIServiceStatus = Field(default=None, description=r""" Status contains derived information about an API server """)


class APIServiceSpec(BaseModel):
    caBundle: str = Field(default=None, description=r""" CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate. If unspecified, system trust roots on the apiserver are used. """)
    group: str = Field(default=None, description=r""" Group is the API group name this server hosts """)
    groupPriorityMinimum: int = Field(default=None, description=r""" GroupPriorityMininum is the priority this group should have at least. Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s """)
    insecureSkipTLSVerify: bool = Field(default=None, description=r""" InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged.  You should use the CABundle instead. """)
    service: ServiceReference = Field(default=None, description=r""" Service is a reference to the service for this API server.  It must communicate on port 443. If the Service is nil, that means the handling for the API groupversion is handled locally on this server. The call will simply delegate to the normal handler chain to be fulfilled. """)
    version: str = Field(default=None, description=r""" Version is the API version this server hosts.  For example, "v1" """)
    versionPriority: int = Field(default=None, description=r""" VersionPriority controls the ordering of this API version inside of its group.  Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10. """)


class APIServiceStatus(BaseModel):
    conditions: List[APIServiceCondition] = Field(default=None, description=r""" Current service state of apiService. """)


class APIServiceList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[APIService] = Field(default=None, description=r""" Items is the list of APIService """)
    kind: str = Field(default="APIServiceList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class Binding(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Binding", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    target: ObjectReference = Field(default=None, description=r""" The target object that you want to bind to the standard object. """)


class CertificateSigningRequest(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="CertificateSigningRequest", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None)
    spec: CertificateSigningRequestSpec = Field(default=None, description=r""" spec contains the certificate request, and is immutable after creation. Only the request, signerName, expirationSeconds, and usages fields can be set on creation. Other fields are derived by Kubernetes and cannot be modified by users. """)
    status: CertificateSigningRequestStatus = Field(default=None, description=r""" status contains information about whether the request is approved or denied, and the certificate issued by the signer, or the failure condition indicating signer failure. """)


class CertificateSigningRequestSpec(BaseModel):
    expirationSeconds: int = Field(default=None, description=r""" expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.  The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.  Certificate signers may not honor this field for various reasons:    1. Old signer that is unaware of the field (such as the in-tree      implementations prior to v1.22)   2. Signer whose configured maximum is shorter than the requested duration   3. Signer whose configured minimum is longer than the requested duration  The minimum valid value for expirationSeconds is 600, i.e. 10 minutes. """)
    extra: dict = Field(default=None, description=r""" extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. """)
    groups: List[str] = Field(default=None, description=r""" groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. """)
    request: str = Field(default=None, description=r""" request contains an x509 certificate signing request encoded in a "CERTIFICATE REQUEST" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded. """)
    signerName: str = Field(default=None, description=r""" signerName indicates the requested signer, and is a qualified name.  List/watch requests for CertificateSigningRequests can filter on this field using a "spec.signerName=NAME" fieldSelector.  Well-known Kubernetes signers are:  1. "kubernetes.io/kube-apiserver-client": issues client certificates that can be used to authenticate to kube-apiserver.   Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the "csrsigning" controller in kube-controller-manager.  2. "kubernetes.io/kube-apiserver-client-kubelet": issues client certificates that kubelets use to authenticate to kube-apiserver.   Requests for this signer can be auto-approved by the "csrapproving" controller in kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.  3. "kubernetes.io/kubelet-serving" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely.   Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.  More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers  Custom signerNames can also be specified. The signer defines:  1. Trust distribution: how trust (CA bundles) are distributed.  2. Permitted subjects: and behavior when a disallowed subject is requested.  3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested.  4. Required, permitted, or forbidden key usages / extended key usages.  5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin.  6. Whether or not requests for CA certificates are allowed. """)
    uid: str = Field(default=None, description=r""" uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. """)
    usages: List[str] = Field(default=None, description=r""" usages specifies a set of key usages requested in the issued certificate.  Requests for TLS client certificates typically request: "digital signature", "key encipherment", "client auth".  Requests for TLS serving certificates typically request: "key encipherment", "digital signature", "server auth".  Valid values are:  "signing", "digital signature", "content commitment",  "key encipherment", "key agreement", "data encipherment",  "cert sign", "crl sign", "encipher only", "decipher only", "any",  "server auth", "client auth",  "code signing", "email protection", "s/mime",  "ipsec end system", "ipsec tunnel", "ipsec user",  "timestamping", "ocsp signing", "microsoft sgc", "netscape sgc" """)
    username: str = Field(default=None, description=r""" username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. """)


class CertificateSigningRequestStatus(BaseModel):
    certificate: str = Field(default=None, description=r""" certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.  If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.  Validation requirements:  1. certificate must contain one or more PEM blocks.  2. All PEM blocks must have the "CERTIFICATE" label, contain no headers, and the encoded data   must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280.  3. Non-PEM content may appear before or after the "CERTIFICATE" PEM blocks and is unvalidated,   to allow for explanatory text as described in section 5.2 of RFC7468.  If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.  The certificate is encoded in PEM format.  When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:      base64(     -----BEGIN CERTIFICATE-----     ...     -----END CERTIFICATE-----     ) """)
    conditions: List[CertificateSigningRequestCondition] = Field(default=None, description=r""" conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed". """)


class CertificateSigningRequestList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[CertificateSigningRequest] = Field(default=None, description=r""" items is a collection of CertificateSigningRequest objects """)
    kind: str = Field(default="CertificateSigningRequestList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None)


class ClusterRole(KubeModel):
    aggregationRule: AggregationRule = Field(default=None, description=r""" AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller. """)
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ClusterRole", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. """)
    rules: List[PolicyRule] = Field(default=None, description=r""" Rules holds all the PolicyRules for this ClusterRole """)


class ClusterRoleList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ClusterRole] = Field(default=None, description=r""" Items is a list of ClusterRoles """)
    kind: str = Field(default="ClusterRoleList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. """)


class ClusterRoleBinding(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ClusterRoleBinding", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. """)
    roleRef: RoleRef = Field(default=None, description=r""" RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. This field is immutable. """)
    subjects: List[Subject] = Field(default=None, description=r""" Subjects holds references to the objects the role applies to. """)


class ClusterRoleBindingList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ClusterRoleBinding] = Field(default=None, description=r""" Items is a list of ClusterRoleBindings """)
    kind: str = Field(default="ClusterRoleBindingList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. """)


class ComponentStatus(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    conditions: List[ComponentCondition] = Field(default=None, description=r""" List of component conditions observed """)
    kind: str = Field(default="ComponentStatus", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class ComponentStatusList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ComponentStatus] = Field(default=None, description=r""" List of ComponentStatus objects. """)
    kind: str = Field(default="ComponentStatusList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class FlowSchema(KubeModel):
    apiVersion: str = Field(default="v1beta3", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="FlowSchema", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: FlowSchemaSpec = Field(default=None, description=r""" `spec` is the specification of the desired behavior of a FlowSchema. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: FlowSchemaStatus = Field(default=None, description=r""" `status` is the current status of a FlowSchema. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class FlowSchemaSpec(BaseModel):
    distinguisherMethod: FlowDistinguisherMethod = Field(default=None, description=r""" `distinguisherMethod` defines how to compute the flow distinguisher for requests that match this schema. `nil` specifies that the distinguisher is disabled and thus will always be the empty string. """)
    matchingPrecedence: int = Field(default=None, description=r""" `matchingPrecedence` is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. """)
    priorityLevelConfiguration: PriorityLevelConfigurationReference = Field(default=None, description=r""" `priorityLevelConfiguration` should reference a PriorityLevelConfiguration in the cluster. If the reference cannot be resolved, the FlowSchema will be ignored and marked as invalid in its status. Required. """)
    rules: List[PolicyRulesWithSubjects] = Field(default=None, description=r""" `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. """)


class FlowSchemaStatus(BaseModel):
    conditions: List[FlowSchemaCondition] = Field(default=None, description=r""" `conditions` is a list of the current states of FlowSchema. """)


class FlowSchemaList(KubeModel):
    apiVersion: str = Field(default="v1beta3", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[FlowSchema] = Field(default=None, description=r""" `items` is a list of FlowSchemas. """)
    kind: str = Field(default="FlowSchemaList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" `metadata` is the standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class IPAddress(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="IPAddress", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: IPAddressSpec = Field(default=None, description=r""" spec is the desired state of the IPAddress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class IPAddressSpec(BaseModel):
    parentRef: ParentReference = Field(default=None, description=r""" ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object. """)


class IPAddressList(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[IPAddress] = Field(default=None, description=r""" items is the list of IPAddresses. """)
    kind: str = Field(default="IPAddressList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class Lease(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Lease", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: LeaseSpec = Field(default=None, description=r""" spec contains the specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class LeaseSpec(BaseModel):
    acquireTime: MicroTime = Field(default=None, description=r""" acquireTime is a time when the current lease was acquired. """)
    holderIdentity: str = Field(default=None, description=r""" holderIdentity contains the identity of the holder of a current lease. """)
    leaseDurationSeconds: int = Field(default=None, description=r""" leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed renewTime. """)
    leaseTransitions: int = Field(default=None, description=r""" leaseTransitions is the number of transitions of a lease between holders. """)
    renewTime: MicroTime = Field(default=None, description=r""" renewTime is a time when the current holder of a lease has last updated the lease. """)


class LeaseList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Lease] = Field(default=None, description=r""" items is a list of schema objects. """)
    kind: str = Field(default="LeaseList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class LocalSubjectAccessReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="LocalSubjectAccessReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: SubjectAccessReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated.  spec.namespace must be equal to the namespace you made the request against.  If empty, it is defaulted. """)
    status: SubjectAccessReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates whether the request is allowed or not """)


class Namespace(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Namespace", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: NamespaceSpec = Field(default=None, description=r""" Spec defines the behavior of the Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: NamespaceStatus = Field(default=None, description=r""" Status describes the current status of a Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class NamespaceSpec(BaseModel):
    finalizers: List[str] = Field(default=None, description=r""" Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ """)


class NamespaceStatus(BaseModel):
    conditions: List[NamespaceCondition] = Field(default=None, description=r""" Represents the latest available observations of a namespace's current state. """)
    phase: str = Field(default=None, description=r""" Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ """)


class NamespaceList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Namespace] = Field(default=None, description=r""" Items is the list of Namespace objects in the list. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ """)
    kind: str = Field(default="NamespaceList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class Node(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Node", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: NodeSpec = Field(default=None, description=r""" Spec defines the behavior of a node. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: NodeStatus = Field(default=None, description=r""" Most recently observed status of the node. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class NodeSpec(BaseModel):
    configSource: NodeConfigSource = Field(default=None, description=r""" Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed. """)
    externalID: str = Field(default=None, description=r""" Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966 """)
    podCIDR: str = Field(default=None, description=r""" PodCIDR represents the pod IP range assigned to the node. """)
    podCIDRs: List[str] = Field(default=None, description=r""" podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6. """)
    providerID: str = Field(default=None, description=r""" ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID> """)
    taints: List[Taint] = Field(default=None, description=r""" If specified, the node's taints. """)
    unschedulable: bool = Field(default=None, description=r""" Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration """)


class NodeStatus(BaseModel):
    addresses: List[NodeAddress] = Field(default=None, description=r""" List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node's address in its own status or consumers of the downward API (status.hostIP). """)
    allocatable: dict = Field(default=None, description=r""" Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity. """)
    capacity: dict = Field(default=None, description=r""" Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity """)
    conditions: List[NodeCondition] = Field(default=None, description=r""" Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition """)
    config: NodeConfigStatus = Field(default=None, description=r""" Status of the config assigned to the node via the dynamic Kubelet config feature. """)
    daemonEndpoints: NodeDaemonEndpoints = Field(default=None, description=r""" Endpoints of daemons running on the Node. """)
    images: List[ContainerImage] = Field(default=None, description=r""" List of container images on this node """)
    nodeInfo: NodeSystemInfo = Field(default=None, description=r""" Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#info """)
    phase: str = Field(default=None, description=r""" NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated. """)
    volumesAttached: List[AttachedVolume] = Field(default=None, description=r""" List of volumes that are attached to the node. """)
    volumesInUse: List[str] = Field(default=None, description=r""" List of attachable volumes in use (mounted) by the node. """)


class NodeList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Node] = Field(default=None, description=r""" List of nodes """)
    kind: str = Field(default="NodeList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class PersistentVolume(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="PersistentVolume", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: PersistentVolumeSpec = Field(default=None, description=r""" spec defines a specification of a persistent volume owned by the cluster. Provisioned by an administrator. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes """)
    status: PersistentVolumeStatus = Field(default=None, description=r""" status represents the current information/status for the persistent volume. Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes """)


class PersistentVolumeSpec(BaseModel):
    accessModes: List[str] = Field(default=None, description=r""" accessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes """)
    awsElasticBlockStore: AWSElasticBlockStoreVolumeSource = Field(default=None, description=r""" awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)
    azureDisk: AzureDiskVolumeSource = Field(default=None, description=r""" azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. """)
    azureFile: AzureFilePersistentVolumeSource = Field(default=None, description=r""" azureFile represents an Azure File Service mount on the host and bind mount to the pod. """)
    capacity: dict = Field(default=None, description=r""" capacity is the description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity """)
    cephfs: CephFSPersistentVolumeSource = Field(default=None, description=r""" cephFS represents a Ceph FS mount on the host that shares a pod's lifetime """)
    cinder: CinderPersistentVolumeSource = Field(default=None, description=r""" cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
    claimRef: ObjectReference = Field(default=None, description=r""" claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding """)
    csi: CSIPersistentVolumeSource = Field(default=None, description=r""" csi represents storage that is handled by an external CSI driver (Beta feature). """)
    fc: FCVolumeSource = Field(default=None, description=r""" fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod. """)
    flexVolume: FlexPersistentVolumeSource = Field(default=None, description=r""" flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. """)
    flocker: FlockerVolumeSource = Field(default=None, description=r""" flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running """)
    gcePersistentDisk: GCEPersistentDiskVolumeSource = Field(default=None, description=r""" gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
    glusterfs: GlusterfsPersistentVolumeSource = Field(default=None, description=r""" glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md """)
    hostPath: HostPathVolumeSource = Field(default=None, description=r""" hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)
    iscsi: ISCSIPersistentVolumeSource = Field(default=None, description=r""" iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. """)
    local: LocalVolumeSource = Field(default=None, description=r""" local represents directly-attached storage with node affinity """)
    mountOptions: List[str] = Field(default=None, description=r""" mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options """)
    nfs: NFSVolumeSource = Field(default=None, description=r""" nfs represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
    nodeAffinity: VolumeNodeAffinity = Field(default=None, description=r""" nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume. """)
    persistentVolumeReclaimPolicy: str = Field(default=None, description=r""" persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming """)
    photonPersistentDisk: PhotonPersistentDiskVolumeSource = Field(default=None, description=r""" photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine """)
    portworxVolume: PortworxVolumeSource = Field(default=None, description=r""" portworxVolume represents a portworx volume attached and mounted on kubelets host machine """)
    quobyte: QuobyteVolumeSource = Field(default=None, description=r""" quobyte represents a Quobyte mount on the host that shares a pod's lifetime """)
    rbd: RBDPersistentVolumeSource = Field(default=None, description=r""" rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md """)
    scaleIO: ScaleIOPersistentVolumeSource = Field(default=None, description=r""" scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. """)
    storageClassName: str = Field(default=None, description=r""" storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass. """)
    storageos: StorageOSPersistentVolumeSource = Field(default=None, description=r""" storageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md """)
    volumeMode: str = Field(default=None, description=r""" volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec. """)
    vsphereVolume: VsphereVirtualDiskVolumeSource = Field(default=None, description=r""" vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine """)


class PersistentVolumeStatus(BaseModel):
    lastPhaseTransitionTime: Time = Field(default=None, description=r""" lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. This is an alpha field and requires enabling PersistentVolumeLastPhaseTransitionTime feature. """)
    message: str = Field(default=None, description=r""" message is a human-readable message indicating details about why the volume is in this state. """)
    phase: str = Field(default=None, description=r""" phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase """)
    reason: str = Field(default=None, description=r""" reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. """)


class PersistentVolumeList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PersistentVolume] = Field(default=None, description=r""" items is a list of persistent volumes. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes """)
    kind: str = Field(default="PersistentVolumeList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class PriorityLevelConfiguration(KubeModel):
    apiVersion: str = Field(default="v1beta3", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="PriorityLevelConfiguration", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: PriorityLevelConfigurationSpec = Field(default=None, description=r""" `spec` is the specification of the desired behavior of a "request-priority". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: PriorityLevelConfigurationStatus = Field(default=None, description=r""" `status` is the current status of a "request-priority". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class PriorityLevelConfigurationSpec(BaseModel):
    exempt: ExemptPriorityLevelConfiguration = Field(default=None, description=r""" `exempt` specifies how requests are handled for an exempt priority level. This field MUST be empty if `type` is `"Limited"`. This field MAY be non-empty if `type` is `"Exempt"`. If empty and `type` is `"Exempt"` then the default values for `ExemptPriorityLevelConfiguration` apply. """)
    limited: LimitedPriorityLevelConfiguration = Field(default=None, description=r""" `limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `"Limited"`. """)
    type: str = Field(default=None, description=r""" `type` indicates whether this priority level is subject to limitation on request execution.  A value of `"Exempt"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `"Limited"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required. """)


class PriorityLevelConfigurationStatus(BaseModel):
    conditions: List[PriorityLevelConfigurationCondition] = Field(default=None, description=r""" `conditions` is the current state of "request-priority". """)


class PriorityLevelConfigurationList(KubeModel):
    apiVersion: str = Field(default="v1beta3", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PriorityLevelConfiguration] = Field(default=None, description=r""" `items` is a list of request-priorities. """)
    kind: str = Field(default="PriorityLevelConfigurationList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class ResourceQuota(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ResourceQuota", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: ResourceQuotaSpec = Field(default=None, description=r""" Spec defines the desired quota. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
    status: ResourceQuotaStatus = Field(default=None, description=r""" Status defines the actual enforced quota and its current usage. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class ResourceQuotaSpec(BaseModel):
    hard: dict = Field(default=None, description=r""" hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """)
    scopeSelector: ScopeSelector = Field(default=None, description=r""" scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched. """)
    scopes: List[str] = Field(default=None, description=r""" A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. """)


class ResourceQuotaStatus(BaseModel):
    hard: dict = Field(default=None, description=r""" Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """)
    used: dict = Field(default=None, description=r""" Used is the current observed total usage of the resource in the namespace. """)


class ResourceQuotaList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ResourceQuota] = Field(default=None, description=r""" Items is a list of ResourceQuota objects. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """)
    kind: str = Field(default="ResourceQuotaList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class Role(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Role", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. """)
    rules: List[PolicyRule] = Field(default=None, description=r""" Rules holds all the PolicyRules for this Role """)


class RoleList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[Role] = Field(default=None, description=r""" Items is a list of Roles """)
    kind: str = Field(default="RoleList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. """)


class RoleBinding(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="RoleBinding", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. """)
    roleRef: RoleRef = Field(default=None, description=r""" RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. This field is immutable. """)
    subjects: List[Subject] = Field(default=None, description=r""" Subjects holds references to the objects the role applies to. """)


class RoleBindingList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[RoleBinding] = Field(default=None, description=r""" Items is a list of RoleBindings """)
    kind: str = Field(default="RoleBindingList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. """)


class RuntimeClass(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    handler: str = Field(default=None, description=r""" handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable. """)
    kind: str = Field(default="RuntimeClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    overhead: Overhead = Field(default=None, description=r""" overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see  https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/ """)
    scheduling: Scheduling = Field(default=None, description=r""" scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes. """)


class RuntimeClassList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[RuntimeClass] = Field(default=None, description=r""" items is a list of schema objects. """)
    kind: str = Field(default="RuntimeClassList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class SelfSubjectAccessReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="SelfSubjectAccessReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: SelfSubjectAccessReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated.  user and groups must be empty """)
    status: SubjectAccessReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates whether the request is allowed or not """)


class SelfSubjectAccessReviewSpec(BaseModel):
    nonResourceAttributes: NonResourceAttributes = Field(default=None, description=r""" NonResourceAttributes describes information for a non-resource access request """)
    resourceAttributes: ResourceAttributes = Field(default=None, description=r""" ResourceAuthorizationAttributes describes information for a resource access request """)


class SelfSubjectReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="SelfSubjectReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    status: SelfSubjectReviewStatus = Field(default=None, description=r""" Status is filled in by the server with the user attributes. """)


class SelfSubjectReviewStatus(BaseModel):
    userInfo: UserInfo = Field(default=None, description=r""" User attributes of the user making this request. """)


class SelfSubjectRulesReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="SelfSubjectRulesReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: SelfSubjectRulesReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated. """)
    status: SubjectRulesReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates the set of actions a user can perform. """)


class SelfSubjectRulesReviewSpec(BaseModel):
    namespace: str = Field(default=None, description=r""" Namespace to evaluate rules for. Required. """)


class ServiceAccount(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    automountServiceAccountToken: bool = Field(default=None, description=r""" AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level. """)
    imagePullSecrets: List[LocalObjectReference] = Field(default=None, description=r""" ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod """)
    kind: str = Field(default="ServiceAccount", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    secrets: List[ObjectReference] = Field(default=None, description=r""" Secrets is a list of the secrets in the same namespace that pods running using this ServiceAccount are allowed to use. Pods are only limited to this list if this service account has a "kubernetes.io/enforce-mountable-secrets" annotation set to "true". This field should not be used to find auto-generated service account token secrets for use outside of pods. Instead, tokens can be requested directly using the TokenRequest API, or service account token secrets can be manually created. More info: https://kubernetes.io/docs/concepts/configuration/secret """)


class ServiceAccountList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ServiceAccount] = Field(default=None, description=r""" List of ServiceAccounts. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ """)
    kind: str = Field(default="ServiceAccountList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)


class StorageVersion(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="StorageVersion", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" The name is <group>.<resource>. """)
    spec: StorageVersionSpec = Field(default=None, description=r""" Spec is an empty spec. It is here to comply with Kubernetes API style. """)
    status: StorageVersionStatus = Field(default=None, description=r""" API server instances report the version they can decode and the version they encode objects to when persisting objects in the backend. """)


class StorageVersionSpec(BaseModel):
    pass



class StorageVersionStatus(BaseModel):
    commonEncodingVersion: str = Field(default=None, description=r""" If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality. """)
    conditions: List[StorageVersionCondition] = Field(default=None, description=r""" The latest available observations of the storageVersion's state. """)
    storageVersions: List[ServerStorageVersion] = Field(default=None, description=r""" The reported versions per API server instance. """)


class StorageVersionList(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[StorageVersion] = Field(default=None, description=r""" Items holds a list of StorageVersion """)
    kind: str = Field(default="StorageVersionList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class SubjectAccessReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="SubjectAccessReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: SubjectAccessReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated """)
    status: SubjectAccessReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates whether the request is allowed or not """)


class SubjectAccessReviewSpec(BaseModel):
    extra: dict = Field(default=None, description=r""" Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here. """)
    groups: List[str] = Field(default=None, description=r""" Groups is the groups you're testing for. """)
    nonResourceAttributes: NonResourceAttributes = Field(default=None, description=r""" NonResourceAttributes describes information for a non-resource access request """)
    resourceAttributes: ResourceAttributes = Field(default=None, description=r""" ResourceAuthorizationAttributes describes information for a resource access request """)
    uid: str = Field(default=None, description=r""" UID information about the requesting user. """)
    user: str = Field(default=None, description=r""" User is the user you're testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups """)


class SubjectAccessReviewStatus(BaseModel):
    allowed: bool = Field(default=None, description=r""" Allowed is required. True if the action would be allowed, false otherwise. """)
    denied: bool = Field(default=None, description=r""" Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true. """)
    evaluationError: str = Field(default=None, description=r""" EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request. """)
    reason: str = Field(default=None, description=r""" Reason is optional.  It indicates why a request was allowed or denied. """)


class TokenRequest(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="TokenRequest", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: TokenRequestSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated """)
    status: TokenRequestStatus = Field(default=None, description=r""" Status is filled in by the server and indicates whether the token can be authenticated. """)


class TokenRequestSpec(BaseModel):
    audiences: List[str] = Field(default=None, description=r""" Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. """)
    boundObjectRef: BoundObjectReference = Field(default=None, description=r""" BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation. """)
    expirationSeconds: int = Field(default=None, description=r""" ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response. """)


class TokenRequestStatus(BaseModel):
    expirationTimestamp: Time = Field(default=None, description=r""" ExpirationTimestamp is the time of expiration of the returned token. """)
    token: str = Field(default=None, description=r""" Token is the opaque bearer token. """)


class TokenReview(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="TokenReview", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: TokenReviewSpec = Field(default=None, description=r""" Spec holds information about the request being evaluated """)
    status: TokenReviewStatus = Field(default=None, description=r""" Status is filled in by the server and indicates whether the request can be authenticated. """)


class TokenReviewSpec(BaseModel):
    audiences: List[str] = Field(default=None, description=r""" Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver. """)
    token: str = Field(default=None, description=r""" Token is the opaque bearer token. """)


class TokenReviewStatus(BaseModel):
    audiences: List[str] = Field(default=None, description=r""" Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server. """)
    authenticated: bool = Field(default=None, description=r""" Authenticated indicates that the token was associated with a known user. """)
    error: str = Field(default=None, description=r""" Error indicates that the token couldn't be checked """)
    user: UserInfo = Field(default=None, description=r""" User is the UserInfo associated with the provided token. """)


class NetworkPolicy(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="NetworkPolicy", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: NetworkPolicySpec = Field(default=None, description=r""" spec represents the specification of the desired behavior for this NetworkPolicy. """)


class NetworkPolicySpec(BaseModel):
    egress: List[NetworkPolicyEgressRule] = Field(default=None, description=r""" egress is a list of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8 """)
    ingress: List[NetworkPolicyIngressRule] = Field(default=None, description=r""" ingress is a list of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default) """)
    podSelector: LabelSelector = Field(default=None, description=r""" podSelector selects the pods to which this NetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace. """)
    policyTypes: List[str] = Field(default=None, description=r""" policyTypes is a list of rule types that the NetworkPolicy relates to. Valid options are ["Ingress"], ["Egress"], or ["Ingress", "Egress"]. If this field is not specified, it will default based on the existence of ingress or egress rules; policies that contain an egress section are assumed to affect egress, and all policies (whether or not they contain an ingress section) are assumed to affect ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include "Egress" (since such a policy would not include an egress section and would otherwise default to just [ "Ingress" ]). This field is beta-level in 1.8 """)


class NetworkPolicyList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[NetworkPolicy] = Field(default=None, description=r""" items is a list of schema objects. """)
    kind: str = Field(default="NetworkPolicyList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)


class APIGroup(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="APIGroup", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" name is the name of the group. """)
    preferredVersion: GroupVersionForDiscovery = Field(default=None, description=r""" preferredVersion is the version preferred by the API server, which probably is the storage version. """)
    serverAddressByClientCIDRs: List[ServerAddressByClientCIDR] = Field(default=None, description=r""" a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP. """)
    versions: List[GroupVersionForDiscovery] = Field(default=None, description=r""" versions are the versions supported in this group. """)


class APIResource(BaseModel):
    categories: List[str] = Field(default=None, description=r""" categories is a list of the grouped resources this resource belongs to (e.g. 'all') """)
    group: str = Field(default=None, description=r""" group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale". """)
    kind: str = Field(default="APIResource", description=r""" kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo') """)
    name: str = Field(default=None, description=r""" name is the plural name of the resource. """)
    namespaced: bool = Field(default=None, description=r""" namespaced indicates if a resource is namespaced or not. """)
    shortNames: List[str] = Field(default=None, description=r""" shortNames is a list of suggested short names of the resource. """)
    singularName: str = Field(default=None, description=r""" singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface. """)
    storageVersionHash: str = Field(default=None, description=r""" The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates. """)
    verbs: List[str] = Field(default=None, description=r""" verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy) """)
    version: str = Field(default=None, description=r""" version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)". """)


class APIServiceCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" Human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" Unique, one-word, CamelCase reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status is the status of the condition. Can be True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type is the type of the condition. """)


class APIVersions(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="APIVersions", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    serverAddressByClientCIDRs: List[ServerAddressByClientCIDR] = Field(default=None, description=r""" a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP. """)
    versions: List[str] = Field(default=None, description=r""" versions are the api versions that are available. """)


class AWSElasticBlockStoreVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)
    partition: int = Field(default=None, description=r""" partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). """)
    readOnly: bool = Field(default=None, description=r""" readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)
    volumeID: str = Field(default=None, description=r""" volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)


class Affinity(BaseModel):
    nodeAffinity: NodeAffinity = Field(default=None, description=r""" Describes node affinity scheduling rules for the pod. """)
    podAffinity: PodAffinity = Field(default=None, description=r""" Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)). """)
    podAntiAffinity: PodAntiAffinity = Field(default=None, description=r""" Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)). """)


class AggregationRule(BaseModel):
    clusterRoleSelectors: List[LabelSelector] = Field(default=None, description=r""" ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added """)


class AllocationResult(BaseModel):
    availableOnNodes: NodeSelector = Field(default=None, description=r""" This field will get set by the resource driver after it has allocated the resource to inform the scheduler where it can schedule Pods using the ResourceClaim.  Setting this field is optional. If null, the resource is available everywhere. """)
    resourceHandles: List[ResourceHandle] = Field(default=None, description=r""" ResourceHandles contain the state associated with an allocation that should be maintained throughout the lifetime of a claim. Each ResourceHandle contains data that should be passed to a specific kubelet plugin once it lands on a node. This data is returned by the driver after a successful allocation and is opaque to Kubernetes. Driver documentation may explain to users how to interpret this data if needed.  Setting this field is optional. It has a maximum size of 32 entries. If null (or empty), it is assumed this allocation will be processed by a single kubelet plugin with no ResourceHandle data attached. The name of the kubelet plugin invoked will match the DriverName set in the ResourceClaimStatus this AllocationResult is embedded in. """)
    shareable: bool = Field(default=None, description=r""" Shareable determines whether the resource supports more than one consumer at a time. """)


class AttachedVolume(BaseModel):
    devicePath: str = Field(default=None, description=r""" DevicePath represents the device path where the volume should be available """)
    name: str = Field(default=None, description=r""" Name of the attached volume """)


class AuditAnnotation(BaseModel):
    key: str = Field(default=None, description=r""" key specifies the audit annotation key. The audit annotation keys of a ValidatingAdmissionPolicy must be unique. The key must be a qualified name ([A-Za-z0-9][-A-Za-z0-9_.]*) no more than 63 bytes in length.  The key is combined with the resource name of the ValidatingAdmissionPolicy to construct an audit annotation key: "{ValidatingAdmissionPolicy name}/{key}".  If an admission webhook uses the same resource name as this ValidatingAdmissionPolicy and the same audit annotation key, the annotation key will be identical. In this case, the first annotation written with the key will be included in the audit event and all subsequent annotations with the same key will be discarded.  Required. """)
    valueExpression: str = Field(default=None, description=r""" valueExpression represents the expression which is evaluated by CEL to produce an audit annotation value. The expression must evaluate to either a string or null value. If the expression evaluates to a string, the audit annotation is included with the string value. If the expression evaluates to null or empty string the audit annotation will be omitted. The valueExpression may be no longer than 5kb in length. If the result of the valueExpression is more than 10kb in length, it will be truncated to 10kb.  If multiple ValidatingAdmissionPolicyBinding resources match an API request, then the valueExpression will be evaluated for each binding. All unique values produced by the valueExpressions will be joined together in a comma-separated list.  Required. """)


class AzureDiskVolumeSource(BaseModel):
    cachingMode: str = Field(default=None, description=r""" cachingMode is the Host Caching mode: None, Read Only, Read Write. """)
    diskName: str = Field(default=None, description=r""" diskName is the Name of the data disk in the blob storage """)
    diskURI: str = Field(default=None, description=r""" diskURI is the URI of data disk in the blob storage """)
    fsType: str = Field(default=None, description=r""" fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    kind: str = Field(default="AzureDiskVolumeSource", description=r""" kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared """)
    readOnly: bool = Field(default=None, description=r""" readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)


class AzureFilePersistentVolumeSource(BaseModel):
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretName: str = Field(default=None, description=r""" secretName is the name of secret that contains Azure Storage Account Name and Key """)
    secretNamespace: str = Field(default=None, description=r""" secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod """)
    shareName: str = Field(default=None, description=r""" shareName is the azure Share Name """)


class AzureFileVolumeSource(BaseModel):
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretName: str = Field(default=None, description=r""" secretName is the  name of secret that contains Azure Storage Account Name and Key """)
    shareName: str = Field(default=None, description=r""" shareName is the azure share Name """)


class BoundObjectReference(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" API version of the referent. """)
    kind: str = Field(default="BoundObjectReference", description=r""" Kind of the referent. Valid kinds are 'Pod' and 'Secret'. """)
    name: str = Field(default=None, description=r""" Name of the referent. """)
    uid: str = Field(default=None, description=r""" UID of the referent. """)


class CSINodeDriver(BaseModel):
    allocatable: VolumeNodeResources = Field(default=None, description=r""" allocatable represents the volume resources of a node that are available for scheduling. This field is beta. """)
    name: str = Field(default=None, description=r""" name represents the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver. """)
    nodeID: str = Field(default=None, description=r""" nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as "node1", but the storage system may refer to the same node as "nodeA". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. "nodeA" instead of "node1". This field is required. """)
    topologyKeys: List[str] = Field(default=None, description=r""" topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. "company.com/zone", "company.com/region"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology. """)


class CSIPersistentVolumeSource(BaseModel):
    controllerExpandSecretRef: SecretReference = Field(default=None, description=r""" controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    controllerPublishSecretRef: SecretReference = Field(default=None, description=r""" controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    driver: str = Field(default=None, description=r""" driver is the name of the driver to use for this volume. Required. """)
    fsType: str = Field(default=None, description=r""" fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". """)
    nodeExpandSecretRef: SecretReference = Field(default=None, description=r""" nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This is a beta field which is enabled default by CSINodeExpandSecret feature gate. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    nodePublishSecretRef: SecretReference = Field(default=None, description=r""" nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    nodeStageSecretRef: SecretReference = Field(default=None, description=r""" nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
    readOnly: bool = Field(default=None, description=r""" readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). """)
    volumeAttributes: dict = Field(default=None, description=r""" volumeAttributes of the volume to publish. """)
    volumeHandle: str = Field(default=None, description=r""" volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. """)


class CSIVolumeSource(BaseModel):
    driver: str = Field(default=None, description=r""" driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. """)
    fsType: str = Field(default=None, description=r""" fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. """)
    nodePublishSecretRef: LocalObjectReference = Field(default=None, description=r""" nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed. """)
    readOnly: bool = Field(default=None, description=r""" readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). """)
    volumeAttributes: dict = Field(default=None, description=r""" volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values. """)


class Capabilities(BaseModel):
    add: List[str] = Field(default=None, description=r""" Added capabilities """)
    drop: List[str] = Field(default=None, description=r""" Removed capabilities """)


class CephFSPersistentVolumeSource(BaseModel):
    monitors: List[str] = Field(default=None, description=r""" monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    path: str = Field(default=None, description=r""" path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    secretFile: str = Field(default=None, description=r""" secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    user: str = Field(default=None, description=r""" user is Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)


class CephFSVolumeSource(BaseModel):
    monitors: List[str] = Field(default=None, description=r""" monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    path: str = Field(default=None, description=r""" path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    secretFile: str = Field(default=None, description=r""" secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
    user: str = Field(default=None, description=r""" user is optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)


class CertificateSigningRequestCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition's status is changed, the server defaults this to the current time. """)
    lastUpdateTime: Time = Field(default=None, description=r""" lastUpdateTime is the time of the last update to this condition """)
    message: str = Field(default=None, description=r""" message contains a human readable message with details about the request state """)
    reason: str = Field(default=None, description=r""" reason indicates a brief reason for the request state """)
    status: str = Field(default=None, description=r""" status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be "False" or "Unknown". """)
    type: str = Field(default=None, description=r""" type of the condition. Known conditions are "Approved", "Denied", and "Failed".  An "Approved" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.  A "Denied" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.  A "Failed" condition is added via the /status subresource, indicating the signer failed to issue the certificate.  Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.  Only one condition of a given type is allowed. """)


class CinderPersistentVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef is Optional: points to a secret object containing parameters used to connect to OpenStack. """)
    volumeID: str = Field(default=None, description=r""" volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)


class CinderVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is optional: points to a secret object containing parameters used to connect to OpenStack. """)
    volumeID: str = Field(default=None, description=r""" volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)


class ClaimSource(BaseModel):
    resourceClaimName: str = Field(default=None, description=r""" ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod. """)
    resourceClaimTemplateName: str = Field(default=None, description=r""" ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim. """)


class ClientIPConfig(BaseModel):
    timeoutSeconds: int = Field(default=None, description=r""" timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours). """)


class ComponentCondition(BaseModel):
    error: str = Field(default=None, description=r""" Condition error code for a component. For example, a health check error code. """)
    message: str = Field(default=None, description=r""" Message about the condition for a component. For example, information about a health check. """)
    status: str = Field(default=None, description=r""" Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown". """)
    type: str = Field(default=None, description=r""" Type of condition for a component. Valid value: "Healthy" """)


class Condition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. """)
    message: str = Field(default=None, description=r""" message is a human readable message indicating details about the transition. This may be an empty string. """)
    observedGeneration: int = Field(default=None, description=r""" observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. """)
    reason: str = Field(default=None, description=r""" reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. """)
    status: str = Field(default=None, description=r""" status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" type of condition in CamelCase or in foo.example.com/CamelCase. """)


class ConfigMapEnvSource(BaseModel):
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" Specify whether the ConfigMap must be defined """)


class ConfigMapKeySelector(BaseModel):
    key: str = Field(default=None, description=r""" The key to select. """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" Specify whether the ConfigMap or its key must be defined """)


class ConfigMapNodeConfigSource(BaseModel):
    kubeletConfigKey: str = Field(default=None, description=r""" KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases. """)
    name: str = Field(default=None, description=r""" Name is the metadata.name of the referenced ConfigMap. This field is required in all cases. """)
    namespace: str = Field(default=None, description=r""" Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases. """)
    resourceVersion: str = Field(default=None, description=r""" ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. """)
    uid: str = Field(default=None, description=r""" UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. """)


class ConfigMapProjection(BaseModel):
    items: List[KeyToPath] = Field(default=None, description=r""" items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" optional specify whether the ConfigMap or its keys must be defined """)


class ConfigMapVolumeSource(BaseModel):
    defaultMode: int = Field(default=None, description=r""" defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
    items: List[KeyToPath] = Field(default=None, description=r""" items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" optional specify whether the ConfigMap or its keys must be defined """)


class ContainerImage(BaseModel):
    names: List[str] = Field(default=None, description=r""" Names by which this image is known. e.g. ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"] """)
    sizeBytes: int = Field(default=None, description=r""" The size of the image in bytes. """)


class ContainerPort(BaseModel):
    containerPort: int = Field(default=None, description=r""" Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. """)
    hostIP: str = Field(default=None, description=r""" What host IP to bind the external port to. """)
    hostPort: int = Field(default=None, description=r""" Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. """)
    name: str = Field(default=None, description=r""" If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. """)
    protocol: str = Field(default=None, description=r""" Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". """)


class ContainerResizePolicy(BaseModel):
    resourceName: str = Field(default=None, description=r""" Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. """)
    restartPolicy: str = Field(default=None, description=r""" Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. """)


class ContainerResourceMetricSource(BaseModel):
    container: str = Field(default=None, description=r""" container is the name of the container in the pods of the scaling target """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)


class ContainerResourceMetricStatus(BaseModel):
    container: str = Field(default=None, description=r""" container is the name of the container in the pods of the scaling target """)
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)


class ContainerState(BaseModel):
    running: ContainerStateRunning = Field(default=None, description=r""" Details about a running container """)
    terminated: ContainerStateTerminated = Field(default=None, description=r""" Details about a terminated container """)
    waiting: ContainerStateWaiting = Field(default=None, description=r""" Details about a waiting container """)


class ContainerStateRunning(BaseModel):
    startedAt: Time = Field(default=None, description=r""" Time at which the container was last (re-)started """)


class ContainerStateTerminated(BaseModel):
    containerID: str = Field(default=None, description=r""" Container's ID in the format '<type>://<container_id>' """)
    exitCode: int = Field(default=None, description=r""" Exit status from the last termination of the container """)
    finishedAt: Time = Field(default=None, description=r""" Time at which the container last terminated """)
    message: str = Field(default=None, description=r""" Message regarding the last termination of the container """)
    reason: str = Field(default=None, description=r""" (brief) reason from the last termination of the container """)
    signal: int = Field(default=None, description=r""" Signal from the last termination of the container """)
    startedAt: Time = Field(default=None, description=r""" Time at which previous execution of the container started """)


class ContainerStateWaiting(BaseModel):
    message: str = Field(default=None, description=r""" Message regarding why the container is not yet running. """)
    reason: str = Field(default=None, description=r""" (brief) reason the container is not yet running. """)


class CrossVersionObjectReference(KubeModel):
    apiVersion: str = Field(default="v2", description=r""" apiVersion is the API version of the referent """)
    kind: str = Field(default="CrossVersionObjectReference", description=r""" kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)


class CustomResourceColumnDefinition(BaseModel):
    description: str = Field(default=None, description=r""" description is a human readable description of this column. """)
    format: str = Field(default=None, description=r""" format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. """)
    jsonPath: str = Field(default=None, description=r""" jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column. """)
    name: str = Field(default=None, description=r""" name is a human readable name for the column. """)
    priority: int = Field(default=None, description=r""" priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0. """)
    type: str = Field(default=None, description=r""" type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. """)


class CustomResourceConversion(BaseModel):
    strategy: str = Field(default=None, description=r""" strategy specifies how custom resources are converted between versions. Allowed values are: - `"None"`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `"Webhook"`: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set. """)
    webhook: WebhookConversion = Field(default=None, description=r""" webhook describes how to call the conversion webhook. Required when `strategy` is set to `"Webhook"`. """)


class CustomResourceDefinitionCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" message is a human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" reason is a unique, one-word, CamelCase reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" status is the status of the condition. Can be True, False, Unknown. """)
    type: str = Field(default=None, description=r""" type is the type of the condition. Types include Established, NamesAccepted and Terminating. """)


class CustomResourceDefinitionNames(BaseModel):
    categories: List[str] = Field(default=None, description=r""" categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`. """)
    kind: str = Field(default="CustomResourceDefinitionNames", description=r""" kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls. """)
    listKind: str = Field(default=None, description=r""" listKind is the serialized kind of the list for this resource. Defaults to "`kind`List". """)
    plural: str = Field(default=None, description=r""" plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase. """)
    shortNames: List[str] = Field(default=None, description=r""" shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase. """)
    singular: str = Field(default=None, description=r""" singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`. """)


class CustomResourceDefinitionVersion(BaseModel):
    additionalPrinterColumns: List[CustomResourceColumnDefinition] = Field(default=None, description=r""" additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. """)
    deprecated: bool = Field(default=None, description=r""" deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false. """)
    deprecationWarning: str = Field(default=None, description=r""" deprecationWarning overrides the default warning returned to API clients. May only be set when `deprecated` is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists. """)
    name: str = Field(default=None, description=r""" name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true. """)
    validation_schema: CustomResourceValidation = Field(default=None, alias="schema", description=r""" schema describes the schema used for validation, pruning, and defaulting of this version of the custom resource. """)
    served: bool = Field(default=None, description=r""" served is a flag enabling/disabling this version from being served via REST APIs """)
    storage: bool = Field(default=None, description=r""" storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true. """)
    subresources: CustomResourceSubresources = Field(default=None, description=r""" subresources specify what subresources this version of the defined custom resource have. """)


class CustomResourceSubresourceScale(BaseModel):
    labelSelectorPath: str = Field(default=None, description=r""" labelSelectorPath defines the JSON path inside of a custom resource that corresponds to Scale `status.selector`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status` or `.spec`. Must be set to work with HorizontalPodAutoscaler. The field pointed by this JSON path must be a string field (not a complex selector struct) which contains a serialized label selector in string form. More info: https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions#scale-subresource If there is no value under the given path in the custom resource, the `status.selector` value in the `/scale` subresource will default to the empty string. """)
    specReplicasPath: str = Field(default=None, description=r""" specReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `spec.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.spec`. If there is no value under the given path in the custom resource, the `/scale` subresource will return an error on GET. """)
    statusReplicasPath: str = Field(default=None, description=r""" statusReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `status.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status`. If there is no value under the given path in the custom resource, the `status.replicas` value in the `/scale` subresource will default to 0. """)


class CustomResourceSubresourceStatus(BaseModel):
    pass



class CustomResourceSubresources(BaseModel):
    scale: CustomResourceSubresourceScale = Field(default=None, description=r""" scale indicates the custom resource should serve a `/scale` subresource that returns an `autoscaling/v1` Scale object. """)
    status: CustomResourceSubresourceStatus = Field(default=None, description=r""" status indicates the custom resource should serve a `/status` subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the `status` stanza of the object. 2. requests to the custom resource `/status` subresource ignore changes to anything other than the `status` stanza of the object. """)


class CustomResourceValidation(BaseModel):
    openAPIV3Schema: JSONSchemaProps = Field(default=None, description=r""" openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning. """)


class DaemonEndpoint(BaseModel):
    Port: int = Field(default=None, description=r""" Port number of the given endpoint. """)


class DaemonSetCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
    reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of DaemonSet condition. """)


class DaemonSetUpdateStrategy(BaseModel):
    rollingUpdate: RollingUpdateDaemonSet = Field(default=None, description=r""" Rolling update config params. Present only if type = "RollingUpdate". """)
    type: str = Field(default=None, description=r""" Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate. """)


class DeleteOptions(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    dryRun: List[str] = Field(default=None, description=r""" When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed """)
    gracePeriodSeconds: int = Field(default=None, description=r""" The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. """)
    kind: str = Field(default="DeleteOptions", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    orphanDependents: bool = Field(default=None, description=r""" Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the "orphan" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. """)
    preconditions: Preconditions = Field(default=None, description=r""" Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned. """)
    propagationPolicy: str = Field(default=None, description=r""" Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. """)


class DeploymentCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
    lastUpdateTime: Time = Field(default=None, description=r""" The last time this condition was updated. """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
    reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of deployment condition. """)


class DownwardAPIProjection(BaseModel):
    items: List[DownwardAPIVolumeFile] = Field(default=None, description=r""" Items is a list of DownwardAPIVolume file """)


class DownwardAPIVolumeFile(BaseModel):
    fieldRef: ObjectFieldSelector = Field(default=None, description=r""" Required: Selects a field of the pod: only annotations, labels, name and namespace are supported. """)
    mode: int = Field(default=None, description=r""" Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
    path: str = Field(default=None, description=r""" Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' """)
    resourceFieldRef: ResourceFieldSelector = Field(default=None, description=r""" Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. """)


class DownwardAPIVolumeSource(BaseModel):
    defaultMode: int = Field(default=None, description=r""" Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
    items: List[DownwardAPIVolumeFile] = Field(default=None, description=r""" Items is a list of downward API volume file """)


class EmptyDirVolumeSource(BaseModel):
    medium: str = Field(default=None, description=r""" medium represents what type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """)
    sizeLimit: Quantity = Field(default=None, description=r""" sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """)


class Endpoint(BaseModel):
    addresses: List[str] = Field(default=None, description=r""" addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267 """)
    conditions: EndpointConditions = Field(default=None, description=r""" conditions contains information about the current status of the endpoint. """)
    deprecatedTopology: dict = Field(default=None, description=r""" deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead. """)
    hints: EndpointHints = Field(default=None, description=r""" hints contains information associated with how an endpoint should be consumed. """)
    hostname: str = Field(default=None, description=r""" hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation. """)
    nodeName: str = Field(default=None, description=r""" nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. """)
    targetRef: ObjectReference = Field(default=None, description=r""" targetRef is a reference to a Kubernetes object that represents this endpoint. """)
    zone: str = Field(default=None, description=r""" zone is the name of the Zone this endpoint exists in. """)


class EndpointAddress(BaseModel):
    hostname: str = Field(default=None, description=r""" The Hostname of this endpoint """)
    ip: str = Field(default=None, description=r""" The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16). """)
    nodeName: str = Field(default=None, description=r""" Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. """)
    targetRef: ObjectReference = Field(default=None, description=r""" Reference to object providing the endpoint. """)


class EndpointConditions(BaseModel):
    ready: bool = Field(default=None, description=r""" ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag. """)
    serving: bool = Field(default=None, description=r""" serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. """)
    terminating: bool = Field(default=None, description=r""" terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. """)


class EndpointHints(BaseModel):
    forZones: List[ForZone] = Field(default=None, description=r""" forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing. """)


class EndpointPort(BaseModel):
    appProtocol: str = Field(default=None, description=r""" The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 over cleartext as described in https://www.rfc-editor.org/rfc/rfc7540   * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol. """)
    name: str = Field(default=None, description=r""" The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined. """)
    port: int = Field(default=None, description=r""" The port number of the endpoint. """)
    protocol: str = Field(default=None, description=r""" The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. """)


class EndpointSubset(BaseModel):
    addresses: List[EndpointAddress] = Field(default=None, description=r""" IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize. """)
    notReadyAddresses: List[EndpointAddress] = Field(default=None, description=r""" IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check. """)
    ports: List[EndpointPort] = Field(default=None, description=r""" Port numbers available on the related IP addresses. """)


class EnvFromSource(BaseModel):
    configMapRef: ConfigMapEnvSource = Field(default=None, description=r""" The ConfigMap to select from """)
    prefix: str = Field(default=None, description=r""" An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER. """)
    secretRef: SecretEnvSource = Field(default=None, description=r""" The Secret to select from """)


class EnvVar(BaseModel):
    name: str = Field(default=None, description=r""" Name of the environment variable. Must be a C_IDENTIFIER. """)
    value: str = Field(default=None, description=r""" Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". """)
    valueFrom: EnvVarSource = Field(default=None, description=r""" Source for the environment variable's value. Cannot be used if value is not empty. """)


class EnvVarSource(BaseModel):
    configMapKeyRef: ConfigMapKeySelector = Field(default=None, description=r""" Selects a key of a ConfigMap. """)
    fieldRef: ObjectFieldSelector = Field(default=None, description=r""" Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. """)
    resourceFieldRef: ResourceFieldSelector = Field(default=None, description=r""" Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. """)
    secretKeyRef: SecretKeySelector = Field(default=None, description=r""" Selects a key of a secret in the pod's namespace """)


class EphemeralContainer(BaseModel):
    args: List[str] = Field(default=None, description=r""" Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """)
    command: List[str] = Field(default=None, description=r""" Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """)
    env: List[EnvVar] = Field(default=None, description=r""" List of environment variables to set in the container. Cannot be updated. """)
    envFrom: List[EnvFromSource] = Field(default=None, description=r""" List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. """)
    image: str = Field(default=None, description=r""" Container image name. More info: https://kubernetes.io/docs/concepts/containers/images """)
    imagePullPolicy: str = Field(default=None, description=r""" Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images """)
    lifecycle: Lifecycle = Field(default=None, description=r""" Lifecycle is not allowed for ephemeral containers. """)
    livenessProbe: Probe = Field(default=None, description=r""" Probes are not allowed for ephemeral containers. """)
    name: str = Field(default=None, description=r""" Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers. """)
    ports: List[ContainerPort] = Field(default=None, description=r""" Ports are not allowed for ephemeral containers. """)
    readinessProbe: Probe = Field(default=None, description=r""" Probes are not allowed for ephemeral containers. """)
    resizePolicy: List[ContainerResizePolicy] = Field(default=None, description=r""" Resources resize policy for the container. """)
    resources: ResourceRequirements = Field(default=None, description=r""" Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod. """)
    restartPolicy: str = Field(default=None, description=r""" Restart policy for the container to manage the restart behavior of each container within a pod. This may only be set for init containers. You cannot set this field on ephemeral containers. """)
    securityContext: SecurityContext = Field(default=None, description=r""" Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. """)
    startupProbe: Probe = Field(default=None, description=r""" Probes are not allowed for ephemeral containers. """)
    stdin: bool = Field(default=None, description=r""" Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. """)
    stdinOnce: bool = Field(default=None, description=r""" Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false """)
    targetContainerName: str = Field(default=None, description=r""" If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.  The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined. """)
    terminationMessagePath: str = Field(default=None, description=r""" Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. """)
    terminationMessagePolicy: str = Field(default=None, description=r""" Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. """)
    tty: bool = Field(default=None, description=r""" Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. """)
    volumeDevices: List[VolumeDevice] = Field(default=None, description=r""" volumeDevices is the list of block devices to be used by the container. """)
    volumeMounts: List[VolumeMount] = Field(default=None, description=r""" Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated. """)
    workingDir: str = Field(default=None, description=r""" Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. """)


class EphemeralVolumeSource(BaseModel):
    volumeClaimTemplate: PersistentVolumeClaimTemplate = Field(default=None, description=r""" Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod.  The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).  An existing PVC with that name that is not owned by the pod will *not* be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.  This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.  Required, must not be nil. """)


class EventSeries(BaseModel):
    count: int = Field(default=None, description=r""" count is the number of occurrences in this series up to the last heartbeat time. """)
    lastObservedTime: MicroTime = Field(default=None, description=r""" lastObservedTime is the time when last Event from the series was seen before last heartbeat. """)


class EventSource(BaseModel):
    component: str = Field(default=None, description=r""" Component from which the event is generated. """)
    host: str = Field(default=None, description=r""" Node name on which the event is generated. """)


class Eviction(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    deleteOptions: DeleteOptions = Field(default=None, description=r""" DeleteOptions may be provided """)
    kind: str = Field(default="Eviction", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" ObjectMeta describes the pod that is being evicted. """)


class ExecAction(BaseModel):
    command: List[str] = Field(default=None, description=r""" Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. """)


class ExemptPriorityLevelConfiguration(BaseModel):
    lendablePercent: int = Field(default=None, description=r""" `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels.  This value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 ) """)
    nominalConcurrencyShares: int = Field(default=None, description=r""" `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally reserved for this priority level. This DOES NOT limit the dispatching from this priority level but affects the other priority levels through the borrowing mechanism. The server's concurrency limit (ServerCL) is divided among all the priority levels in proportion to their NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of zero. """)


class ExpressionWarning(BaseModel):
    fieldRef: str = Field(default=None, description=r""" The path to the field that refers the expression. For example, the reference to the expression of the first item of validations is "spec.validations[0].expression" """)
    warning: str = Field(default=None, description=r""" The content of type checking information in a human-readable form. Each line of the warning contains the type that the expression is checked against, followed by the type check error from the compiler. """)


class ExternalDocumentation(BaseModel):
    description: str = Field(default=None)
    url: str = Field(default=None)


class ExternalMetricSource(BaseModel):
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)


class ExternalMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)


class FCVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    lun: int = Field(default=None, description=r""" lun is Optional: FC target lun number """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    targetWWNs: List[str] = Field(default=None, description=r""" targetWWNs is Optional: FC target worldwide names (WWNs) """)
    wwids: List[str] = Field(default=None, description=r""" wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. """)


class FieldsV1(BaseModel):
    pass



class FlexPersistentVolumeSource(BaseModel):
    driver: str = Field(default=None, description=r""" driver is the name of the driver to use for this volume. """)
    fsType: str = Field(default=None, description=r""" fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. """)
    options: dict = Field(default=None, description=r""" options is Optional: this field holds extra command options if any. """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef is Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. """)


class FlexVolumeSource(BaseModel):
    driver: str = Field(default=None, description=r""" driver is the name of the driver to use for this volume. """)
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. """)
    options: dict = Field(default=None, description=r""" options is Optional: this field holds extra command options if any. """)
    readOnly: bool = Field(default=None, description=r""" readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. """)


class FlockerVolumeSource(BaseModel):
    datasetName: str = Field(default=None, description=r""" datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated """)
    datasetUUID: str = Field(default=None, description=r""" datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset """)


class FlowDistinguisherMethod(BaseModel):
    type: str = Field(default=None, description=r""" `type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required. """)


class FlowSchemaCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" `lastTransitionTime` is the last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" `message` is a human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" `reason` is a unique, one-word, CamelCase reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" `status` is the status of the condition. Can be True, False, Unknown. Required. """)
    type: str = Field(default=None, description=r""" `type` is the type of the condition. Required. """)


class ForZone(BaseModel):
    name: str = Field(default=None, description=r""" name represents the name of the zone. """)


class GCEPersistentDiskVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
    partition: int = Field(default=None, description=r""" partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
    pdName: str = Field(default=None, description=r""" pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)


class GRPCAction(BaseModel):
    port: int = Field(default=None, description=r""" Port number of the gRPC service. Number must be in the range 1 to 65535. """)
    service: str = Field(default=None, description=r""" Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).  If this is not specified, the default behavior is defined by gRPC. """)


class GitRepoVolumeSource(BaseModel):
    directory: str = Field(default=None, description=r""" directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. """)
    repository: str = Field(default=None, description=r""" repository is the URL """)
    revision: str = Field(default=None, description=r""" revision is the commit hash for the specified revision. """)


class GlusterfsPersistentVolumeSource(BaseModel):
    endpoints: str = Field(default=None, description=r""" endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
    endpointsNamespace: str = Field(default=None, description=r""" endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
    path: str = Field(default=None, description=r""" path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)


class GlusterfsVolumeSource(BaseModel):
    endpoints: str = Field(default=None, description=r""" endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
    path: str = Field(default=None, description=r""" path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)


class GroupSubject(BaseModel):
    name: str = Field(default=None, description=r""" name is the user group that matches, or "*" to match all user groups. See https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go for some well-known group names. Required. """)


class GroupVersionForDiscovery(BaseModel):
    groupVersion: str = Field(default=None, description=r""" groupVersion specifies the API group and version in the form "group/version" """)
    version: str = Field(default=None, description=r""" version specifies the version in the form of "version". This is to save the clients the trouble of splitting the GroupVersion. """)


class HPAScalingPolicy(BaseModel):
    periodSeconds: int = Field(default=None, description=r""" periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). """)
    type: str = Field(default=None, description=r""" type is used to specify the scaling policy. """)
    value: int = Field(default=None, description=r""" value contains the amount of change which is permitted by the policy. It must be greater than zero """)


class HPAScalingRules(BaseModel):
    policies: List[HPAScalingPolicy] = Field(default=None, description=r""" policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid """)
    selectPolicy: str = Field(default=None, description=r""" selectPolicy is used to specify which policy should be used. If not set, the default value Max is used. """)
    stabilizationWindowSeconds: int = Field(default=None, description=r""" stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). """)


class HTTPGetAction(BaseModel):
    host: str = Field(default=None, description=r""" Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. """)
    httpHeaders: List[HTTPHeader] = Field(default=None, description=r""" Custom headers to set in the request. HTTP allows repeated headers. """)
    path: str = Field(default=None, description=r""" Path to access on the HTTP server. """)
    port: Any = Field(default=None, description=r""" Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. """)
    scheme: str = Field(default=None, description=r""" Scheme to use for connecting to the host. Defaults to HTTP. """)


class HTTPHeader(BaseModel):
    name: str = Field(default=None, description=r""" The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. """)
    value: str = Field(default=None, description=r""" The header field value """)


class HTTPIngressPath(BaseModel):
    backend: IngressBackend = Field(default=None, description=r""" backend defines the referenced service endpoint to which the traffic will be forwarded to. """)
    path: str = Field(default=None, description=r""" path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix". """)
    pathType: str = Field(default=None, description=r""" pathType determines the interpretation of the path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is   done on a path element by element basis. A path element refers is the   list of labels in the path split by the '/' separator. A request is a   match for path p if every p is an element-wise prefix of p of the   request path. Note that if the last element of the path is a substring   of the last element in request path, it is not a match (e.g. /foo/bar   matches /foo/bar/baz, but does not match /foo/barbaz). * ImplementationSpecific: Interpretation of the Path matching is up to   the IngressClass. Implementations can treat this as a separate PathType   or treat it identically to Prefix or Exact path types. Implementations are required to support all path types. """)


class HTTPIngressRuleValue(BaseModel):
    paths: List[HTTPIngressPath] = Field(default=None, description=r""" paths is a collection of paths that map requests to backends. """)


class HorizontalPodAutoscalerBehavior(BaseModel):
    scaleDown: HPAScalingRules = Field(default=None, description=r""" scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used). """)
    scaleUp: HPAScalingRules = Field(default=None, description=r""" scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:   * increase no more than 4 pods per 60 seconds   * double the number of pods per 60 seconds No stabilization is used. """)


class HorizontalPodAutoscalerCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the last time the condition transitioned from one status to another """)
    message: str = Field(default=None, description=r""" message is a human-readable explanation containing details about the transition """)
    reason: str = Field(default=None, description=r""" reason is the reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" status is the status of the condition (True, False, Unknown) """)
    type: str = Field(default=None, description=r""" type describes the current condition """)


class HostAlias(BaseModel):
    hostnames: List[str] = Field(default=None, description=r""" Hostnames for the above IP address. """)
    ip: str = Field(default=None, description=r""" IP address of the host file entry. """)


class HostIP(BaseModel):
    ip: str = Field(default=None, description=r""" IP is the IP address assigned to the host """)


class HostPathVolumeSource(BaseModel):
    path: str = Field(default=None, description=r""" path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)
    type: str = Field(default=None, description=r""" type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)


class IPBlock(BaseModel):
    cidr: str = Field(default=None, description=r""" cidr is a string representing the IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64" """)
    besides: List[str] = Field(default=None, alias="except", description=r""" except is a slice of CIDRs that should not be included within an IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64" Except values will be rejected if they are outside the cidr range """)


class ISCSIPersistentVolumeSource(BaseModel):
    chapAuthDiscovery: bool = Field(default=None, description=r""" chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication """)
    chapAuthSession: bool = Field(default=None, description=r""" chapAuthSession defines whether support iSCSI Session CHAP authentication """)
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi """)
    initiatorName: str = Field(default=None, description=r""" initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection. """)
    iqn: str = Field(default=None, description=r""" iqn is Target iSCSI Qualified Name. """)
    iscsiInterface: str = Field(default=None, description=r""" iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). """)
    lun: int = Field(default=None, description=r""" lun is iSCSI Target Lun number. """)
    portals: List[str] = Field(default=None, description=r""" portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef is the CHAP Secret for iSCSI target and initiator authentication """)
    targetPortal: str = Field(default=None, description=r""" targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)


class ISCSIVolumeSource(BaseModel):
    chapAuthDiscovery: bool = Field(default=None, description=r""" chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication """)
    chapAuthSession: bool = Field(default=None, description=r""" chapAuthSession defines whether support iSCSI Session CHAP authentication """)
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi """)
    initiatorName: str = Field(default=None, description=r""" initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection. """)
    iqn: str = Field(default=None, description=r""" iqn is the target iSCSI Qualified Name. """)
    iscsiInterface: str = Field(default=None, description=r""" iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). """)
    lun: int = Field(default=None, description=r""" lun represents iSCSI Target Lun number. """)
    portals: List[str] = Field(default=None, description=r""" portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is the CHAP Secret for iSCSI target and initiator authentication """)
    targetPortal: str = Field(default=None, description=r""" targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)


class IngressBackend(BaseModel):
    resource: TypedLocalObjectReference = Field(default=None, description=r""" resource is an ObjectRef to another Kubernetes resource in the namespace of the Ingress object. If resource is specified, a service.Name and service.Port must not be specified. This is a mutually exclusive setting with "Service". """)
    service: IngressServiceBackend = Field(default=None, description=r""" service references a service as a backend. This is a mutually exclusive setting with "Resource". """)


class IngressClassParametersReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
    kind: str = Field(default="IngressClassParametersReference", description=r""" kind is the type of resource being referenced. """)
    name: str = Field(default=None, description=r""" name is the name of resource being referenced. """)
    namespace: str = Field(default=None, description=r""" namespace is the namespace of the resource being referenced. This field is required when scope is set to "Namespace" and must be unset when scope is set to "Cluster". """)
    scope: str = Field(default=None, description=r""" scope represents if this refers to a cluster or namespace scoped resource. This may be set to "Cluster" (default) or "Namespace". """)


class IngressLoadBalancerIngress(BaseModel):
    hostname: str = Field(default=None, description=r""" hostname is set for load-balancer ingress points that are DNS based. """)
    ip: str = Field(default=None, description=r""" ip is set for load-balancer ingress points that are IP based. """)
    ports: List[IngressPortStatus] = Field(default=None, description=r""" ports provides information about the ports exposed by this LoadBalancer. """)


class IngressLoadBalancerStatus(BaseModel):
    ingress: List[IngressLoadBalancerIngress] = Field(default=None, description=r""" ingress is a list containing ingress points for the load-balancer. """)


class IngressPortStatus(BaseModel):
    error: str = Field(default=None, description=r""" error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use   CamelCase names - cloud provider specific error values must have names that comply with the   format foo.example.com/CamelCase. """)
    port: int = Field(default=None, description=r""" port is the port number of the ingress port. """)
    protocol: str = Field(default=None, description=r""" protocol is the protocol of the ingress port. The supported values are: "TCP", "UDP", "SCTP" """)


class IngressRule(BaseModel):
    host: str = Field(default=None, description=r""" host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to    the IP in the Spec of the parent Ingress. 2. The `:` delimiter is not respected because ports are not allowed. 	  Currently the port of an Ingress is implicitly :80 for http and 	  :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.  host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '\*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If host is precise, the request matches this rule if the http host header is equal to Host. 2. If host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule. """)
    http: HTTPIngressRuleValue = Field(default=None)


class IngressServiceBackend(BaseModel):
    name: str = Field(default=None, description=r""" name is the referenced service. The service must exist in the same namespace as the Ingress object. """)
    port: ServiceBackendPort = Field(default=None, description=r""" port of the referenced service. A port name or port number is required for a IngressServiceBackend. """)


class IngressTLS(BaseModel):
    hosts: List[str] = Field(default=None, description=r""" hosts is a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified. """)
    secretName: str = Field(default=None, description=r""" secretName is the name of the secret used to terminate TLS traffic on port 443. Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the "Host" header is used for routing. """)


class JSON(BaseModel):
    pass



class JSONSchemaProps(KubeModel):
    json_schema_ref: str = Field(default=None, alias="$ref")
    json_schema_uri: str = Field(default=None, alias="$schema")
    additionalItems: JSONSchemaPropsOrBool = Field(default=None)
    additionalProperties: JSONSchemaPropsOrBool = Field(default=None)
    allOf: List[JSONSchemaProps] = Field(default=None)
    anyOf: List[JSONSchemaProps] = Field(default=None)
    default: JSON = Field(default=None, description=r""" default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. Defaulting requires spec.preserveUnknownFields to be false. """)
    definitions: dict = Field(default=None)
    dependencies: dict = Field(default=None)
    description: str = Field(default=None)
    enum: List[JSON] = Field(default=None)
    example: JSON = Field(default=None)
    exclusiveMaximum: bool = Field(default=None)
    exclusiveMinimum: bool = Field(default=None)
    externalDocs: ExternalDocumentation = Field(default=None)
    format: str = Field(default=None, description=r""" format is an OpenAPI v3 format string. Unknown formats are ignored. The following formats are validated:  - bsonobjectid: a bson object ID, i.e. a 24 characters hex string - uri: an URI as parsed by Golang net/url.ParseRequestURI - email: an email address as parsed by Golang net/mail.ParseAddress - hostname: a valid representation for an Internet host name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid3: an UUID3 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid4: an UUID4 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - uuid5: an UUID5 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - isbn: an ISBN10 or ISBN13 number string like "0321751043" or "978-0321751041" - isbn10: an ISBN10 number string like "0321751043" - isbn13: an ISBN13 number string like "978-0321751041" - creditcard: a credit card number defined by the regex ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$ with any non digit characters mixed in - ssn: a U.S. social security number following the regex ^\d{3}[- ]?\d{2}[- ]?\d{4}$ - hexcolor: an hexadecimal color code like "#FFFFFF: following the regex ^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb like "rgb(255,255,2559" - byte: base64 encoded binary data - password: any kind of string - date: a date string like "2006-01-02" as defined by full-date in RFC3339 - duration: a duration string like "22 ns" as parsed by Golang time.ParseDuration or compatible with Scala duration format - datetime: a date time string like "2014-12-15T19:30:20.000Z" as defined by date-time in RFC3339. """)
    id: str = Field(default=None)
    items: JSONSchemaPropsOrArray = Field(default=None)
    maxItems: int = Field(default=None)
    maxLength: int = Field(default=None)
    maxProperties: int = Field(default=None)
    maximum: float = Field(default=None)
    minItems: int = Field(default=None)
    minLength: int = Field(default=None)
    minProperties: int = Field(default=None)
    minimum: float = Field(default=None)
    multipleOf: float = Field(default=None)
    nay: JSONSchemaProps = Field(default=None, alias="not")
    nullable: bool = Field(default=None)
    oneOf: List[JSONSchemaProps] = Field(default=None)
    pattern: str = Field(default=None)
    patternProperties: dict = Field(default=None)
    properties: dict = Field(default=None)
    required: List[str] = Field(default=None)
    title: str = Field(default=None)
    type: str = Field(default=None)
    uniqueItems: bool = Field(default=None)
    x_kubernetes_embedded_resource: bool = Field(default=None, alias="x-kubernetes-embedded-resource", description=r""" x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata). """)
    x_kubernetes_int_or_string: bool = Field(default=None, alias="x-kubernetes-int-or-string", description=r""" x-kubernetes-int-or-string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:  1) anyOf:    - type: integer    - type: string 2) allOf:    - anyOf:      - type: integer      - type: string    - ... zero or more """)
    x_kubernetes_list_map_keys: List[str] = Field(default=None, alias="x-kubernetes-list-map-keys", description=r""" x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type `map` by specifying the keys used as the index of the map.  This tag MUST only be used on lists that have the "x-kubernetes-list-type" extension set to "map". Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).  The properties specified must either be required or have a default value, to ensure those properties are present for all list items. """)
    x_kubernetes_list_type: str = Field(default=None, alias="x-kubernetes-list-type", description=r""" x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:  1) `atomic`: the list is treated as a single entity, like a scalar.      Atomic lists will be entirely replaced when updated. This extension      may be used on any type of list (struct, scalar, ...). 2) `set`:      Sets are lists that must not have multiple items with the same value. Each      value must be a scalar, an object with x-kubernetes-map-type `atomic` or an      array with x-kubernetes-list-type `atomic`. 3) `map`:      These lists are like maps in that their elements have a non-index key      used to identify them. Order is preserved upon merge. The map tag      must only be used on a list with elements of type object. Defaults to atomic for arrays. """)
    x_kubernetes_map_type: str = Field(default=None, alias="x-kubernetes-map-type", description=r""" x-kubernetes-map-type annotates an object to further describe its topology. This extension must only be used when type is object and may have 2 possible values:  1) `granular`:      These maps are actual maps (key-value pairs) and each fields are independent      from each other (they can each be manipulated by separate actors). This is      the default behaviour for all maps. 2) `atomic`: the list is treated as a single entity, like a scalar.      Atomic maps will be entirely replaced when updated. """)
    x_kubernetes_preserve_unknown_fields: bool = Field(default=None, alias="x-kubernetes-preserve-unknown-fields", description=r""" x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden. """)
    x_kubernetes_validations: List[ValidationRule] = Field(default=None, alias="x-kubernetes-validations", description=r""" x-kubernetes-validations describes a list of validation rules written in the CEL expression language. This field is an alpha-level. Using this field requires the feature gate `CustomResourceValidationExpressions` to be enabled. """)


class JSONSchemaPropsOrArray(BaseModel):
    pass



class JSONSchemaPropsOrBool(BaseModel):
    pass



class JobCondition(BaseModel):
    lastProbeTime: Time = Field(default=None, description=r""" Last time the condition was checked. """)
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transit from one status to another. """)
    message: str = Field(default=None, description=r""" Human readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" (brief) reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of job condition, Complete or Failed. """)


class JobTemplateSpec(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: JobSpec = Field(default=None, description=r""" Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class KeyToPath(BaseModel):
    key: str = Field(default=None, description=r""" key is the key to project. """)
    mode: int = Field(default=None, description=r""" mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
    path: str = Field(default=None, description=r""" path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. """)


class LabelSelector(BaseModel):
    matchExpressions: List[LabelSelectorRequirement] = Field(default=None, description=r""" matchExpressions is a list of label selector requirements. The requirements are ANDed. """)
    matchLabels: dict = Field(default=None, description=r""" matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. """)


class LabelSelectorRequirement(BaseModel):
    key: str = Field(default=None, description=r""" key is the label key that the selector applies to. """)
    operator: str = Field(default=None, description=r""" operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. """)
    values: List[str] = Field(default=None, description=r""" values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. """)


class Lifecycle(BaseModel):
    postStart: LifecycleHandler = Field(default=None, description=r""" PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks """)
    preStop: LifecycleHandler = Field(default=None, description=r""" PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod's termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks """)


class LifecycleHandler(BaseModel):
    exec: ExecAction = Field(default=None, description=r""" Exec specifies the action to take. """)
    httpGet: HTTPGetAction = Field(default=None, description=r""" HTTPGet specifies the http request to perform. """)
    tcpSocket: TCPSocketAction = Field(default=None, description=r""" Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified. """)


class LimitRangeItem(BaseModel):
    default: dict = Field(default=None, description=r""" Default resource requirement limit value by resource name if resource limit is omitted. """)
    defaultRequest: dict = Field(default=None, description=r""" DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. """)
    max: dict = Field(default=None, description=r""" Max usage constraints on this kind by resource name. """)
    maxLimitRequestRatio: dict = Field(default=None, description=r""" MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. """)
    min: dict = Field(default=None, description=r""" Min usage constraints on this kind by resource name. """)
    type: str = Field(default=None, description=r""" Type of resource that this limit applies to. """)


class LimitResponse(BaseModel):
    queuing: QueuingConfiguration = Field(default=None, description=r""" `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `"Queue"`. """)
    type: str = Field(default=None, description=r""" `type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required. """)


class LimitedPriorityLevelConfiguration(BaseModel):
    borrowingLimitPercent: int = Field(default=None, description=r""" `borrowingLimitPercent`, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level's BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level's nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.  BorrowingCL(i) = round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )  The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left `nil`, the limit is effectively infinite. """)
    lendablePercent: int = Field(default=None, description=r""" `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 ) """)
    limitResponse: LimitResponse = Field(default=None, description=r""" `limitResponse` indicates what to do with requests that can not be executed right now """)
    nominalConcurrencyShares: int = Field(default=None, description=r""" `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server's concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of 30. """)


class ListMeta(BaseModel):
    keep_on: str = Field(default=None, alias="continue", description=r""" continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message. """)
    remainingItemCount: int = Field(default=None, description=r""" remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact. """)
    resourceVersion: str = Field(default=None, description=r""" String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency """)
    selfLink: str = Field(default=None, description=r""" Deprecated: selfLink is a legacy read-only field that is no longer populated by the system. """)


class LoadBalancerIngress(BaseModel):
    hostname: str = Field(default=None, description=r""" Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers) """)
    ip: str = Field(default=None, description=r""" IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers) """)
    ports: List[PortStatus] = Field(default=None, description=r""" Ports is a list of records of service ports If used, every port defined in the service should have an entry in it """)


class LoadBalancerStatus(BaseModel):
    ingress: List[LoadBalancerIngress] = Field(default=None, description=r""" Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. """)


class LocalObjectReference(BaseModel):
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)


class LocalVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified. """)
    path: str = Field(default=None, description=r""" path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, ...). """)


class ManagedFieldsEntry(BaseModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted. """)
    fieldsType: str = Field(default=None, description=r""" FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1" """)
    fieldsV1: FieldsV1 = Field(default=None, description=r""" FieldsV1 holds the first JSON version format as described in the "FieldsV1" type. """)
    manager: str = Field(default=None, description=r""" Manager is an identifier of the workflow managing these fields. """)
    operation: str = Field(default=None, description=r""" Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'. """)
    subresource: str = Field(default=None, description=r""" Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource. """)
    time: Time = Field(default=None, description=r""" Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be updated if a field is added, the manager changes any of the owned fields value or removes a field. The timestamp does not update when a field is removed from the entry because another manager took it over. """)


class MatchCondition(BaseModel):
    expression: str = Field(default=None, description=r""" Expression represents the expression which will be evaluated by CEL. Must evaluate to bool. CEL expressions have access to the contents of the AdmissionRequest and Authorizer, organized into CEL variables:  'object' - The object from the incoming request. The value is null for DELETE requests. 'oldObject' - The existing object. The value is null for CREATE requests. 'request' - Attributes of the admission request(/pkg/apis/admission/types.go#AdmissionRequest). 'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal (user or service account) of the request.   See https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz 'authorizer.requestResource' - A CEL ResourceCheck constructed from the 'authorizer' and configured with the   request resource. Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/  Required. """)
    name: str = Field(default=None, description=r""" Name is an identifier for this match condition, used for strategic merging of MatchConditions, as well as providing an identifier for logging purposes. A good name should be descriptive of the associated expression. Name must be a qualified name consisting of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName',  or 'my.name',  or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]') with an optional DNS subdomain prefix and '/' (e.g. 'example.com/MyName')  Required. """)


class MatchResources(BaseModel):
    excludeResourceRules: List[NamedRuleWithOperations] = Field(default=None, description=r""" ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded) """)
    matchPolicy: str = Field(default=None, description=r""" matchPolicy defines how the "MatchResources" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the ValidatingAdmissionPolicy.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the ValidatingAdmissionPolicy.  Defaults to "Equivalent" """)
    namespaceSelector: LabelSelector = Field(default=None, description=r""" NamespaceSelector decides whether to run the admission control policy on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the policy.  For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1";  you will set the selector as follows: "namespaceSelector": {   "matchExpressions": [     {       "key": "runlevel",       "operator": "NotIn",       "values": [         "0",         "1"       ]     }   ] }  If instead you want to only run the policy on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": {   "matchExpressions": [     {       "key": "environment",       "operator": "In",       "values": [         "prod",         "staging"       ]     }   ] }  See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ for more examples of label selectors.  Default to the empty LabelSelector, which matches everything. """)
    objectSelector: LabelSelector = Field(default=None, description=r""" ObjectSelector decides whether to run the validation based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the cel validation, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything. """)
    resourceRules: List[NamedRuleWithOperations] = Field(default=None, description=r""" ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches _any_ Rule. """)


class MetricIdentifier(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the given metric """)
    selector: LabelSelector = Field(default=None, description=r""" selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics. """)


class MetricSpec(BaseModel):
    containerResource: ContainerResourceMetricSource = Field(default=None, description=r""" containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag. """)
    external: ExternalMetricSource = Field(default=None, description=r""" external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). """)
    object: ObjectMetricSource = Field(default=None, description=r""" object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). """)
    pods: PodsMetricSource = Field(default=None, description=r""" pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. """)
    resource: ResourceMetricSource = Field(default=None, description=r""" resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    type: str = Field(default=None, description=r""" type is the type of metric source.  It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled """)


class MetricStatus(BaseModel):
    containerResource: ContainerResourceMetricStatus = Field(default=None, description=r""" container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    external: ExternalMetricStatus = Field(default=None, description=r""" external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). """)
    object: ObjectMetricStatus = Field(default=None, description=r""" object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). """)
    pods: PodsMetricStatus = Field(default=None, description=r""" pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. """)
    resource: ResourceMetricStatus = Field(default=None, description=r""" resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """)
    type: str = Field(default=None, description=r""" type is the type of metric source.  It will be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each corresponds to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled """)


class MetricTarget(BaseModel):
    averageUtilization: int = Field(default=None, description=r""" averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type """)
    averageValue: Quantity = Field(default=None, description=r""" averageValue is the target value of the average of the metric across all relevant pods (as a quantity) """)
    type: str = Field(default=None, description=r""" type represents whether the metric type is Utilization, Value, or AverageValue """)
    value: Quantity = Field(default=None, description=r""" value is the target value of the metric (as a quantity). """)


class MetricValueStatus(BaseModel):
    averageUtilization: int = Field(default=None, description=r""" currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. """)
    averageValue: Quantity = Field(default=None, description=r""" averageValue is the current value of the average of the metric across all relevant pods (as a quantity) """)
    value: Quantity = Field(default=None, description=r""" value is the current value of the metric (as a quantity). """)


class MicroTime(BaseModel):
    pass



class MutatingWebhook(BaseModel):
    admissionReviewVersions: List[str] = Field(default=None, description=r""" AdmissionReviewVersions is an ordered list of preferred `AdmissionReview` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. """)
    clientConfig: WebhookClientConfig = Field(default=None, description=r""" ClientConfig defines how to communicate with the hook. Required """)
    failurePolicy: str = Field(default=None, description=r""" FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail. """)
    matchConditions: List[MatchCondition] = Field(default=None, description=r""" MatchConditions is a list of conditions that must be met for a request to be sent to this webhook. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  The exact matching logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the webhook is skipped.   2. If ALL matchConditions evaluate to TRUE, the webhook is called.   3. If any matchCondition evaluates to an error (but none are FALSE):      - If failurePolicy=Fail, reject the request      - If failurePolicy=Ignore, the error is ignored and the webhook is skipped  This is a beta feature and managed by the AdmissionWebhookMatchConditions feature gate. """)
    matchPolicy: str = Field(default=None, description=r""" matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.  Defaults to "Equivalent" """)
    name: str = Field(default=None, description=r""" The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required. """)
    namespaceSelector: LabelSelector = Field(default=None, description=r""" NamespaceSelector decides whether to run the webhook on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the webhook.  For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1";  you will set the selector as follows: "namespaceSelector": {   "matchExpressions": [     {       "key": "runlevel",       "operator": "NotIn",       "values": [         "0",         "1"       ]     }   ] }  If instead you want to only run the webhook on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": {   "matchExpressions": [     {       "key": "environment",       "operator": "In",       "values": [         "prod",         "staging"       ]     }   ] }  See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ for more examples of label selectors.  Default to the empty LabelSelector, which matches everything. """)
    objectSelector: LabelSelector = Field(default=None, description=r""" ObjectSelector decides whether to run the webhook based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the webhook, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything. """)
    reinvocationPolicy: str = Field(default=None, description=r""" reinvocationPolicy indicates whether this webhook should be called multiple times as part of a single admission evaluation. Allowed values are "Never" and "IfNeeded".  Never: the webhook will not be called more than once in a single admission evaluation.  IfNeeded: the webhook will be called at least one additional time as part of the admission evaluation if the object being admitted is modified by other admission plugins after the initial webhook call. Webhooks that specify this option *must* be idempotent, able to process objects they previously admitted. Note: * the number of additional invocations is not guaranteed to be exactly one. * if additional invocations result in further modifications to the object, webhooks are not guaranteed to be invoked again. * webhooks that use this option may be reordered to minimize the number of additional invocations. * to validate an object after all mutations are guaranteed complete, use a validating admission webhook instead.  Defaults to "Never". """)
    rules: List[RuleWithOperations] = Field(default=None, description=r""" Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects. """)
    sideEffects: str = Field(default=None, description=r""" SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. """)
    timeoutSeconds: int = Field(default=None, description=r""" TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds. """)


class NFSVolumeSource(BaseModel):
    path: str = Field(default=None, description=r""" path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
    server: str = Field(default=None, description=r""" server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)


class NamedRuleWithOperations(BaseModel):
    apiGroups: List[str] = Field(default=None, description=r""" APIGroups is the API groups the resources belong to. '\*' is all groups. If '\*' is present, the length of the slice must be one. Required. """)
    apiVersions: List[str] = Field(default=None, description=r""" APIVersions is the API versions the resources belong to. '\*' is all versions. If '\*' is present, the length of the slice must be one. Required. """)
    operations: List[str] = Field(default=None, description=r""" Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '\*' is present, the length of the slice must be one. Required. """)
    resourceNames: List[str] = Field(default=None, description=r""" ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. """)
    resources: List[str] = Field(default=None, description=r""" Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '\*' means all resources, but not subresources. 'pods/\*' means all subresources of pods. '\*/scale' means all scale subresources. '\*/\*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required. """)
    scope: str = Field(default=None, description=r""" scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "*" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "*" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*". """)


class NamespaceCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None)
    message: str = Field(default=None)
    reason: str = Field(default=None)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of namespace controller condition. """)


class NetworkPolicyEgressRule(BaseModel):
    ports: List[NetworkPolicyPort] = Field(default=None, description=r""" ports is a list of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. """)
    to: List[NetworkPolicyPeer] = Field(default=None, description=r""" to is a list of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list. """)


class NetworkPolicyIngressRule(BaseModel):
    sources: List[NetworkPolicyPeer] = Field(default=None, alias="from", description=r""" from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list. """)
    ports: List[NetworkPolicyPort] = Field(default=None, description=r""" ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. """)


class NetworkPolicyPeer(BaseModel):
    ipBlock: IPBlock = Field(default=None, description=r""" ipBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be. """)
    namespaceSelector: LabelSelector = Field(default=None, description=r""" namespaceSelector selects namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.  If podSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the namespaces selected by namespaceSelector. Otherwise it selects all pods in the namespaces selected by namespaceSelector. """)
    podSelector: LabelSelector = Field(default=None, description=r""" podSelector is a label selector which selects pods. This field follows standard label selector semantics; if present but empty, it selects all pods.  If namespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the pods matching podSelector in the policy's own namespace. """)


class NetworkPolicyPort(BaseModel):
    endPort: int = Field(default=None, description=r""" endPort indicates that the range of ports from port to endPort if set, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port. """)
    port: Any = Field(default=None, description=r""" port represents the port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched. """)
    protocol: str = Field(default=None, description=r""" protocol represents the protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP. """)


class NodeAddress(BaseModel):
    address: str = Field(default=None, description=r""" The node address. """)
    type: str = Field(default=None, description=r""" Node address type, one of Hostname, ExternalIP or InternalIP. """)


class NodeAffinity(BaseModel):
    preferredDuringSchedulingIgnoredDuringExecution: List[PreferredSchedulingTerm] = Field(default=None, description=r""" The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred. """)
    requiredDuringSchedulingIgnoredDuringExecution: NodeSelector = Field(default=None, description=r""" If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node. """)


class NodeCondition(BaseModel):
    lastHeartbeatTime: Time = Field(default=None, description=r""" Last time we got an update on a given condition. """)
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transit from one status to another. """)
    message: str = Field(default=None, description=r""" Human readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" (brief) reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of node condition. """)


class NodeConfigSource(BaseModel):
    configMap: ConfigMapNodeConfigSource = Field(default=None, description=r""" ConfigMap is a reference to a Node's ConfigMap """)


class NodeConfigStatus(BaseModel):
    active: NodeConfigSource = Field(default=None, description=r""" Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error. """)
    assigned: NodeConfigSource = Field(default=None, description=r""" Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned. """)
    error: str = Field(default=None, description=r""" Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions. """)
    lastKnownGood: NodeConfigSource = Field(default=None, description=r""" LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future. """)


class NodeDaemonEndpoints(BaseModel):
    kubeletEndpoint: DaemonEndpoint = Field(default=None, description=r""" Endpoint on which Kubelet is listening. """)


class NodeSelector(BaseModel):
    nodeSelectorTerms: List[NodeSelectorTerm] = Field(default=None, description=r""" Required. A list of node selector terms. The terms are ORed. """)


class NodeSelectorRequirement(BaseModel):
    key: str = Field(default=None, description=r""" The label key that the selector applies to. """)
    operator: str = Field(default=None, description=r""" Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt. """)
    values: List[str] = Field(default=None, description=r""" An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. """)


class NodeSelectorTerm(BaseModel):
    matchExpressions: List[NodeSelectorRequirement] = Field(default=None, description=r""" A list of node selector requirements by node's labels. """)
    matchFields: List[NodeSelectorRequirement] = Field(default=None, description=r""" A list of node selector requirements by node's fields. """)


class NodeSystemInfo(BaseModel):
    architecture: str = Field(default=None, description=r""" The Architecture reported by the node """)
    bootID: str = Field(default=None, description=r""" Boot ID reported by the node. """)
    containerRuntimeVersion: str = Field(default=None, description=r""" ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2). """)
    kernelVersion: str = Field(default=None, description=r""" Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64). """)
    kubeProxyVersion: str = Field(default=None, description=r""" KubeProxy Version reported by the node. """)
    kubeletVersion: str = Field(default=None, description=r""" Kubelet Version reported by the node. """)
    machineID: str = Field(default=None, description=r""" MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html """)
    operatingSystem: str = Field(default=None, description=r""" The Operating System reported by the node """)
    osImage: str = Field(default=None, description=r""" OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)). """)
    systemUUID: str = Field(default=None, description=r""" SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid """)


class NonResourceAttributes(BaseModel):
    path: str = Field(default=None, description=r""" Path is the URL path of the request """)
    verb: str = Field(default=None, description=r""" Verb is the standard HTTP verb """)


class NonResourcePolicyRule(BaseModel):
    nonResourceURLs: List[str] = Field(default=None, description=r""" `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:   - "/healthz" is legal   - "/hea*" is illegal   - "/hea" is legal but matches nothing   - "/hea/*" also matches nothing   - "/healthz/*" matches all per-component health checks. "*" matches all non-resource urls. if it is present, it must be the only entry. Required. """)
    verbs: List[str] = Field(default=None, description=r""" `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs. If it is present, it must be the only entry. Required. """)


class NonResourceRule(BaseModel):
    nonResourceURLs: List[str] = Field(default=None, description=r""" NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all. """)
    verbs: List[str] = Field(default=None, description=r""" Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all. """)


class ObjectFieldSelector(BaseModel):
    apiVersion: str = Field(default="v1", description=r""" Version of the schema the FieldPath is written in terms of, defaults to "v1". """)
    fieldPath: str = Field(default=None, description=r""" Path of the field to select in the specified API version. """)


class ObjectMeta(BaseModel):
    annotations: dict = Field(default=None, description=r""" Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations """)
    creationTimestamp: Time = Field(default=None, description=r""" CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.  Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    deletionGracePeriodSeconds: int = Field(default=None, description=r""" Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only. """)
    deletionTimestamp: Time = Field(default=None, description=r""" DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.  Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    finalizers: List[str] = Field(default=None, description=r""" Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list. """)
    generateName: str = Field(default=None, description=r""" GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will return a 409.  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency """)
    generation: int = Field(default=None, description=r""" A sequence number representing a specific generation of the desired state. Populated by the system. Read-only. """)
    labels: dict = Field(default=None, description=r""" Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels """)
    managedFields: List[ManagedFieldsEntry] = Field(default=None, description=r""" ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object. """)
    name: str = Field(default=None, description=r""" Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names """)
    namespace: str = Field(default=None, description=r""" Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces """)
    ownerReferences: List[OwnerReference] = Field(default=None, description=r""" List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller. """)
    resourceVersion: str = Field(default=None, description=r""" An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency """)
    selfLink: str = Field(default=None, description=r""" Deprecated: selfLink is a legacy read-only field that is no longer populated by the system. """)
    uid: str = Field(default=None, description=r""" UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids """)


class ObjectMetricSource(KubeModel):
    describedObject: CrossVersionObjectReference = Field(default=None, description=r""" describedObject specifies the descriptions of a object,such as kind,name apiVersion """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)


class ObjectMetricStatus(KubeModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    describedObject: CrossVersionObjectReference = Field(default=None, description=r""" DescribedObject specifies the descriptions of a object,such as kind,name apiVersion """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)


class ObjectReference(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" API version of the referent. """)
    fieldPath: str = Field(default=None, description=r""" If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. """)
    kind: str = Field(default="ObjectReference", description=r""" Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    namespace: str = Field(default=None, description=r""" Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ """)
    resourceVersion: str = Field(default=None, description=r""" Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency """)
    uid: str = Field(default=None, description=r""" UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids """)


class Overhead(BaseModel):
    podFixed: dict = Field(default=None, description=r""" podFixed represents the fixed resource overhead associated with running a pod. """)


class OwnerReference(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" API version of the referent. """)
    blockOwnerDeletion: bool = Field(default=None, description=r""" If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned. """)
    controller: bool = Field(default=None, description=r""" If true, this reference points to the managing controller. """)
    kind: str = Field(default="OwnerReference", description=r""" Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names """)
    uid: str = Field(default=None, description=r""" UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids """)


class ParamKind(KubeModel):
    apiVersion: str = Field(default="v1beta1", description=r""" APIVersion is the API group version the resources belong to. In format of "group/version". Required. """)
    kind: str = Field(default="ParamKind", description=r""" Kind is the API kind the resources belong to. Required. """)


class ParamRef(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the resource being referenced.  One of `name` or `selector` must be set, but `name` and `selector` are mutually exclusive properties. If one is set, the other must be unset.  A single parameter used for all admission requests can be configured by setting the `name` field, leaving `selector` blank, and setting namespace if `paramKind` is namespace-scoped. """)
    namespace: str = Field(default=None, description=r""" namespace is the namespace of the referenced resource. Allows limiting the search for params to a specific namespace. Applies to both `name` and `selector` fields.  A per-namespace parameter may be used by specifying a namespace-scoped `paramKind` in the policy and leaving this field empty.  - If `paramKind` is cluster-scoped, this field MUST be unset. Setting this field results in a configuration error.  - If `paramKind` is namespace-scoped, the namespace of the object being evaluated for admission will be used when this field is left unset. Take care that if this is left empty the binding must not match any cluster-scoped resources, which will result in an error. """)
    parameterNotFoundAction: str = Field(default=None, description=r""" `parameterNotFoundAction` controls the behavior of the binding when the resource exists, and name or selector is valid, but there are no parameters matched by the binding. If the value is set to `Allow`, then no matched parameters will be treated as successful validation by the binding. If set to `Deny`, then no matched parameters will be subject to the `failurePolicy` of the policy.  Allowed values are `Allow` or `Deny`  Required """)
    selector: LabelSelector = Field(default=None, description=r""" selector can be used to match multiple param objects based on their labels. Supply selector: {} to match all resources of the ParamKind.  If multiple params are found, they are all evaluated with the policy expressions and the results are ANDed together.  One of `name` or `selector` must be set, but `name` and `selector` are mutually exclusive properties. If one is set, the other must be unset. """)


class ParentReference(BaseModel):
    group: str = Field(default=None, description=r""" Group is the group of the object being referenced. """)
    name: str = Field(default=None, description=r""" Name is the name of the object being referenced. """)
    namespace: str = Field(default=None, description=r""" Namespace is the namespace of the object being referenced. """)
    resource: str = Field(default=None, description=r""" Resource is the resource of the object being referenced. """)
    uid: str = Field(default=None, description=r""" UID is the uid of the object being referenced. """)


class Patch(BaseModel):
    pass



class PersistentVolumeClaimCondition(BaseModel):
    lastProbeTime: Time = Field(default=None, description=r""" lastProbeTime is the time we probed the condition. """)
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" message is the human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized. """)
    status: str = Field(default=None)
    type: str = Field(default=None)


class PersistentVolumeClaimTemplate(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """)
    spec: PersistentVolumeClaimSpec = Field(default=None, description=r""" The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here. """)


class PersistentVolumeClaimVolumeSource(BaseModel):
    claimName: str = Field(default=None, description=r""" claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
    readOnly: bool = Field(default=None, description=r""" readOnly Will force the ReadOnly setting in VolumeMounts. Default false. """)


class PhotonPersistentDiskVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    pdID: str = Field(default=None, description=r""" pdID is the ID that identifies Photon Controller persistent disk """)


class PodAffinity(BaseModel):
    preferredDuringSchedulingIgnoredDuringExecution: List[WeightedPodAffinityTerm] = Field(default=None, description=r""" The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. """)
    requiredDuringSchedulingIgnoredDuringExecution: List[PodAffinityTerm] = Field(default=None, description=r""" If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. """)


class PodAffinityTerm(BaseModel):
    labelSelector: LabelSelector = Field(default=None, description=r""" A label query over a set of resources, in this case pods. """)
    namespaceSelector: LabelSelector = Field(default=None, description=r""" A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces. """)
    namespaces: List[str] = Field(default=None, description=r""" namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace". """)
    topologyKey: str = Field(default=None, description=r""" This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. """)


class PodAntiAffinity(BaseModel):
    preferredDuringSchedulingIgnoredDuringExecution: List[WeightedPodAffinityTerm] = Field(default=None, description=r""" The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. """)
    requiredDuringSchedulingIgnoredDuringExecution: List[PodAffinityTerm] = Field(default=None, description=r""" If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. """)


class PodCondition(BaseModel):
    lastProbeTime: Time = Field(default=None, description=r""" Last time we probed the condition. """)
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" Human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" Unique, one-word, CamelCase reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """)
    type: str = Field(default=None, description=r""" Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """)


class PodDNSConfig(BaseModel):
    nameservers: List[str] = Field(default=None, description=r""" A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed. """)
    options: List[PodDNSConfigOption] = Field(default=None, description=r""" A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy. """)
    searches: List[str] = Field(default=None, description=r""" A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed. """)


class PodDNSConfigOption(BaseModel):
    name: str = Field(default=None, description=r""" Required. """)
    value: str = Field(default=None)


class PodFailurePolicy(BaseModel):
    rules: List[PodFailurePolicyRule] = Field(default=None, description=r""" A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed. """)


class PodFailurePolicyOnExitCodesRequirement(BaseModel):
    containerName: str = Field(default=None, description=r""" Restricts the check for exit codes to the container with the specified name. When null, the rule applies to all containers. When specified, it should match one the container or initContainer names in the pod template. """)
    operator: str = Field(default=None, description=r""" Represents the relationship between the container exit code(s) and the specified values. Containers completed with success (exit code 0) are excluded from the requirement check. Possible values are:  - In: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the 'containerName' field) is in the set of specified values. - NotIn: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the 'containerName' field) is not in the set of specified values. Additional values are considered to be added in the future. Clients should react to an unknown operator by assuming the requirement is not satisfied. """)
    values: List[int] = Field(default=None, description=r""" Specifies the set of values. Each returned container exit code (might be multiple in case of multiple containers) is checked against this set of values with respect to the operator. The list of values must be ordered and must not contain duplicates. Value '0' cannot be used for the In operator. At least one element is required. At most 255 elements are allowed. """)


class PodFailurePolicyOnPodConditionsPattern(BaseModel):
    status: str = Field(default=None, description=r""" Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True. """)
    type: str = Field(default=None, description=r""" Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type. """)


class PodFailurePolicyRule(BaseModel):
    action: str = Field(default=None, description=r""" Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are:  - FailJob: indicates that the pod's job is marked as Failed and all   running pods are terminated. - FailIndex: indicates that the pod's index is marked as Failed and will   not be restarted.   This value is alpha-level. It can be used when the   `JobBackoffLimitPerIndex` feature gate is enabled (disabled by default). - Ignore: indicates that the counter towards the .backoffLimit is not   incremented and a replacement pod is created. - Count: indicates that the pod is handled in the default way - the   counter towards the .backoffLimit is incremented. Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule. """)
    onExitCodes: PodFailurePolicyOnExitCodesRequirement = Field(default=None, description=r""" Represents the requirement on the container exit codes. """)
    onPodConditions: List[PodFailurePolicyOnPodConditionsPattern] = Field(default=None, description=r""" Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed. """)


class PodIP(BaseModel):
    ip: str = Field(default=None, description=r""" IP is the IP address assigned to the pod """)


class PodOS(BaseModel):
    name: str = Field(default=None, description=r""" Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration Clients should expect to handle additional values and treat unrecognized values in this field as os: null """)


class PodReadinessGate(BaseModel):
    conditionType: str = Field(default=None, description=r""" ConditionType refers to a condition in the pod's condition list with matching type. """)


class PodResourceClaim(BaseModel):
    name: str = Field(default=None, description=r""" Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL. """)
    source: ClaimSource = Field(default=None, description=r""" Source describes where to find the ResourceClaim. """)


class PodSchedulingGate(BaseModel):
    name: str = Field(default=None, description=r""" Name of the scheduling gate. Each scheduling gate must have a unique name field. """)


class PodSecurityContext(BaseModel):
    fsGroup: int = Field(default=None, description=r""" A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows. """)
    fsGroupChangePolicy: str = Field(default=None, description=r""" fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows. """)
    runAsGroup: int = Field(default=None, description=r""" The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """)
    runAsNonRoot: bool = Field(default=None, description=r""" Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """)
    runAsUser: int = Field(default=None, description=r""" The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """)
    seLinuxOptions: SELinuxOptions = Field(default=None, description=r""" The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """)
    seccompProfile: SeccompProfile = Field(default=None, description=r""" The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows. """)
    supplementalGroups: List[int] = Field(default=None, description=r""" A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows. """)
    sysctls: List[Sysctl] = Field(default=None, description=r""" Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows. """)
    windowsOptions: WindowsSecurityContextOptions = Field(default=None, description=r""" The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. """)


class PodsMetricSource(BaseModel):
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)


class PodsMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    metric: MetricIdentifier = Field(default=None, description=r""" metric identifies the target metric by name and selector """)


class PolicyRule(BaseModel):
    apiGroups: List[str] = Field(default=None, description=r""" APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "*" represents all API groups. """)
    nonResourceURLs: List[str] = Field(default=None, description=r""" NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both. """)
    resourceNames: List[str] = Field(default=None, description=r""" ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. """)
    resources: List[str] = Field(default=None, description=r""" Resources is a list of resources this rule applies to. '\*' represents all resources. """)
    verbs: List[str] = Field(default=None, description=r""" Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '\*' represents all verbs. """)


class PolicyRulesWithSubjects(BaseModel):
    nonResourceRules: List[NonResourcePolicyRule] = Field(default=None, description=r""" `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL. """)
    resourceRules: List[ResourcePolicyRule] = Field(default=None, description=r""" `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty. """)
    subjects: List[Subject] = Field(default=None, description=r""" subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required. """)


class PortStatus(BaseModel):
    error: str = Field(default=None, description=r""" Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use   CamelCase names - cloud provider specific error values must have names that comply with the   format foo.example.com/CamelCase. """)
    port: int = Field(default=None, description=r""" Port is the port number of the service port of which status is recorded here """)
    protocol: str = Field(default=None, description=r""" Protocol is the protocol of the service port of which status is recorded here The supported values are: "TCP", "UDP", "SCTP" """)


class PortworxVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. """)
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    volumeID: str = Field(default=None, description=r""" volumeID uniquely identifies a Portworx volume """)


class Preconditions(BaseModel):
    resourceVersion: str = Field(default=None, description=r""" Specifies the target ResourceVersion """)
    uid: str = Field(default=None, description=r""" Specifies the target UID. """)


class PreferredSchedulingTerm(BaseModel):
    preference: NodeSelectorTerm = Field(default=None, description=r""" A node selector term, associated with the corresponding weight. """)
    weight: int = Field(default=None, description=r""" Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. """)


class PriorityLevelConfigurationCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" `lastTransitionTime` is the last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" `message` is a human-readable message indicating details about last transition. """)
    reason: str = Field(default=None, description=r""" `reason` is a unique, one-word, CamelCase reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" `status` is the status of the condition. Can be True, False, Unknown. Required. """)
    type: str = Field(default=None, description=r""" `type` is the type of the condition. Required. """)


class PriorityLevelConfigurationReference(BaseModel):
    name: str = Field(default=None, description=r""" `name` is the name of the priority level configuration being referenced Required. """)


class Probe(BaseModel):
    exec: ExecAction = Field(default=None, description=r""" Exec specifies the action to take. """)
    failureThreshold: int = Field(default=None, description=r""" Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. """)
    grpc: GRPCAction = Field(default=None, description=r""" GRPC specifies an action involving a GRPC port. """)
    httpGet: HTTPGetAction = Field(default=None, description=r""" HTTPGet specifies the http request to perform. """)
    initialDelaySeconds: int = Field(default=None, description=r""" Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)
    periodSeconds: int = Field(default=None, description=r""" How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. """)
    successThreshold: int = Field(default=None, description=r""" Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. """)
    tcpSocket: TCPSocketAction = Field(default=None, description=r""" TCPSocket specifies an action involving a TCP port. """)
    terminationGracePeriodSeconds: int = Field(default=None, description=r""" Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. """)
    timeoutSeconds: int = Field(default=None, description=r""" Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)


class ProjectedVolumeSource(BaseModel):
    defaultMode: int = Field(default=None, description=r""" defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
    sources: List[VolumeProjection] = Field(default=None, description=r""" sources is the list of volume projections """)


class Quantity(BaseModel):
    pass



class QueuingConfiguration(BaseModel):
    handSize: int = Field(default=None, description=r""" `handSize` is a small positive number that configures the shuffle sharding of requests into queues.  When enqueuing a request at this priority level the request's flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here.  The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues).  See the user-facing documentation for more extensive guidance on setting this field.  This field has a default value of 8. """)
    queueLengthLimit: int = Field(default=None, description=r""" `queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected.  This value must be positive.  If not specified, it will be defaulted to 50. """)
    queues: int = Field(default=None, description=r""" `queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive.  Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant.  This field has a default value of 64. """)


class QuobyteVolumeSource(BaseModel):
    group: str = Field(default=None, description=r""" group to map volume access to Default is no group """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. """)
    registry: str = Field(default=None, description=r""" registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes """)
    tenant: str = Field(default=None, description=r""" tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin """)
    user: str = Field(default=None, description=r""" user to map volume access to Defaults to serivceaccount user """)
    volume: str = Field(default=None, description=r""" volume is a string that references an already created Quobyte volume by name. """)


class RBDPersistentVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd """)
    image: str = Field(default=None, description=r""" image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    keyring: str = Field(default=None, description=r""" keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    monitors: List[str] = Field(default=None, description=r""" monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    pool: str = Field(default=None, description=r""" pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    user: str = Field(default=None, description=r""" user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)


class RBDVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd """)
    image: str = Field(default=None, description=r""" image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    keyring: str = Field(default=None, description=r""" keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    monitors: List[str] = Field(default=None, description=r""" monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    pool: str = Field(default=None, description=r""" pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
    user: str = Field(default=None, description=r""" user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)


class ReplicaSetCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" The last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
    reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of replica set condition. """)


class ReplicationControllerCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" The last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
    reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of replication controller condition. """)


class ResourceAttributes(BaseModel):
    group: str = Field(default=None, description=r""" Group is the API Group of the Resource.  "*" means all. """)
    name: str = Field(default=None, description=r""" Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all. """)
    namespace: str = Field(default=None, description=r""" Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview """)
    resource: str = Field(default=None, description=r""" Resource is one of the existing resource types.  "*" means all. """)
    subresource: str = Field(default=None, description=r""" Subresource is one of the existing resource types.  "" means none. """)
    verb: str = Field(default=None, description=r""" Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all. """)
    version: str = Field(default=None, description=r""" Version is the API Version of the Resource.  "*" means all. """)


class ResourceClaimV1(BaseModel):
    name: str = Field(default=None, description=r""" Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. """)


class ResourceClaimConsumerReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced. """)
    resource: str = Field(default=None, description=r""" Resource is the type of resource being referenced, for example "pods". """)
    uid: str = Field(default=None, description=r""" UID identifies exactly one incarnation of the resource. """)


class ResourceClaimParametersReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """)
    kind: str = Field(default="ResourceClaimParametersReference", description=r""" Kind is the type of resource being referenced. This is the same value as in the parameter object's metadata, for example "ConfigMap". """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced. """)


class ResourceClaimSchedulingStatus(BaseModel):
    name: str = Field(default=None, description=r""" Name matches the pod.spec.resourceClaims[*].Name field. """)
    unsuitableNodes: List[str] = Field(default=None, description=r""" UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced. """)


class ResourceClassParametersReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """)
    kind: str = Field(default="ResourceClassParametersReference", description=r""" Kind is the type of resource being referenced. This is the same value as in the parameter object's metadata. """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced. """)
    namespace: str = Field(default=None, description=r""" Namespace that contains the referenced resource. Must be empty for cluster-scoped resources and non-empty for namespaced resources. """)


class ResourceFieldSelector(BaseModel):
    containerName: str = Field(default=None, description=r""" Container name: required for volumes, optional for env vars """)
    divisor: Quantity = Field(default=None, description=r""" Specifies the output format of the exposed resources, defaults to "1" """)
    resource: str = Field(default=None, description=r""" Required: resource to select """)


class ResourceHandle(BaseModel):
    data: str = Field(default=None, description=r""" Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced. """)
    driverName: str = Field(default=None, description=r""" DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle's data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in. """)


class ResourceMetricSource(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
    target: MetricTarget = Field(default=None, description=r""" target specifies the target value for the given metric """)


class ResourceMetricStatus(BaseModel):
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)


class ResourcePolicyRule(BaseModel):
    apiGroups: List[str] = Field(default=None, description=r""" `apiGroups` is a list of matching API groups and may not be empty. "*" matches all API groups and, if present, must be the only entry. Required. """)
    clusterScope: bool = Field(default=None, description=r""" `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list. """)
    namespaces: List[str] = Field(default=None, description=r""" `namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains "*".  Note that "*" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true. """)
    resources: List[str] = Field(default=None, description=r""" `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ "services", "nodes/status" ].  This list may not be empty. "*" matches all resources and, if present, must be the only entry. Required. """)
    verbs: List[str] = Field(default=None, description=r""" `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs and, if present, must be the only entry. Required. """)


class ResourceRequirements(BaseModel):
    claims: List[ResourceClaimV1] = Field(default=None, description=r""" Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. """)
    limits: dict = Field(default=None, description=r""" Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """)
    requests: dict = Field(default=None, description=r""" Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """)


class ResourceRule(BaseModel):
    apiGroups: List[str] = Field(default=None, description=r""" APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  "*" means all. """)
    resourceNames: List[str] = Field(default=None, description=r""" ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  "*" means all. """)
    resources: List[str] = Field(default=None, description=r""" Resources is a list of resources this rule applies to.  "*" means all in the specified apiGroups.  "*/foo" represents the subresource 'foo' for all resources in the specified apiGroups. """)
    verbs: List[str] = Field(default=None, description=r""" Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  "*" means all. """)


class RoleRef(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced """)
    kind: str = Field(default="RoleRef", description=r""" Kind is the type of resource being referenced """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)


class RollingUpdateStatefulSetStrategy(BaseModel):
    maxUnavailable: Any = Field(default=None, description=r""" The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable. """)
    partition: int = Field(default=None, description=r""" Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0. """)


class RuleWithOperations(BaseModel):
    apiGroups: List[str] = Field(default=None, description=r""" APIGroups is the API groups the resources belong to. '\*' is all groups. If '\*' is present, the length of the slice must be one. Required. """)
    apiVersions: List[str] = Field(default=None, description=r""" APIVersions is the API versions the resources belong to. '\*' is all versions. If '\*' is present, the length of the slice must be one. Required. """)
    operations: List[str] = Field(default=None, description=r""" Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '\*' is present, the length of the slice must be one. Required. """)
    resources: List[str] = Field(default=None, description=r""" Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '\*' means all resources, but not subresources. 'pods/\*' means all subresources of pods. '\*/scale' means all scale subresources. '\*/\*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required. """)
    scope: str = Field(default=None, description=r""" scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "*" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "*" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*". """)


class SELinuxOptions(BaseModel):
    level: str = Field(default=None, description=r""" Level is SELinux level label that applies to the container. """)
    role: str = Field(default=None, description=r""" Role is a SELinux role label that applies to the container. """)
    type: str = Field(default=None, description=r""" Type is a SELinux type label that applies to the container. """)
    user: str = Field(default=None, description=r""" User is a SELinux user label that applies to the container. """)


class Scale(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="Scale", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """)
    spec: ScaleSpec = Field(default=None, description=r""" spec defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. """)
    status: ScaleStatus = Field(default=None, description=r""" status is the current status of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. Read-only. """)


class ScaleIOPersistentVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs" """)
    gateway: str = Field(default=None, description=r""" gateway is the host address of the ScaleIO API Gateway. """)
    protectionDomain: str = Field(default=None, description=r""" protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. """)
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretRef: SecretReference = Field(default=None, description=r""" secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. """)
    sslEnabled: bool = Field(default=None, description=r""" sslEnabled is the flag to enable/disable SSL communication with Gateway, default false """)
    storageMode: str = Field(default=None, description=r""" storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. """)
    storagePool: str = Field(default=None, description=r""" storagePool is the ScaleIO Storage Pool associated with the protection domain. """)
    system: str = Field(default=None, description=r""" system is the name of the storage system as configured in ScaleIO. """)
    volumeName: str = Field(default=None, description=r""" volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. """)


class ScaleIOVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs". """)
    gateway: str = Field(default=None, description=r""" gateway is the host address of the ScaleIO API Gateway. """)
    protectionDomain: str = Field(default=None, description=r""" protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. """)
    readOnly: bool = Field(default=None, description=r""" readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. """)
    sslEnabled: bool = Field(default=None, description=r""" sslEnabled Flag enable/disable SSL communication with Gateway, default false """)
    storageMode: str = Field(default=None, description=r""" storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. """)
    storagePool: str = Field(default=None, description=r""" storagePool is the ScaleIO Storage Pool associated with the protection domain. """)
    system: str = Field(default=None, description=r""" system is the name of the storage system as configured in ScaleIO. """)
    volumeName: str = Field(default=None, description=r""" volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. """)


class Scheduling(BaseModel):
    nodeSelector: dict = Field(default=None, description=r""" nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission. """)
    tolerations: List[Toleration] = Field(default=None, description=r""" tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass. """)


class ScopeSelector(BaseModel):
    matchExpressions: List[ScopedResourceSelectorRequirement] = Field(default=None, description=r""" A list of scope selector requirements by scope of the resources. """)


class ScopedResourceSelectorRequirement(BaseModel):
    operator: str = Field(default=None, description=r""" Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. """)
    scopeName: str = Field(default=None, description=r""" The name of the scope that the selector applies to. """)
    values: List[str] = Field(default=None, description=r""" An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. """)


class SeccompProfile(BaseModel):
    localhostProfile: str = Field(default=None, description=r""" localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type. """)
    type: str = Field(default=None, description=r""" type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied. """)


class SecretEnvSource(BaseModel):
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" Specify whether the Secret must be defined """)


class SecretKeySelector(BaseModel):
    key: str = Field(default=None, description=r""" The key of the secret to select from.  Must be a valid secret key. """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" Specify whether the Secret or its key must be defined """)


class SecretProjection(BaseModel):
    items: List[KeyToPath] = Field(default=None, description=r""" items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" optional field specify whether the Secret or its key must be defined """)


class SecretReference(BaseModel):
    name: str = Field(default=None, description=r""" name is unique within a namespace to reference a secret resource. """)
    namespace: str = Field(default=None, description=r""" namespace defines the space within which the secret name must be unique. """)


class SecretVolumeSource(BaseModel):
    defaultMode: int = Field(default=None, description=r""" defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
    items: List[KeyToPath] = Field(default=None, description=r""" items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
    optional: bool = Field(default=None, description=r""" optional field specify whether the Secret or its keys must be defined """)
    secretName: str = Field(default=None, description=r""" secretName is the name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret """)


class SecurityContext(BaseModel):
    allowPrivilegeEscalation: bool = Field(default=None, description=r""" AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows. """)
    capabilities: Capabilities = Field(default=None, description=r""" The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows. """)
    privileged: bool = Field(default=None, description=r""" Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. """)
    procMount: str = Field(default=None, description=r""" procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows. """)
    readOnlyRootFilesystem: bool = Field(default=None, description=r""" Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. """)
    runAsGroup: int = Field(default=None, description=r""" The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """)
    runAsNonRoot: bool = Field(default=None, description=r""" Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """)
    runAsUser: int = Field(default=None, description=r""" The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """)
    seLinuxOptions: SELinuxOptions = Field(default=None, description=r""" The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """)
    seccompProfile: SeccompProfile = Field(default=None, description=r""" The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows. """)
    windowsOptions: WindowsSecurityContextOptions = Field(default=None, description=r""" The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. """)


class ServerAddressByClientCIDR(BaseModel):
    clientCIDR: str = Field(default=None, description=r""" The CIDR with which clients can match their IP to figure out the server address that they should use. """)
    serverAddress: str = Field(default=None, description=r""" Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port. """)


class ServerStorageVersion(BaseModel):
    apiServerID: str = Field(default=None, description=r""" The ID of the reporting API server. """)
    decodableVersions: List[str] = Field(default=None, description=r""" The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. """)
    encodingVersion: str = Field(default=None, description=r""" The API server encodes the object to this version when persisting it in the backend (e.g., etcd). """)
    servedVersions: List[str] = Field(default=None, description=r""" The API server can serve these versions. DecodableVersions must include all ServedVersions. """)


class ServiceAccountSubject(BaseModel):
    name: str = Field(default=None, description=r""" `name` is the name of matching ServiceAccount objects, or "*" to match regardless of name. Required. """)
    namespace: str = Field(default=None, description=r""" `namespace` is the namespace of matching ServiceAccount objects. Required. """)


class ServiceAccountTokenProjection(BaseModel):
    audience: str = Field(default=None, description=r""" audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver. """)
    expirationSeconds: int = Field(default=None, description=r""" expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes. """)
    path: str = Field(default=None, description=r""" path is the path relative to the mount point of the file to project the token into. """)


class ServiceBackendPort(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the port on the Service. This is a mutually exclusive setting with "Number". """)
    number: int = Field(default=None, description=r""" number is the numerical port number (e.g. 80) on the Service. This is a mutually exclusive setting with "Name". """)


class ServicePort(BaseModel):
    appProtocol: str = Field(default=None, description=r""" The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 over cleartext as described in https://www.rfc-editor.org/rfc/rfc7540   * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol. """)
    name: str = Field(default=None, description=r""" The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service. """)
    nodePort: int = Field(default=None, description=r""" The port on each node on which this service is exposed when type is NodePort or LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if this Service requires one.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type from NodePort to ClusterIP). More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport """)
    port: int = Field(default=None, description=r""" The port that will be exposed by this service. """)
    protocol: str = Field(default=None, description=r""" The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. """)
    targetPort: Any = Field(default=None, description=r""" Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service """)


class ServiceReference(BaseModel):
    name: str = Field(default=None, description=r""" `name` is the name of the service. Required """)
    namespace: str = Field(default=None, description=r""" `namespace` is the namespace of the service. Required """)
    path: str = Field(default=None, description=r""" `path` is an optional URL path which will be sent in any request to this service. """)
    port: int = Field(default=None, description=r""" If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive). """)


class SessionAffinityConfig(BaseModel):
    clientIP: ClientIPConfig = Field(default=None, description=r""" clientIP contains the configurations of Client IP based session affinity. """)


class StatefulSetCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
    reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of statefulset condition. """)


class StatefulSetOrdinals(BaseModel):
    start: int = Field(default=None, description=r""" start is the number representing the first replica's index. It may be used to number replicas from an alternate index (eg: 1-indexed) over the default 0-indexed names, or to orchestrate progressive movement of replicas from one StatefulSet to another. If set, replica indices will be in the range:   [.spec.ordinals.start, .spec.ordinals.start + .spec.replicas). If unset, defaults to 0. Replica indices will be in the range:   [0, .spec.replicas). """)


class StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    whenDeleted: str = Field(default=None, description=r""" WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted. """)
    whenScaled: str = Field(default=None, description=r""" WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted. """)


class StatefulSetUpdateStrategy(BaseModel):
    rollingUpdate: RollingUpdateStatefulSetStrategy = Field(default=None, description=r""" RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType. """)
    type: str = Field(default=None, description=r""" Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate. """)


class Status(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    code: int = Field(default=None, description=r""" Suggested HTTP return code for this status, 0 if not set. """)
    details: StatusDetails = Field(default=None, description=r""" Extended data associated with the reason.  Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. """)
    kind: str = Field(default="Status", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    message: str = Field(default=None, description=r""" A human-readable description of the status of this operation. """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    reason: str = Field(default=None, description=r""" A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. """)
    status: str = Field(default=None, description=r""" Status of the operation. One of: "Success" or "Failure". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)


class StatusCause(BaseModel):
    field: str = Field(default=None, description=r""" The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.  Examples:   "name" - the field "name" on the current resource   "items[0].name" - the field "name" on the first array entry in "items" """)
    message: str = Field(default=None, description=r""" A human-readable description of the cause of the error.  This field may be presented as-is to a reader. """)
    reason: str = Field(default=None, description=r""" A machine-readable description of the cause of the error. If this value is empty there is no information available. """)


class StatusDetails(BaseModel):
    causes: List[StatusCause] = Field(default=None, description=r""" The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes. """)
    group: str = Field(default=None, description=r""" The group attribute of the resource associated with the status StatusReason. """)
    kind: str = Field(default="StatusDetails", description=r""" The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described). """)
    retryAfterSeconds: int = Field(default=None, description=r""" If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action. """)
    uid: str = Field(default=None, description=r""" UID of the resource. (when there is a single resource which can be described). More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids """)


class StorageOSPersistentVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretRef: ObjectReference = Field(default=None, description=r""" secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted. """)
    volumeName: str = Field(default=None, description=r""" volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace. """)
    volumeNamespace: str = Field(default=None, description=r""" volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. """)


class StorageOSVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
    secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted. """)
    volumeName: str = Field(default=None, description=r""" volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace. """)
    volumeNamespace: str = Field(default=None, description=r""" volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. """)


class StorageVersionCondition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
    message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
    observedGeneration: int = Field(default=None, description=r""" If set, this represents the .metadata.generation that the condition was set based upon. """)
    reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
    status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" Type of the condition. """)


class Subject(BaseModel):
    group: GroupSubject = Field(default=None, description=r""" `group` matches based on user group name. """)
    kind: str = Field(default="Subject", description=r""" `kind` indicates which one of the other fields is non-empty. Required """)
    serviceAccount: ServiceAccountSubject = Field(default=None, description=r""" `serviceAccount` matches ServiceAccounts. """)
    user: UserSubject = Field(default=None, description=r""" `user` matches based on username. """)


class SubjectRulesReviewStatus(BaseModel):
    evaluationError: str = Field(default=None, description=r""" EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. """)
    incomplete: bool = Field(default=None, description=r""" Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation. """)
    nonResourceRules: List[NonResourceRule] = Field(default=None, description=r""" NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete. """)
    resourceRules: List[ResourceRule] = Field(default=None, description=r""" ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete. """)


class Sysctl(BaseModel):
    name: str = Field(default=None, description=r""" Name of a property to set """)
    value: str = Field(default=None, description=r""" Value of a property to set """)


class TCPSocketAction(BaseModel):
    host: str = Field(default=None, description=r""" Optional: Host name to connect to, defaults to the pod IP. """)
    port: Any = Field(default=None, description=r""" Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. """)


class Taint(BaseModel):
    effect: str = Field(default=None, description=r""" Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. """)
    key: str = Field(default=None, description=r""" Required. The taint key to be applied to a node. """)
    timeAdded: Time = Field(default=None, description=r""" TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. """)
    value: str = Field(default=None, description=r""" The taint value corresponding to the taint key. """)


class Time(BaseModel):
    pass



class Toleration(BaseModel):
    effect: str = Field(default=None, description=r""" Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. """)
    key: str = Field(default=None, description=r""" Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. """)
    operator: str = Field(default=None, description=r""" Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. """)
    tolerationSeconds: int = Field(default=None, description=r""" TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. """)
    value: str = Field(default=None, description=r""" Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. """)


class TopologySelectorLabelRequirement(BaseModel):
    key: str = Field(default=None, description=r""" The label key that the selector applies to. """)
    values: List[str] = Field(default=None, description=r""" An array of string values. One value must match the label to be selected. Each entry in Values is ORed. """)


class TopologySelectorTerm(BaseModel):
    matchLabelExpressions: List[TopologySelectorLabelRequirement] = Field(default=None, description=r""" A list of topology selector requirements by labels. """)


class TopologySpreadConstraint(BaseModel):
    labelSelector: LabelSelector = Field(default=None, description=r""" LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain. """)
    matchLabelKeys: List[str] = Field(default=None, description=r""" MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default). """)
    maxSkew: int = Field(default=None, description=r""" MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed. """)
    minDomains: int = Field(default=None, description=r""" MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.  For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.  This is a beta field and requires the MinDomainsInPodTopologySpread feature gate to be enabled (enabled by default). """)
    nodeAffinityPolicy: str = Field(default=None, description=r""" NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.  If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag. """)
    nodeTaintsPolicy: str = Field(default=None, description=r""" NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.  If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag. """)
    topologyKey: str = Field(default=None, description=r""" TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It's a required field. """)
    whenUnsatisfiable: str = Field(default=None, description=r""" WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,   but giving higher precedence to topologies that would help reduce the   skew. A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field. """)


class TypeChecking(BaseModel):
    expressionWarnings: List[ExpressionWarning] = Field(default=None, description=r""" The type checking warnings for each expression. """)


class TypedLocalObjectReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
    kind: str = Field(default="TypedLocalObjectReference", description=r""" Kind is the type of resource being referenced """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)


class TypedObjectReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
    kind: str = Field(default="TypedObjectReference", description=r""" Kind is the type of resource being referenced """)
    name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)
    namespace: str = Field(default=None, description=r""" Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. """)


class UncountedTerminatedPods(BaseModel):
    failed: List[str] = Field(default=None, description=r""" failed holds UIDs of failed Pods. """)
    succeeded: List[str] = Field(default=None, description=r""" succeeded holds UIDs of succeeded Pods. """)


class UserInfo(BaseModel):
    extra: dict = Field(default=None, description=r""" Any additional information provided by the authenticator. """)
    groups: List[str] = Field(default=None, description=r""" The names of groups this user is a part of. """)
    uid: str = Field(default=None, description=r""" A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. """)
    username: str = Field(default=None, description=r""" The name that uniquely identifies this user among all active users. """)


class UserSubject(BaseModel):
    name: str = Field(default=None, description=r""" `name` is the username that matches, or "*" to match all usernames. Required. """)


class ValidatingWebhook(BaseModel):
    admissionReviewVersions: List[str] = Field(default=None, description=r""" AdmissionReviewVersions is an ordered list of preferred `AdmissionReview` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. """)
    clientConfig: WebhookClientConfig = Field(default=None, description=r""" ClientConfig defines how to communicate with the hook. Required """)
    failurePolicy: str = Field(default=None, description=r""" FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail. """)
    matchConditions: List[MatchCondition] = Field(default=None, description=r""" MatchConditions is a list of conditions that must be met for a request to be sent to this webhook. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  The exact matching logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the webhook is skipped.   2. If ALL matchConditions evaluate to TRUE, the webhook is called.   3. If any matchCondition evaluates to an error (but none are FALSE):      - If failurePolicy=Fail, reject the request      - If failurePolicy=Ignore, the error is ignored and the webhook is skipped  This is a beta feature and managed by the AdmissionWebhookMatchConditions feature gate. """)
    matchPolicy: str = Field(default=None, description=r""" matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.  Defaults to "Equivalent" """)
    name: str = Field(default=None, description=r""" The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required. """)
    namespaceSelector: LabelSelector = Field(default=None, description=r""" NamespaceSelector decides whether to run the webhook on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the webhook.  For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1";  you will set the selector as follows: "namespaceSelector": {   "matchExpressions": [     {       "key": "runlevel",       "operator": "NotIn",       "values": [         "0",         "1"       ]     }   ] }  If instead you want to only run the webhook on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": {   "matchExpressions": [     {       "key": "environment",       "operator": "In",       "values": [         "prod",         "staging"       ]     }   ] }  See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels for more examples of label selectors.  Default to the empty LabelSelector, which matches everything. """)
    objectSelector: LabelSelector = Field(default=None, description=r""" ObjectSelector decides whether to run the webhook based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the webhook, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything. """)
    rules: List[RuleWithOperations] = Field(default=None, description=r""" Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects. """)
    sideEffects: str = Field(default=None, description=r""" SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. """)
    timeoutSeconds: int = Field(default=None, description=r""" TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds. """)


class Validation(KubeModel):
    expression: str = Field(default=None, description=r""" Expression represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec CEL expressions have access to the contents of the API request/response, organized into CEL variables as well as some other useful variables:  - 'object' - The object from the incoming request. The value is null for DELETE requests. - 'oldObject' - The existing object. The value is null for CREATE requests. - 'request' - Attributes of the API request([ref](/pkg/apis/admission/types.go#AdmissionRequest)). - 'params' - Parameter resource referred to by the policy binding being evaluated. Only populated if the policy has a ParamKind. - 'namespaceObject' - The namespace object that the incoming object belongs to. The value is null for cluster-scoped resources. - 'variables' - Map of composited variables, from its name to its lazily evaluated value.   For example, a variable named 'foo' can be accessed as 'variables.foo'. - 'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal (user or service account) of the request.   See https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz - 'authorizer.requestResource' - A CEL ResourceCheck constructed from the 'authorizer' and configured with the   request resource.  The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object. No other metadata properties are accessible.  Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are: 	  "true", "false", "null", "in", "as", "break", "const", "continue", "else", "for", "function", "if", 	  "import", "let", "loop", "package", "namespace", "return". Examples:   - Expression accessing a property named "namespace": {"Expression": "object.__namespace__ > 0"}   - Expression accessing a property named "x-prop": {"Expression": "object.x__dash__prop > 0"}   - Expression accessing a property named "redact__d": {"Expression": "object.redact__underscores__d > 0"}  Equality on arrays with list type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and     non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values     are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with     non-intersecting keys are appended, retaining their partial order. Required. """)
    message: str = Field(default=None, description=r""" Message represents the message displayed when validation fails. The message is required if the Expression contains line breaks. The message must not contain line breaks. If unset, the message is "failed rule: {Rule}". e.g. "must be a URL with the host matching spec.host" If the Expression contains line breaks. Message is required. The message must not contain line breaks. If unset, the message is "failed Expression: {Expression}". """)
    messageExpression: str = Field(default=None, description=r""" messageExpression declares a CEL expression that evaluates to the validation failure message that is returned when this rule fails. Since messageExpression is used as a failure message, it must evaluate to a string. If both message and messageExpression are present on a validation, then messageExpression will be used if validation fails. If messageExpression results in a runtime error, the runtime error is logged, and the validation failure message is produced as if the messageExpression field were unset. If messageExpression evaluates to an empty string, a string with only spaces, or a string that contains line breaks, then the validation failure message will also be produced as if the messageExpression field were unset, and the fact that messageExpression produced an empty string/string with only spaces/string with line breaks will be logged. messageExpression has access to all the same variables as the `expression` except for 'authorizer' and 'authorizer.requestResource'. Example: "object.x must be less than max ("+string(params.max)+")" """)
    reason: str = Field(default=None, description=r""" Reason represents a machine-readable description of why this validation failed. If this is the first validation in the list to fail, this reason, as well as the corresponding HTTP response code, are used in the HTTP response to the client. The currently supported reasons are: "Unauthorized", "Forbidden", "Invalid", "RequestEntityTooLarge". If not set, StatusReasonInvalid is used in the response to the client. """)


class ValidationRule(KubeModel):
    fieldPath: str = Field(default=None, description=r""" fieldPath represents the field path returned when the validation fails. It must be a relative JSON path (i.e. with array notation) scoped to the location of this x-kubernetes-validations extension in the schema and refer to an existing field. e.g. when validation checks if a specific attribute `foo` under a map `testMap`, the fieldPath could be set to `.testMap.foo` If the validation checks two lists must have unique attributes, the fieldPath could be set to either of the list: e.g. `.testList` It does not support list numeric index. It supports child operation to refer to an existing field currently. Refer to [JSONPath support in Kubernetes](https://kubernetes.io/docs/reference/kubectl/jsonpath/) for more info. Numeric index of array is not supported. For field name which contains special characters, use `['specialName']` to refer the field name. e.g. for attribute `foo.34$` appears in a list `testList`, the fieldPath could be set to `.testList['foo.34$']` """)
    message: str = Field(default=None, description=r""" Message represents the message displayed when validation fails. The message is required if the Rule contains line breaks. The message must not contain line breaks. If unset, the message is "failed rule: {Rule}". e.g. "must be a URL with the host matching spec.host" """)
    messageExpression: str = Field(default=None, description=r""" MessageExpression declares a CEL expression that evaluates to the validation failure message that is returned when this rule fails. Since messageExpression is used as a failure message, it must evaluate to a string. If both message and messageExpression are present on a rule, then messageExpression will be used if validation fails. If messageExpression results in a runtime error, the runtime error is logged, and the validation failure message is produced as if the messageExpression field were unset. If messageExpression evaluates to an empty string, a string with only spaces, or a string that contains line breaks, then the validation failure message will also be produced as if the messageExpression field were unset, and the fact that messageExpression produced an empty string/string with only spaces/string with line breaks will be logged. messageExpression has access to all the same variables as the rule; the only difference is the return type. Example: "x must be less than max ("+string(self.max)+")" """)
    reason: str = Field(default=None, description=r""" reason provides a machine-readable validation failure reason that is returned to the caller when a request fails this validation rule. The HTTP status code returned to the caller will match the reason of the reason of the first failed validation rule. The currently supported reasons are: "FieldValueInvalid", "FieldValueForbidden", "FieldValueRequired", "FieldValueDuplicate". If not set, default to use "FieldValueInvalid". All future added reasons must be accepted by clients when reading this value and unknown reasons should be treated as FieldValueInvalid. """)
    rule: str = Field(default=None, description=r""" Rule represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec The Rule is scoped to the location of the x-kubernetes-validations extension in the schema. The `self` variable in the CEL expression is bound to the scoped value. Example: - Rule scoped to the root of a resource with a status subresource: {"rule": "self.status.actual <= self.spec.maxDesired"}  If the Rule is scoped to an object with properties, the accessible properties of the object are field selectable via `self.field` and field presence can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL expressions. If the Rule is scoped to an object with additionalProperties (i.e. a map) the value of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self` and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`. If the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by macros and functions. If the Rule is scoped to a scalar, `self` is bound to the scalar value. Examples: - Rule scoped to a map of objects: {"rule": "self.components['Widget'].priority < 10"} - Rule scoped to a list of integers: {"rule": "self.values.all(value, value >= 0 && value < 100)"} - Rule scoped to a string value: {"rule": "self.startsWith('kube')"}  The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object and from any x-kubernetes-embedded-resource annotated objects. No other metadata properties are accessible.  Unknown data preserved in custom resources via x-kubernetes-preserve-unknown-fields is not accessible in CEL expressions. This includes: - Unknown field values that are preserved by object schemas with x-kubernetes-preserve-unknown-fields. - Object properties where the property schema is of an "unknown type". An "unknown type" is recursively defined as:   - A schema with no type and x-kubernetes-preserve-unknown-fields set to true   - An array where the items schema is of an "unknown type"   - An object where the additionalProperties schema is of an "unknown type"  Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are: 	  "true", "false", "null", "in", "as", "break", "const", "continue", "else", "for", "function", "if", 	  "import", "let", "loop", "package", "namespace", "return". Examples:   - Rule accessing a property named "namespace": {"rule": "self.__namespace__ > 0"}   - Rule accessing a property named "x-prop": {"rule": "self.x__dash__prop > 0"}   - Rule accessing a property named "redact__d": {"rule": "self.redact__underscores__d > 0"}  Equality on arrays with x-kubernetes-list-type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and     non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values     are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with     non-intersecting keys are appended, retaining their partial order. """)


class Variable(BaseModel):
    expression: str = Field(default=None, description=r""" Expression is the expression that will be evaluated as the value of the variable. The CEL expression has access to the same identifiers as the CEL expressions in Validation. """)
    name: str = Field(default=None, description=r""" Name is the name of the variable. The name must be a valid CEL identifier and unique among all variables. The variable can be accessed in other expressions through `variables` For example, if name is "foo", the variable will be available as `variables.foo` """)


class VolumeAttachmentSource(BaseModel):
    inlineVolumeSpec: PersistentVolumeSpec = Field(default=None, description=r""" inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature. """)
    persistentVolumeName: str = Field(default=None, description=r""" persistentVolumeName represents the name of the persistent volume to attach. """)


class VolumeDevice(BaseModel):
    devicePath: str = Field(default=None, description=r""" devicePath is the path inside of the container that the device will be mapped to. """)
    name: str = Field(default=None, description=r""" name must match the name of a persistentVolumeClaim in the pod """)


class VolumeError(BaseModel):
    message: str = Field(default=None, description=r""" message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information. """)
    time: Time = Field(default=None, description=r""" time represents the time the error was encountered. """)


class VolumeMount(BaseModel):
    mountPath: str = Field(default=None, description=r""" Path within the container at which the volume should be mounted.  Must not contain ':'. """)
    mountPropagation: str = Field(default=None, description=r""" mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. """)
    name: str = Field(default=None, description=r""" This must match the Name of a Volume. """)
    readOnly: bool = Field(default=None, description=r""" Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. """)
    subPath: str = Field(default=None, description=r""" Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root). """)
    subPathExpr: str = Field(default=None, description=r""" Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive. """)


class VolumeNodeAffinity(BaseModel):
    required: NodeSelector = Field(default=None, description=r""" required specifies hard node constraints that must be met. """)


class VolumeNodeResources(BaseModel):
    count: int = Field(default=None, description=r""" count indicates the maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded. """)


class VolumeProjection(BaseModel):
    configMap: ConfigMapProjection = Field(default=None, description=r""" configMap information about the configMap data to project """)
    downwardAPI: DownwardAPIProjection = Field(default=None, description=r""" downwardAPI information about the downwardAPI data to project """)
    secret: SecretProjection = Field(default=None, description=r""" secret information about the secret data to project """)
    serviceAccountToken: ServiceAccountTokenProjection = Field(default=None, description=r""" serviceAccountToken is information about the serviceAccountToken data to project """)


class VsphereVirtualDiskVolumeSource(BaseModel):
    fsType: str = Field(default=None, description=r""" fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
    storagePolicyID: str = Field(default=None, description=r""" storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. """)
    storagePolicyName: str = Field(default=None, description=r""" storagePolicyName is the storage Policy Based Management (SPBM) profile name. """)
    volumePath: str = Field(default=None, description=r""" volumePath is the path that identifies vSphere volume vmdk """)


class WatchEvent(BaseModel):
    object: Any = Field(default=None, description=r""" Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context. """)
    type: str = Field(default=None)


class WebhookClientConfig(BaseModel):
    caBundle: str = Field(default=None, description=r""" `caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. """)
    service: ServiceReference = Field(default=None, description=r""" `service` is a reference to the service for this webhook. Either `service` or `url` must be specified.  If the webhook is running within the cluster, then you should use `service`. """)
    url: str = Field(default=None, description=r""" `url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.  The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be "https"; the URL must begin with "https://".  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either. """)


class WebhookConversion(BaseModel):
    clientConfig: WebhookClientConfig = Field(default=None, description=r""" clientConfig is the instructions for how to call the webhook if strategy is `Webhook`. """)
    conversionReviewVersions: List[str] = Field(default=None, description=r""" conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. """)


class WeightedPodAffinityTerm(BaseModel):
    podAffinityTerm: PodAffinityTerm = Field(default=None, description=r""" Required. A pod affinity term, associated with the corresponding weight. """)
    weight: int = Field(default=None, description=r""" weight associated with matching the corresponding podAffinityTerm, in the range 1-100. """)


class WindowsSecurityContextOptions(BaseModel):
    gmsaCredentialSpec: str = Field(default=None, description=r""" GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. """)
    gmsaCredentialSpecName: str = Field(default=None, description=r""" GMSACredentialSpecName is the name of the GMSA credential spec to use. """)
    hostProcess: bool = Field(default=None, description=r""" HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. """)
    runAsUserName: str = Field(default=None, description=r""" The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """)

