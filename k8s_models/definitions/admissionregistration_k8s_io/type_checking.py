from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.admissionregistration_k8s_io.expression_warning import ExpressionWarning


class TypeChecking(BaseModel):
    expressionWarnings: List[ExpressionWarning] = Field(default=None, description=r""" The type checking warnings for each expression. """)
