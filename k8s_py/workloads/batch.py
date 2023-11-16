from typing import Optional

from pydantic import BaseModel, Field

from k8s_py.types import JobTemplateSpec, ObjectMeta

# Pydantic model for CronJob
class CronJob(BaseModel):
    apiVersion: str = Field(default="batch/v1", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.")
    kind: str = Field(default="CronJob", description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated.")
    metadata: ObjectMeta = Field(default=None, description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata")
    spec: JobTemplateSpec = Field(..., description="Specification of the desired behavior of the CronJob.")
    status: Optional[dict] = Field(default=None, description="Current status of a CronJob. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status")
