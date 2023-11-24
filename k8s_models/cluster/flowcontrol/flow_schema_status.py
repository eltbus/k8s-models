from pydantic import BaseModel, Field


class FlowSchemaStatus(BaseModel):
    conditions: List[FlowSchemaCondition] = Field(default=None, description=r""" `conditions` is a list of the current states of FlowSchema. """)
