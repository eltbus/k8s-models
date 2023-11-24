from pydantic import BaseModel, Field


class CustomResourceSubresources(BaseModel):
    scale: CustomResourceSubresourceScale = Field(default=None, description=r""" scale indicates the custom resource should serve a `/scale` subresource that returns an `autoscaling/v1` Scale object. """)
    status: CustomResourceSubresourceStatus = Field(default=None, description=r""" status indicates the custom resource should serve a `/status` subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the `status` stanza of the object. 2. requests to the custom resource `/status` subresource ignore changes to anything other than the `status` stanza of the object. """)
