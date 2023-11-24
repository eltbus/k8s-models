from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.meta.label_selector_requirement import LabelSelectorRequirement


class LabelSelector(BaseModel):
    matchExpressions: List[LabelSelectorRequirement] = Field(default=None, description=r""" matchExpressions is a list of label selector requirements. The requirements are ANDed. """)
    matchLabels: dict = Field(default=None, description=r""" matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. """)
