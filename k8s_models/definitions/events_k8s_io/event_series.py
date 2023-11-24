from pydantic import BaseModel, Field


class EventSeries(BaseModel):
    count: int = Field(default=None, description=r""" count is the number of occurrences in this series up to the last heartbeat time. """)
    lastObservedTime: MicroTime = Field(default=None, description=r""" lastObservedTime is the time when last Event from the series was seen before last heartbeat. """)
