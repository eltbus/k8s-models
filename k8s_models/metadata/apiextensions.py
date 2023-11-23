from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta import ListMeta
from k8s_models.metadata.apiextensions_k8s_io import CustomResourceDefinition
from k8s_models.definitions.apiextensions_k8s_io import (
    CustomResourceConversion,
    CustomResourceDefinitionNames,
    CustomResourceDefinitionVersion,
    CustomResourceDefinitionCondition,
)

class CustomResourceDefinitionSpec(BaseModel):
    conversion: CustomResourceConversion = Field(default=None, description=r""" conversion defines conversion settings for the CRD. """)
    group: str = Field(default=None, description=r""" group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). """)
    names: CustomResourceDefinitionNames = Field(default=None, description=r""" names specify the resource and kind names for the custom resource. """)
    preserveUnknownFields: bool = Field(default=None, description=r""" preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. This field is deprecated in favor of setting `x-preserve-unknown-fields` to true in `spec.versions[*].schema.openAPIV3Schema`. See https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#field-pruning for details. """)
    scope: str = Field(default=None, description=r""" scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`. """)
    versions: List[CustomResourceDefinitionVersion] = Field(default=None, description=r""" versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10. """)

class CustomResourceDefinitionStatus(BaseModel):
    acceptedNames: CustomResourceDefinitionNames = Field(default=None, description=r""" acceptedNames are the names that are actually being used to serve discovery. They may be different than the names in spec. """)
    conditions: List[CustomResourceDefinitionCondition] = Field(default=None, description=r""" conditions indicate state for particular aspects of a CustomResourceDefinition """)
    storedVersions: List[str] = Field(default=None, description=r""" storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list. """)

class CustomResourceDefinitionList(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[CustomResourceDefinition] = Field(default=None, description=r""" items list individual CustomResourceDefinition objects """)
    kind: str = Field(default="CustomResourceDefinitionList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
