from pydantic import BaseModel, Field


class WeightedPodAffinityTerm(BaseModel):
    podAffinityTerm: PodAffinityTerm = Field(default=None, description=r""" Required. A pod affinity term, associated with the corresponding weight. """)
    weight: int = Field(default=None, description=r""" weight associated with matching the corresponding podAffinityTerm, in the range 1-100. """)
