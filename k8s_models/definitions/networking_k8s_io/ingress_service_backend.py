from pydantic import BaseModel, Field

from k8s_models.definitions.networking_k8s_io.service_backend_port import ServiceBackendPort


class IngressServiceBackend(BaseModel):
    name: str = Field(default=None, description=r""" name is the referenced service. The service must exist in the same namespace as the Ingress object. """)
    port: ServiceBackendPort = Field(default=None, description=r""" port of the referenced service. A port name or port number is required for a IngressServiceBackend. """)
