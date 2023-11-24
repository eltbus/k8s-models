from pydantic import BaseModel, Field


class EndpointPort(BaseModel):
    appProtocol: str = Field(default=None, description=r""" The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 over cleartext as described in https://www.rfc-editor.org/rfc/rfc7540   * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol. """)
    name: str = Field(default=None, description=r""" The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined. """)
    port: int = Field(default=None, description=r""" The port number of the endpoint. """)
    protocol: str = Field(default=None, description=r""" The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. """)
