from pydantic import Field

from k8s_models.models import KubeModel


class StorageClass(KubeModel):
    allowVolumeExpansion: bool = Field(default=None, description=r""" allowVolumeExpansion shows whether the storage class allow volume expand. """)
    allowedTopologies: List[TopologySelectorTerm] = Field(default=None, description=r""" allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature. """)
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="StorageClass", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    mountOptions: List[str] = Field(default=None, description=r""" mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid. """)
    parameters: dict = Field(default=None, description=r""" parameters holds the parameters for the provisioner that should create volumes of this storage class. """)
    provisioner: str = Field(default=None, description=r""" provisioner indicates the type of the provisioner. """)
    reclaimPolicy: str = Field(default=None, description=r""" reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete. """)
    volumeBindingMode: str = Field(default=None, description=r""" volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature. """)
