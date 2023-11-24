from pydantic import BaseModel, Field


class WatchEvent(BaseModel):
    object: Any = Field(default=None, description=r""" Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context. """)
    type: str = Field(default=None)
