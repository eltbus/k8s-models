from pydantic import BaseModel, Field


class Affinity(BaseModel):
    nodeAffinity: NodeAffinity = Field(default=None, description=r""" Describes node affinity scheduling rules for the pod. """)
    podAffinity: PodAffinity = Field(default=None, description=r""" Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)). """)
    podAntiAffinity: PodAntiAffinity = Field(default=None, description=r""" Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)). """)
