from pydantic import BaseModel, Field

from k8s_models.definitions.core.container_state_running import ContainerStateRunning
from k8s_models.definitions.core.container_state_terminated import ContainerStateTerminated
from k8s_models.definitions.core.container_state_waiting import ContainerStateWaiting


class ContainerState(BaseModel):
    running: ContainerStateRunning = Field(default=None, description=r""" Details about a running container """)
    terminated: ContainerStateTerminated = Field(default=None, description=r""" Details about a terminated container """)
    waiting: ContainerStateWaiting = Field(default=None, description=r""" Details about a waiting container """)
