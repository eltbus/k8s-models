from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import Time, ObjectMeta
from k8s_models.workloads.batch import JobSpec

class JobCondition(BaseModel):
	lastProbeTime: Time = Field(default=None, description=r""" Last time the condition was checked. """)
	lastTransitionTime: Time = Field(default=None, description=r""" Last time the condition transit from one status to another. """)
	message: str = Field(default=None, description=r""" Human readable message indicating details about last transition. """)
	reason: str = Field(default=None, description=r""" (brief) reason for the condition's last transition. """)
	status: str = Field(default=None, description=r""" Status of the condition, one of True, False, Unknown. """)
	type: str = Field(default=None, description=r""" Type of job condition, Complete or Failed. """)

class JobTemplateSpec(BaseModel):
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	spec: JobSpec = Field(default=None, description=r""" Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """)

class PodFailurePolicy(BaseModel):
	rules: List[PodFailurePolicyRule] = Field(default=None, description=r""" A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed. """)

class PodFailurePolicyOnExitCodesRequirement(BaseModel):
	containerName: str = Field(default=None, description=r""" Restricts the check for exit codes to the container with the specified name. When null, the rule applies to all containers. When specified, it should match one the container or initContainer names in the pod template. """)
	operator: str = Field(default=None, description=r""" Represents the relationship between the container exit code(s) and the specified values. Containers completed with success (exit code 0) are excluded from the requirement check. Possible values are:  - In: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the 'containerName' field) is in the set of specified values. - NotIn: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the 'containerName' field) is not in the set of specified values. Additional values are considered to be added in the future. Clients should react to an unknown operator by assuming the requirement is not satisfied. """)
	values: List[int] = Field(default=None, description=r""" Specifies the set of values. Each returned container exit code (might be multiple in case of multiple containers) is checked against this set of values with respect to the operator. The list of values must be ordered and must not contain duplicates. Value '0' cannot be used for the In operator. At least one element is required. At most 255 elements are allowed. """)

class PodFailurePolicyOnPodConditionsPattern(BaseModel):
	status: str = Field(default=None, description=r""" Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True. """)
	type: str = Field(default=None, description=r""" Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type. """)

class PodFailurePolicyRule(BaseModel):
	action: str = Field(default=None, description=r""" Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are:  - FailJob: indicates that the pod's job is marked as Failed and all   running pods are terminated. - FailIndex: indicates that the pod's index is marked as Failed and will   not be restarted.   This value is alpha-level. It can be used when the   `JobBackoffLimitPerIndex` feature gate is enabled (disabled by default). - Ignore: indicates that the counter towards the .backoffLimit is not   incremented and a replacement pod is created. - Count: indicates that the pod is handled in the default way - the   counter towards the .backoffLimit is incremented. Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule. """)
	onExitCodes: PodFailurePolicyOnExitCodesRequirement = Field(default=None, description=r""" Represents the requirement on the container exit codes. """)
	onPodConditions: List[PodFailurePolicyOnPodConditionsPattern] = Field(default=None, description=r""" Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed. """)

class UncountedTerminatedPods(BaseModel):
	failed: List[str] = Field(default=None, description=r""" failed holds UIDs of failed Pods. """)
	succeeded: List[str] = Field(default=None, description=r""" succeeded holds UIDs of succeeded Pods. """)
