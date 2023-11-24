from pydantic import BaseModel, Field


class SELinuxOptions(BaseModel):
    level: str = Field(default=None, description=r""" Level is SELinux level label that applies to the container. """)
    role: str = Field(default=None, description=r""" Role is a SELinux role label that applies to the container. """)
    type: str = Field(default=None, description=r""" Type is a SELinux type label that applies to the container. """)
    user: str = Field(default=None, description=r""" User is a SELinux user label that applies to the container. """)
