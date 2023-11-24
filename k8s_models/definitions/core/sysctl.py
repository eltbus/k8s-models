from pydantic import BaseModel, Field


class Sysctl(BaseModel):
    name: str = Field(default=None, description=r""" Name of a property to set """)
    value: str = Field(default=None, description=r""" Value of a property to set """)
