from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.batch.pod_failure_policy_on_exit_codes_requirement import PodFailurePolicyOnExitCodesRequirement
from k8s_models.definitions.batch.pod_failure_policy_on_pod_conditions_pattern import PodFailurePolicyOnPodConditionsPattern


class PodFailurePolicyRule(BaseModel):
    action: str = Field(default=None, description=r""" Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are:  - FailJob: indicates that the pod's job is marked as Failed and all   running pods are terminated. - FailIndex: indicates that the pod's index is marked as Failed and will   not be restarted.   This value is alpha-level. It can be used when the   `JobBackoffLimitPerIndex` feature gate is enabled (disabled by default). - Ignore: indicates that the counter towards the .backoffLimit is not   incremented and a replacement pod is created. - Count: indicates that the pod is handled in the default way - the   counter towards the .backoffLimit is incremented. Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule. """)
    onExitCodes: PodFailurePolicyOnExitCodesRequirement = Field(default=None, description=r""" Represents the requirement on the container exit codes. """)
    onPodConditions: List[PodFailurePolicyOnPodConditionsPattern] = Field(default=None, description=r""" Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed. """)
