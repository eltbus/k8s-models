from pydantic import BaseModel, Field


class CSINodeSpec(BaseModel):
    drivers: List[CSINodeDriver] = Field(default=None, description=r""" drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty. """)
