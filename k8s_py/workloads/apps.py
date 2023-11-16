from pydantic import BaseModel, Field
from typing import Optional

from k8s_py.types import DaemonSetSpec, DaemonSetStatus

# Pydantic model for DaemonSet
class DaemonSet(BaseModel):
    apiVersion: str = Field(default="apps/v1", description="APIVersion defines the versioned schema of this representation of an object.")
    kind: str = Field(default="DaemonSet", description="Kind is a string value representing the REST resource this object represents.")
    metadata: ObjectMeta = Field(default=None, description="Standard object's metadata.")
    spec: DaemonSetSpec = Field(..., description="The desired behavior of this daemon set.")
    status: Optional[DaemonSetStatus] = Field(default=None, description="The current status of this daemon set. Read-only.")
