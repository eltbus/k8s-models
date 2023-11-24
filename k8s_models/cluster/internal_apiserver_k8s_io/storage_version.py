from pydantic import Field

from k8s_models.models import KubeModel


class StorageVersion(KubeModel):
    apiVersion: str = Field(default="v1alpha1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="StorageVersion", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" The name is <group>.<resource>. """)
    spec: StorageVersionSpec = Field(default=None, description=r""" Spec is an empty spec. It is here to comply with Kubernetes API style. """)
    status: StorageVersionStatus = Field(default=None, description=r""" API server instances report the version they can decode and the version they encode objects to when persisting objects in the backend. """)
