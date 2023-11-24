from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta.object_meta import ObjectMeta
from k8s_models.metadata.resource.resource_claim_template_spec import ResourceClaimTemplateSpec


class ResourceClaimTemplate(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ResourceClaimTemplate", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata """)
    spec: ResourceClaimTemplateSpec = Field(default=None, description=r""" Describes the ResourceClaim that is to be generated.  This field is immutable. A ResourceClaim will get created by the control plane for a Pod when needed and then not get updated anymore. """)
