from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.flowcontrol_apiserver_k8s_io.flow_schema_condition import FlowSchemaCondition


class FlowSchemaStatus(BaseModel):
    conditions: List[FlowSchemaCondition] = Field(default=None, description=r""" `conditions` is a list of the current states of FlowSchema. """)
