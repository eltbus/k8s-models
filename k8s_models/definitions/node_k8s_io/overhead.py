from pydantic import BaseModel, Field


class Overhead(BaseModel):
    podFixed: dict = Field(default=None, description=r""" podFixed represents the fixed resource overhead associated with running a pod. """)
