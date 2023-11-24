from pydantic import BaseModel, Field


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
