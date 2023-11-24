from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.object_reference import ObjectReference
from k8s_models.definitions.meta.time import Time


class CronJobStatus(BaseModel):
    active: List[ObjectReference] = Field(default=None, description=r""" A list of pointers to currently running jobs. """)
    lastScheduleTime: Time = Field(default=None, description=r""" Information when was the last time the job was successfully scheduled. """)
    lastSuccessfulTime: Time = Field(default=None, description=r""" Information when was the last time the job successfully completed. """)
