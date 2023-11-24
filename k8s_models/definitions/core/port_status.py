from pydantic import BaseModel, Field


class PortStatus(BaseModel):
    error: str = Field(default=None, description=r""" Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use   CamelCase names - cloud provider specific error values must have names that comply with the   format foo.example.com/CamelCase. """)
    port: int = Field(default=None, description=r""" Port is the port number of the service port of which status is recorded here """)
    protocol: str = Field(default=None, description=r""" Protocol is the protocol of the service port of which status is recorded here The supported values are: "TCP", "UDP", "SCTP" """)
