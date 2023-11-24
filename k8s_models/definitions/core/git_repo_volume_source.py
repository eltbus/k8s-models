from pydantic import BaseModel, Field


class GitRepoVolumeSource(BaseModel):
    directory: str = Field(default=None, description=r""" directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. """)
    repository: str = Field(default=None, description=r""" repository is the URL """)
    revision: str = Field(default=None, description=r""" revision is the commit hash for the specified revision. """)
