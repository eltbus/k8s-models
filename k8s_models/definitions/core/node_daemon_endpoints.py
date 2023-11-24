from pydantic import BaseModel, Field

from k8s_models.definitions.core.daemon_endpoint import DaemonEndpoint


class NodeDaemonEndpoints(BaseModel):
    kubeletEndpoint: DaemonEndpoint = Field(default=None, description=r""" Endpoint on which Kubelet is listening. """)
