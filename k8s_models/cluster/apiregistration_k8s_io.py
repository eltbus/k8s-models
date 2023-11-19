from __future__ import annotations

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta
from k8s_models.cluster.apiregistration import APIServiceSpec
from k8s_models.definitions.unknown import APIServiceStatus

class APIService(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: APIServiceSpec = Field(default=None, description=r""" Spec contains information for locating and communicating with a server """)
	status: APIServiceStatus = Field(default=None, description=r""" Status contains derived information about an API server """)
