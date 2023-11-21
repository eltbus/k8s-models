from __future__ import annotations

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.definitions.node_k8s_io import Overhead, Scheduling

class RuntimeClass(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	handler: str = Field(default=None, description=r""" handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable. """)
	kind: str = Field(default="RuntimeClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	overhead: Overhead = Field(default=None, description=r""" overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see  https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/ """)
	scheduling: Scheduling = Field(default=None, description=r""" scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes. """)
