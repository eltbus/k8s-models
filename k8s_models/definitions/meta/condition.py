from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time


class Condition(BaseModel):
    lastTransitionTime: Time = Field(default=None, description=r""" lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. """)
    message: str = Field(default=None, description=r""" message is a human readable message indicating details about the transition. This may be an empty string. """)
    observedGeneration: int = Field(default=None, description=r""" observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. """)
    reason: str = Field(default=None, description=r""" reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. """)
    status: str = Field(default=None, description=r""" status of the condition, one of True, False, Unknown. """)
    type: str = Field(default=None, description=r""" type of condition in CamelCase or in foo.example.com/CamelCase. """)
