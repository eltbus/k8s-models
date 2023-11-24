from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.apps.replica_set_condition import ReplicaSetCondition


class ReplicaSetStatus(BaseModel):
    availableReplicas: int = Field(default=None, description=r""" The number of available replicas (ready for at least minReadySeconds) for this replica set. """)
    conditions: List[ReplicaSetCondition] = Field(default=None, description=r""" Represents the latest available observations of a replica set's current state. """)
    fullyLabeledReplicas: int = Field(default=None, description=r""" The number of pods that have labels matching the labels of the pod template of the replicaset. """)
    observedGeneration: int = Field(default=None, description=r""" ObservedGeneration reflects the generation of the most recently observed ReplicaSet. """)
    readyReplicas: int = Field(default=None, description=r""" readyReplicas is the number of pods targeted by this ReplicaSet with a Ready Condition. """)
    replicas: int = Field(default=None, description=r""" Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller """)
