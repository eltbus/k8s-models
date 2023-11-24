from pydantic import BaseModel, Field


class PersistentVolumeClaimVolumeSource(BaseModel):
    claimName: str = Field(default=None, description=r""" claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """)
    readOnly: bool = Field(default=None, description=r""" readOnly Will force the ReadOnly setting in VolumeMounts. Default false. """)
