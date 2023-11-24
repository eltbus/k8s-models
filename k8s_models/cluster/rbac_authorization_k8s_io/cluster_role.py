from typing import List

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.rbac_authorization_k8s_io.aggregation_rule import AggregationRule
from k8s_models.definitions.meta.object_meta import ObjectMeta
from k8s_models.definitions.rbac_authorization_k8s_io.policy_rule import PolicyRule


class ClusterRole(KubeModel):
    aggregationRule: AggregationRule = Field(default=None, description=r""" AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller. """)
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ClusterRole", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. """)
    rules: List[PolicyRule] = Field(default=None, description=r""" Rules holds all the PolicyRules for this ClusterRole """)
