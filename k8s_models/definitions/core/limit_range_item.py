from pydantic import BaseModel, Field


class LimitRangeItem(BaseModel):
    default: dict = Field(default=None, description=r""" Default resource requirement limit value by resource name if resource limit is omitted. """)
    defaultRequest: dict = Field(default=None, description=r""" DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. """)
    max: dict = Field(default=None, description=r""" Max usage constraints on this kind by resource name. """)
    maxLimitRequestRatio: dict = Field(default=None, description=r""" MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. """)
    min: dict = Field(default=None, description=r""" Min usage constraints on this kind by resource name. """)
    type: str = Field(default=None, description=r""" Type of resource that this limit applies to. """)
