from pydantic import BaseModel, Field


class DeploymentStatus(BaseModel):
    availableReplicas: int = Field(default=None, description=r""" Total number of available pods (ready for at least minReadySeconds) targeted by this deployment. """)
    collisionCount: int = Field(default=None, description=r""" Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet. """)
    conditions: List[DeploymentCondition] = Field(default=None, description=r""" Represents the latest available observations of a deployment's current state. """)
    observedGeneration: int = Field(default=None, description=r""" The generation observed by the deployment controller. """)
    readyReplicas: int = Field(default=None, description=r""" readyReplicas is the number of pods targeted by this Deployment with a Ready Condition. """)
    replicas: int = Field(default=None, description=r""" Total number of non-terminated pods targeted by this deployment (their labels match the selector). """)
    unavailableReplicas: int = Field(default=None, description=r""" Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created. """)
    updatedReplicas: int = Field(default=None, description=r""" Total number of non-terminated pods targeted by this deployment that have the desired template spec. """)
