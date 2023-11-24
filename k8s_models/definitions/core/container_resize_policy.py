from pydantic import BaseModel, Field


class ContainerResizePolicy(BaseModel):
    resourceName: str = Field(default=None, description=r""" Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. """)
    restartPolicy: str = Field(default=None, description=r""" Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. """)
