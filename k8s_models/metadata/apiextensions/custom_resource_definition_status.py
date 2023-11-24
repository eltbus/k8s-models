from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.apiextensions_k8s_io.custom_resource_definition_names import CustomResourceDefinitionNames
from k8s_models.definitions.apiextensions_k8s_io.custom_resource_definition_condition import CustomResourceDefinitionCondition


class CustomResourceDefinitionStatus(BaseModel):
    acceptedNames: CustomResourceDefinitionNames = Field(default=None, description=r""" acceptedNames are the names that are actually being used to serve discovery. They may be different than the names in spec. """)
    conditions: List[CustomResourceDefinitionCondition] = Field(default=None, description=r""" conditions indicate state for particular aspects of a CustomResourceDefinition """)
    storedVersions: List[str] = Field(default=None, description=r""" storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list. """)
