from pydantic import BaseModel, Field

from k8s_models.definitions.flowcontrol_apiserver_k8s_io.group_subject import GroupSubject
from k8s_models.definitions.flowcontrol_apiserver_k8s_io.service_account_subject import ServiceAccountSubject
from k8s_models.definitions.flowcontrol_apiserver_k8s_io.user_subject import UserSubject


class Subject(BaseModel):
    group: GroupSubject = Field(default=None, description=r""" `group` matches based on user group name. """)
    kind: str = Field(default="Subject", description=r""" `kind` indicates which one of the other fields is non-empty. Required """)
    serviceAccount: ServiceAccountSubject = Field(default=None, description=r""" `serviceAccount` matches ServiceAccounts. """)
    user: UserSubject = Field(default=None, description=r""" `user` matches based on username. """)
