from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from k8s_py.definitions.meta import Time
from k8s_py.definitions.admissionregistration_k8s_io import WebhookClientConfig


class CustomResourceColumnDefinition(BaseModel):
    description: str = Field(
        default=None,
        description=r""" description is a human readable description of this column. """,
    )
    format: str = Field(
        default=None,
        description=r""" format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. """,
    )
    jsonPath: str = Field(
        default=None,
        description=r""" jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column. """,
    )
    name: str = Field(
        default=None, description=r""" name is a human readable name for the column. """
    )
    priority: int = Field(
        default=None,
        description=r""" priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0. """,
    )
    type: str = Field(
        default=None,
        description=r""" type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. """,
    )


class CustomResourceConversion(BaseModel):
    strategy: str = Field(
        default=None,
        description=r""" strategy specifies how custom resources are converted between versions. Allowed values are: - `"None"`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `"Webhook"`: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set. """,
    )
    webhook: WebhookConversion = Field(
        default=None,
        description=r""" webhook describes how to call the conversion webhook. Required when `strategy` is set to `"Webhook"`. """,
    )


class CustomResourceDefinitionCondition(BaseModel):
    lastTransitionTime: Time = Field(
        default=None,
        description=r""" lastTransitionTime last time the condition transitioned from one status to another. """,
    )
    message: str = Field(
        default=None,
        description=r""" message is a human-readable message indicating details about last transition. """,
    )
    reason: str = Field(
        default=None,
        description=r""" reason is a unique, one-word, CamelCase reason for the condition's last transition. """,
    )
    status: str = Field(
        default=None,
        description=r""" status is the status of the condition. Can be True, False, Unknown. """,
    )
    type: str = Field(
        default=None,
        description=r""" type is the type of the condition. Types include Established, NamesAccepted and Terminating. """,
    )


class CustomResourceDefinitionNames(BaseModel):
    categories: List[str] = Field(
        default=None,
        description=r""" categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`. """,
    )
    kind: str = Field(
        default=None,
        description=r""" kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls. """,
    )
    listKind: str = Field(
        default=None,
        description=r""" listKind is the serialized kind of the list for this resource. Defaults to "`kind`List". """,
    )
    plural: str = Field(
        default=None,
        description=r""" plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase. """,
    )
    shortNames: List[str] = Field(
        default=None,
        description=r""" shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase. """,
    )
    singular: str = Field(
        default=None,
        description=r""" singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`. """,
    )


class CustomResourceDefinitionVersion(BaseModel):
    additionalPrinterColumns: List[CustomResourceColumnDefinition] = Field(
        default=None,
        description=r""" additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. """,
    )
    deprecated: bool = Field(
        default=None,
        description=r""" deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false. """,
    )
    deprecationWarning: str = Field(
        default=None,
        description=r""" deprecationWarning overrides the default warning returned to API clients. May only be set when `deprecated` is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists. """,
    )
    name: str = Field(
        default=None,
        description=r""" name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true. """,
    )
    schema: CustomResourceValidation = Field(
        default=None,
        description=r""" schema describes the schema used for validation, pruning, and defaulting of this version of the custom resource. """,
    )
    served: bool = Field(
        default=None,
        description=r""" served is a flag enabling/disabling this version from being served via REST APIs """,
    )
    storage: bool = Field(
        default=None,
        description=r""" storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true. """,
    )
    subresources: CustomResourceSubresources = Field(
        default=None,
        description=r""" subresources specify what subresources this version of the defined custom resource have. """,
    )


class CustomResourceSubresourceScale(BaseModel):
    labelSelectorPath: str = Field(
        default=None,
        description=r""" labelSelectorPath defines the JSON path inside of a custom resource that corresponds to Scale `status.selector`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status` or `.spec`. Must be set to work with HorizontalPodAutoscaler. The field pointed by this JSON path must be a string field (not a complex selector struct) which contains a serialized label selector in string form. More info: https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions#scale-subresource If there is no value under the given path in the custom resource, the `status.selector` value in the `/scale` subresource will default to the empty string. """,
    )
    specReplicasPath: str = Field(
        default=None,
        description=r""" specReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `spec.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.spec`. If there is no value under the given path in the custom resource, the `/scale` subresource will return an error on GET. """,
    )
    statusReplicasPath: str = Field(
        default=None,
        description=r""" statusReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `status.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status`. If there is no value under the given path in the custom resource, the `status.replicas` value in the `/scale` subresource will default to 0. """,
    )


