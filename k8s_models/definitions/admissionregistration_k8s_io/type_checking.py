from pydantic import BaseModel, Field


class TypeChecking(BaseModel):
    expressionWarnings: List[ExpressionWarning] = Field(default=None, description=r""" The type checking warnings for each expression. """)
