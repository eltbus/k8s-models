from typing import List

from pydantic import BaseModel, Field


class Capabilities(BaseModel):
    add: List[str] = Field(default=None, description=r""" Added capabilities """)
    drop: List[str] = Field(default=None, description=r""" Removed capabilities """)
