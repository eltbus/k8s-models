from pydantic import BaseModel, Field

from k8s_models.definitions.meta.object_meta import ObjectMeta
from k8s_models.workloads.batch.job_spec import JobSpec


class JobTemplateSpec(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: JobSpec = Field(default=None, description=r""" Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
