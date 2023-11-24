from pydantic import BaseModel, Field


class ContainerResourceMetricStatus(BaseModel):
    container: str = Field(default=None, description=r""" container is the name of the container in the pods of the scaling target """)
    current: MetricValueStatus = Field(default=None, description=r""" current contains the current value for the given metric """)
    name: str = Field(default=None, description=r""" name is the name of the resource in question. """)
