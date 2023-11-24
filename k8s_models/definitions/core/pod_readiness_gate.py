from pydantic import BaseModel, Field


class PodReadinessGate(BaseModel):
    conditionType: str = Field(default=None, description=r""" ConditionType refers to a condition in the pod's condition list with matching type. """)
