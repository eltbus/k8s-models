from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time


class VolumeError(BaseModel):
    message: str = Field(default=None, description=r""" message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information. """)
    time: Time = Field(default=None, description=r""" time represents the time the error was encountered. """)
