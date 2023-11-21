from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.models import KubeModel
from k8s_models.definitions.core import (
    AWSElasticBlockStoreVolumeSource,
    AzureDiskVolumeSource,
    AzureFileVolumeSource,
    CSIVolumeSource,
    CephFSVolumeSource,
    CinderVolumeSource,
    ConfigMapVolumeSource,
    DownwardAPIVolumeSource,
    EmptyDirVolumeSource,
    EphemeralVolumeSource,
    FCVolumeSource,
    FlexVolumeSource,
    FlockerVolumeSource,
    GCEPersistentDiskVolumeSource,
    GitRepoVolumeSource,
    GlusterfsVolumeSource,
    HostPathVolumeSource,
    ISCSIVolumeSource,
    NFSVolumeSource,
    PersistentVolumeClaimCondition,
    PersistentVolumeClaimVolumeSource,
    PhotonPersistentDiskVolumeSource,
    PortworxVolumeSource,
    ProjectedVolumeSource,
    QuobyteVolumeSource,
    RBDVolumeSource,
    ResourceRequirements,
    ScaleIOVolumeSource,
    SecretVolumeSource,
    StorageOSVolumeSource,
    TypedLocalObjectReference,
    TypedObjectReference,
    VsphereVirtualDiskVolumeSource,
)
from k8s_models.definitions.meta import ObjectMeta, LabelSelector, ListMeta

