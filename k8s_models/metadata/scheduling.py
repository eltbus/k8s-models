from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ListMeta
from k8s_models.metadata.scheduling_k8s_io import PriorityClass

class PriorityClassList(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[PriorityClass] = Field(default=None, description=r""" items is the list of PriorityClasses """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)