from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.meta import Time

class ExemptPriorityLevelConfiguration(BaseModel):
	lendablePercent: int = Field(default=None, description=r""" `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels.  This value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 ) """)
	nominalConcurrencyShares: int = Field(default=None, description=r""" `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally reserved for this priority level. This DOES NOT limit the dispatching from this priority level but affects the other priority levels through the borrowing mechanism. The server's concurrency limit (ServerCL) is divided among all the priority levels in proportion to their NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of zero. """)

class FlowDistinguisherMethod(BaseModel):
	type: str = Field(default=None, description=r""" `type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required. """)

class FlowSchemaCondition(BaseModel):
	lastTransitionTime: Time = Field(default=None, description=r""" `lastTransitionTime` is the last time the condition transitioned from one status to another. """)
	message: str = Field(default=None, description=r""" `message` is a human-readable message indicating details about last transition. """)
	reason: str = Field(default=None, description=r""" `reason` is a unique, one-word, CamelCase reason for the condition's last transition. """)
	status: str = Field(default=None, description=r""" `status` is the status of the condition. Can be True, False, Unknown. Required. """)
	type: str = Field(default=None, description=r""" `type` is the type of the condition. Required. """)

class GroupSubject(BaseModel):
	name: str = Field(default=None, description=r""" name is the user group that matches, or "*" to match all user groups. See https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go for some well-known group names. Required. """)

class LimitResponse(BaseModel):
	queuing: QueuingConfiguration = Field(default=None, description=r""" `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `"Queue"`. """)
	type: str = Field(default=None, description=r""" `type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required. """)

class LimitedPriorityLevelConfiguration(BaseModel):
	borrowingLimitPercent: int = Field(default=None, description=r""" `borrowingLimitPercent`, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level's BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level's nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.  BorrowingCL(i) = round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )  The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left `nil`, the limit is effectively infinite. """)
	lendablePercent: int = Field(default=None, description=r""" `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 ) """)
	limitResponse: LimitResponse = Field(default=None, description=r""" `limitResponse` indicates what to do with requests that can not be executed right now """)
	nominalConcurrencyShares: int = Field(default=None, description=r""" `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server's concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of 30. """)

class NonResourcePolicyRule(BaseModel):
	nonResourceURLs: List[str] = Field(default=None, description=r""" `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:   - "/healthz" is legal   - "/hea*" is illegal   - "/hea" is legal but matches nothing   - "/hea/*" also matches nothing   - "/healthz/*" matches all per-component health checks. "*" matches all non-resource urls. if it is present, it must be the only entry. Required. """)
	verbs: List[str] = Field(default=None, description=r""" `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs. If it is present, it must be the only entry. Required. """)

class PolicyRulesWithSubjects(BaseModel):
	nonResourceRules: List[NonResourcePolicyRule] = Field(default=None, description=r""" `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL. """)
	resourceRules: List[ResourcePolicyRule] = Field(default=None, description=r""" `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty. """)
	subjects: List[Subject] = Field(default=None, description=r""" subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required. """)

class PriorityLevelConfigurationCondition(BaseModel):
	lastTransitionTime: Time = Field(default=None, description=r""" `lastTransitionTime` is the last time the condition transitioned from one status to another. """)
	message: str = Field(default=None, description=r""" `message` is a human-readable message indicating details about last transition. """)
	reason: str = Field(default=None, description=r""" `reason` is a unique, one-word, CamelCase reason for the condition's last transition. """)
	status: str = Field(default=None, description=r""" `status` is the status of the condition. Can be True, False, Unknown. Required. """)
	type: str = Field(default=None, description=r""" `type` is the type of the condition. Required. """)

class PriorityLevelConfigurationReference(BaseModel):
	name: str = Field(default=None, description=r""" `name` is the name of the priority level configuration being referenced Required. """)

class QueuingConfiguration(BaseModel):
	handSize: int = Field(default=None, description=r""" `handSize` is a small positive number that configures the shuffle sharding of requests into queues.  When enqueuing a request at this priority level the request's flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here.  The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues).  See the user-facing documentation for more extensive guidance on setting this field.  This field has a default value of 8. """)
	queueLengthLimit: int = Field(default=None, description=r""" `queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected.  This value must be positive.  If not specified, it will be defaulted to 50. """)
	queues: int = Field(default=None, description=r""" `queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive.  Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant.  This field has a default value of 64. """)

class ResourcePolicyRule(BaseModel):
	apiGroups: List[str] = Field(default=None, description=r""" `apiGroups` is a list of matching API groups and may not be empty. "*" matches all API groups and, if present, must be the only entry. Required. """)
	clusterScope: bool = Field(default=None, description=r""" `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list. """)
	namespaces: List[str] = Field(default=None, description=r""" `namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains "*".  Note that "*" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true. """)
	resources: List[str] = Field(default=None, description=r""" `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ "services", "nodes/status" ].  This list may not be empty. "*" matches all resources and, if present, must be the only entry. Required. """)
	verbs: List[str] = Field(default=None, description=r""" `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs and, if present, must be the only entry. Required. """)

class ServiceAccountSubject(BaseModel):
	name: str = Field(default=None, description=r""" `name` is the name of matching ServiceAccount objects, or "*" to match regardless of name. Required. """)
	namespace: str = Field(default=None, description=r""" `namespace` is the namespace of matching ServiceAccount objects. Required. """)

class Subject(BaseModel):
	group: GroupSubject = Field(default=None, description=r""" `group` matches based on user group name. """)
	kind: str = Field(default="Subject", description=r""" `kind` indicates which one of the other fields is non-empty. Required """)
	serviceAccount: ServiceAccountSubject = Field(default=None, description=r""" `serviceAccount` matches ServiceAccounts. """)
	user: UserSubject = Field(default=None, description=r""" `user` matches based on username. """)

class UserSubject(BaseModel):
	name: str = Field(default=None, description=r""" `name` is the username that matches, or "*" to match all usernames. Required. """)
