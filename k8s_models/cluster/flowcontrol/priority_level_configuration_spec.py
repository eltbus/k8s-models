from pydantic import BaseModel, Field

from k8s_models.definitions.flowcontrol_apiserver_k8s_io.exempt_priority_level_configuration import ExemptPriorityLevelConfiguration
from k8s_models.definitions.flowcontrol_apiserver_k8s_io.limited_priority_level_configuration import LimitedPriorityLevelConfiguration


class PriorityLevelConfigurationSpec(BaseModel):
    exempt: ExemptPriorityLevelConfiguration = Field(default=None, description=r""" `exempt` specifies how requests are handled for an exempt priority level. This field MUST be empty if `type` is `"Limited"`. This field MAY be non-empty if `type` is `"Exempt"`. If empty and `type` is `"Exempt"` then the default values for `ExemptPriorityLevelConfiguration` apply. """)
    limited: LimitedPriorityLevelConfiguration = Field(default=None, description=r""" `limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `"Limited"`. """)
    type: str = Field(default=None, description=r""" `type` indicates whether this priority level is subject to limitation on request execution.  A value of `"Exempt"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `"Limited"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required. """)
