from pydantic import BaseModel, Field


class PriorityLevelConfigurationReference(BaseModel):
    name: str = Field(default=None, description=r""" `name` is the name of the priority level configuration being referenced Required. """)
