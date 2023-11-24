from pydantic import BaseModel, Field


class LimitRangeSpec(BaseModel):
    limits: List[LimitRangeItem] = Field(default=None, description=r""" Limits is the list of LimitRangeItem objects that are enforced. """)
