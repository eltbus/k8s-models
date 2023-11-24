from pydantic import BaseModel, Field


class Variable(BaseModel):
    expression: str = Field(default=None, description=r""" Expression is the expression that will be evaluated as the value of the variable. The CEL expression has access to the same identifiers as the CEL expressions in Validation. """)
    name: str = Field(default=None, description=r""" Name is the name of the variable. The name must be a valid CEL identifier and unique among all variables. The variable can be accessed in other expressions through `variables` For example, if name is "foo", the variable will be available as `variables.foo` """)
