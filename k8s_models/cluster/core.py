from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta, ListMeta, Time
from k8s_models.definitions.core import (
    AWSElasticBlockStoreVolumeSource,
    AttachedVolume,
    AzureDiskVolumeSource,
    AzureFilePersistentVolumeSource,
    CSIPersistentVolumeSource,
    CephFSPersistentVolumeSource,
    CinderPersistentVolumeSource,
    ComponentCondition,
    ContainerImage,
    FCVolumeSource,
    FlexPersistentVolumeSource,
    FlockerVolumeSource,
    GCEPersistentDiskVolumeSource,
    GlusterfsPersistentVolumeSource,
    HostPathVolumeSource,
    ISCSIPersistentVolumeSource,
    LocalObjectReference,
    LocalVolumeSource,
    NFSVolumeSource,
    NamespaceCondition,
    NodeAddress,
    NodeCondition,
    NodeConfigSource,
    NodeConfigStatus,
    NodeDaemonEndpoints,
    NodeSystemInfo,
    ObjectReference,
    PhotonPersistentDiskVolumeSource,
    PortworxVolumeSource,
    QuobyteVolumeSource,
    RBDPersistentVolumeSource,
    ScaleIOPersistentVolumeSource,
    ScopeSelector,
    StorageOSPersistentVolumeSource,
    Taint,
    VolumeNodeAffinity,
    VsphereVirtualDiskVolumeSource,
)

