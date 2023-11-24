from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.admissionregistration_k8s_io.webhook_client_config import WebhookClientConfig


class WebhookConversion(BaseModel):
    clientConfig: WebhookClientConfig = Field(default=None, description=r""" clientConfig is the instructions for how to call the webhook if strategy is `Webhook`. """)
    conversionReviewVersions: List[str] = Field(default=None, description=r""" conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. """)
