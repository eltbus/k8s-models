from pydantic import BaseModel, Field


class APIServiceStatus(BaseModel):
    conditions: List[APIServiceCondition] = Field(default=None, description=r""" Current service state of apiService. """)
