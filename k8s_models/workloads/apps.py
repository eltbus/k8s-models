from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.apps import (
    DaemonSetUpdateStrategy,
    StatefulSetOrdinals,
    StatefulSetPersistentVolumeClaimRetentionPolicy,
    StatefulSetUpdateStrategy,
)
from k8s_models.definitions.meta import ObjectMeta, LabelSelector
from k8s_models.metadata.core import PodTemplateSpec
from k8s_models.definitions.unknown import (
    DaemonSetStatus,
    DeploymentStatus,
    ReplicaSetStatus,
    StatefulSetStatus,
    DeploymentStrategy,
)
from k8s_models.config_and_storage.core import PersistentVolumeClaim


class DaemonSet(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="DaemonSet",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: DaemonSetSpec = Field(
        default=None,
        description=r""" The desired behavior of this daemon set. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """,
    )
    status: DaemonSetStatus = Field(
        default=None,
        description=r""" The current status of this daemon set. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """,
    )


class DaemonSetSpec(BaseModel):
    minReadySeconds: int = Field(
        default=None,
        description=r""" The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready). """,
    )
    revisionHistoryLimit: int = Field(
        default=None,
        description=r""" The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. """,
    )
    selector: LabelSelector = Field(
        default=None,
        description=r""" A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """,
    )
    template: PodTemplateSpec = Field(
        default=None,
        description=r""" An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """,
    )
    updateStrategy: DaemonSetUpdateStrategy = Field(
        default=None,
        description=r""" An update strategy to replace existing DaemonSet pods with new pods. """,
    )


class Deployment(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="Deployment",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: DeploymentSpec = Field(
        default=None,
        description=r""" Specification of the desired behavior of the Deployment. """,
    )
    status: DeploymentStatus = Field(
        default=None,
        description=r""" Most recently observed status of the Deployment. """,
    )


class DeploymentSpec(BaseModel):
    minReadySeconds: int = Field(
        default=None,
        description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """,
    )
    paused: bool = Field(
        default=None, description=r""" Indicates that the deployment is paused. """
    )
    progressDeadlineSeconds: int = Field(
        default=None,
        description=r""" The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. """,
    )
    replicas: int = Field(
        default=None,
        description=r""" Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. """,
    )
    revisionHistoryLimit: int = Field(
        default=None,
        description=r""" The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. """,
    )
    selector: LabelSelector = Field(
        default=None,
        description=r""" Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels. """,
    )
    strategy: DeploymentStrategy = Field(
        default=None,
        description=r""" The deployment strategy to use to replace existing pods with new ones. """,
    )
    template: PodTemplateSpec = Field(
        default=None,
        description=r""" Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always". """,
    )


class ReplicaSet(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="ReplicaSet",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: ReplicaSetSpec = Field(
        default=None,
        description=r""" Spec defines the specification of the desired behavior of the ReplicaSet. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """,
    )
    status: ReplicaSetStatus = Field(
        default=None,
        description=r""" Status is the most recently observed status of the ReplicaSet. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """,
    )


class ReplicaSetSpec(BaseModel):
    minReadySeconds: int = Field(
        default=None,
        description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """,
    )
    replicas: int = Field(
        default=None,
        description=r""" Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller """,
    )
    selector: LabelSelector = Field(
        default=None,
        description=r""" Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """,
    )
    template: PodTemplateSpec = Field(
        default=None,
        description=r""" Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """,
    )


class StatefulSet(BaseModel):
    apiVersion: str = Field(
        default="v1",
        description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """,
    )
    kind: str = Field(
        default="StatefulSet",
        description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """,
    )
    metadata: ObjectMeta = Field(
        default=None,
        description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """,
    )
    spec: StatefulSetSpec = Field(
        default=None,
        description=r""" Spec defines the desired identities of pods in this set. """,
    )
    status: StatefulSetStatus = Field(
        default=None,
        description=r""" Status is the current status of Pods in this StatefulSet. This data may be out of date by some window of time. """,
    )


class StatefulSetSpec(BaseModel):
    minReadySeconds: int = Field(
        default=None,
        description=r""" Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """,
    )
    ordinals: StatefulSetOrdinals = Field(
        default=None,
        description=r""" ordinals controls the numbering of replica indices in a StatefulSet. The default ordinals behavior assigns a "0" index to the first replica and increments the index by one for each additional replica requested. Using the ordinals field requires the StatefulSetStartOrdinal feature gate to be enabled, which is beta. """,
    )
    persistentVolumeClaimRetentionPolicy: StatefulSetPersistentVolumeClaimRetentionPolicy = Field(
        default=None,
        description=r""" persistentVolumeClaimRetentionPolicy describes the lifecycle of persistent volume claims created from volumeClaimTemplates. By default, all persistent volume claims are created as needed and retained until manually deleted. This policy allows the lifecycle to be altered, for example by deleting persistent volume claims when their stateful set is deleted, or when their pod is scaled down. This requires the StatefulSetAutoDeletePVC feature gate to be enabled, which is alpha.  +optional """,
    )
    podManagementPolicy: str = Field(
        default=None,
        description=r""" podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once. """,
    )
    replicas: int = Field(
        default=None,
        description=r""" replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1. """,
    )
    revisionHistoryLimit: int = Field(
        default=None,
        description=r""" revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10. """,
    )
    selector: LabelSelector = Field(
        default=None,
        description=r""" selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """,
    )
    serviceName: str = Field(
        default=None,
        description=r""" serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller. """,
    )
    template: PodTemplateSpec = Field(
        default=None,
        description=r""" template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet. Each pod will be named with the format <statefulsetname>-<podindex>. For example, a pod in a StatefulSet named "web" with index number "3" would be named "web-3". The only allowed template.spec.restartPolicy value is "Always". """,
    )
    updateStrategy: StatefulSetUpdateStrategy = Field(
        default=None,
        description=r""" updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template. """,
    )
    volumeClaimTemplates: List[PersistentVolumeClaim] = Field(
        default=None,
        description=r""" volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name. """,
    )
