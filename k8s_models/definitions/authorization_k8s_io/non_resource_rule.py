from pydantic import BaseModel, Field


class NonResourceRule(BaseModel):
    nonResourceURLs: List[str] = Field(default=None, description=r""" NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all. """)
    verbs: List[str] = Field(default=None, description=r""" Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all. """)
