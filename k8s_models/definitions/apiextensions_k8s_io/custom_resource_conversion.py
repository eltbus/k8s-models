from pydantic import BaseModel, Field


class CustomResourceConversion(BaseModel):
    strategy: str = Field(default=None, description=r""" strategy specifies how custom resources are converted between versions. Allowed values are: - `"None"`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `"Webhook"`: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set. """)
    webhook: WebhookConversion = Field(default=None, description=r""" webhook describes how to call the conversion webhook. Required when `strategy` is set to `"Webhook"`. """)