class Binding(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="Binding", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	target: ObjectReference = Field(default=None, description=r""" The target object that you want to bind to the standard object. """)

class ComponentStatus(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	conditions: List[ComponentCondition] = Field(default=None, description=r""" List of component conditions observed """)
	kind: str = Field(default="ComponentStatus", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)

class ComponentStatusList(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ComponentStatus] = Field(default=None, description=r""" List of ComponentStatus objects. """)
	kind: str = Field(default="ComponentStatusList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)

class Namespace(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="Namespace", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: NamespaceSpec = Field(default=None, description=r""" Spec defines the behavior of the Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
	status: NamespaceStatus = Field(default=None, description=r""" Status describes the current status of a Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)

class NamespaceSpec(BaseModel):
	finalizers: List[str] = Field(default=None, description=r""" Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ """)

class NamespaceStatus(BaseModel):
	conditions: List[NamespaceCondition] = Field(default=None, description=r""" Represents the latest available observations of a namespace's current state. """)
	phase: str = Field(default=None, description=r""" Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ """)

class NamespaceList(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[Namespace] = Field(default=None, description=r""" Items is the list of Namespace objects in the list. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ """)
	kind: str = Field(default="NamespaceList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)

class Node(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="Node", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: NodeSpec = Field(default=None, description=r""" Spec defines the behavior of a node. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
	status: NodeStatus = Field(default=None, description=r""" Most recently observed status of the node. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)

class NodeSpec(BaseModel):
	configSource: NodeConfigSource = Field(default=None, description=r""" Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed. """)
	externalID: str = Field(default=None, description=r""" Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966 """)
	podCIDR: str = Field(default=None, description=r""" PodCIDR represents the pod IP range assigned to the node. """)
	podCIDRs: List[str] = Field(default=None, description=r""" podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6. """)
	providerID: str = Field(default=None, description=r""" ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID> """)
	taints: List[Taint] = Field(default=None, description=r""" If specified, the node's taints. """)
	unschedulable: bool = Field(default=None, description=r""" Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration """)

class NodeStatus(BaseModel):
	addresses: List[NodeAddress] = Field(default=None, description=r""" List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node's address in its own status or consumers of the downward API (status.hostIP). """)
	allocatable: dict = Field(default=None, description=r""" Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity. """)
	capacity: dict = Field(default=None, description=r""" Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity """)
	conditions: List[NodeCondition] = Field(default=None, description=r""" Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition """)
	config: NodeConfigStatus = Field(default=None, description=r""" Status of the config assigned to the node via the dynamic Kubelet config feature. """)
	daemonEndpoints: NodeDaemonEndpoints = Field(default=None, description=r""" Endpoints of daemons running on the Node. """)
	images: List[ContainerImage] = Field(default=None, description=r""" List of container images on this node """)
	nodeInfo: NodeSystemInfo = Field(default=None, description=r""" Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#info """)
	phase: str = Field(default=None, description=r""" NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated. """)
	volumesAttached: List[AttachedVolume] = Field(default=None, description=r""" List of volumes that are attached to the node. """)
	volumesInUse: List[str] = Field(default=None, description=r""" List of attachable volumes in use (mounted) by the node. """)

class NodeList(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[Node] = Field(default=None, description=r""" List of nodes """)
	kind: str = Field(default="NodeList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)

class PersistentVolume(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="PersistentVolume", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: PersistentVolumeSpec = Field(default=None, description=r""" spec defines a specification of a persistent volume owned by the cluster. Provisioned by an administrator. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes """)
	status: PersistentVolumeStatus = Field(default=None, description=r""" status represents the current information/status for the persistent volume. Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes """)

class PersistentVolumeSpec(BaseModel):
	accessModes: List[str] = Field(default=None, description=r""" accessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes """)
	awsElasticBlockStore: AWSElasticBlockStoreVolumeSource = Field(default=None, description=r""" awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)
	azureDisk: AzureDiskVolumeSource = Field(default=None, description=r""" azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. """)
	azureFile: AzureFilePersistentVolumeSource = Field(default=None, description=r""" azureFile represents an Azure File Service mount on the host and bind mount to the pod. """)
	capacity: dict = Field(default=None, description=r""" capacity is the description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity """)
	cephfs: CephFSPersistentVolumeSource = Field(default=None, description=r""" cephFS represents a Ceph FS mount on the host that shares a pod's lifetime """)
	cinder: CinderPersistentVolumeSource = Field(default=None, description=r""" cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
	claimRef: ObjectReference = Field(default=None, description=r""" claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding """)
	csi: CSIPersistentVolumeSource = Field(default=None, description=r""" csi represents storage that is handled by an external CSI driver (Beta feature). """)
	fc: FCVolumeSource = Field(default=None, description=r""" fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod. """)
	flexVolume: FlexPersistentVolumeSource = Field(default=None, description=r""" flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. """)
	flocker: FlockerVolumeSource = Field(default=None, description=r""" flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running """)
	gcePersistentDisk: GCEPersistentDiskVolumeSource = Field(default=None, description=r""" gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
	glusterfs: GlusterfsPersistentVolumeSource = Field(default=None, description=r""" glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md """)
	hostPath: HostPathVolumeSource = Field(default=None, description=r""" hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)
	iscsi: ISCSIPersistentVolumeSource = Field(default=None, description=r""" iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. """)
	local: LocalVolumeSource = Field(default=None, description=r""" local represents directly-attached storage with node affinity """)
	mountOptions: List[str] = Field(default=None, description=r""" mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options """)
	nfs: NFSVolumeSource = Field(default=None, description=r""" nfs represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
	nodeAffinity: VolumeNodeAffinity = Field(default=None, description=r""" nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume. """)
	persistentVolumeReclaimPolicy: str = Field(default=None, description=r""" persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming """)
	photonPersistentDisk: PhotonPersistentDiskVolumeSource = Field(default=None, description=r""" photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine """)
	portworxVolume: PortworxVolumeSource = Field(default=None, description=r""" portworxVolume represents a portworx volume attached and mounted on kubelets host machine """)
	quobyte: QuobyteVolumeSource = Field(default=None, description=r""" quobyte represents a Quobyte mount on the host that shares a pod's lifetime """)
	rbd: RBDPersistentVolumeSource = Field(default=None, description=r""" rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md """)
	scaleIO: ScaleIOPersistentVolumeSource = Field(default=None, description=r""" scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. """)
	storageClassName: str = Field(default=None, description=r""" storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass. """)
	storageos: StorageOSPersistentVolumeSource = Field(default=None, description=r""" storageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md """)
	volumeMode: str = Field(default=None, description=r""" volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec. """)
	vsphereVolume: VsphereVirtualDiskVolumeSource = Field(default=None, description=r""" vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine """)

class PersistentVolumeStatus(BaseModel):
	lastPhaseTransitionTime: Time = Field(default=None, description=r""" lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. This is an alpha field and requires enabling PersistentVolumeLastPhaseTransitionTime feature. """)
	message: str = Field(default=None, description=r""" message is a human-readable message indicating details about why the volume is in this state. """)
	phase: str = Field(default=None, description=r""" phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase """)
	reason: str = Field(default=None, description=r""" reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. """)

class PersistentVolumeList(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[PersistentVolume] = Field(default=None, description=r""" items is a list of persistent volumes. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes """)
	kind: str = Field(default="PersistentVolumeList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)

class ResourceQuota(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="ResourceQuota", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: ResourceQuotaSpec = Field(default=None, description=r""" Spec defines the desired quota. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
	status: ResourceQuotaStatus = Field(default=None, description=r""" Status defines the actual enforced quota and its current usage. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)

class ResourceQuotaSpec(BaseModel):
	hard: dict = Field(default=None, description=r""" hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """)
	scopeSelector: ScopeSelector = Field(default=None, description=r""" scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched. """)
	scopes: List[str] = Field(default=None, description=r""" A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. """)

class ResourceQuotaStatus(BaseModel):
	hard: dict = Field(default=None, description=r""" Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """)
	used: dict = Field(default=None, description=r""" Used is the current observed total usage of the resource in the namespace. """)

class ResourceQuotaList(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ResourceQuota] = Field(default=None, description=r""" Items is a list of ResourceQuota objects. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """)
	kind: str = Field(default="ResourceQuotaList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)

class ServiceAccount(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	automountServiceAccountToken: bool = Field(default=None, description=r""" AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level. """)
	imagePullSecrets: List[LocalObjectReference] = Field(default=None, description=r""" ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod """)
	kind: str = Field(default="ServiceAccount", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	secrets: List[ObjectReference] = Field(default=None, description=r""" Secrets is a list of the secrets in the same namespace that pods running using this ServiceAccount are allowed to use. Pods are only limited to this list if this service account has a "kubernetes.io/enforce-mountable-secrets" annotation set to "true". This field should not be used to find auto-generated service account token secrets for use outside of pods. Instead, tokens can be requested directly using the TokenRequest API, or service account token secrets can be manually created. More info: https://kubernetes.io/docs/concepts/configuration/secret """)

class ServiceAccountList(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ServiceAccount] = Field(default=None, description=r""" List of ServiceAccounts. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ """)
	kind: str = Field(default="ServiceAccountList", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
