from typing import List

from pydantic import BaseModel, Field


class UncountedTerminatedPods(BaseModel):
    failed: List[str] = Field(default=None, description=r""" failed holds UIDs of failed Pods. """)
    succeeded: List[str] = Field(default=None, description=r""" succeeded holds UIDs of succeeded Pods. """)
