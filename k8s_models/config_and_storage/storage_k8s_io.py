from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta, LabelSelector
from k8s_models.definitions.core import TopologySelectorTerm, Quantity
from k8s_models.definitions.unknown import VolumeAttachmentStatus
from k8s_models.config_and_storage.storage import CSIDriverSpec, CSINodeSpec, VolumeAttachmentSpec

class CSIDriver(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata. metadata.Name indicates the name of the CSI driver that this object refers to; it MUST be the same name returned by the CSI GetPluginName() call for that driver. The driver name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics between. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: CSIDriverSpec = Field(default=None, description=r""" spec represents the specification of the CSI Driver. """)

class CSINode(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. metadata.name must be the Kubernetes node name. """)
	spec: CSINodeSpec = Field(default=None, description=r""" spec is the specification of CSINode """)

class StorageClass(BaseModel):
	allowVolumeExpansion: bool = Field(default=None, description=r""" allowVolumeExpansion shows whether the storage class allow volume expand. """)
	allowedTopologies: List[TopologySelectorTerm] = Field(default=None, description=r""" allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature. """)
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	mountOptions: List[str] = Field(default=None, description=r""" mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid. """)
	parameters: dict = Field(default=None, description=r""" parameters holds the parameters for the provisioner that should create volumes of this storage class. """)
	provisioner: str = Field(default=None, description=r""" provisioner indicates the type of the provisioner. """)
	reclaimPolicy: str = Field(default=None, description=r""" reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete. """)
	volumeBindingMode: str = Field(default=None, description=r""" volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature. """)

class CSIStorageCapacity(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	capacity: Quantity = Field(default=None, description=r""" capacity is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  The semantic is currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be used to provision volumes. If not set, that information is currently unavailable. """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	maximumVolumeSize: Quantity = Field(default=None, description=r""" maximumVolumeSize is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  This is defined since CSI spec 1.4.0 as the largest size that may be used in a CreateVolumeRequest.capacity_range.required_bytes field to create a volume with the same parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is ResourceRequirements.Requests in a volume claim. """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. The name has no particular meaning. It must be a DNS subdomain (dots allowed, 253 characters). To ensure that there are no conflicts with other CSI drivers on the cluster, the recommendation is to use csisc-<uuid>, a generated name, or a reverse-domain name which ends with the unique CSI driver name.  Objects are namespaced.  More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	nodeTopology: LabelSelector = Field(default=None, description=r""" nodeTopology defines which nodes have access to the storage for which capacity was reported. If not set, the storage is not accessible from any node in the cluster. If empty, the storage is accessible from all nodes. This field is immutable. """)
	storageClassName: str = Field(default=None, description=r""" storageClassName represents the name of the StorageClass that the reported capacity applies to. It must meet the same requirements as the name of a StorageClass object (non-empty, DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and should be removed by its creator. This field is immutable. """)

class VolumeAttachment(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: VolumeAttachmentSpec = Field(default=None, description=r""" spec represents specification of the desired attach/detach volume behavior. Populated by the Kubernetes system. """)
	status: VolumeAttachmentStatus = Field(default=None, description=r""" status represents status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher. """)
