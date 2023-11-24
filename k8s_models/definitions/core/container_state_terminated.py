from pydantic import BaseModel, Field


class ContainerStateTerminated(BaseModel):
    containerID: str = Field(default=None, description=r""" Container's ID in the format '<type>://<container_id>' """)
    exitCode: int = Field(default=None, description=r""" Exit status from the last termination of the container """)
    finishedAt: Time = Field(default=None, description=r""" Time at which the container last terminated """)
    message: str = Field(default=None, description=r""" Message regarding the last termination of the container """)
    reason: str = Field(default=None, description=r""" (brief) reason from the last termination of the container """)
    signal: int = Field(default=None, description=r""" Signal from the last termination of the container """)
    startedAt: Time = Field(default=None, description=r""" Time at which previous execution of the container started """)
