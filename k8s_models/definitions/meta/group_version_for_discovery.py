from pydantic import BaseModel, Field


class GroupVersionForDiscovery(BaseModel):
    groupVersion: str = Field(default=None, description=r""" groupVersion specifies the API group and version in the form "group/version" """)
    version: str = Field(default=None, description=r""" version specifies the version in the form of "version". This is to save the clients the trouble of splitting the GroupVersion. """)
