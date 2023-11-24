from pydantic import BaseModel, Field


class ValidatingAdmissionPolicyStatus(BaseModel):
    conditions: List[Condition] = Field(default=None, description=r""" The conditions represent the latest available observations of a policy's current state. """)
    observedGeneration: int = Field(default=None, description=r""" The generation observed by the controller. """)
    typeChecking: TypeChecking = Field(default=None, description=r""" The results of type checking for each expression. Presence of this field indicates the completion of the type checking. """)
