from pydantic import BaseModel, Field


class DeploymentStrategy(BaseModel):
    rollingUpdate: RollingUpdateDeployment = Field(default=None, description=r""" Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate. """)
    type: str = Field(default=None, description=r""" Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate. """)
