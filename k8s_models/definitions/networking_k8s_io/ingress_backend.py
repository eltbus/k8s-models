from pydantic import BaseModel, Field

from k8s_models.definitions.core.typed_local_object_reference import TypedLocalObjectReference
from k8s_models.definitions.networking_k8s_io.ingress_service_backend import IngressServiceBackend


class IngressBackend(BaseModel):
    resource: TypedLocalObjectReference = Field(default=None, description=r""" resource is an ObjectRef to another Kubernetes resource in the namespace of the Ingress object. If resource is specified, a service.Name and service.Port must not be specified. This is a mutually exclusive setting with "Service". """)
    service: IngressServiceBackend = Field(default=None, description=r""" service references a service as a backend. This is a mutually exclusive setting with "Resource". """)
