from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.apiregistration_k8s_io.api_service_condition import APIServiceCondition


class APIServiceStatus(BaseModel):
    conditions: List[APIServiceCondition] = Field(default=None, description=r""" Current service state of apiService. """)
