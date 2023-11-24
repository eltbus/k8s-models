from pydantic import BaseModel, Field

from k8s_models.definitions.authentication_k8s_io.user_info import UserInfo


class SelfSubjectReviewStatus(BaseModel):
    userInfo: UserInfo = Field(default=None, description=r""" User attributes of the user making this request. """)
