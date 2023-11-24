from pydantic import BaseModel, Field


class LimitResponse(BaseModel):
    queuing: QueuingConfiguration = Field(default=None, description=r""" `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `"Queue"`. """)
    type: str = Field(default=None, description=r""" `type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required. """)
