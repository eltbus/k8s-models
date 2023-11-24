from pydantic import BaseModel, Field


class NodeConfigSource(BaseModel):
    configMap: ConfigMapNodeConfigSource = Field(default=None, description=r""" ConfigMap is a reference to a Node's ConfigMap """)
