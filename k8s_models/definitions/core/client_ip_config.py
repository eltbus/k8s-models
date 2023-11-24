from pydantic import BaseModel, Field


class ClientIPConfig(BaseModel):
    timeoutSeconds: int = Field(default=None, description=r""" timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours). """)
