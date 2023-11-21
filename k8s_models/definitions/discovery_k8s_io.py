from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_models.definitions.core import ObjectReference

class Endpoint(BaseModel):
	addresses: List[str] = Field(default=None, description=r""" addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267 """)
	conditions: EndpointConditions = Field(default=None, description=r""" conditions contains information about the current status of the endpoint. """)
	deprecatedTopology: dict = Field(default=None, description=r""" deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead. """)
	hints: EndpointHints = Field(default=None, description=r""" hints contains information associated with how an endpoint should be consumed. """)
	hostname: str = Field(default=None, description=r""" hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation. """)
	nodeName: str = Field(default=None, description=r""" nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. """)
	targetRef: ObjectReference = Field(default=None, description=r""" targetRef is a reference to a Kubernetes object that represents this endpoint. """)
	zone: str = Field(default=None, description=r""" zone is the name of the Zone this endpoint exists in. """)

class EndpointConditions(BaseModel):
	ready: bool = Field(default=None, description=r""" ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag. """)
	serving: bool = Field(default=None, description=r""" serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. """)
	terminating: bool = Field(default=None, description=r""" terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. """)

class EndpointHints(BaseModel):
	forZones: List[ForZone] = Field(default=None, description=r""" forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing. """)

class ForZone(BaseModel):
	name: str = Field(default=None, description=r""" name represents the name of the zone. """)
