from pydantic import BaseModel, Field


class ResourceQuotaStatus(BaseModel):
    hard: dict = Field(default=None, description=r""" Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """)
    used: dict = Field(default=None, description=r""" Used is the current observed total usage of the resource in the namespace. """)
