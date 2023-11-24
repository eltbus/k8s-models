from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.limit_range_item import LimitRangeItem


class LimitRangeSpec(BaseModel):
    limits: List[LimitRangeItem] = Field(default=None, description=r""" Limits is the list of LimitRangeItem objects that are enforced. """)
