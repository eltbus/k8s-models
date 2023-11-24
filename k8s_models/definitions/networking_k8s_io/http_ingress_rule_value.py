from pydantic import BaseModel, Field


class HTTPIngressRuleValue(BaseModel):
    paths: List[HTTPIngressPath] = Field(default=None, description=r""" paths is a collection of paths that map requests to backends. """)
