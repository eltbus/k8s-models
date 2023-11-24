from pydantic import BaseModel, Field


class CustomResourceDefinitionNames(BaseModel):
    categories: List[str] = Field(default=None, description=r""" categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`. """)
    kind: str = Field(default="CustomResourceDefinitionNames", description=r""" kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls. """)
    listKind: str = Field(default=None, description=r""" listKind is the serialized kind of the list for this resource. Defaults to "`kind`List". """)
    plural: str = Field(default=None, description=r""" plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase. """)
    shortNames: List[str] = Field(default=None, description=r""" shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase. """)
    singular: str = Field(default=None, description=r""" singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`. """)
