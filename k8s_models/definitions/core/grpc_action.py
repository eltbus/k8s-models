from pydantic import BaseModel, Field


class GRPCAction(BaseModel):
    port: int = Field(default=None, description=r""" Port number of the gRPC service. Number must be in the range 1 to 65535. """)
    service: str = Field(default=None, description=r""" Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).  If this is not specified, the default behavior is defined by gRPC. """)