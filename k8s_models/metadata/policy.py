from __future__ import annotations
from typing import Any

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta, LabelSelector
from k8s_models.definitions.unknown import PodDisruptionBudgetStatus


class PodDisruptionBudget(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="PodDisruptionBudget",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: PodDisruptionBudgetSpec = Field(
        default=None,
        description=r""" Specification of the desired behavior of the PodDisruptionBudget. """,
    )
    status: PodDisruptionBudgetStatus = Field(
        default=None,
        description=r""" Most recently observed status of the PodDisruptionBudget. """,
    )


class PodDisruptionBudgetSpec(BaseModel):
    maxUnavailable: Any = Field(
        default=None,
        description=r""" An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable". """,
    )
    minAvailable: Any = Field(
        default=None,
        description=r""" An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%". """,
    )
    selector: LabelSelector = Field(
        default=None,
        description=r""" Label query over pods whose evictions are managed by the disruption budget. A null selector will match no pods, while an empty ({}) selector will select all pods within the namespace. """,
    )
    unhealthyPodEvictionPolicy: str = Field(
        default=None,
        description=r""" UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods should be considered for eviction. Current implementation considers healthy pods, as pods that have status.conditions item with type="Ready",status="True".  Valid policies are IfHealthyBudget and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds to the IfHealthyBudget policy.  IfHealthyBudget policy means that running pods (status.phase="Running"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction.  AlwaysAllow policy means that all running pods (status.phase="Running"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction.  Additional policies may be added in the future. Clients making eviction decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in this field.  This field is beta-level. The eviction API uses this field when the feature gate PDBUnhealthyPodEvictionPolicy is enabled (enabled by default). """,
    )
