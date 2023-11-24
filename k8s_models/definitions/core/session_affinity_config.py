from pydantic import BaseModel, Field

from k8s_models.definitions.core.client_ip_config import ClientIPConfig


class SessionAffinityConfig(BaseModel):
    clientIP: ClientIPConfig = Field(default=None, description=r""" clientIP contains the configurations of Client IP based session affinity. """)
