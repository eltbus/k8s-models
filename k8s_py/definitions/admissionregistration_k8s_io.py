from pydantic import BaseModel

class AuditAnnotation(BaseModel):
    pass

class ExpressionWarning(BaseModel):
    pass

class MatchCondition(BaseModel):
    pass

class MatchResources(BaseModel):
    pass

class MutatingWebhook(BaseModel):
    pass

class NamedRuleWithOperations(BaseModel):
    pass

class ParamKind(BaseModel):
    pass

class ParamRef(BaseModel):
    pass

class RuleWithOperations(BaseModel):
    pass

class ServiceReference(BaseModel):
    pass

class TypeChecking(BaseModel):
    pass

class ValidatingWebhook(BaseModel):
    pass

class Validation(BaseModel):
    pass

class WebhookClientConfig(BaseModel):
    pass
