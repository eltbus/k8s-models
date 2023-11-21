from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.core import NodeSelector
from k8s_models.definitions.networking_k8s_io import (
    IngressBackend,
    IngressRule,
    IngressTLS,
    IngressClassParametersReference,
)


class ClusterCIDRSpec(BaseModel):
    ipv4: str = Field(
        default=None,
        description=r""" ipv4 defines an IPv4 IP block in CIDR notation(e.g. "10.0.0.0/8"). At least one of ipv4 and ipv6 must be specified. This field is immutable. """,
    )
    ipv6: str = Field(
        default=None,
        description=r""" ipv6 defines an IPv6 IP block in CIDR notation(e.g. "2001:db8::/64"). At least one of ipv4 and ipv6 must be specified. This field is immutable. """,
    )
    nodeSelector: NodeSelector = Field(
        default=None,
        description=r""" nodeSelector defines which nodes the config is applicable to. An empty or nil nodeSelector selects all nodes. This field is immutable. """,
    )
    perNodeHostBits: int = Field(
        default=None,
        description=r""" perNodeHostBits defines the number of host bits to be configured per node. A subnet mask determines how much of the address is used for network bits and host bits. For example an IPv4 address of 192.168.0.0/24, splits the address into 24 bits for the network portion and 8 bits for the host portion. To allocate 256 IPs, set this field to 8 (a /24 mask for IPv4 or a /120 for IPv6). Minimum value is 4 (16 IPs). This field is immutable. """,
    )


class IngressSpec(BaseModel):
    defaultBackend: IngressBackend = Field(
        default=None,
        description=r""" defaultBackend is the backend that should handle requests that don't match any rule. If Rules are not specified, DefaultBackend must be specified. If DefaultBackend is not set, the handling of requests that do not match any of the rules will be up to the Ingress controller. """,
    )
    ingressClassName: str = Field(
        default=None,
        description=r""" ingressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the `kubernetes.io/ingress.class` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present. """,
    )
    rules: List[IngressRule] = Field(
        default=None,
        description=r""" rules is a list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend. """,
    )
    tls: List[IngressTLS] = Field(
        default=None,
        description=r""" tls represents the TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI. """,
    )


class IngressClassSpec(BaseModel):
    controller: str = Field(
        default=None,
        description=r""" controller refers to the name of the controller that should handle this class. This allows for different "flavors" that are controlled by the same controller. For example, you may have different parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. "acme.io/ingress-controller". This field is immutable. """,
    )
    parameters: IngressClassParametersReference = Field(
        default=None,
        description=r""" parameters is a link to a custom resource containing additional configuration for the controller. This is optional if the controller does not require extra parameters. """,
    )
