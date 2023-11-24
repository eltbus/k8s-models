from pydantic import BaseModel, Field


class NodeDaemonEndpoints(BaseModel):
    kubeletEndpoint: DaemonEndpoint = Field(default=None, description=r""" Endpoint on which Kubelet is listening. """)
