from pydantic import BaseModel, Field


class VolumeError(BaseModel):
    message: str = Field(default=None, description=r""" message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information. """)
    time: Time = Field(default=None, description=r""" time represents the time the error was encountered. """)
