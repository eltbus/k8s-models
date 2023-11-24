from pydantic import BaseModel, Field

from k8s_models.definitions.core.capabilities import Capabilities
from k8s_models.definitions.core.se_linux_options import SELinuxOptions
from k8s_models.definitions.core.seccomp_profile import SeccompProfile
from k8s_models.definitions.core.windows_security_context_options import WindowsSecurityContextOptions


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
