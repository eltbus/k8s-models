from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.definitions.core import LimitRangeItem
from k8s_models.metadata.core import PodTemplateSpec
from k8s_models.workloads.core import PodSpec

class LimitRange(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: LimitRangeSpec = Field(default=None, description=r""" Spec defines the limits enforced. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)

class LimitRangeSpec(BaseModel):
	limits: List[LimitRangeItem] = Field(default=None, description=r""" Limits is the list of LimitRangeItem objects that are enforced. """)

class PodTemplate(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	template: PodTemplateSpec = Field(default=None, description=r""" Template defines the pods that will be created from this pod template. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)

class PodTemplateSpec(BaseModel):
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: PodSpec = Field(default=None, description=r""" Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
