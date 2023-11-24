from pydantic import BaseModel, Field


class QuobyteVolumeSource(BaseModel):
    group: str = Field(default=None, description=r""" group to map volume access to Default is no group """)
    readOnly: bool = Field(default=None, description=r""" readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. """)
    registry: str = Field(default=None, description=r""" registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes """)
    tenant: str = Field(default=None, description=r""" tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin """)
    user: str = Field(default=None, description=r""" user to map volume access to Defaults to serivceaccount user """)
    volume: str = Field(default=None, description=r""" volume is a string that references an already created Quobyte volume by name. """)
