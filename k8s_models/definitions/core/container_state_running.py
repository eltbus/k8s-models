from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time


class ContainerStateRunning(BaseModel):
    startedAt: Time = Field(default=None, description=r""" Time at which the container was last (re-)started """)
