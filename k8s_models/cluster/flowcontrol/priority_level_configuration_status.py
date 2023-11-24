from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.flowcontrol_apiserver_k8s_io.priority_level_configuration_condition import PriorityLevelConfigurationCondition


class PriorityLevelConfigurationStatus(BaseModel):
    conditions: List[PriorityLevelConfigurationCondition] = Field(default=None, description=r""" `conditions` is the current state of "request-priority". """)
