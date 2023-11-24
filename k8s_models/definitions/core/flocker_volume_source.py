from pydantic import BaseModel, Field


class FlockerVolumeSource(BaseModel):
    datasetName: str = Field(default=None, description=r""" datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated """)
    datasetUUID: str = Field(default=None, description=r""" datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset """)
