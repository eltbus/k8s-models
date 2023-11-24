from pydantic import BaseModel, Field


class SelfSubjectReviewStatus(BaseModel):
    userInfo: UserInfo = Field(default=None, description=r""" User attributes of the user making this request. """)
