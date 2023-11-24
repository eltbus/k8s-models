from pydantic import BaseModel, Field


class Subject(BaseModel):
    group: GroupSubject = Field(default=None, description=r""" `group` matches based on user group name. """)
    kind: str = Field(default="Subject", description=r""" `kind` indicates which one of the other fields is non-empty. Required """)
    serviceAccount: ServiceAccountSubject = Field(default=None, description=r""" `serviceAccount` matches ServiceAccounts. """)
    user: UserSubject = Field(default=None, description=r""" `user` matches based on username. """)