class CustomResourceSubresourceStatus(BaseModel):
    pass


class CustomResourceSubresources(BaseModel):
    scale: CustomResourceSubresourceScale = Field(
        default=None,
        description=r""" scale indicates the custom resource should serve a `/scale` subresource that returns an `autoscaling/v1` Scale object. """,
    )
    status: CustomResourceSubresourceStatus = Field(
        default=None,
        description=r""" status indicates the custom resource should serve a `/status` subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the `status` stanza of the object. 2. requests to the custom resource `/status` subresource ignore changes to anything other than the `status` stanza of the object. """,
    )


class CustomResourceValidation(BaseModel):
    openAPIV3Schema: JSONSchemaProps = Field(
        default=None,
        description=r""" openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning. """,
    )


class ExternalDocumentation(BaseModel):
    description: str = Field(default=None, description=r"""  """)
    url: str = Field(default=None, description=r"""  """)


class JSON(BaseModel):
    pass


class JSONSchemaProps(BaseModel):
    ref: str = Field(default=None, description=r"""  """, alias="$ref")
    schema: str = Field(default=None, description=r"""  """, alias="$schema")
    additionalItems: JSONSchemaPropsOrBool = Field(default=None, description=r"""  """)
    additionalProperties: JSONSchemaPropsOrBool = Field(
        default=None, description=r"""  """
    )
    allOf: List[JSONSchemaProps] = Field(default=None, description=r"""  """)
    anyOf: List[JSONSchemaProps] = Field(default=None, description=r"""  """)
    default: JSON = Field(
        default=None,
        description=r""" default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. Defaulting requires spec.preserveUnknownFields to be false. """,
    )
    definitions: dict = Field(default=None, description=r"""  """)
    dependencies: dict = Field(default=None, description=r"""  """)
    description: str = Field(default=None, description=r"""  """)
    enum: List[JSON] = Field(default=None, description=r"""  """)
    example: JSON = Field(default=None, description=r"""  """)
    exclusiveMaximum: bool = Field(default=None, description=r"""  """)
    exclusiveMinimum: bool = Field(default=None, description=r"""  """)
    externalDocs: ExternalDocumentation = Field(default=None, description=r"""  """)
    format: str = Field(
        default=None,
        description=r""" format is an OpenAPI v3 format string. Unknown formats are ignored. The following formats are validated:  - bsonobjectid: a bson object ID, i.e. a 24 characters hex string - uri: an URI as parsed by Golang net/url.ParseRequestURI - email: an email address as parsed by Golang net/mail.ParseAddress - hostname: a valid representation for an Internet host name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid3: an UUID3 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid4: an UUID4 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - uuid5: an UUID5 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - isbn: an ISBN10 or ISBN13 number string like "0321751043" or "978-0321751041" - isbn10: an ISBN10 number string like "0321751043" - isbn13: an ISBN13 number string like "978-0321751041" - creditcard: a credit card number defined by the regex ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$ with any non digit characters mixed in - ssn: a U.S. social security number following the regex ^\d{3}[- ]?\d{2}[- ]?\d{4}$ - hexcolor: an hexadecimal color code like "#FFFFFF: following the regex ^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb like "rgb(255,255,2559" - byte: base64 encoded binary data - password: any kind of string - date: a date string like "2006-01-02" as defined by full-date in RFC3339 - duration: a duration string like "22 ns" as parsed by Golang time.ParseDuration or compatible with Scala duration format - datetime: a date time string like "2014-12-15T19:30:20.000Z" as defined by date-time in RFC3339. """,
    )
    id: str = Field(default=None, description=r"""  """)
    items: JSONSchemaPropsOrArray = Field(default=None, description=r"""  """)
    maxItems: int = Field(default=None, description=r"""  """)
    maxLength: int = Field(default=None, description=r"""  """)
    maxProperties: int = Field(default=None, description=r"""  """)
    maximum: float = Field(default=None, description=r"""  """)
    minItems: int = Field(default=None, description=r"""  """)
    minLength: int = Field(default=None, description=r"""  """)
    minProperties: int = Field(default=None, description=r"""  """)
    minimum: float = Field(default=None, description=r"""  """)
    multipleOf: float = Field(default=None, description=r"""  """)
    nay: JSONSchemaProps = Field(default=None, description=r"""  """, alias="not")
    nullable: bool = Field(default=None, description=r"""  """)
    oneOf: List[JSONSchemaProps] = Field(default=None, description=r"""  """)
    pattern: str = Field(default=None, description=r"""  """)
    patternProperties: dict = Field(default=None, description=r"""  """)
    properties: dict = Field(default=None, description=r"""  """)
    required: List[str] = Field(default=None, description=r"""  """)
    title: str = Field(default=None, description=r"""  """)
    type: str = Field(default=None, description=r"""  """)
    uniqueItems: bool = Field(default=None, description=r"""  """)
    x_kubernetes_embedded_resource: bool = Field(
        default=None,
        description=r""" x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata). """,
        alias="x-kubernetes-embedded-resource",
    )
    x_kubernetes_int_or_string: bool = Field(
        default=None,
        description=r""" x_kubernetes_int_or_string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:  1) anyOf:    _ type: integer    _ type: string 2) allOf:    _ anyOf:      _ type: integer      _ type: string    _ ... zero or more """,
        alias="x_kubernetes_int_or_string",
    )
    x_kubernetes_list_map_keys: List[str] = Field(
        default=None,
        description=r""" x_kubernetes_list_map_keys annotates an array with the x_kubernetes_list_type `map` by specifying the keys used as the index of the map.  This tag MUST only be used on lists that have the "x_kubernetes_list_type" extension set to "map". Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).  The properties specified must either be required or have a default value, to ensure those properties are present for all list items. """,
        alias="x_kubernetes_list_map_keys",
    )
    x_kubernetes_list_type: str = Field(
        default=None,
        description=r""" x_kubernetes_list_type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:  1) `atomic`: the list is treated as a single entity, like a scalar.      Atomic lists will be entirely replaced when updated. This extension      may be used on any type of list (struct, scalar, ...). 2) `set`:      Sets are lists that must not have multiple items with the same value. Each      value must be a scalar, an object with x_kubernetes_map_type `atomic` or an      array with x_kubernetes_list_type `atomic`. 3) `map`:      These lists are like maps in that their elements have a non_index key      used to identify them. Order is preserved upon merge. The map tag      must only be used on a list with elements of type object. Defaults to atomic for arrays. """,
        alias="x_kubernetes_list_type",
    )
    x_kubernetes_map_type: str = Field(
        default=None,
        description=r""" x_kubernetes_map_type annotates an object to further describe its topology. This extension must only be used when type is object and may have 2 possible values:  1) `granular`:      These maps are actual maps (key_value pairs) and each fields are independent      from each other (they can each be manipulated by separate actors). This is      the default behaviour for all maps. 2) `atomic`: the list is treated as a single entity, like a scalar.      Atomic maps will be entirely replaced when updated. """,
        alias="x_kubernetes_map_type",
    )
    x_kubernetes_preserve_unknown_fields: bool = Field(
        default=None,
        description=r""" x_kubernetes_preserve_unknown_fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden. """,
        alias="x_kubernetes_preserve_unknown_fields",
    )
    x_kubernetes_validations: List[ValidationRule] = Field(
        default=None,
        description=r""" x_kubernetes_validations describes a list of validation rules written in the CEL expression language. This field is an alpha_level. Using this field requires the feature gate `CustomResourceValidationExpressions` to be enabled. """,
        alias="x_kubernetes_validations",
    )


