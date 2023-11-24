from pydantic import BaseModel, Field

from k8s_models.definitions.apps.rolling_update_stateful_set_strategy import RollingUpdateStatefulSetStrategy


class StatefulSetUpdateStrategy(BaseModel):
    rollingUpdate: RollingUpdateStatefulSetStrategy = Field(default=None, description=r""" RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType. """)
    type: str = Field(default=None, description=r""" Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate. """)
