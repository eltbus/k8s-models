from pydantic import BaseModel, Field


class ContainerState(BaseModel):
    running: ContainerStateRunning = Field(default=None, description=r""" Details about a running container """)
    terminated: ContainerStateTerminated = Field(default=None, description=r""" Details about a terminated container """)
    waiting: ContainerStateWaiting = Field(default=None, description=r""" Details about a waiting container """)
