from pydantic import BaseModel, Field

from k8s_models.definitions.networking_k8s_io.ingress_class_parameters_reference import IngressClassParametersReference


class IngressClassSpec(BaseModel):
    controller: str = Field(default=None, description=r""" controller refers to the name of the controller that should handle this class. This allows for different "flavors" that are controlled by the same controller. For example, you may have different parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. "acme.io/ingress-controller". This field is immutable. """)
    parameters: IngressClassParametersReference = Field(default=None, description=r""" parameters is a link to a custom resource containing additional configuration for the controller. This is optional if the controller does not require extra parameters. """)
