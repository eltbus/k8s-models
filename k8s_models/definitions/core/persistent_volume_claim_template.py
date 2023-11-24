from pydantic import BaseModel, Field

from k8s_models.definitions.meta.object_meta import ObjectMeta
from k8s_models.config_and_storage.core.persistent_volume_claim_spec import PersistentVolumeClaimSpec


class PersistentVolumeClaimTemplate(BaseModel):
    metadata: ObjectMeta = Field(default=None, description=r""" May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """)
    spec: PersistentVolumeClaimSpec = Field(default=None, description=r""" The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here. """)
