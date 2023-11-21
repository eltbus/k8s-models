from __future__ import annotations
from typing import List, Any

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import Time, ObjectMeta, LabelSelector
from k8s_models.config_and_storage.core import PersistentVolumeClaimSpec

class AWSElasticBlockStoreVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)
	partition: int = Field(default=None, description=r""" partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). """)
	readOnly: bool = Field(default=None, description=r""" readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)
	volumeID: str = Field(default=None, description=r""" volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """)

class Affinity(BaseModel):
	nodeAffinity: NodeAffinity = Field(default=None, description=r""" Describes node affinity scheduling rules for the pod. """)
	podAffinity: PodAffinity = Field(default=None, description=r""" Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)). """)
	podAntiAffinity: PodAntiAffinity = Field(default=None, description=r""" Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)). """)

class AttachedVolume(BaseModel):
	devicePath: str = Field(default=None, description=r""" DevicePath represents the device path where the volume should be available """)
	name: str = Field(default=None, description=r""" Name of the attached volume """)

class AzureDiskVolumeSource(BaseModel):
	cachingMode: str = Field(default=None, description=r""" cachingMode is the Host Caching mode: None, Read Only, Read Write. """)
	diskName: str = Field(default=None, description=r""" diskName is the Name of the data disk in the blob storage """)
	diskURI: str = Field(default=None, description=r""" diskURI is the URI of data disk in the blob storage """)
	fsType: str = Field(default=None, description=r""" fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
	kind: str = Field(default="AzureDiskVolumeSource", description=r""" kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared """)
	readOnly: bool = Field(default=None, description=r""" readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)

class AzureFilePersistentVolumeSource(BaseModel):
	readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	secretName: str = Field(default=None, description=r""" secretName is the name of secret that contains Azure Storage Account Name and Key """)
	secretNamespace: str = Field(default=None, description=r""" secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod """)
	shareName: str = Field(default=None, description=r""" shareName is the azure Share Name """)

class AzureFileVolumeSource(BaseModel):
	readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	secretName: str = Field(default=None, description=r""" secretName is the  name of secret that contains Azure Storage Account Name and Key """)
	shareName: str = Field(default=None, description=r""" shareName is the azure share Name """)

class CSIPersistentVolumeSource(BaseModel):
	controllerExpandSecretRef: SecretReference = Field(default=None, description=r""" controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
	controllerPublishSecretRef: SecretReference = Field(default=None, description=r""" controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
	driver: str = Field(default=None, description=r""" driver is the name of the driver to use for this volume. Required. """)
	fsType: str = Field(default=None, description=r""" fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". """)
	nodeExpandSecretRef: SecretReference = Field(default=None, description=r""" nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This is a beta field which is enabled default by CSINodeExpandSecret feature gate. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
	nodePublishSecretRef: SecretReference = Field(default=None, description=r""" nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
	nodeStageSecretRef: SecretReference = Field(default=None, description=r""" nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """)
	readOnly: bool = Field(default=None, description=r""" readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). """)
	volumeAttributes: dict = Field(default=None, description=r""" volumeAttributes of the volume to publish. """)
	volumeHandle: str = Field(default=None, description=r""" volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. """)

class CSIVolumeSource(BaseModel):
	driver: str = Field(default=None, description=r""" driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. """)
	fsType: str = Field(default=None, description=r""" fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. """)
	nodePublishSecretRef: LocalObjectReference = Field(default=None, description=r""" nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed. """)
	readOnly: bool = Field(default=None, description=r""" readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). """)
	volumeAttributes: dict = Field(default=None, description=r""" volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values. """)

class Capabilities(BaseModel):
	add: List[str] = Field(default=None, description=r""" Added capabilities """)
	drop: List[str] = Field(default=None, description=r""" Removed capabilities """)

class CephFSPersistentVolumeSource(BaseModel):
	monitors: List[str] = Field(default=None, description=r""" monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
	path: str = Field(default=None, description=r""" path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / """)
	readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
	secretFile: str = Field(default=None, description=r""" secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
	secretRef: SecretReference = Field(default=None, description=r""" secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
	user: str = Field(default=None, description=r""" user is Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)

class CephFSVolumeSource(BaseModel):
	monitors: List[str] = Field(default=None, description=r""" monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
	path: str = Field(default=None, description=r""" path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / """)
	readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
	secretFile: str = Field(default=None, description=r""" secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
	secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)
	user: str = Field(default=None, description=r""" user is optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """)

class CinderPersistentVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
	readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
	secretRef: SecretReference = Field(default=None, description=r""" secretRef is Optional: points to a secret object containing parameters used to connect to OpenStack. """)
	volumeID: str = Field(default=None, description=r""" volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)

class CinderVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
	readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)
	secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is optional: points to a secret object containing parameters used to connect to OpenStack. """)
	volumeID: str = Field(default=None, description=r""" volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """)

class ClaimSource(BaseModel):
	resourceClaimName: str = Field(default=None, description=r""" ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod. """)
	resourceClaimTemplateName: str = Field(default=None, description=r""" ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim. """)

class ClientIPConfig(BaseModel):
	timeoutSeconds: int = Field(default=None, description=r""" timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours). """)

class ComponentCondition(BaseModel):
	error: str = Field(default=None, description=r""" Condition error code for a component. For example, a health check error code. """)
	message: str = Field(default=None, description=r""" Message about the condition for a component. For example, information about a health check. """)
	status: str = Field(default=None, description=r""" Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown". """)
	type: str = Field(default=None, description=r""" Type of condition for a component. Valid value: "Healthy" """)

class ConfigMapEnvSource(BaseModel):
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	optional: bool = Field(default=None, description=r""" Specify whether the ConfigMap must be defined """)

class ConfigMapKeySelector(BaseModel):
	key: str = Field(default=None, description=r""" The key to select. """)
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	optional: bool = Field(default=None, description=r""" Specify whether the ConfigMap or its key must be defined """)

class ConfigMapNodeConfigSource(BaseModel):
	kubeletConfigKey: str = Field(default=None, description=r""" KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases. """)
	name: str = Field(default=None, description=r""" Name is the metadata.name of the referenced ConfigMap. This field is required in all cases. """)
	namespace: str = Field(default=None, description=r""" Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases. """)
	resourceVersion: str = Field(default=None, description=r""" ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. """)
	uid: str = Field(default=None, description=r""" UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. """)

class ConfigMapProjection(BaseModel):
	items: List[KeyToPath] = Field(default=None, description=r""" items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	optional: bool = Field(default=None, description=r""" optional specify whether the ConfigMap or its keys must be defined """)

class ConfigMapVolumeSource(BaseModel):
	defaultMode: int = Field(default=None, description=r""" defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
	items: List[KeyToPath] = Field(default=None, description=r""" items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	optional: bool = Field(default=None, description=r""" optional specify whether the ConfigMap or its keys must be defined """)

class ContainerImage(BaseModel):
	names: List[str] = Field(default=None, description=r""" Names by which this image is known. e.g. ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"] """)
	sizeBytes: int = Field(default=None, description=r""" The size of the image in bytes. """)

class ContainerPort(BaseModel):
	containerPort: int = Field(default=None, description=r""" Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. """)
	hostIP: str = Field(default=None, description=r""" What host IP to bind the external port to. """)
	hostPort: int = Field(default=None, description=r""" Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. """)
	name: str = Field(default=None, description=r""" If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. """)
	protocol: str = Field(default=None, description=r""" Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". """)

class ContainerResizePolicy(BaseModel):
	resourceName: str = Field(default=None, description=r""" Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. """)
	restartPolicy: str = Field(default=None, description=r""" Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. """)

class ContainerState(BaseModel):
	running: ContainerStateRunning = Field(default=None, description=r""" Details about a running container """)
	terminated: ContainerStateTerminated = Field(default=None, description=r""" Details about a terminated container """)
	waiting: ContainerStateWaiting = Field(default=None, description=r""" Details about a waiting container """)

class ContainerStateRunning(BaseModel):
	startedAt: Time = Field(default=None, description=r""" Time at which the container was last (re-)started """)

class ContainerStateTerminated(BaseModel):
	containerID: str = Field(default=None, description=r""" Container's ID in the format '<type>://<container_id>' """)
	exitCode: int = Field(default=None, description=r""" Exit status from the last termination of the container """)
	finishedAt: Time = Field(default=None, description=r""" Time at which the container last terminated """)
	message: str = Field(default=None, description=r""" Message regarding the last termination of the container """)
	reason: str = Field(default=None, description=r""" (brief) reason from the last termination of the container """)
	signal: int = Field(default=None, description=r""" Signal from the last termination of the container """)
	startedAt: Time = Field(default=None, description=r""" Time at which previous execution of the container started """)

class ContainerStateWaiting(BaseModel):
	message: str = Field(default=None, description=r""" Message regarding why the container is not yet running. """)
	reason: str = Field(default=None, description=r""" (brief) reason the container is not yet running. """)

class DaemonEndpoint(BaseModel):
	Port: int = Field(default=None, description=r""" Port number of the given endpoint. """)

class DownwardAPIProjection(BaseModel):
	items: List[DownwardAPIVolumeFile] = Field(default=None, description=r""" Items is a list of DownwardAPIVolume file """)

class DownwardAPIVolumeFile(BaseModel):
	fieldRef: ObjectFieldSelector = Field(default=None, description=r""" Required: Selects a field of the pod: only annotations, labels, name and namespace are supported. """)
	mode: int = Field(default=None, description=r""" Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
	path: str = Field(default=None, description=r""" Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' """)
	resourceFieldRef: ResourceFieldSelector = Field(default=None, description=r""" Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. """)

class DownwardAPIVolumeSource(BaseModel):
	defaultMode: int = Field(default=None, description=r""" Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
	items: List[DownwardAPIVolumeFile] = Field(default=None, description=r""" Items is a list of downward API volume file """)

class EmptyDirVolumeSource(BaseModel):
	medium: str = Field(default=None, description=r""" medium represents what type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """)
	sizeLimit: Quantity = Field(default=None, description=r""" sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """)

class EndpointAddress(BaseModel):
	hostname: str = Field(default=None, description=r""" The Hostname of this endpoint """)
	ip: str = Field(default=None, description=r""" The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16). """)
	nodeName: str = Field(default=None, description=r""" Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. """)
	targetRef: ObjectReference = Field(default=None, description=r""" Reference to object providing the endpoint. """)

class EndpointPort(BaseModel):
	appProtocol: str = Field(default=None, description=r""" The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 over cleartext as described in https://www.rfc-editor.org/rfc/rfc7540   * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol. """)
	name: str = Field(default=None, description=r""" The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined. """)
	port: int = Field(default=None, description=r""" The port number of the endpoint. """)
	protocol: str = Field(default=None, description=r""" The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. """)

class EndpointSubset(BaseModel):
	addresses: List[EndpointAddress] = Field(default=None, description=r""" IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize. """)
	notReadyAddresses: List[EndpointAddress] = Field(default=None, description=r""" IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check. """)
	ports: List[EndpointPort] = Field(default=None, description=r""" Port numbers available on the related IP addresses. """)

class EnvFromSource(BaseModel):
	configMapRef: ConfigMapEnvSource = Field(default=None, description=r""" The ConfigMap to select from """)
	prefix: str = Field(default=None, description=r""" An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER. """)
	secretRef: SecretEnvSource = Field(default=None, description=r""" The Secret to select from """)

class EnvVar(BaseModel):
	name: str = Field(default=None, description=r""" Name of the environment variable. Must be a C_IDENTIFIER. """)
	value: str = Field(default=None, description=r""" Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". """)
	valueFrom: EnvVarSource = Field(default=None, description=r""" Source for the environment variable's value. Cannot be used if value is not empty. """)

class EnvVarSource(BaseModel):
	configMapKeyRef: ConfigMapKeySelector = Field(default=None, description=r""" Selects a key of a ConfigMap. """)
	fieldRef: ObjectFieldSelector = Field(default=None, description=r""" Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. """)
	resourceFieldRef: ResourceFieldSelector = Field(default=None, description=r""" Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. """)
	secretKeyRef: SecretKeySelector = Field(default=None, description=r""" Selects a key of a secret in the pod's namespace """)

class EphemeralContainer(BaseModel):
	args: List[str] = Field(default=None, description=r""" Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """)
	command: List[str] = Field(default=None, description=r""" Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """)
	env: List[EnvVar] = Field(default=None, description=r""" List of environment variables to set in the container. Cannot be updated. """)
	envFrom: List[EnvFromSource] = Field(default=None, description=r""" List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. """)
	image: str = Field(default=None, description=r""" Container image name. More info: https://kubernetes.io/docs/concepts/containers/images """)
	imagePullPolicy: str = Field(default=None, description=r""" Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images """)
	lifecycle: Lifecycle = Field(default=None, description=r""" Lifecycle is not allowed for ephemeral containers. """)
	livenessProbe: Probe = Field(default=None, description=r""" Probes are not allowed for ephemeral containers. """)
	name: str = Field(default=None, description=r""" Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers. """)
	ports: List[ContainerPort] = Field(default=None, description=r""" Ports are not allowed for ephemeral containers. """)
	readinessProbe: Probe = Field(default=None, description=r""" Probes are not allowed for ephemeral containers. """)
	resizePolicy: List[ContainerResizePolicy] = Field(default=None, description=r""" Resources resize policy for the container. """)
	resources: ResourceRequirements = Field(default=None, description=r""" Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod. """)
	restartPolicy: str = Field(default=None, description=r""" Restart policy for the container to manage the restart behavior of each container within a pod. This may only be set for init containers. You cannot set this field on ephemeral containers. """)
	securityContext: SecurityContext = Field(default=None, description=r""" Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. """)
	startupProbe: Probe = Field(default=None, description=r""" Probes are not allowed for ephemeral containers. """)
	stdin: bool = Field(default=None, description=r""" Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. """)
	stdinOnce: bool = Field(default=None, description=r""" Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false """)
	targetContainerName: str = Field(default=None, description=r""" If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.  The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined. """)
	terminationMessagePath: str = Field(default=None, description=r""" Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. """)
	terminationMessagePolicy: str = Field(default=None, description=r""" Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. """)
	tty: bool = Field(default=None, description=r""" Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. """)
	volumeDevices: List[VolumeDevice] = Field(default=None, description=r""" volumeDevices is the list of block devices to be used by the container. """)
	volumeMounts: List[VolumeMount] = Field(default=None, description=r""" Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated. """)
	workingDir: str = Field(default=None, description=r""" Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. """)

class EphemeralVolumeSource(BaseModel):
	volumeClaimTemplate: PersistentVolumeClaimTemplate = Field(default=None, description=r""" Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod.  The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).  An existing PVC with that name that is not owned by the pod will *not* be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.  This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.  Required, must not be nil. """)

class EventSource(BaseModel):
	component: str = Field(default=None, description=r""" Component from which the event is generated. """)
	host: str = Field(default=None, description=r""" Node name on which the event is generated. """)

class ExecAction(BaseModel):
	command: List[str] = Field(default=None, description=r""" Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. """)

class FCVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
	lun: int = Field(default=None, description=r""" lun is Optional: FC target lun number """)
	readOnly: bool = Field(default=None, description=r""" readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	targetWWNs: List[str] = Field(default=None, description=r""" targetWWNs is Optional: FC target worldwide names (WWNs) """)
	wwids: List[str] = Field(default=None, description=r""" wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. """)

class FlexPersistentVolumeSource(BaseModel):
	driver: str = Field(default=None, description=r""" driver is the name of the driver to use for this volume. """)
	fsType: str = Field(default=None, description=r""" fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. """)
	options: dict = Field(default=None, description=r""" options is Optional: this field holds extra command options if any. """)
	readOnly: bool = Field(default=None, description=r""" readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	secretRef: SecretReference = Field(default=None, description=r""" secretRef is Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. """)

class FlexVolumeSource(BaseModel):
	driver: str = Field(default=None, description=r""" driver is the name of the driver to use for this volume. """)
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. """)
	options: dict = Field(default=None, description=r""" options is Optional: this field holds extra command options if any. """)
	readOnly: bool = Field(default=None, description=r""" readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. """)

class FlockerVolumeSource(BaseModel):
	datasetName: str = Field(default=None, description=r""" datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated """)
	datasetUUID: str = Field(default=None, description=r""" datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset """)

class GCEPersistentDiskVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
	partition: int = Field(default=None, description=r""" partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
	pdName: str = Field(default=None, description=r""" pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """)

class GRPCAction(BaseModel):
	port: int = Field(default=None, description=r""" Port number of the gRPC service. Number must be in the range 1 to 65535. """)
	service: str = Field(default=None, description=r""" Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).  If this is not specified, the default behavior is defined by gRPC. """)

class GitRepoVolumeSource(BaseModel):
	directory: str = Field(default=None, description=r""" directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. """)
	repository: str = Field(default=None, description=r""" repository is the URL """)
	revision: str = Field(default=None, description=r""" revision is the commit hash for the specified revision. """)

class GlusterfsPersistentVolumeSource(BaseModel):
	endpoints: str = Field(default=None, description=r""" endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
	endpointsNamespace: str = Field(default=None, description=r""" endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
	path: str = Field(default=None, description=r""" path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)

class GlusterfsVolumeSource(BaseModel):
	endpoints: str = Field(default=None, description=r""" endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
	path: str = Field(default=None, description=r""" path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """)

class HTTPGetAction(BaseModel):
	host: str = Field(default=None, description=r""" Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. """)
	httpHeaders: List[HTTPHeader] = Field(default=None, description=r""" Custom headers to set in the request. HTTP allows repeated headers. """)
	path: str = Field(default=None, description=r""" Path to access on the HTTP server. """)
	port: Any = Field(default=None, description=r""" Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. """)
	scheme: str = Field(default=None, description=r""" Scheme to use for connecting to the host. Defaults to HTTP. """)

class HTTPHeader(BaseModel):
	name: str = Field(default=None, description=r""" The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. """)
	value: str = Field(default=None, description=r""" The header field value """)

class HostAlias(BaseModel):
	hostnames: List[str] = Field(default=None, description=r""" Hostnames for the above IP address. """)
	ip: str = Field(default=None, description=r""" IP address of the host file entry. """)

class HostIP(BaseModel):
	ip: str = Field(default=None, description=r""" IP is the IP address assigned to the host """)

class HostPathVolumeSource(BaseModel):
	path: str = Field(default=None, description=r""" path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)
	type: str = Field(default=None, description=r""" type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """)

class ISCSIPersistentVolumeSource(BaseModel):
	chapAuthDiscovery: bool = Field(default=None, description=r""" chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication """)
	chapAuthSession: bool = Field(default=None, description=r""" chapAuthSession defines whether support iSCSI Session CHAP authentication """)
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi """)
	initiatorName: str = Field(default=None, description=r""" initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection. """)
	iqn: str = Field(default=None, description=r""" iqn is Target iSCSI Qualified Name. """)
	iscsiInterface: str = Field(default=None, description=r""" iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). """)
	lun: int = Field(default=None, description=r""" lun is iSCSI Target Lun number. """)
	portals: List[str] = Field(default=None, description=r""" portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. """)
	secretRef: SecretReference = Field(default=None, description=r""" secretRef is the CHAP Secret for iSCSI target and initiator authentication """)
	targetPortal: str = Field(default=None, description=r""" targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)

class ISCSIVolumeSource(BaseModel):
	chapAuthDiscovery: bool = Field(default=None, description=r""" chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication """)
	chapAuthSession: bool = Field(default=None, description=r""" chapAuthSession defines whether support iSCSI Session CHAP authentication """)
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi """)
	initiatorName: str = Field(default=None, description=r""" initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection. """)
	iqn: str = Field(default=None, description=r""" iqn is the target iSCSI Qualified Name. """)
	iscsiInterface: str = Field(default=None, description=r""" iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). """)
	lun: int = Field(default=None, description=r""" lun represents iSCSI Target Lun number. """)
	portals: List[str] = Field(default=None, description=r""" portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. """)
	secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is the CHAP Secret for iSCSI target and initiator authentication """)
	targetPortal: str = Field(default=None, description=r""" targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """)

class KeyToPath(BaseModel):
	key: str = Field(default=None, description=r""" key is the key to project. """)
	mode: int = Field(default=None, description=r""" mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
	path: str = Field(default=None, description=r""" path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. """)

class Lifecycle(BaseModel):
	postStart: LifecycleHandler = Field(default=None, description=r""" PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks """)
	preStop: LifecycleHandler = Field(default=None, description=r""" PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod's termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks """)

class LifecycleHandler(BaseModel):
	exec: ExecAction = Field(default=None, description=r""" Exec specifies the action to take. """)
	httpGet: HTTPGetAction = Field(default=None, description=r""" HTTPGet specifies the http request to perform. """)
	tcpSocket: TCPSocketAction = Field(default=None, description=r""" Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified. """)

class LimitRangeItem(BaseModel):
	default: dict = Field(default=None, description=r""" Default resource requirement limit value by resource name if resource limit is omitted. """)
	defaultRequest: dict = Field(default=None, description=r""" DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. """)
	max: dict = Field(default=None, description=r""" Max usage constraints on this kind by resource name. """)
	maxLimitRequestRatio: dict = Field(default=None, description=r""" MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. """)
	min: dict = Field(default=None, description=r""" Min usage constraints on this kind by resource name. """)
	type: str = Field(default=None, description=r""" Type of resource that this limit applies to. """)

class LoadBalancerIngress(BaseModel):
	hostname: str = Field(default=None, description=r""" Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers) """)
	ip: str = Field(default=None, description=r""" IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers) """)
	ports: List[PortStatus] = Field(default=None, description=r""" Ports is a list of records of service ports If used, every port defined in the service should have an entry in it """)

class LoadBalancerStatus(BaseModel):
	ingress: List[LoadBalancerIngress] = Field(default=None, description=r""" Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. """)

class LocalObjectReference(BaseModel):
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)

class LocalVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified. """)
	path: str = Field(default=None, description=r""" path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, ...). """)

class NFSVolumeSource(BaseModel):
	path: str = Field(default=None, description=r""" path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)
	server: str = Field(default=None, description=r""" server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """)

class NamespaceCondition(BaseModel):
	lastTransitionTime: Time = Field(default=None, description=r"""  """)
	message: str = Field(default=None, description=r"""  """)
	reason: str = Field(default=None, description=r"""  """)
	status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
	type: str = Field(default=None, description=r""" Type of namespace controller condition. """)

class NodeAddress(BaseModel):
	address: str = Field(default=None, description=r""" The node address. """)
	type: str = Field(default=None, description=r""" Node address type, one of Hostname, ExternalIP or InternalIP. """)

class NodeAffinity(BaseModel):
	preferredDuringSchedulingIgnoredDuringExecution: List[PreferredSchedulingTerm] = Field(default=None, description=r""" The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred. """)
	requiredDuringSchedulingIgnoredDuringExecution: NodeSelector = Field(default=None, description=r""" If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node. """)

class NodeCondition(BaseModel):
	lastHeartbeatTime: Time = Field(default=None, description=r""" Last time we got an update on a given condition. """)
	lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transit from one status to another. """)
	message: str = Field(default=None, description=r""" Human readable message indicating details about last transition. """)
	reason: str = Field(default=None, description=r""" (brief) reason for the condition's last transition. """)
	status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
	type: str = Field(default=None, description=r""" Type of node condition. """)

class NodeConfigSource(BaseModel):
	configMap: ConfigMapNodeConfigSource = Field(default=None, description=r""" ConfigMap is a reference to a Node's ConfigMap """)

class NodeConfigStatus(BaseModel):
	active: NodeConfigSource = Field(default=None, description=r""" Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error. """)
	assigned: NodeConfigSource = Field(default=None, description=r""" Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned. """)
	error: str = Field(default=None, description=r""" Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions. """)
	lastKnownGood: NodeConfigSource = Field(default=None, description=r""" LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future. """)

class NodeDaemonEndpoints(BaseModel):
	kubeletEndpoint: DaemonEndpoint = Field(default=None, description=r""" Endpoint on which Kubelet is listening. """)

class NodeSelector(BaseModel):
	nodeSelectorTerms: List[NodeSelectorTerm] = Field(default=None, description=r""" Required. A list of node selector terms. The terms are ORed. """)

class NodeSelectorRequirement(BaseModel):
	key: str = Field(default=None, description=r""" The label key that the selector applies to. """)
	operator: str = Field(default=None, description=r""" Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt. """)
	values: List[str] = Field(default=None, description=r""" An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. """)

class NodeSelectorTerm(BaseModel):
	matchExpressions: List[NodeSelectorRequirement] = Field(default=None, description=r""" A list of node selector requirements by node's labels. """)
	matchFields: List[NodeSelectorRequirement] = Field(default=None, description=r""" A list of node selector requirements by node's fields. """)

class NodeSystemInfo(BaseModel):
	architecture: str = Field(default=None, description=r""" The Architecture reported by the node """)
	bootID: str = Field(default=None, description=r""" Boot ID reported by the node. """)
	containerRuntimeVersion: str = Field(default=None, description=r""" ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2). """)
	kernelVersion: str = Field(default=None, description=r""" Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64). """)
	kubeProxyVersion: str = Field(default=None, description=r""" KubeProxy Version reported by the node. """)
	kubeletVersion: str = Field(default=None, description=r""" Kubelet Version reported by the node. """)
	machineID: str = Field(default=None, description=r""" MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html """)
	operatingSystem: str = Field(default=None, description=r""" The Operating System reported by the node """)
	osImage: str = Field(default=None, description=r""" OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)). """)
	systemUUID: str = Field(default=None, description=r""" SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid """)

class ObjectFieldSelector(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" Version of the schema the FieldPath is written in terms of, defaults to "v1". """)
	fieldPath: str = Field(default=None, description=r""" Path of the field to select in the specified API version. """)

class ObjectReference(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" API version of the referent. """)
	fieldPath: str = Field(default=None, description=r""" If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. """)
	kind: str = Field(default="ObjectReference", description=r""" Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	namespace: str = Field(default=None, description=r""" Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ """)
	resourceVersion: str = Field(default=None, description=r""" Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency """)
	uid: str = Field(default=None, description=r""" UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids """)

class PersistentVolumeClaimCondition(BaseModel):
	lastProbeTime: Time = Field(default=None, description=r""" lastProbeTime is the time we probed the condition. """)
	lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the time the condition transitioned from one status to another. """)
	message: str = Field(default=None, description=r""" message is the human-readable message indicating details about last transition. """)
	reason: str = Field(default=None, description=r""" reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized. """)
	status: str = Field(default=None, description=r"""  """)
	type: str = Field(default=None, description=r"""  """)

class PersistentVolumeClaimTemplate(BaseModel):
	metadata: ObjectMeta = Field(default=None, description=r""" May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """)
	spec: PersistentVolumeClaimSpec = Field(default=None, description=r""" The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here. """)

class PersistentVolumeClaimVolumeSource(BaseModel):
	claimName: str = Field(default=None, description=r""" claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
	readOnly: bool = Field(default=None, description=r""" readOnly Will force the ReadOnly setting in VolumeMounts. Default false. """)

class PhotonPersistentDiskVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
	pdID: str = Field(default=None, description=r""" pdID is the ID that identifies Photon Controller persistent disk """)

class PodAffinity(BaseModel):
	preferredDuringSchedulingIgnoredDuringExecution: List[WeightedPodAffinityTerm] = Field(default=None, description=r""" The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. """)
	requiredDuringSchedulingIgnoredDuringExecution: List[PodAffinityTerm] = Field(default=None, description=r""" If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. """)

class PodAffinityTerm(BaseModel):
	labelSelector: LabelSelector = Field(default=None, description=r""" A label query over a set of resources, in this case pods. """)
	namespaceSelector: LabelSelector = Field(default=None, description=r""" A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces. """)
	namespaces: List[str] = Field(default=None, description=r""" namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace". """)
	topologyKey: str = Field(default=None, description=r""" This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. """)

class PodAntiAffinity(BaseModel):
	preferredDuringSchedulingIgnoredDuringExecution: List[WeightedPodAffinityTerm] = Field(default=None, description=r""" The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. """)
	requiredDuringSchedulingIgnoredDuringExecution: List[PodAffinityTerm] = Field(default=None, description=r""" If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. """)

class PodCondition(BaseModel):
	lastProbeTime: Time = Field(default=None, description=r""" Last time we probed the condition. """)
	lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transitioned from one status to another. """)
	message: str = Field(default=None, description=r""" Human-readable message indicating details about last transition. """)
	reason: str = Field(default=None, description=r""" Unique, one-word, CamelCase reason for the condition's last transition. """)
	status: str = Field(default=None, description=r""" Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """)
	type: str = Field(default=None, description=r""" Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """)

class PodDNSConfig(BaseModel):
	nameservers: List[str] = Field(default=None, description=r""" A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed. """)
	options: List[PodDNSConfigOption] = Field(default=None, description=r""" A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy. """)
	searches: List[str] = Field(default=None, description=r""" A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed. """)

class PodDNSConfigOption(BaseModel):
	name: str = Field(default=None, description=r""" Required. """)
	value: str = Field(default=None, description=r"""  """)

class PodIP(BaseModel):
	ip: str = Field(default=None, description=r""" IP is the IP address assigned to the pod """)

class PodOS(BaseModel):
	name: str = Field(default=None, description=r""" Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration Clients should expect to handle additional values and treat unrecognized values in this field as os: null """)

class PodReadinessGate(BaseModel):
	conditionType: str = Field(default=None, description=r""" ConditionType refers to a condition in the pod's condition list with matching type. """)

class PodResourceClaim(BaseModel):
	name: str = Field(default=None, description=r""" Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL. """)
	source: ClaimSource = Field(default=None, description=r""" Source describes where to find the ResourceClaim. """)

class PodSchedulingGate(BaseModel):
	name: str = Field(default=None, description=r""" Name of the scheduling gate. Each scheduling gate must have a unique name field. """)

class PodSecurityContext(BaseModel):
	fsGroup: int = Field(default=None, description=r""" A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows. """)
	fsGroupChangePolicy: str = Field(default=None, description=r""" fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows. """)
	runAsGroup: int = Field(default=None, description=r""" The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """)
	runAsNonRoot: bool = Field(default=None, description=r""" Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """)
	runAsUser: int = Field(default=None, description=r""" The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """)
	seLinuxOptions: SELinuxOptions = Field(default=None, description=r""" The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """)
	seccompProfile: SeccompProfile = Field(default=None, description=r""" The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows. """)
	supplementalGroups: List[int] = Field(default=None, description=r""" A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows. """)
	sysctls: List[Sysctl] = Field(default=None, description=r""" Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows. """)
	windowsOptions: WindowsSecurityContextOptions = Field(default=None, description=r""" The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. """)

class PortStatus(BaseModel):
	error: str = Field(default=None, description=r""" Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use   CamelCase names - cloud provider specific error values must have names that comply with the   format foo.example.com/CamelCase. """)
	port: int = Field(default=None, description=r""" Port is the port number of the service port of which status is recorded here """)
	protocol: str = Field(default=None, description=r""" Protocol is the protocol of the service port of which status is recorded here The supported values are: "TCP", "UDP", "SCTP" """)

class PortworxVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. """)
	readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	volumeID: str = Field(default=None, description=r""" volumeID uniquely identifies a Portworx volume """)

class PreferredSchedulingTerm(BaseModel):
	preference: NodeSelectorTerm = Field(default=None, description=r""" A node selector term, associated with the corresponding weight. """)
	weight: int = Field(default=None, description=r""" Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. """)

class Probe(BaseModel):
	exec: ExecAction = Field(default=None, description=r""" Exec specifies the action to take. """)
	failureThreshold: int = Field(default=None, description=r""" Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. """)
	grpc: GRPCAction = Field(default=None, description=r""" GRPC specifies an action involving a GRPC port. """)
	httpGet: HTTPGetAction = Field(default=None, description=r""" HTTPGet specifies the http request to perform. """)
	initialDelaySeconds: int = Field(default=None, description=r""" Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)
	periodSeconds: int = Field(default=None, description=r""" How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. """)
	successThreshold: int = Field(default=None, description=r""" Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. """)
	tcpSocket: TCPSocketAction = Field(default=None, description=r""" TCPSocket specifies an action involving a TCP port. """)
	terminationGracePeriodSeconds: int = Field(default=None, description=r""" Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. """)
	timeoutSeconds: int = Field(default=None, description=r""" Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)

class ProjectedVolumeSource(BaseModel):
	defaultMode: int = Field(default=None, description=r""" defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
	sources: List[VolumeProjection] = Field(default=None, description=r""" sources is the list of volume projections """)

class Quantity(BaseModel):
    pass


class QuobyteVolumeSource(BaseModel):
	group: str = Field(default=None, description=r""" group to map volume access to Default is no group """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. """)
	registry: str = Field(default=None, description=r""" registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes """)
	tenant: str = Field(default=None, description=r""" tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin """)
	user: str = Field(default=None, description=r""" user to map volume access to Defaults to serivceaccount user """)
	volume: str = Field(default=None, description=r""" volume is a string that references an already created Quobyte volume by name. """)

class RBDPersistentVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd """)
	image: str = Field(default=None, description=r""" image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	keyring: str = Field(default=None, description=r""" keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	monitors: List[str] = Field(default=None, description=r""" monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	pool: str = Field(default=None, description=r""" pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	secretRef: SecretReference = Field(default=None, description=r""" secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	user: str = Field(default=None, description=r""" user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)

class RBDVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd """)
	image: str = Field(default=None, description=r""" image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	keyring: str = Field(default=None, description=r""" keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	monitors: List[str] = Field(default=None, description=r""" monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	pool: str = Field(default=None, description=r""" pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	readOnly: bool = Field(default=None, description=r""" readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)
	user: str = Field(default=None, description=r""" user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """)

class ReplicationControllerCondition(BaseModel):
	lastTransitionTime: Time = Field(default=None, description=r""" The last time the condition transitioned from one status to another. """)
	message: str = Field(default=None, description=r""" A human readable message indicating details about the transition. """)
	reason: str = Field(default=None, description=r""" The reason for the condition's last transition. """)
	status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
	type: str = Field(default=None, description=r""" Type of replication controller condition. """)

class ResourceClaim(BaseModel):
	name: str = Field(default=None, description=r""" Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. """)

class ResourceFieldSelector(BaseModel):
	containerName: str = Field(default=None, description=r""" Container name: required for volumes, optional for env vars """)
	divisor: Quantity = Field(default=None, description=r""" Specifies the output format of the exposed resources, defaults to "1" """)
	resource: str = Field(default=None, description=r""" Required: resource to select """)

class ResourceRequirements(BaseModel):
	claims: List[ResourceClaim] = Field(default=None, description=r""" Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. """)
	limits: dict = Field(default=None, description=r""" Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """)
	requests: dict = Field(default=None, description=r""" Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """)

class SELinuxOptions(BaseModel):
	level: str = Field(default=None, description=r""" Level is SELinux level label that applies to the container. """)
	role: str = Field(default=None, description=r""" Role is a SELinux role label that applies to the container. """)
	type: str = Field(default=None, description=r""" Type is a SELinux type label that applies to the container. """)
	user: str = Field(default=None, description=r""" User is a SELinux user label that applies to the container. """)

class ScaleIOPersistentVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs" """)
	gateway: str = Field(default=None, description=r""" gateway is the host address of the ScaleIO API Gateway. """)
	protectionDomain: str = Field(default=None, description=r""" protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. """)
	readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	secretRef: SecretReference = Field(default=None, description=r""" secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. """)
	sslEnabled: bool = Field(default=None, description=r""" sslEnabled is the flag to enable/disable SSL communication with Gateway, default false """)
	storageMode: str = Field(default=None, description=r""" storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. """)
	storagePool: str = Field(default=None, description=r""" storagePool is the ScaleIO Storage Pool associated with the protection domain. """)
	system: str = Field(default=None, description=r""" system is the name of the storage system as configured in ScaleIO. """)
	volumeName: str = Field(default=None, description=r""" volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. """)

class ScaleIOVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs". """)
	gateway: str = Field(default=None, description=r""" gateway is the host address of the ScaleIO API Gateway. """)
	protectionDomain: str = Field(default=None, description=r""" protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. """)
	readOnly: bool = Field(default=None, description=r""" readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. """)
	sslEnabled: bool = Field(default=None, description=r""" sslEnabled Flag enable/disable SSL communication with Gateway, default false """)
	storageMode: str = Field(default=None, description=r""" storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. """)
	storagePool: str = Field(default=None, description=r""" storagePool is the ScaleIO Storage Pool associated with the protection domain. """)
	system: str = Field(default=None, description=r""" system is the name of the storage system as configured in ScaleIO. """)
	volumeName: str = Field(default=None, description=r""" volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. """)

class ScopeSelector(BaseModel):
	matchExpressions: List[ScopedResourceSelectorRequirement] = Field(default=None, description=r""" A list of scope selector requirements by scope of the resources. """)

class ScopedResourceSelectorRequirement(BaseModel):
	operator: str = Field(default=None, description=r""" Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. """)
	scopeName: str = Field(default=None, description=r""" The name of the scope that the selector applies to. """)
	values: List[str] = Field(default=None, description=r""" An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. """)

class SeccompProfile(BaseModel):
	localhostProfile: str = Field(default=None, description=r""" localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type. """)
	type: str = Field(default=None, description=r""" type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied. """)

class SecretEnvSource(BaseModel):
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	optional: bool = Field(default=None, description=r""" Specify whether the Secret must be defined """)

class SecretKeySelector(BaseModel):
	key: str = Field(default=None, description=r""" The key of the secret to select from.  Must be a valid secret key. """)
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	optional: bool = Field(default=None, description=r""" Specify whether the Secret or its key must be defined """)

class SecretProjection(BaseModel):
	items: List[KeyToPath] = Field(default=None, description=r""" items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
	name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
	optional: bool = Field(default=None, description=r""" optional field specify whether the Secret or its key must be defined """)

class SecretReference(BaseModel):
	name: str = Field(default=None, description=r""" name is unique within a namespace to reference a secret resource. """)
	namespace: str = Field(default=None, description=r""" namespace defines the space within which the secret name must be unique. """)

class SecretVolumeSource(BaseModel):
	defaultMode: int = Field(default=None, description=r""" defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """)
	items: List[KeyToPath] = Field(default=None, description=r""" items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
	optional: bool = Field(default=None, description=r""" optional field specify whether the Secret or its keys must be defined """)
	secretName: str = Field(default=None, description=r""" secretName is the name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret """)

class SecurityContext(BaseModel):
	allowPrivilegeEscalation: bool = Field(default=None, description=r""" AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows. """)
	capabilities: Capabilities = Field(default=None, description=r""" The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows. """)
	privileged: bool = Field(default=None, description=r""" Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. """)
	procMount: str = Field(default=None, description=r""" procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows. """)
	readOnlyRootFilesystem: bool = Field(default=None, description=r""" Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. """)
	runAsGroup: int = Field(default=None, description=r""" The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """)
	runAsNonRoot: bool = Field(default=None, description=r""" Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """)
	runAsUser: int = Field(default=None, description=r""" The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """)
	seLinuxOptions: SELinuxOptions = Field(default=None, description=r""" The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """)
	seccompProfile: SeccompProfile = Field(default=None, description=r""" The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows. """)
	windowsOptions: WindowsSecurityContextOptions = Field(default=None, description=r""" The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. """)

class ServiceAccountTokenProjection(BaseModel):
	audience: str = Field(default=None, description=r""" audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver. """)
	expirationSeconds: int = Field(default=None, description=r""" expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes. """)
	path: str = Field(default=None, description=r""" path is the path relative to the mount point of the file to project the token into. """)

class ServicePort(BaseModel):
	appProtocol: str = Field(default=None, description=r""" The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 over cleartext as described in https://www.rfc-editor.org/rfc/rfc7540   * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol. """)
	name: str = Field(default=None, description=r""" The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service. """)
	nodePort: int = Field(default=None, description=r""" The port on each node on which this service is exposed when type is NodePort or LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if this Service requires one.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type from NodePort to ClusterIP). More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport """)
	port: int = Field(default=None, description=r""" The port that will be exposed by this service. """)
	protocol: str = Field(default=None, description=r""" The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. """)
	targetPort: Any = Field(default=None, description=r""" Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service """)

class SessionAffinityConfig(BaseModel):
	clientIP: ClientIPConfig = Field(default=None, description=r""" clientIP contains the configurations of Client IP based session affinity. """)

class StorageOSPersistentVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
	readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	secretRef: ObjectReference = Field(default=None, description=r""" secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted. """)
	volumeName: str = Field(default=None, description=r""" volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace. """)
	volumeNamespace: str = Field(default=None, description=r""" volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. """)

class StorageOSVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
	readOnly: bool = Field(default=None, description=r""" readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """)
	secretRef: LocalObjectReference = Field(default=None, description=r""" secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted. """)
	volumeName: str = Field(default=None, description=r""" volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace. """)
	volumeNamespace: str = Field(default=None, description=r""" volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. """)

class Sysctl(BaseModel):
	name: str = Field(default=None, description=r""" Name of a property to set """)
	value: str = Field(default=None, description=r""" Value of a property to set """)

class TCPSocketAction(BaseModel):
	host: str = Field(default=None, description=r""" Optional: Host name to connect to, defaults to the pod IP. """)
	port: Any = Field(default=None, description=r""" Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. """)

class Taint(BaseModel):
	effect: str = Field(default=None, description=r""" Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. """)
	key: str = Field(default=None, description=r""" Required. The taint key to be applied to a node. """)
	timeAdded: Time = Field(default=None, description=r""" TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. """)
	value: str = Field(default=None, description=r""" The taint value corresponding to the taint key. """)

class Toleration(BaseModel):
	effect: str = Field(default=None, description=r""" Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. """)
	key: str = Field(default=None, description=r""" Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. """)
	operator: str = Field(default=None, description=r""" Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. """)
	tolerationSeconds: int = Field(default=None, description=r""" TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. """)
	value: str = Field(default=None, description=r""" Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. """)

class TopologySelectorLabelRequirement(BaseModel):
	key: str = Field(default=None, description=r""" The label key that the selector applies to. """)
	values: List[str] = Field(default=None, description=r""" An array of string values. One value must match the label to be selected. Each entry in Values is ORed. """)

class TopologySelectorTerm(BaseModel):
	matchLabelExpressions: List[TopologySelectorLabelRequirement] = Field(default=None, description=r""" A list of topology selector requirements by labels. """)

class TopologySpreadConstraint(BaseModel):
	labelSelector: LabelSelector = Field(default=None, description=r""" LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain. """)
	matchLabelKeys: List[str] = Field(default=None, description=r""" MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default). """)
	maxSkew: int = Field(default=None, description=r""" MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed. """)
	minDomains: int = Field(default=None, description=r""" MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.  For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.  This is a beta field and requires the MinDomainsInPodTopologySpread feature gate to be enabled (enabled by default). """)
	nodeAffinityPolicy: str = Field(default=None, description=r""" NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.  If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag. """)
	nodeTaintsPolicy: str = Field(default=None, description=r""" NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.  If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag. """)
	topologyKey: str = Field(default=None, description=r""" TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It's a required field. """)
	whenUnsatisfiable: str = Field(default=None, description=r""" WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,   but giving higher precedence to topologies that would help reduce the   skew. A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field. """)

class TypedLocalObjectReference(BaseModel):
	apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
	kind: str = Field(default="TypedLocalObjectReference", description=r""" Kind is the type of resource being referenced """)
	name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)

class TypedObjectReference(BaseModel):
	apiGroup: str = Field(default=None, description=r""" APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
	kind: str = Field(default="TypedObjectReference", description=r""" Kind is the type of resource being referenced """)
	name: str = Field(default=None, description=r""" Name is the name of resource being referenced """)
	namespace: str = Field(default=None, description=r""" Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. """)

class VolumeDevice(BaseModel):
	devicePath: str = Field(default=None, description=r""" devicePath is the path inside of the container that the device will be mapped to. """)
	name: str = Field(default=None, description=r""" name must match the name of a persistentVolumeClaim in the pod """)

class VolumeMount(BaseModel):
	mountPath: str = Field(default=None, description=r""" Path within the container at which the volume should be mounted.  Must not contain ':'. """)
	mountPropagation: str = Field(default=None, description=r""" mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. """)
	name: str = Field(default=None, description=r""" This must match the Name of a Volume. """)
	readOnly: bool = Field(default=None, description=r""" Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. """)
	subPath: str = Field(default=None, description=r""" Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root). """)
	subPathExpr: str = Field(default=None, description=r""" Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive. """)

class VolumeNodeAffinity(BaseModel):
	required: NodeSelector = Field(default=None, description=r""" required specifies hard node constraints that must be met. """)

class VolumeProjection(BaseModel):
	configMap: ConfigMapProjection = Field(default=None, description=r""" configMap information about the configMap data to project """)
	downwardAPI: DownwardAPIProjection = Field(default=None, description=r""" downwardAPI information about the downwardAPI data to project """)
	secret: SecretProjection = Field(default=None, description=r""" secret information about the secret data to project """)
	serviceAccountToken: ServiceAccountTokenProjection = Field(default=None, description=r""" serviceAccountToken is information about the serviceAccountToken data to project """)

class VsphereVirtualDiskVolumeSource(BaseModel):
	fsType: str = Field(default=None, description=r""" fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """)
	storagePolicyID: str = Field(default=None, description=r""" storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. """)
	storagePolicyName: str = Field(default=None, description=r""" storagePolicyName is the storage Policy Based Management (SPBM) profile name. """)
	volumePath: str = Field(default=None, description=r""" volumePath is the path that identifies vSphere volume vmdk """)

class WeightedPodAffinityTerm(BaseModel):
	podAffinityTerm: PodAffinityTerm = Field(default=None, description=r""" Required. A pod affinity term, associated with the corresponding weight. """)
	weight: int = Field(default=None, description=r""" weight associated with matching the corresponding podAffinityTerm, in the range 1-100. """)

class WindowsSecurityContextOptions(BaseModel):
	gmsaCredentialSpec: str = Field(default=None, description=r""" GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. """)
	gmsaCredentialSpecName: str = Field(default=None, description=r""" GMSACredentialSpecName is the name of the GMSA credential spec to use. """)
	hostProcess: bool = Field(default=None, description=r""" HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. """)
	runAsUserName: str = Field(default=None, description=r""" The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """)