class ConfigMap(KubeModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	binaryData: dict = Field(default=None, description=r""" BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet. """)
	data: dict = Field(default=None, description=r""" Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. """)
	immutable: bool = Field(default=None, description=r""" Immutable, if set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. """)
	kind: str = Field(default="ConfigMap", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)

class ConfigMapList(KubeModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ConfigMap] = Field(default=None, description=r""" Items is the list of ConfigMaps. """)
	kind: str = Field(default="ConfigMapList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)

class Secret(KubeModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	data: dict = Field(default=None, description=r""" Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4 """)
	immutable: bool = Field(default=None, description=r""" Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. """)
	kind: str = Field(default="Secret", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	stringData: dict = Field(default=None, description=r""" stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API. """)
	type: str = Field(default=None, description=r""" Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types """)

class SecretList(KubeModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[Secret] = Field(default=None, description=r""" Items is a list of secret objects. More info: https://kubernetes.io/docs/concepts/configuration/secret """)
	kind: str = Field(default="SecretList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)

class PersistentVolumeClaim(KubeModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="PersistentVolumeClaim", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: PersistentVolumeClaimSpec = Field(default=None, description=r""" spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
	status: PersistentVolumeClaimStatus = Field(default=None, description=r""" status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)

class PersistentVolumeClaimSpec(BaseModel):
	accessModes: List[str] = Field(default=None, description=r""" accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 """)
	dataSource: TypedLocalObjectReference = Field(default=None, description=r""" dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource. """)
	dataSourceRef: TypedObjectReference = Field(default=None, description=r""" dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef   allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef   preserves all values, and generates an error if a disallowed value is   specified. * While dataSource only allows local objects, dataSourceRef allows objects   in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled. """)
	resources: ResourceRequirements = Field(default=None, description=r""" resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources """)
	selector: LabelSelector = Field(default=None, description=r""" selector is a label query over volumes to consider for binding. """)
	storageClassName: str = Field(default=None, description=r""" storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 """)
	volumeMode: str = Field(default=None, description=r""" volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. """)
	volumeName: str = Field(default=None, description=r""" volumeName is the binding reference to the PersistentVolume backing this claim. """)

class PersistentVolumeClaimStatus(BaseModel):
	accessModes: List[str] = Field(default=None, description=r""" accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 """)
	allocatedResourceStatuses: dict = Field(default=None, description=r""" allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either: 	* Un-prefixed keys: 		- storage - the capacity of the volume. 	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states: 	- ControllerResizeInProgress: 		State set when resize controller starts resizing the volume in control-plane. 	- ControllerResizeFailed: 		State set when resize has failed in resize controller with a terminal error. 	- NodeResizePending: 		State set when resize controller has finished resizing the volume but further resizing of 		volume is needed on the node. 	- NodeResizeInProgress: 		State set when kubelet starts resizing the volume. 	- NodeResizeFailed: 		State set when resizing has failed in kubelet with a terminal error. Transient errors don't set 		NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states: 	- pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress"      - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed"      - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending"      - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress"      - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature. """)
	allocatedResources: dict = Field(default=None, description=r""" allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either: 	* Un-prefixed keys: 		- storage - the capacity of the volume. 	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature. """)
	capacity: dict = Field(default=None, description=r""" capacity represents the actual resources of the underlying volume. """)
	conditions: List[PersistentVolumeClaimCondition] = Field(default=None, description=r""" conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'. """)
	phase: str = Field(default=None, description=r""" phase represents the current phase of PersistentVolumeClaim. """)

class PersistentVolumeClaimList(KubeModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[PersistentVolumeClaim] = Field(default=None, description=r""" items is a list of persistent volume claims. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
	kind: str = Field(default="PersistentVolumeClaimList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)

class Volume(BaseModel):
	awsElasticBlockStore: AWSElasticBlockStoreVolumeSource = Field(default=None, description=r""" awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)
	azureDisk: AzureDiskVolumeSource = Field(default=None, description=r""" azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. """)
	azureFile: AzureFileVolumeSource = Field(default=None, description=r""" azureFile represents an Azure File Service mount on the host and bind mount to the pod. """)
	cephfs: CephFSVolumeSource = Field(default=None, description=r""" cephFS represents a Ceph FS mount on the host that shares a pod's lifetime """)
	cinder: CinderVolumeSource = Field(default=None, description=r""" cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
	configMap: ConfigMapVolumeSource = Field(default=None, description=r""" configMap represents a configMap that should populate this volume """)
	csi: CSIVolumeSource = Field(default=None, description=r""" csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers (Beta feature). """)
	downwardAPI: DownwardAPIVolumeSource = Field(default=None, description=r""" downwardAPI represents downward API about the pod that should populate this volume """)
	emptyDir: EmptyDirVolumeSource = Field(default=None, description=r""" emptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """)
	ephemeral: EphemeralVolumeSource = Field(default=None, description=r""" ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.  Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity    tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through    a PersistentVolumeClaim (see EphemeralVolumeSource for more    information on the connection between this volume type    and PersistentVolumeClaim).  Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.  Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.  A pod can use both types of ephemeral volumes and persistent volumes at the same time. """)
	fc: FCVolumeSource = Field(default=None, description=r""" fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod. """)
	flexVolume: FlexVolumeSource = Field(default=None, description=r""" flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. """)
	flocker: FlockerVolumeSource = Field(default=None, description=r""" flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running """)
	gcePersistentDisk: GCEPersistentDiskVolumeSource = Field(default=None, description=r""" gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
	gitRepo: GitRepoVolumeSource = Field(default=None, description=r""" gitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container. """)
	glusterfs: GlusterfsVolumeSource = Field(default=None, description=r""" glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md """)
	hostPath: HostPathVolumeSource = Field(default=None, description=r""" hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)
	iscsi: ISCSIVolumeSource = Field(default=None, description=r""" iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md """)
	name: str = Field(default=None, description=r""" name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	nfs: NFSVolumeSource = Field(default=None, description=r""" nfs represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
	persistentVolumeClaim: PersistentVolumeClaimVolumeSource = Field(default=None, description=r""" persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
	photonPersistentDisk: PhotonPersistentDiskVolumeSource = Field(default=None, description=r""" photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine """)
	portworxVolume: PortworxVolumeSource = Field(default=None, description=r""" portworxVolume represents a portworx volume attached and mounted on kubelets host machine """)
	projected: ProjectedVolumeSource = Field(default=None, description=r""" projected items for all in one resources secrets, configmaps, and downward API """)
	quobyte: QuobyteVolumeSource = Field(default=None, description=r""" quobyte represents a Quobyte mount on the host that shares a pod's lifetime """)
	rbd: RBDVolumeSource = Field(default=None, description=r""" rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md """)
	scaleIO: ScaleIOVolumeSource = Field(default=None, description=r""" scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. """)
	secret: SecretVolumeSource = Field(default=None, description=r""" secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret """)
	storageos: StorageOSVolumeSource = Field(default=None, description=r""" storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. """)
	vsphereVolume: VsphereVirtualDiskVolumeSource = Field(default=None, description=r""" vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine """)
