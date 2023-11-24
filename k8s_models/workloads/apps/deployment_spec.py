from pydantic import BaseModel, Field


class DeploymentSpec(BaseModel):
    minReadySeconds: int = Field(default=None, description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """)
    paused: bool = Field(default=None, description=r""" Indicates that the deployment is paused. """)
    progressDeadlineSeconds: int = Field(default=None, description=r""" The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. """)
    replicas: int = Field(default=None, description=r""" Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. """)
    revisionHistoryLimit: int = Field(default=None, description=r""" The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. """)
    selector: LabelSelector = Field(default=None, description=r""" Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels. """)
    strategy: DeploymentStrategy = Field(default=None, description=r""" The deployment strategy to use to replace existing pods with new ones. """)
    template: PodTemplateSpec = Field(default=None, description=r""" Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always". """)
