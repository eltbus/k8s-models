from pydantic import BaseModel, Field


class ContainerImage(BaseModel):
    names: List[str] = Field(default=None, description=r""" Names by which this image is known. e.g. ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"] """)
    sizeBytes: int = Field(default=None, description=r""" The size of the image in bytes. """)
