from pydantic import BaseModel, Field


class ServiceAccountSubject(BaseModel):
    name: str = Field(default=None, description=r""" `name` is the name of matching ServiceAccount objects, or "*" to match regardless of name. Required. """)
    namespace: str = Field(default=None, description=r""" `namespace` is the namespace of matching ServiceAccount objects. Required. """)
