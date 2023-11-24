from pydantic import BaseModel, Field


class NodeSpec(BaseModel):
    configSource: NodeConfigSource = Field(default=None, description=r""" Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed. """)
    externalID: str = Field(default=None, description=r""" Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966 """)
    podCIDR: str = Field(default=None, description=r""" PodCIDR represents the pod IP range assigned to the node. """)
    podCIDRs: List[str] = Field(default=None, description=r""" podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6. """)
    providerID: str = Field(default=None, description=r""" ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID> """)
    taints: List[Taint] = Field(default=None, description=r""" If specified, the node's taints. """)
    unschedulable: bool = Field(default=None, description=r""" Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration """)
