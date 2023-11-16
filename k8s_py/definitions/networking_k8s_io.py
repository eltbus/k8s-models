from pydantic import BaseModel

class HTTPIngressPath(BaseModel):
    pass

class HTTPIngressRuleValue(BaseModel):
    pass

class IPBlock(BaseModel):
    pass

class IngressBackend(BaseModel):
    pass

class IngressClassParametersReference(BaseModel):
    pass

class IngressLoadBalancerIngress(BaseModel):
    pass

class IngressLoadBalancerStatus(BaseModel):
    pass

class IngressPortStatus(BaseModel):
    pass

class IngressRule(BaseModel):
    pass

class IngressServiceBackend(BaseModel):
    pass

class IngressTLS(BaseModel):
    pass

class NetworkPolicyEgressRule(BaseModel):
    pass

class NetworkPolicyIngressRule(BaseModel):
    pass

class NetworkPolicyPeer(BaseModel):
    pass

class NetworkPolicyPort(BaseModel):
    pass

class ParentReference(BaseModel):
    pass

class ServiceBackendPort(BaseModel):
    pass
