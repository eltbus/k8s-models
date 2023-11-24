from pydantic import BaseModel, Field

from k8s_models.definitions.meta.fields_v1 import FieldsV1
from k8s_models.definitions.meta.time import Time


class ManagedFieldsEntry(BaseModel):
    apiVersion: str = Field(default="v1", description=r""" APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted. """)
    fieldsType: str = Field(default=None, description=r""" FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1" """)
    fieldsV1: FieldsV1 = Field(default=None, description=r""" FieldsV1 holds the first JSON version format as described in the "FieldsV1" type. """)
    manager: str = Field(default=None, description=r""" Manager is an identifier of the workflow managing these fields. """)
    operation: str = Field(default=None, description=r""" Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'. """)
    subresource: str = Field(default=None, description=r""" Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource. """)
    time: Time = Field(default=None, description=r""" Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be updated if a field is added, the manager changes any of the owned fields value or removes a field. The timestamp does not update when a field is removed from the entry because another manager took it over. """)
