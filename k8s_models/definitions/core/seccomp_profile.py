from pydantic import BaseModel, Field


class SeccompProfile(BaseModel):
    localhostProfile: str = Field(default=None, description=r""" localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type. """)
    type: str = Field(default=None, description=r""" type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied. """)
