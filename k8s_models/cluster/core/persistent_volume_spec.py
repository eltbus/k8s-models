from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.core.aws_elastic_block_store_volume_source import AWSElasticBlockStoreVolumeSource
from k8s_models.definitions.core.azure_disk_volume_source import AzureDiskVolumeSource
from k8s_models.definitions.core.azure_file_persistent_volume_source import AzureFilePersistentVolumeSource
from k8s_models.definitions.core.ceph_fs_persistent_volume_source import CephFSPersistentVolumeSource
from k8s_models.definitions.core.cinder_persistent_volume_source import CinderPersistentVolumeSource
from k8s_models.definitions.core.object_reference import ObjectReference
from k8s_models.definitions.core.csi_persistent_volume_source import CSIPersistentVolumeSource
from k8s_models.definitions.core.fc_volume_source import FCVolumeSource
from k8s_models.definitions.core.flex_persistent_volume_source import FlexPersistentVolumeSource
from k8s_models.definitions.core.flocker_volume_source import FlockerVolumeSource
from k8s_models.definitions.core.gce_persistent_disk_volume_source import GCEPersistentDiskVolumeSource
from k8s_models.definitions.core.glusterfs_persistent_volume_source import GlusterfsPersistentVolumeSource
from k8s_models.definitions.core.host_path_volume_source import HostPathVolumeSource
from k8s_models.definitions.core.iscsi_persistent_volume_source import ISCSIPersistentVolumeSource
from k8s_models.definitions.core.local_volume_source import LocalVolumeSource
from k8s_models.definitions.core.nfs_volume_source import NFSVolumeSource
from k8s_models.definitions.core.volume_node_affinity import VolumeNodeAffinity
from k8s_models.definitions.core.photon_persistent_disk_volume_source import PhotonPersistentDiskVolumeSource
from k8s_models.definitions.core.portworx_volume_source import PortworxVolumeSource
from k8s_models.definitions.core.quobyte_volume_source import  QuobyteVolumeSource
from k8s_models.definitions.core.rbd_persistent_volume_source import RBDPersistentVolumeSource
from k8s_models.definitions.core.scale_io_persistent_volume_source import ScaleIOPersistentVolumeSource
from k8s_models.definitions.core.storage_os_persistent_volume_source import StorageOSPersistentVolumeSource
from k8s_models.definitions.core.vsphere_virtual_disk_volume_source import VsphereVirtualDiskVolumeSource


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
