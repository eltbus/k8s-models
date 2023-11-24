from pydantic import BaseModel, Field


class GroupSubject(BaseModel):
    name: str = Field(default=None, description=r""" name is the user group that matches, or "*" to match all user groups. See https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go for some well-known group names. Required. """)
