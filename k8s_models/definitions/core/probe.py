from pydantic import BaseModel, Field


class Probe(BaseModel):
    exec: ExecAction = Field(default=None, description=r""" Exec specifies the action to take. """)
    failureThreshold: int = Field(default=None, description=r""" Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. """)
    grpc: GRPCAction = Field(default=None, description=r""" GRPC specifies an action involving a GRPC port. """)
    httpGet: HTTPGetAction = Field(default=None, description=r""" HTTPGet specifies the http request to perform. """)
    initialDelaySeconds: int = Field(default=None, description=r""" Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)
    periodSeconds: int = Field(default=None, description=r""" How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. """)
    successThreshold: int = Field(default=None, description=r""" Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. """)
    tcpSocket: TCPSocketAction = Field(default=None, description=r""" TCPSocket specifies an action involving a TCP port. """)
    terminationGracePeriodSeconds: int = Field(default=None, description=r""" Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. """)
    timeoutSeconds: int = Field(default=None, description=r""" Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """)
