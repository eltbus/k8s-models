from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.core.node_address import  NodeAddress
from k8s_models.definitions.core.node_condition import NodeCondition
from k8s_models.definitions.core.node_config_status import NodeConfigStatus
from k8s_models.definitions.core.node_daemon_endpoints import NodeDaemonEndpoints
from k8s_models.definitions.core.container_image import ContainerImage
from k8s_models.definitions.core.node_system_info import NodeSystemInfo
from k8s_models.definitions.core.attached_volume import AttachedVolume


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
