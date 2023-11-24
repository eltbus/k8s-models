from typing import List

from pydantic import BaseModel, Field

from k8s_models.definitions.apiextensions_k8s_io.custom_resource_column_definition import CustomResourceColumnDefinition
from k8s_models.definitions.apiextensions_k8s_io.custom_resource_validation import CustomResourceValidation
from k8s_models.definitions.apiextensions_k8s_io.custom_resource_subresources import CustomResourceSubresources


class CustomResourceDefinitionVersion(BaseModel):
    additionalPrinterColumns: List[CustomResourceColumnDefinition] = Field(default=None, description=r""" additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. """)
    deprecated: bool = Field(default=None, description=r""" deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false. """)
    deprecationWarning: str = Field(default=None, description=r""" deprecationWarning overrides the default warning returned to API clients. May only be set when `deprecated` is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists. """)
    name: str = Field(default=None, description=r""" name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true. """)
    validation_schema: CustomResourceValidation = Field(default=None, alias="schema", description=r""" schema describes the schema used for validation, pruning, and defaulting of this version of the custom resource. """)
    served: bool = Field(default=None, description=r""" served is a flag enabling/disabling this version from being served via REST APIs """)
    storage: bool = Field(default=None, description=r""" storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true. """)
    subresources: CustomResourceSubresources = Field(default=None, description=r""" subresources specify what subresources this version of the defined custom resource have. """)
