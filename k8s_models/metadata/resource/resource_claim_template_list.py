from typing import List

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.metadata.resource_k8s_io.resource_claim_template import ResourceClaimTemplate
from k8s_models.definitions.meta.list_meta import ListMeta



class ResourceClaimTemplateList(KubeModel):
    apiVersion: str = Field(default="v1alpha2", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[ResourceClaimTemplate] = Field(default=None, description=r""" Items is the list of resource claim templates. """)
    kind: str = Field(default="ResourceClaimTemplateList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard list metadata """)