class JSONSchemaPropsOrArray(BaseModel):
    pass


class JSONSchemaPropsOrBool(BaseModel):
    pass


class ValidationRule(BaseModel):
    fieldPath: str = Field(
        default=None,
        description=r""" fieldPath represents the field path returned when the validation fails. It must be a relative JSON path (i.e. with array notation) scoped to the location of this x-kubernetes-validations extension in the schema and refer to an existing field. e.g. when validation checks if a specific attribute `foo` under a map `testMap`, the fieldPath could be set to `.testMap.foo` If the validation checks two lists must have unique attributes, the fieldPath could be set to either of the list: e.g. `.testList` It does not support list numeric index. It supports child operation to refer to an existing field currently. Refer to [JSONPath support in Kubernetes](https://kubernetes.io/docs/reference/kubectl/jsonpath/) for more info. Numeric index of array is not supported. For field name which contains special characters, use `['specialName']` to refer the field name. e.g. for attribute `foo.34$` appears in a list `testList`, the fieldPath could be set to `.testList['foo.34$']` """,
    )
    message: str = Field(
        default=None,
        description=r""" Message represents the message displayed when validation fails. The message is required if the Rule contains line breaks. The message must not contain line breaks. If unset, the message is "failed rule: {Rule}". e.g. "must be a URL with the host matching spec.host" """,
    )
    messageExpression: str = Field(
        default=None,
        description=r""" MessageExpression declares a CEL expression that evaluates to the validation failure message that is returned when this rule fails. Since messageExpression is used as a failure message, it must evaluate to a string. If both message and messageExpression are present on a rule, then messageExpression will be used if validation fails. If messageExpression results in a runtime error, the runtime error is logged, and the validation failure message is produced as if the messageExpression field were unset. If messageExpression evaluates to an empty string, a string with only spaces, or a string that contains line breaks, then the validation failure message will also be produced as if the messageExpression field were unset, and the fact that messageExpression produced an empty string/string with only spaces/string with line breaks will be logged. messageExpression has access to all the same variables as the rule; the only difference is the return type. Example: "x must be less than max ("+string(self.max)+")" """,
    )
    reason: str = Field(
        default=None,
        description=r""" reason provides a machine-readable validation failure reason that is returned to the caller when a request fails this validation rule. The HTTP status code returned to the caller will match the reason of the reason of the first failed validation rule. The currently supported reasons are: "FieldValueInvalid", "FieldValueForbidden", "FieldValueRequired", "FieldValueDuplicate". If not set, default to use "FieldValueInvalid". All future added reasons must be accepted by clients when reading this value and unknown reasons should be treated as FieldValueInvalid. """,
    )
    rule: str = Field(
        default=None,
        description=r""" Rule represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec The Rule is scoped to the location of the x-kubernetes-validations extension in the schema. The `self` variable in the CEL expression is bound to the scoped value. Example: - Rule scoped to the root of a resource with a status subresource: {"rule": "self.status.actual <= self.spec.maxDesired"}  If the Rule is scoped to an object with properties, the accessible properties of the object are field selectable via `self.field` and field presence can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL expressions. If the Rule is scoped to an object with additionalProperties (i.e. a map) the value of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self` and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`. If the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by macros and functions. If the Rule is scoped to a scalar, `self` is bound to the scalar value. Examples: - Rule scoped to a map of objects: {"rule": "self.components['Widget'].priority < 10"} - Rule scoped to a list of integers: {"rule": "self.values.all(value, value >= 0 && value < 100)"} - Rule scoped to a string value: {"rule": "self.startsWith('kube')"}  The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object and from any x-kubernetes-embedded-resource annotated objects. No other metadata properties are accessible.  Unknown data preserved in custom resources via x-kubernetes-preserve-unknown-fields is not accessible in CEL expressions. This includes: - Unknown field values that are preserved by object schemas with x-kubernetes-preserve-unknown-fields. - Object properties where the property schema is of an "unknown type". An "unknown type" is recursively defined as:   - A schema with no type and x-kubernetes-preserve-unknown-fields set to true   - An array where the items schema is of an "unknown type"   - An object where the additionalProperties schema is of an "unknown type"  Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are: 	  "true", "false", "null", "in", "as", "break", "const", "continue", "else", "for", "function", "if", 	  "import", "let", "loop", "package", "namespace", "return". Examples:   - Rule accessing a property named "namespace": {"rule": "self.__namespace__ > 0"}   - Rule accessing a property named "x-prop": {"rule": "self.x__dash__prop > 0"}   - Rule accessing a property named "redact__d": {"rule": "self.redact__underscores__d > 0"}  Equality on arrays with x-kubernetes-list-type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and     non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values     are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with     non-intersecting keys are appended, retaining their partial order. """,
    )


class WebhookConversion(BaseModel):
    clientConfig: WebhookClientConfig = Field(
        default=None,
        description=r""" clientConfig is the instructions for how to call the webhook if strategy is `Webhook`. """,
    )
    conversionReviewVersions: List[str] = Field(
        default=None,
        description=r""" conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. """,
    )
