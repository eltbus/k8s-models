from pydantic import BaseModel, Field


class ContainerStateRunning(BaseModel):
    startedAt: Time = Field(default=None, description=r""" Time at which the container was last (re-)started """)
