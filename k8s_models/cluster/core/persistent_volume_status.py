from pydantic import BaseModel, Field

from k8s_models.definitions.meta.time import Time


class PersistentVolumeStatus(BaseModel):
    lastPhaseTransitionTime: Time = Field(default=None, description=r""" lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. This is an alpha field and requires enabling PersistentVolumeLastPhaseTransitionTime feature. """)
    message: str = Field(default=None, description=r""" message is a human-readable message indicating details about why the volume is in this state. """)
    phase: str = Field(default=None, description=r""" phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase """)
    reason: str = Field(default=None, description=r""" reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. """)
