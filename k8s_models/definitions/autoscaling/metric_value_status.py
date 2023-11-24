from pydantic import BaseModel, Field


class MetricValueStatus(BaseModel):
    averageUtilization: int = Field(default=None, description=r""" currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. """)
    averageValue: Quantity = Field(default=None, description=r""" averageValue is the current value of the average of the metric across all relevant pods (as a quantity) """)
    value: Quantity = Field(default=None, description=r""" value is the current value of the metric (as a quantity). """)
