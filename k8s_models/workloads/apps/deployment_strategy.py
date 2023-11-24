from pydantic import BaseModel, Field

from k8s_models.workloads.apps.rolling_update_deployment import RollingUpdateDeployment


class DeploymentStrategy(BaseModel):
    rollingUpdate: RollingUpdateDeployment = Field(default=None, description=r""" Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate. """)
    type: str = Field(default=None, description=r""" Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate. """)
