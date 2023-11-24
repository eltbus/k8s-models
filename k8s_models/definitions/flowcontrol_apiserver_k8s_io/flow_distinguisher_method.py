from pydantic import BaseModel, Field


class FlowDistinguisherMethod(BaseModel):
    type: str = Field(default=None, description=r""" `type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required. """)
