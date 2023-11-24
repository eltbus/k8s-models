from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.networking_k8s_io.http_ingress_path import HTTPIngressPath


class HTTPIngressRuleValue(BaseModel):
    paths: List[HTTPIngressPath] = Field(default=None, description=r""" paths is a collection of paths that map requests to backends. """)
