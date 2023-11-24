from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta.object_meta import ObjectMeta
from k8s_models.definitions.resource_k8s_io.resource_class_parameters_reference import ResourceClassParametersReference
from k8s_models.definitions.core.node_selector import NodeSelector


class ResourceClass(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    driverName: str = Field(default=None, description=r""" DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.  Resource drivers have a unique name in forward domain order (acme.example.com). """)
    kind: str = Field(default="ResourceClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata """)
    parametersRef: ResourceClassParametersReference = Field(default=None, description=r""" ParametersRef references an arbitrary separate object that may hold parameters that will be used by the driver when allocating a resource that uses this class. A dynamic resource driver can distinguish between parameters stored here and and those stored in ResourceClaimSpec. """)
    suitableNodes: NodeSelector = Field(default=None, description=r""" Only nodes matching the selector will be considered by the scheduler when trying to find a Node that fits a Pod when that Pod uses a ResourceClaim that has not been allocated yet.  Setting this field is optional. If null, all nodes are candidates. """)
