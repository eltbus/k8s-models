from pydantic import BaseModel, Field


class NetworkPolicyIngressRule(BaseModel):
    sources: List[NetworkPolicyPeer] = Field(default=None, alias="from", description=r""" from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list. """)
    ports: List[NetworkPolicyPort] = Field(default=None, description=r""" ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. """)
