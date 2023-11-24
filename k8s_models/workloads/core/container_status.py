from pydantic import BaseModel, Field

from k8s_models.definitions.core.container_state import ContainerState
from k8s_models.definitions.core.resource_requirements import ResourceRequirements


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
