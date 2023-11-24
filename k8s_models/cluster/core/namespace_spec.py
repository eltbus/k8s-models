from typing import List

from pydantic import BaseModel, Field


class NamespaceSpec(BaseModel):
    finalizers: List[str] = Field(default=None, description=r""" Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ """)
