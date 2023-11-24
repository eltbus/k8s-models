from pydantic import BaseModel, Field


class ResourceClaimSpec(BaseModel):
    allocationMode: str = Field(default=None, description=r""" Allocation can start immediately or when a Pod wants to use the resource. "WaitForFirstConsumer" is the default. """)
    parametersRef: ResourceClaimParametersReference = Field(default=None, description=r""" ParametersRef references a separate object with arbitrary parameters that will be used by the driver when allocating a resource for the claim.  The object must be in the same namespace as the ResourceClaim. """)
    resourceClassName: str = Field(default=None, description=r""" ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment. """)
