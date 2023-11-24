from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.core.key_to_path import KeyToPath


class SecretProjection(BaseModel):
    items: List[KeyToPath] = Field(default=None, description=r""" items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    optional: bool = Field(default=None, description=r""" optional field specify whether the Secret or its key must be defined """)
