from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.namespace_condition import NamespaceCondition


class NamespaceStatus(BaseModel):
    conditions: List[NamespaceCondition] = Field(default=None, description=r""" Represents the latest available observations of a namespace's current state. """)
    phase: str = Field(default=None, description=r""" Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ """)
