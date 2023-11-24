from pydantic import BaseModel, Field


class StatusDetails(BaseModel):
    causes: List[StatusCause] = Field(default=None, description=r""" The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes. """)
    group: str = Field(default=None, description=r""" The group attribute of the resource associated with the status StatusReason. """)
    kind: str = Field(default="StatusDetails", description=r""" The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described). """)
    retryAfterSeconds: int = Field(default=None, description=r""" If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action. """)
    uid: str = Field(default=None, description=r""" UID of the resource. (when there is a single resource which can be described). More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids """)
