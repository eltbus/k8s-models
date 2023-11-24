from pydantic import BaseModel, Field


class DaemonSetUpdateStrategy(BaseModel):
    rollingUpdate: RollingUpdateDaemonSet = Field(default=None, description=r""" Rolling update config params. Present only if type = "RollingUpdate". """)
    type: str = Field(default=None, description=r""" Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate. """)
