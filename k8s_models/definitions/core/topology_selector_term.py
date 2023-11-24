from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.topology_selector_label_requirement import TopologySelectorLabelRequirement


class TopologySelectorTerm(BaseModel):
    matchLabelExpressions: List[TopologySelectorLabelRequirement] = Field(default=None, description=r""" A list of topology selector requirements by labels. """)
