from typing import Optional

from pydantic import BaseModel, Field

from k8s_py.types import (
    EnvVar,
    EnvFromSource,
    Lifecycle,
    Probe,
    ContainerPort,
    ResourceRequirements,
    SecurityContext, 
    VolumeDevice, 
    VolumeMount,
    ObjectMeta,
    PodSpec,
    PodStatus,
    ReplicationControllerSpec,
    ReplicationControllerStatus
)


class Container(BaseModel):
    args: list = Field(default=[], description="Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell")
    command: list = Field(default=[], description="The command to run when starting the container. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell")
    env: list[EnvVar] = Field(default=[], description="List of environment variables to set in the container. Cannot be updated.")
    envFrom: list[EnvFromSource] = Field(default=[], description="List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.")
    image: str = Field(default=None, description="Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images")
    imagePullPolicy: str = Field(default=None, description="Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images")
    lifecycle: Lifecycle = Field(default=None, description="Actions that the management system should take in response to container lifecycle events. Cannot be updated.")
    livenessProbe: Probe = Field(default=None, description="Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes")
    name: str = Field(..., description="Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.")
    ports: list[ContainerPort] = Field(default=[], description="List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.")
    readinessProbe: Probe = Field(default=None, description="Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes")
    resources: ResourceRequirements = Field(default=None, description="Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/")
    securityContext: SecurityContext = Field(default=None, description="Security options that the container should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/")
    startupProbe: Probe = Field(default=None, description="StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the container will be killed and restarted, subject to the container's restart policy. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes")
    stdin: bool = Field(default=None, description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.")
    stdinOnce: bool = Field(default=None, description="Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false")
    terminationMessagePath: str = Field(default=None, description="Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.")
    terminationMessagePolicy: str = Field(default=None, description="Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.")
    tty: bool = Field(default=None, description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.")
    volumeDevices: list[VolumeDevice] = Field(default=[], description="volumeDevices is the list of block devices to be used by the container.")
    volumeMounts: list[VolumeMount] = Field(default=[], description="Pod volumes to mount into the container's filesystem. Cannot be updated.")
    workingDir: str = Field(default=None, description="Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.")


class Pod(BaseModel):
    apiVersion: str = Field(default="v1", description="APIVersion defines the versioned schema of this representation of an object.")
    kind: str = Field(default="Pod", description="Kind is a string value representing the REST resource this object represents.")
    metadata: ObjectMeta = Field(default=None, description="Standard object's metadata.")
    spec: PodSpec = Field(..., description="Specification of the desired behavior of the pod.")
    status: Optional[PodStatus] = Field(default=None, description="Current status of the pod. Read-only.")

class ReplicationController(BaseModel):
    apiVersion: str = Field(default="v1", description="APIVersion defines the versioned schema of this representation of an object.")
    kind: str = Field(default="ReplicationController", description="Kind is a string value representing the REST resource this object represents.")
    metadata: ObjectMeta = Field(default=None, description="Standard object's metadata.")
    spec: ReplicationControllerSpec = Field(..., description="Specification of the desired behavior of the replication controller.")
    status: Optional[ReplicationControllerStatus] = Field(default=None, description="Most recently observed status of the replication controller.")
