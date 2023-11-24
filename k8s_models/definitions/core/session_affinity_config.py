from pydantic import BaseModel, Field


class SessionAffinityConfig(BaseModel):
    clientIP: ClientIPConfig = Field(default=None, description=r""" clientIP contains the configurations of Client IP based session affinity. """)
