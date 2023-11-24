from pydantic import BaseModel, Field


class SubjectRulesReviewStatus(BaseModel):
    evaluationError: str = Field(default=None, description=r""" EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. """)
    incomplete: bool = Field(default=None, description=r""" Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation. """)
    nonResourceRules: List[NonResourceRule] = Field(default=None, description=r""" NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete. """)
    resourceRules: List[ResourceRule] = Field(default=None, description=r""" ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete. """)
