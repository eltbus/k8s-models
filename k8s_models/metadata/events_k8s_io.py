from __future__ import annotations

from pydantic import BaseModel, Field
from k8s_models.definitions.meta import ObjectMeta, Time, MicroTime
from k8s_models.definitions.core import EventSource, ObjectReference
from k8s_models.definitions.events_k8s_io import EventSeries

class Event(BaseModel):
	action: str = Field(default=None, description=r""" action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters. """)
	apiVersion: str = Field(default="v1", description=r""" APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources """)
	deprecatedCount: int = Field(default=None, description=r""" deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type. """)
	deprecatedFirstTimestamp: Time = Field(default=None, description=r""" deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. """)
	deprecatedLastTimestamp: Time = Field(default=None, description=r""" deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. """)
	deprecatedSource: EventSource = Field(default=None, description=r""" deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type. """)
	eventTime: MicroTime = Field(default=None, description=r""" eventTime is the time when this Event was first observed. It is required. """)
	kind: str = Field(default="Event", description=r""" Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
	metadata: ObjectMeta = Field(default=None, description=r""" Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """)
	note: str = Field(default=None, description=r""" note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB. """)
	reason: str = Field(default=None, description=r""" reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters. """)
	regarding: ObjectReference = Field(default=None, description=r""" regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object. """)
	related: ObjectReference = Field(default=None, description=r""" related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object. """)
	reportingController: str = Field(default=None, description=r""" reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events. """)
	reportingInstance: str = Field(default=None, description=r""" reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters. """)
	series: EventSeries = Field(default=None, description=r""" series is data about the Event series this event represents or nil if it's a singleton Event. """)
	type: str = Field(default=None, description=r""" type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events. """)
