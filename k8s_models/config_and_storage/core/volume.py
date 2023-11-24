from pydantic import BaseModel, Field

from k8s_models.definitions.core.aws_elastic_block_store_volume_source import AWSElasticBlockStoreVolumeSource
from k8s_models.definitions.core.azure_disk_volume_source import AzureDiskVolumeSource
from k8s_models.definitions.core.azure_file_volume_source import AzureFileVolumeSource
from k8s_models.definitions.core.ceph_fs_volume_source import CephFSVolumeSource
from k8s_models.definitions.core.cinder_volume_source import CinderVolumeSource
from k8s_models.definitions.core.config_map_volume_source import ConfigMapVolumeSource
from k8s_models.definitions.core.csi_volume_source import CSIVolumeSource
from k8s_models.definitions.core.downward_api_volume_source import DownwardAPIVolumeSource
from k8s_models.definitions.core.empty_dir_volume_source import EmptyDirVolumeSource
from k8s_models.definitions.core.ephemeral_volume_source import EphemeralVolumeSource
from k8s_models.definitions.core.fc_volume_source import FCVolumeSource
from k8s_models.definitions.core.flex_volume_source import FlexVolumeSource
from k8s_models.definitions.core.flocker_volume_source import FlockerVolumeSource
from k8s_models.definitions.core.gce_persistent_disk_volume_source import GCEPersistentDiskVolumeSource
from k8s_models.definitions.core.git_repo_volume_source import GitRepoVolumeSource
from k8s_models.definitions.core.glusterfs_volume_source import GlusterfsVolumeSource
from k8s_models.definitions.core.host_path_volume_source import HostPathVolumeSource
from k8s_models.definitions.core.iscsi_volume_source import ISCSIVolumeSource
from k8s_models.definitions.core.nfs_volume_source import NFSVolumeSource
from k8s_models.definitions.core.persistent_volume_claim_volume_source import PersistentVolumeClaimVolumeSource
from k8s_models.definitions.core.photon_persistent_disk_volume_source import PhotonPersistentDiskVolumeSource
from k8s_models.definitions.core.portworx_volume_source import PortworxVolumeSource
from k8s_models.definitions.core.projected_volume_source import ProjectedVolumeSource
from k8s_models.definitions.core.quobyte_volume_source import QuobyteVolumeSource
from k8s_models.definitions.core.rbd_volume_source import RBDVolumeSource
from k8s_models.definitions.core.scale_io_volume_source import ScaleIOVolumeSource
from k8s_models.definitions.core.secret_volume_source import SecretVolumeSource
from k8s_models.definitions.core.storage_os_volume_source import StorageOSVolumeSource
from k8s_models.definitions.core.vsphere_virtual_disk_volume_source import VsphereVirtualDiskVolumeSource


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
