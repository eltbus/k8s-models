from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.cluster.rbac_authorization_k8s_io import ClusterRole, ClusterRoleBinding, Role, RoleBinding
from k8s_models.definitions.meta import ListMeta

class ClusterRoleList(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ClusterRole] = Field(default=None, description=r""" Items is a list of ClusterRoles """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. """)

class ClusterRoleBindingList(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[ClusterRoleBinding] = Field(default=None, description=r""" Items is a list of ClusterRoleBindings """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. """)

class RoleList(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[Role] = Field(default=None, description=r""" Items is a list of Roles """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. """)

class RoleBindingList(BaseModel):
	apiVersion: str = Field(default=None, description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	items: List[RoleBinding] = Field(default=None, description=r""" Items is a list of RoleBindings """)
	kind: str = Field(default=None, description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ListMeta = Field(default=None, description=r""" Standard object's metadata. """)