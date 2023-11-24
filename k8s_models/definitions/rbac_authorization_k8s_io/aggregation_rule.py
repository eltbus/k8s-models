from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.meta.label_selector import LabelSelector


class AggregationRule(BaseModel):
    clusterRoleSelectors: List[LabelSelector] = Field(default=None, description=r""" ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added """)
