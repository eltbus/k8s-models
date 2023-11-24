from pydantic import BaseModel, Field


class ConfigMapNodeConfigSource(BaseModel):
    kubeletConfigKey: str = Field(default=None, description=r""" KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases. """)
    name: str = Field(default=None, description=r""" Name is the metadata.name of the referenced ConfigMap. This field is required in all cases. """)
    namespace: str = Field(default=None, description=r""" Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases. """)
    resourceVersion: str = Field(default=None, description=r""" ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. """)
    uid: str = Field(default=None, description=r""" UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. """)
