from __future__ import annotations

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.metadata.apiextensions import CustomResourceDefinitionSpec, CustomResourceDefinitionStatus

class CustomResourceDefinition(BaseModel):
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default="CustomResourceDefinition", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: CustomResourceDefinitionSpec = Field(default=None, description=r""" spec describes how the user wants the resources to appear """)
	status: CustomResourceDefinitionStatus = Field(default=None, description=r""" status indicates the actual state of the CustomResourceDefinition """)
