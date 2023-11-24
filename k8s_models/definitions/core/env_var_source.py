from pydantic import BaseModel, Field


class EnvVarSource(BaseModel):
    configMapKeyRef: ConfigMapKeySelector = Field(default=None, description=r""" Selects a key of a ConfigMap. """)
    fieldRef: ObjectFieldSelector = Field(default=None, description=r""" Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. """)
    resourceFieldRef: ResourceFieldSelector = Field(default=None, description=r""" Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. """)
    secretKeyRef: SecretKeySelector = Field(default=None, description=r""" Selects a key of a secret in the pod's namespace """)
