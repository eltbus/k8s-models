from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.replication_controller_condition import ReplicationControllerCondition


class ReplicationControllerStatus(BaseModel):
    availableReplicas: int = Field(default=None, description=r""" The number of available replicas (ready for at least minReadySeconds) for this replication controller. """)
    conditions: List[ReplicationControllerCondition] = Field(default=None, description=r""" Represents the latest available observations of a replication controller's current state. """)
    fullyLabeledReplicas: int = Field(default=None, description=r""" The number of pods that have labels matching the labels of the pod template of the replication controller. """)
    observedGeneration: int = Field(default=None, description=r""" ObservedGeneration reflects the generation of the most recently observed replication controller. """)
    readyReplicas: int = Field(default=None, description=r""" The number of ready replicas for this replication controller. """)
    replicas: int = Field(default=None, description=r""" Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller """)
