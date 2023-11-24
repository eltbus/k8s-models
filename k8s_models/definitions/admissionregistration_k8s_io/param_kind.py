from pydantic import Field

from k8s_models.models import KubeModel


class ParamKind(KubeModel):
    apiVersion: str = Field(default="v1beta1", description=r""" APIVersion is the API group version the resources belong to. In format of "group/version". Required. """)
    kind: str = Field(default="ParamKind", description=r""" Kind is the API kind the resources belong to. Required. """)
