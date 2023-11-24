from pydantic import BaseModel, Field


class MetricIdentifier(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the given metric """)
    selector: LabelSelector = Field(default=None, description=r""" selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics. """)
