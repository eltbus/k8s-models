from pydantic import BaseModel, Field


class StatefulSetUpdateStrategy(BaseModel):
    rollingUpdate: RollingUpdateStatefulSetStrategy = Field(default=None, description=r""" RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType. """)
    type: str = Field(default=None, description=r""" Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate. """)
