from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.env_var import EnvVar
from k8s_models.definitions.core.env_from_source import EnvFromSource
from k8s_models.definitions.core.lifecycle import Lifecycle
from k8s_models.definitions.core.probe import Probe
from k8s_models.definitions.core.container_port import ContainerPort
from k8s_models.definitions.core.container_resize_policy import ContainerResizePolicy
from k8s_models.definitions.core.resource_requirements import ResourceRequirements
from k8s_models.definitions.core.security_context import SecurityContext
from k8s_models.definitions.core.volume_device import VolumeDevice
from k8s_models.definitions.core.volume_mount import VolumeMount


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
