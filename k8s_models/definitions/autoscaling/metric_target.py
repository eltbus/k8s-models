from pydantic import BaseModel, Field


class MetricTarget(BaseModel):
    averageUtilization: int = Field(default=None, description=r""" averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type """)
    averageValue: Quantity = Field(default=None, description=r""" averageValue is the target value of the average of the metric across all relevant pods (as a quantity) """)
    type: str = Field(default=None, description=r""" type represents whether the metric type is Utilization, Value, or AverageValue """)
    value: Quantity = Field(default=None, description=r""" value is the target value of the metric (as a quantity). """)
