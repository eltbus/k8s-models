from pydantic import BaseModel, Field

from k8s_models.definitions.core.config_map_node_config_source import ConfigMapNodeConfigSource


class NodeConfigSource(BaseModel):
    configMap: ConfigMapNodeConfigSource = Field(default=None, description=r""" ConfigMap is a reference to a Node's ConfigMap """)
