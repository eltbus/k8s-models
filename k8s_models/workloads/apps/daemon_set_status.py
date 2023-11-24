from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.apps.daemon_set_condition import DaemonSetCondition


class DaemonSetStatus(BaseModel):
    collisionCount: int = Field(default=None, description=r""" Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. """)
    conditions: List[DaemonSetCondition] = Field(default=None, description=r""" Represents the latest available observations of a DaemonSet's current state. """)
    currentNumberScheduled: int = Field(default=None, description=r""" The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """)
    desiredNumberScheduled: int = Field(default=None, description=r""" The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """)
    numberAvailable: int = Field(default=None, description=r""" The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds) """)
    numberMisscheduled: int = Field(default=None, description=r""" The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """)
    numberReady: int = Field(default=None, description=r""" numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition. """)
    numberUnavailable: int = Field(default=None, description=r""" The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds) """)
    observedGeneration: int = Field(default=None, description=r""" The most recent generation observed by the daemon set controller. """)
    updatedNumberScheduled: int = Field(default=None, description=r""" The total number of nodes that are running updated daemon pod """)
