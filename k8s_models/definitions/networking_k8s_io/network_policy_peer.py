from pydantic import BaseModel, Field

from k8s_models.definitions.networking_k8s_io.ip_block import IPBlock
from k8s_models.definitions.meta.label_selector import LabelSelector


class NetworkPolicyPeer(BaseModel):
    ipBlock: IPBlock = Field(default=None, description=r""" ipBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be. """)
    namespaceSelector: LabelSelector = Field(default=None, description=r""" namespaceSelector selects namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.  If podSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the namespaces selected by namespaceSelector. Otherwise it selects all pods in the namespaces selected by namespaceSelector. """)
    podSelector: LabelSelector = Field(default=None, description=r""" podSelector is a label selector which selects pods. This field follows standard label selector semantics; if present but empty, it selects all pods.  If namespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the pods matching podSelector in the policy's own namespace. """)
