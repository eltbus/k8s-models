from pydantic import BaseModel, Field
from typing import Optional

from k8s_py.types import DaemonSetSpec, DaemonSetStatus, ObjectMeta, DeploymentSpec, DeploymentStatus, ReplicaSetSpec, ReplicaSetStatus

class DaemonSet(BaseModel):
    apiVersion: str = Field(default="apps/v1", description="APIVersion defines the versioned schema of this representation of an object.")
    kind: str = Field(default="DaemonSet", description="Kind is a string value representing the REST resource this object represents.")
    metadata: ObjectMeta = Field(default=None, description="Standard object's metadata.")
    spec: DaemonSetSpec = Field(..., description="The desired behavior of this daemon set.")
    status: Optional[DaemonSetStatus] = Field(default=None, description="The current status of this daemon set. Read-only.")

class Deployment(BaseModel):
    apiVersion: str = Field(default="apps/v1", description="APIVersion defines the versioned schema of this representation of an object.")
    kind: str = Field(default="Deployment", description="Kind is a string value representing the REST resource this object represents.")
    metadata: ObjectMeta = Field(default=None, description="Standard object's metadata.")
    spec: DeploymentSpec = Field(..., description="The specification of the desired behavior of the Deployment.")
    status: Optional[DeploymentStatus] = Field(default=None, description="The most recently observed status of the Deployment. Read-only.")

class ReplicaSet(BaseModel):
    apiVersion: str = Field(default="apps/v1", description="APIVersion defines the versioned schema of this representation of an object.")
    kind: str = Field(default="ReplicaSet", description="Kind is a string value representing the REST resource this object represents.")
    metadata: ObjectMeta = Field(default=None, description="Standard object's metadata.")
    spec: ReplicaSetSpec = Field(..., description="Specification of the desired behavior of the ReplicaSet.")
    status: Optional[ReplicaSetStatus] = Field(default=None, description="Most recently observed status of the ReplicaSet.")
