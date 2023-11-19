from __future__ import annotations
from typing import Any

from pydantic import BaseModel, Field
from k8s_py.definitions.meta import Time
from k8s_py.definitions.unknown import RollingUpdateDaemonSet


class DaemonSetCondition(BaseModel):
    lastTransitionTime: Time = Field(
        default=None,
        description=r""" Last time the condition transitioned from one status to another. """,
    )
    message: str = Field(
        default=None,
        description=r""" A human readable message indicating details about the transition. """,
    )
    reason: str = Field(
        default=None,
        description=r""" The reason for the condition's last transition. """,
    )
    status: str = Field(
        default=None,
        description=r""" Status of the condition, one of True, False, Unknown. """,
    )
    type: str = Field(default=None, description=r""" Type of DaemonSet condition. """)


class DaemonSetUpdateStrategy(BaseModel):
    rollingUpdate: RollingUpdateDaemonSet = Field(
        default=None,
        description=r""" Rolling update config params. Present only if type = "RollingUpdate". """,
    )
    type: str = Field(
        default=None,
        description=r""" Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate. """,
    )


class DeploymentCondition(BaseModel):
    lastTransitionTime: Time = Field(
        default=None,
        description=r""" Last time the condition transitioned from one status to another. """,
    )
    lastUpdateTime: Time = Field(
        default=None, description=r""" The last time this condition was updated. """
    )
    message: str = Field(
        default=None,
        description=r""" A human readable message indicating details about the transition. """,
    )
    reason: str = Field(
        default=None,
        description=r""" The reason for the condition's last transition. """,
    )
    status: str = Field(
        default=None,
        description=r""" Status of the condition, one of True, False, Unknown. """,
    )
    type: str = Field(default=None, description=r""" Type of deployment condition. """)


class ReplicaSetCondition(BaseModel):
    lastTransitionTime: Time = Field(
        default=None,
        description=r""" The last time the condition transitioned from one status to another. """,
    )
    message: str = Field(
        default=None,
        description=r""" A human readable message indicating details about the transition. """,
    )
    reason: str = Field(
        default=None,
        description=r""" The reason for the condition's last transition. """,
    )
    status: str = Field(
        default=None,
        description=r""" Status of the condition, one of True, False, Unknown. """,
    )
    type: str = Field(default=None, description=r""" Type of replica set condition. """)


class RollingUpdateStatefulSetStrategy(BaseModel):
    maxUnavailable: Any = Field(
        default=None,
        description=r""" The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable. """,
    )
    partition: int = Field(
        default=None,
        description=r""" Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0. """,
    )


class StatefulSetCondition(BaseModel):
    lastTransitionTime: Time = Field(
        default=None,
        description=r""" Last time the condition transitioned from one status to another. """,
    )
    message: str = Field(
        default=None,
        description=r""" A human readable message indicating details about the transition. """,
    )
    reason: str = Field(
        default=None,
        description=r""" The reason for the condition's last transition. """,
    )
    status: str = Field(
        default=None,
        description=r""" Status of the condition, one of True, False, Unknown. """,
    )
    type: str = Field(default=None, description=r""" Type of statefulset condition. """)


class StatefulSetOrdinals(BaseModel):
    start: int = Field(
        default=None,
        description=r""" start is the number representing the first replica's index. It may be used to number replicas from an alternate index (eg: 1-indexed) over the default 0-indexed names, or to orchestrate progressive movement of replicas from one StatefulSet to another. If set, replica indices will be in the range:   [.spec.ordinals.start, .spec.ordinals.start + .spec.replicas). If unset, defaults to 0. Replica indices will be in the range:   [0, .spec.replicas). """,
    )


class StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    whenDeleted: str = Field(
        default=None,
        description=r""" WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted. """,
    )
    whenScaled: str = Field(
        default=None,
        description=r""" WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted. """,
    )


class StatefulSetUpdateStrategy(BaseModel):
    rollingUpdate: RollingUpdateStatefulSetStrategy = Field(
        default=None,
        description=r""" RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType. """,
    )
    type: str = Field(
        default=None,
        description=r""" Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate. """,
    )
