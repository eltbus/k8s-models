from pydantic import Field

from k8s_models.models import KubeModel
from k8s_models.definitions.meta.object_meta import ObjectMeta
from k8s_models.metadata.admissionregistration.validating_admission_policy_spec import ValidatingAdmissionPolicySpec
from k8s_models.metadata.admissionregistration.validating_admission_policy_status import ValidatingAdmissionPolicyStatus


class ValidatingAdmissionPolicy(KubeModel):
    apiVersion: str = Field(default="v1beta1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
    kind: str = Field(default="ValidatingAdmissionPolicy", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """)
    spec: ValidatingAdmissionPolicySpec = Field(default=None, description=r""" Specification of the desired behavior of the ValidatingAdmissionPolicy. """)
    status: ValidatingAdmissionPolicyStatus = Field(default=None, description=r""" The status of the ValidatingAdmissionPolicy, including warnings that are useful to determine if the policy behaves in the expected way. Populated by the system. Read-only. """)
