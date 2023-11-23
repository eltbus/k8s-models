from __future__ import annotations

from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.cluster.certificates import CertificateSigningRequestSpec, CertificateSigningRequestStatus

class CertificateSigningRequest(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="CertificateSigningRequest", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None)
    spec: CertificateSigningRequestSpec = Field(default=None, description=r""" spec contains the certificate request, and is immutable after creation. Only the request, signerName, expirationSeconds, and usages fields can be set on creation. Other fields are derived by Kubernetes and cannot be modified by users. """)
    status: CertificateSigningRequestStatus = Field(default=None, description=r""" status contains information about whether the request is approved or denied, and the certificate issued by the signer, or the failure condition indicating signer failure. """)
