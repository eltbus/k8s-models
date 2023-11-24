from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.apps.stateful_set_condition import StatefulSetCondition


class StatefulSetStatus(BaseModel):
    availableReplicas: int = Field(default=None, description=r""" Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset. """)
    collisionCount: int = Field(default=None, description=r""" collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. """)
    conditions: List[StatefulSetCondition] = Field(default=None, description=r""" Represents the latest available observations of a statefulset's current state. """)
    currentReplicas: int = Field(default=None, description=r""" currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision. """)
    currentRevision: str = Field(default=None, description=r""" currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas). """)
    observedGeneration: int = Field(default=None, description=r""" observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server. """)
    readyReplicas: int = Field(default=None, description=r""" readyReplicas is the number of pods created for this StatefulSet with a Ready Condition. """)
    replicas: int = Field(default=None, description=r""" replicas is the number of Pods created by the StatefulSet controller. """)
    updateRevision: str = Field(default=None, description=r""" updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas) """)
    updatedReplicas: int = Field(default=None, description=r""" updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision. """)
