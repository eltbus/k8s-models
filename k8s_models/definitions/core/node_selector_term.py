from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.node_selector_requirement import NodeSelectorRequirement


class NodeSelectorTerm(BaseModel):
    matchExpressions: List[NodeSelectorRequirement] = Field(default=None, description=r""" A list of node selector requirements by node's labels. """)
    matchFields: List[NodeSelectorRequirement] = Field(default=None, description=r""" A list of node selector requirements by node's fields. """)
