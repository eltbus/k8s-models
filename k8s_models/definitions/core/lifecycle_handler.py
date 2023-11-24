from pydantic import BaseModel, Field

from k8s_models.definitions.core.exec_action import ExecAction
from k8s_models.definitions.core.http_get_action import HTTPGetAction
from k8s_models.definitions.core.tcp_socket_action import TCPSocketAction


class LifecycleHandler(BaseModel):
    exec: ExecAction = Field(default=None, description=r""" Exec specifies the action to take. """)
    httpGet: HTTPGetAction = Field(default=None, description=r""" HTTPGet specifies the http request to perform. """)
    tcpSocket: TCPSocketAction = Field(default=None, description=r""" Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified. """)
