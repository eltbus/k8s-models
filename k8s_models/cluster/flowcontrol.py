from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.models import KubeModel
from k8s_models.cluster.flowcontrol_apiserver_k8s_io import FlowSchema
from k8s_models.cluster.flowcontrol_apiserver_k8s_io import PriorityLevelConfiguration
from k8s_models.definitions.meta import ListMeta
from k8s_models.definitions.flowcontrol_apiserver_k8s_io import (
    ExemptPriorityLevelConfiguration,
    FlowDistinguisherMethod,
    FlowSchemaCondition,
    LimitedPriorityLevelConfiguration,
    PolicyRulesWithSubjects,
    PriorityLevelConfigurationCondition,
    PriorityLevelConfigurationReference,
)

class FlowSchemaSpec(BaseModel):
    distinguisherMethod: FlowDistinguisherMethod = Field(default=None, description=r""" `distinguisherMethod` defines how to compute the flow distinguisher for requests that match this schema. `nil` specifies that the distinguisher is disabled and thus will always be the empty string. """)
    matchingPrecedence: int = Field(default=None, description=r""" `matchingPrecedence` is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. """)
    priorityLevelConfiguration: PriorityLevelConfigurationReference = Field(default=None, description=r""" `priorityLevelConfiguration` should reference a PriorityLevelConfiguration in the cluster. If the reference cannot be resolved, the FlowSchema will be ignored and marked as invalid in its status. Required. """)
    rules: List[PolicyRulesWithSubjects] = Field(default=None, description=r""" `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. """)

class FlowSchemaStatus(BaseModel):
    conditions: List[FlowSchemaCondition] = Field(default=None, description=r""" `conditions` is a list of the current states of FlowSchema. """)

class FlowSchemaList(KubeModel):
    apiVersion: str = Field(default="v1beta3", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[FlowSchema] = Field(default=None, description=r""" `items` is a list of FlowSchemas. """)
    kind: str = Field(default="FlowSchemaList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" `metadata` is the standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)

class PriorityLevelConfigurationSpec(BaseModel):
    exempt: ExemptPriorityLevelConfiguration = Field(default=None, description=r""" `exempt` specifies how requests are handled for an exempt priority level. This field MUST be empty if `type` is `"Limited"`. This field MAY be non-empty if `type` is `"Exempt"`. If empty and `type` is `"Exempt"` then the default values for `ExemptPriorityLevelConfiguration` apply. """)
    limited: LimitedPriorityLevelConfiguration = Field(default=None, description=r""" `limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `"Limited"`. """)
    type: str = Field(default=None, description=r""" `type` indicates whether this priority level is subject to limitation on request execution.  A value of `"Exempt"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `"Limited"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required. """)

class PriorityLevelConfigurationStatus(BaseModel):
    conditions: List[PriorityLevelConfigurationCondition] = Field(default=None, description=r""" `conditions` is the current state of "request-priority". """)

class PriorityLevelConfigurationList(KubeModel):
    apiVersion: str = Field(default="v1beta3", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    items: List[PriorityLevelConfiguration] = Field(default=None, description=r""" `items` is a list of request-priorities. """)
    kind: str = Field(default="PriorityLevelConfigurationList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ListMeta = Field(default=None, description=r""" `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
