from pydantic import BaseModel, Field


class ContainerStateWaiting(BaseModel):
    message: str = Field(default=None, description=r""" Message regarding why the container is not yet running. """)
    reason: str = Field(default=None, description=r""" (brief) reason the container is not yet running. """)
