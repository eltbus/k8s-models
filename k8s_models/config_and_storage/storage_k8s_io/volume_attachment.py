from pydantic import Field

from k8s_models.models import KubeModel


class VolumeAttachment(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="VolumeAttachment", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: VolumeAttachmentSpec = Field(default=None, description=r""" spec represents specification of the desired attach/detach volume behavior. Populated by the Kubernetes system. """)
    status: VolumeAttachmentStatus = Field(default=None, description=r""" status represents status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher. """)
