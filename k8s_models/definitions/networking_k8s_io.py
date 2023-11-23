from __future__ import annotations
from typing import List, Any

from pydantic import BaseModel, Field

from k8s_models.definitions.core import TypedLocalObjectReference
from k8s_models.definitions.meta import LabelSelector

class HTTPIngressPath(BaseModel):
    backend: IngressBackend = Field(default=None, description=r""" backend defines the referenced service endpoint to which the traffic will be forwarded to. """)
    path: str = Field(default=None, description=r""" path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix". """)
    pathType: str = Field(default=None, description=r""" pathType determines the interpretation of the path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is   done on a path element by element basis. A path element refers is the   list of labels in the path split by the '/' separator. A request is a   match for path p if every p is an element-wise prefix of p of the   request path. Note that if the last element of the path is a substring   of the last element in request path, it is not a match (e.g. /foo/bar   matches /foo/bar/baz, but does not match /foo/barbaz). * ImplementationSpecific: Interpretation of the Path matching is up to   the IngressClass. Implementations can treat this as a separate PathType   or treat it identically to Prefix or Exact path types. Implementations are required to support all path types. """)

class HTTPIngressRuleValue(BaseModel):
    paths: List[HTTPIngressPath] = Field(default=None, description=r""" paths is a collection of paths that map requests to backends. """)

class IPBlock(BaseModel):
    cidr: str = Field(default=None, description=r""" cidr is a string representing the IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64" """)
    besides: List[str] = Field(default=None, alias="except", description=r""" except is a slice of CIDRs that should not be included within an IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64" Except values will be rejected if they are outside the cidr range """)

class IngressBackend(BaseModel):
    resource: TypedLocalObjectReference = Field(default=None, description=r""" resource is an ObjectRef to another Kubernetes resource in the namespace of the Ingress object. If resource is specified, a service.Name and service.Port must not be specified. This is a mutually exclusive setting with "Service". """)
    service: IngressServiceBackend = Field(default=None, description=r""" service references a service as a backend. This is a mutually exclusive setting with "Resource". """)

class IngressClassParametersReference(BaseModel):
    apiGroup: str = Field(default=None, description=r""" apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """)
    kind: str = Field(default="IngressClassParametersReference", description=r""" kind is the type of resource being referenced. """)
    name: str = Field(default=None, description=r""" name is the name of resource being referenced. """)
    namespace: str = Field(default=None, description=r""" namespace is the namespace of the resource being referenced. This field is required when scope is set to "Namespace" and must be unset when scope is set to "Cluster". """)
    scope: str = Field(default=None, description=r""" scope represents if this refers to a cluster or namespace scoped resource. This may be set to "Cluster" (default) or "Namespace". """)

class IngressLoadBalancerIngress(BaseModel):
    hostname: str = Field(default=None, description=r""" hostname is set for load-balancer ingress points that are DNS based. """)
    ip: str = Field(default=None, description=r""" ip is set for load-balancer ingress points that are IP based. """)
    ports: List[IngressPortStatus] = Field(default=None, description=r""" ports provides information about the ports exposed by this LoadBalancer. """)

class IngressLoadBalancerStatus(BaseModel):
    ingress: List[IngressLoadBalancerIngress] = Field(default=None, description=r""" ingress is a list containing ingress points for the load-balancer. """)

class IngressPortStatus(BaseModel):
    error: str = Field(default=None, description=r""" error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use   CamelCase names - cloud provider specific error values must have names that comply with the   format foo.example.com/CamelCase. """)
    port: int = Field(default=None, description=r""" port is the port number of the ingress port. """)
    protocol: str = Field(default=None, description=r""" protocol is the protocol of the ingress port. The supported values are: "TCP", "UDP", "SCTP" """)

class IngressRule(BaseModel):
    host: str = Field(default=None, description=r""" host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to    the IP in the Spec of the parent Ingress. 2. The `:` delimiter is not respected because ports are not allowed. 	  Currently the port of an Ingress is implicitly :80 for http and 	  :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.  host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '\*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If host is precise, the request matches this rule if the http host header is equal to Host. 2. If host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule. """)
    http: HTTPIngressRuleValue = Field(default=None)

class IngressServiceBackend(BaseModel):
    name: str = Field(default=None, description=r""" name is the referenced service. The service must exist in the same namespace as the Ingress object. """)
    port: ServiceBackendPort = Field(default=None, description=r""" port of the referenced service. A port name or port number is required for a IngressServiceBackend. """)

class IngressTLS(BaseModel):
    hosts: List[str] = Field(default=None, description=r""" hosts is a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified. """)
    secretName: str = Field(default=None, description=r""" secretName is the name of the secret used to terminate TLS traffic on port 443. Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the "Host" header is used for routing. """)

class NetworkPolicyEgressRule(BaseModel):
    ports: List[NetworkPolicyPort] = Field(default=None, description=r""" ports is a list of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. """)
    to: List[NetworkPolicyPeer] = Field(default=None, description=r""" to is a list of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list. """)

class NetworkPolicyIngressRule(BaseModel):
    sources: List[NetworkPolicyPeer] = Field(default=None, alias="from", description=r""" from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list. """)
    ports: List[NetworkPolicyPort] = Field(default=None, description=r""" ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. """)

class NetworkPolicyPeer(BaseModel):
    ipBlock: IPBlock = Field(default=None, description=r""" ipBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be. """)
    namespaceSelector: LabelSelector = Field(default=None, description=r""" namespaceSelector selects namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.  If podSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the namespaces selected by namespaceSelector. Otherwise it selects all pods in the namespaces selected by namespaceSelector. """)
    podSelector: LabelSelector = Field(default=None, description=r""" podSelector is a label selector which selects pods. This field follows standard label selector semantics; if present but empty, it selects all pods.  If namespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the pods matching podSelector in the policy's own namespace. """)

class NetworkPolicyPort(BaseModel):
    endPort: int = Field(default=None, description=r""" endPort indicates that the range of ports from port to endPort if set, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port. """)
    port: Any = Field(default=None, description=r""" port represents the port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched. """)
    protocol: str = Field(default=None, description=r""" protocol represents the protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP. """)

class ParentReference(BaseModel):
    group: str = Field(default=None, description=r""" Group is the group of the object being referenced. """)
    name: str = Field(default=None, description=r""" Name is the name of the object being referenced. """)
    namespace: str = Field(default=None, description=r""" Namespace is the namespace of the object being referenced. """)
    resource: str = Field(default=None, description=r""" Resource is the resource of the object being referenced. """)
    uid: str = Field(default=None, description=r""" UID is the uid of the object being referenced. """)

class ServiceBackendPort(BaseModel):
    name: str = Field(default=None, description=r""" name is the name of the port on the Service. This is a mutually exclusive setting with "Number". """)
    number: int = Field(default=None, description=r""" number is the numerical port number (e.g. 80) on the Service. This is a mutually exclusive setting with "Name". """)
