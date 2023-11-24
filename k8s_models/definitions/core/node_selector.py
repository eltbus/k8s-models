from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.node_selector_term import NodeSelectorTerm


class NodeSelector(BaseModel):
    nodeSelectorTerms: List[NodeSelectorTerm] = Field(default=None, description=r""" Required. A list of node selector terms. The terms are ORed. """)
