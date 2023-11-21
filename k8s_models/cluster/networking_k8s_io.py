from __future__ import annotations

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.cluster.networking import IPAddressSpec, NetworkPolicySpec

class IPAddress(KubeModel):
	apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="IPAddress", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: IPAddressSpec = Field(default=None, description=r""" spec is the desired state of the IPAddress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)

class NetworkPolicy(KubeModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="NetworkPolicy", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: NetworkPolicySpec = Field(default=None, description=r""" spec represents the specification of the desired behavior for this NetworkPolicy. """)
