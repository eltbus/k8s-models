from pydantic import BaseModel, Field


class JobTemplateSpec(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
    spec: JobSpec = Field(default=None, description=r""" Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)
