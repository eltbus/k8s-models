from pydantic import BaseModel, Field

from k8s_models.workloads.apps.rolling_update_daemon_set import RollingUpdateDaemonSet


class DaemonSetUpdateStrategy(BaseModel):
    rollingUpdate: RollingUpdateDaemonSet = Field(default=None, description=r""" Rolling update config params. Present only if type = "RollingUpdate". """)
    type: str = Field(default=None, description=r""" Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate. """)
