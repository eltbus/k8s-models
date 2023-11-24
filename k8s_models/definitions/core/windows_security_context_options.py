from pydantic import BaseModel, Field


class WindowsSecurityContextOptions(BaseModel):
    gmsaCredentialSpec: str = Field(default=None, description=r""" GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. """)
    gmsaCredentialSpecName: str = Field(default=None, description=r""" GMSACredentialSpecName is the name of the GMSA credential spec to use. """)
    hostProcess: bool = Field(default=None, description=r""" HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. """)
    runAsUserName: str = Field(default=None, description=r""" The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """)
