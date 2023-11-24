from pydantic import BaseModel, Field


class PriorityLevelConfigurationStatus(BaseModel):
    conditions: List[PriorityLevelConfigurationCondition] = Field(default=None, description=r""" `conditions` is the current state of "request-priority". """)
