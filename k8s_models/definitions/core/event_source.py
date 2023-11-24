from pydantic import BaseModel, Field


class EventSource(BaseModel):
    component: str = Field(default=None, description=r""" Component from which the event is generated. """)
    host: str = Field(default=None, description=r""" Node name on which the event is generated. """)
