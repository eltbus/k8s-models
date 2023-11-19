from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_py.definitions.core import Toleration


class Overhead(BaseModel):
    podFixed: dict = Field(
        default=None,
        description=r""" podFixed represents the fixed resource overhead associated with running a pod. """,
    )


class Scheduling(BaseModel):
    nodeSelector: dict = Field(
        default=None,
        description=r""" nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission. """,
    )
    tolerations: List[Toleration] = Field(
        default=None,
        description=r""" tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass. """,
    )
