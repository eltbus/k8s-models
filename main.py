from __future__ import annotations

from pathlib import Path
from typing import List, Iterator, Optional
import re

from bs4 import BeautifulSoup, Tag
# from inflection import underscore
from pydantic import BaseModel, Field


def is_apis_div(element) -> bool:
    return element.name == "div" and element.get("id", "").endswith("-apis")


def is_definition_div(element) -> bool:
    return element.name == "div" and element.get("id") == "definitions"


def is_deprecated_div(element) -> bool:
    return element.name == "div" and element.get("id") == "old-api-versions"


def is_resource_container_div(element) -> bool:
    return element.name == "div" and "resource-container" in element.get("class", [])


def is_params_table(element) -> bool:
    return element.name == "table" and "col-md-8" not in element.get("class", [])


def is_inline_definition_container_div(element) -> bool:
    return element.name == "div" and "inline-definitions-container" in element.get(
        "class", []
    )


def is_inline_definition_h3(element) -> bool:
    return element.name == "h3" and "inline-definition" in element.get("class", [])


def is_definition_container_div(element) -> bool:
    return element.name == "div" and "definition-container" in element.get("class", [])


def is_api_div(element) -> bool:
    return (
        is_apis_div(element) or is_definition_div(element) or is_deprecated_div(element)
    )


def is_resource_div(element) -> bool:
    return (
        is_resource_container_div(element)
        or is_inline_definition_container_div(element)
        or is_definition_container_div(element)
    )


def is_handled_div(element) -> bool:
    return is_api_div(element) or is_resource_div(element)


def gen_api_tags(soup: BeautifulSoup) -> Iterator[Tag]:
    "There can be multiple api tags"
    for tag in soup.find_all(lambda element: is_apis_div(element)):
        if isinstance(tag, Tag):
            yield tag


def gen_definition_tags(soup: BeautifulSoup) -> Iterator[Tag]:
    "There should be only ONE definition tag"
    for tag in soup.find_all(lambda element: is_definition_div(element)):
        if isinstance(tag, Tag):
            yield tag


def map_kind_to_type(kind: str) -> str:
    match kind:
        case "array":
            return "List"
        case "boolean":
            return "bool"
        case "integer":
            return "int"
        case "number":
            return "float"
        case "object":
            return "dict"
        case "string":
            return "str"
        case "":
            return "Any"
        case _:
            return kind


def convert_invalid_parameter_name(name: str) -> str:
    match name:
        # Python reserved words
        case "continue":
            return "keep_on"
        case "except":
            return "besides"
        case "from":
            return "sources"
        case "not":
            return "nay"
        # Pydantic reserved words (mypy complains)
        case "schema":
            return "validation_schema"
        # Invalid starting character
        case "$ref":
            return "json_schema_ref"
        case "$schema":
            return "json_schema_uri"
        # Invalid hyphens
        case "x-kubernetes-embedded-resource":
            return "x_kubernetes_embedded_resource"
        case "x-kubernetes-int-or-string":
            return "x_kubernetes_int_or_string"
        case "x-kubernetes-list-map-keys":
            return "x_kubernetes_list_map_keys"
        case "x-kubernetes-list-type":
            return "x_kubernetes_list_type"
        case "x-kubernetes-map-type":
            return "x_kubernetes_map_type"
        case "x-kubernetes-preserve-unknown-fields":
            return "x_kubernetes_preserve_unknown_fields"
        case "x-kubernetes-validations":
            return "x_kubernetes_validations"
        case _:
            return name


class Parameter(BaseModel):
    name: str
    kind: str
    description: str

    @classmethod
    def from_tr_tag(cls, tag: Tag) -> Parameter:
        if isinstance(tag, Tag):
            col_tags = tag.find_all("td")
            name_tag = col_tags[0].find("code")
            name = (
                name_tag.get_text()
                if isinstance(name_tag, Tag) and name_tag is not None
                else ""
            )
            kind_tag = col_tags[0].find("i")
            kind = (
                kind_tag.get_text()
                if isinstance(kind_tag, Tag) and kind_tag is not None
                else ""
            )
            description = col_tags[1].get_text().strip()
        return cls(name=name, kind=kind, description=description)

    def repr_as_pydantic_field(
        self,
        resource_kind: Optional[str] = None,
        resource_version: Optional[str] = None,
    ):
        parts = [map_kind_to_type(self) for self in self.kind.split(" ")]
        field_type = f"{parts[1]}[{parts[0]}]" if len(parts) == 2 else parts[0]
        field_arg_list = []

        if self.name == "apiVersion":
            field_arg_list.append(f'default="{resource_version}"')
        elif self.name == "kind":
            field_arg_list.append(f'default="{resource_kind}"')
        else:
            field_arg_list.append('default=None')

        # Append alias if needed
        if self.name != self.valid_name:
            field_arg_list.append(f'alias="{self.name}"')

        if self.description:
            field_arg_list.append(f'description=r""" {self.description} """')

        field_args = ", ".join(field_arg_list)
        result = f"{self.valid_name}: {field_type} = Field({field_args})"
        return result

    @property
    def valid_name(self):
        return convert_invalid_parameter_name(self.name)


class Resource(BaseModel):
    kind: str
    version: str
    group: str
    parameters: List[Parameter] = Field(default_factory=list)

    @classmethod
    def from_resource_container_tag(cls, tag: Tag) -> Resource:
        kind_tag = tag.find("span", class_="k")
        kind = (
            kind_tag.get_text()
            if isinstance(kind_tag, Tag) and kind_tag is not None
            else ""
        )

        version_tag = tag.find("span", class_="v")
        version = (
            version_tag.get_text()
            if isinstance(version_tag, Tag) and version_tag is not None
            else ""
        )

        group_tag = tag.find("span", class_="g")
        group = (
            group_tag.get_text()
            if isinstance(group_tag, Tag) and group_tag is not None
            else ""
        )

        parameters = []
        table_tag = tag.find(is_params_table)
        if isinstance(table_tag, Tag):
            tbody_tag = table_tag.find("tbody")
            if isinstance(tbody_tag, Tag):
                for row_tag in tbody_tag.find_all("tr"):
                    parameters.append(Parameter.from_tr_tag(row_tag))
        return cls(kind=kind, version=version, group=group, parameters=parameters)

    @classmethod
    def from_inline_definition_tag(cls, tag: Tag) -> Resource:
        kind, version, group = (
            tag.get_text().split(" ")
            if isinstance(tag, Tag)
            and tag is not None
            else ""
        )
        parameters = []
        table_tag = tag.find_next_sibling("table")
        if isinstance(table_tag, Tag):
            tbody_tag = table_tag.find("tbody")
            if isinstance(tbody_tag, Tag):
                for row_tag in tbody_tag.find_all("tr"):
                    parameters.append(Parameter.from_tr_tag(row_tag))
        return cls(kind=kind, version=version, group=group, parameters=parameters)

    def repr_as_pydantic_model(self) -> str:
        fields = [
            parameter.repr_as_pydantic_field(
                resource_kind=self.kind, resource_version=self.version
            )
            for parameter in self.parameters
        ]
        # Calculate head
        match_api_version = any(re.search("apiVersion", field) for field in fields)
        match_kind = any(re.search("kind", field) for field in fields)
        if match_api_version and match_kind:
            head = f"class {self.kind}(KubeModel):\n"
        else:
            head = f"class {self.kind}(BaseModel):\n"

        # Calculate body
        if not fields:
            body = " " * 4 + "pass\n"
        else:
            fields_with_indentation = [" " * 4 + field for field in fields]
            body = "\n".join(fields_with_indentation)
        return head + body

    @property
    def submodule_name(self):
        return self.group.replace(".", "_")

    def create_submodule(self, module_path: Path) -> Path:
        # Create submodule folder
        submodule_path = module_path / self.submodule_name
        submodule_path.mkdir(parents=True, exist_ok=True)

        # Init submodule
        submodule_init_file_path = submodule_path / "__init__.py"
        submodule_init_file_path.touch(exist_ok=True)

        return submodule_path


class API(BaseModel):
    name: str
    description: str
    resources: List[Resource] = Field(default_factory=list)

    @classmethod
    def from_api_tag(cls, tag: Tag) -> API:
        name_tag = tag.find("h1")
        name = name_tag.get_text() if name_tag is not None else ""

        description_tag = tag.find("p")
        description = (
            description_tag.get_text().replace("\n", " ")
            if description_tag is not None
            else ""
        )

        resources = []

        while (next_element := tag.find_next_sibling(is_handled_div)) is not None:
            if not isinstance(next_element, Tag):
                break
            tag = next_element

            if is_resource_container_div(tag):
                resources.append(Resource.from_resource_container_tag(tag))

                for inline_definition_container_tag in tag.find_all(
                    is_inline_definition_container_div
                ):
                    for inline_definition_tag in inline_definition_container_tag.find_all(is_inline_definition_h3):
                        result = Resource.from_inline_definition_tag(
                            inline_definition_tag
                        )
                        resources.append(result)
                continue

            if is_definition_container_div(tag):
                name_tag = tag.find("h2")
                name = name_tag.get_text() if name_tag is not None else ""

            if is_api_div(tag) or is_definition_div(tag):
                break

            if is_deprecated_div(tag):
                break

        return cls(name=name, description=description, resources=resources)

    @property
    def module_name(self):
        return self.name.lower().replace(" ", "_").replace("&", "and")

    def create_module(self, package_path: Path) -> Path:
        # Create module folder
        module_path = package_path / self.module_name
        module_path.mkdir(parents=True, exist_ok=True)

        # Init module
        module_init_filepath = module_path / "__init__.py"
        module_init_filepath.touch(exist_ok=True)

        return module_path



def gen_apis_from_kubernetes_docs(soup: BeautifulSoup) -> Iterator[API]:
    api_tags = soup.find_all("div", attrs={"id": lambda x: x and x.endswith("-apis")})
    apis = map(lambda x: API.from_api_tag(x), api_tags)
    for api in apis:
        yield api


def gen_definitions_from_kubernetes_docs(soup: BeautifulSoup) -> Iterator[Resource]:
    definition_tags = soup.find_all(is_definition_container_div)
    definitions = map(
        lambda x: Resource.from_resource_container_tag(x), definition_tags
    )
    for definition in definitions:
        yield definition


def gen_resources_from_kubernetes_docs(soup: BeautifulSoup) -> Iterator[Resource]:
    for api in gen_apis_from_kubernetes_docs(soup):
        for resource in api.resources:
            yield resource


def load_soup():
    with open("v1.28.html", "r") as f:
        html_doc = f.read()
    return BeautifulSoup(html_doc, "html.parser")


def main():
    # Parse soup
    soup: BeautifulSoup = load_soup()

    # Create package
    package_path = Path(__file__).parent / "k8s_models_info"
    package_path.mkdir(exist_ok=True)

    # Init package
    package_init_file_path = package_path / "__init__.py"
    package_init_file_path.touch(exist_ok=True)

    hidden_module_name = "_generated"
    hidden_module = package_path / f"{hidden_module_name}.py"
    with open(hidden_module, "w") as f:
        lines = [
            "from __future__ import annotations",
            "from typing import Any, List\n",
            "from pydantic import BaseModel, Field",
            "from yaml import safe_dump\n\n",
            "class KubeModel(BaseModel):",
            " " * 4 + "def model_to_yaml(self):",
            " " * 8 + "model_data = self.model_dump(by_alias=True, exclude_none=True)",
            " " * 8 + "return safe_dump(",
            " " * 12 + "data=model_data,",
            " " * 12 + "sort_keys=False,",
            " " * 12 + "default_flow_style=False,",
            " " * 12 + "indent=2,",
            " " * 12 + "allow_unicode=True,",
            " " * 12 + "explicit_start=True",
            " " * 8 + ")\n\n",
            "ScaleSpec = Any",
            "ScaleStatus = Any",
            "PodResourceClaimStatus = Any\n\n",
        ]
        f.write("\n".join(lines))

        resource = Resource.model_construct()

        for api in gen_apis_from_kubernetes_docs(soup):
            # Create module folder
            module_path = api.create_module(package_path=package_path)
            api_group_resource_dict = {}

            for resource in api.resources:
                # Create submodule
                submodule_path = resource.create_submodule(module_path=module_path)
                submodule_filepath = submodule_path / "__init__.py"

                # Store information to generate __init__ file imports
                (
                    api_group_resource_dict
                    .setdefault(submodule_filepath, [])
                    .append(resource.kind)
                )

                # Generate resource code and write it 
                f.write(f"\n{resource.repr_as_pydantic_model()}\n\n")
            else:
                # Generate __init__ file imports
                for submodule_filepath, resource_kinds in api_group_resource_dict.items():
                    with open(submodule_filepath, "w") as g:
                        # Write imports
                        for resource_kind in resource_kinds:
                            g.write(f"from {hidden_module_name} import {resource_kind}\n")

                        # Write __all__ variable
                        g.write(f"\n__all__ = [\n")
                        for resource_kind in resource_kinds:
                            g.write(f'    "{resource_kind}",\n')
                        g.write(f"]")

        # Create module folder
        module_path = package_path / "definitions"
        module_path.mkdir(parents=True, exist_ok=True)

        # Init module
        module_init_filepath = module_path / "__init__.py"
        module_init_filepath.touch(exist_ok=True)

        submodule_filepath = Path("")
        api_group_resource_dict = {}

        for definition in gen_definitions_from_kubernetes_docs(soup):
            # Create submodule
            submodule_path = definition.create_submodule(module_path=module_path)
            submodule_filepath = submodule_path / "__init__.py"

            # Store information to generate __init__ file imports
            (
                api_group_resource_dict
                .setdefault(submodule_filepath, [])
                .append(definition.kind)
            )

            # Generate resource code and write it 
            f.write(f"\n{definition.repr_as_pydantic_model()}\n\n")
        else:
            # # Generate __init__ file imports
            for submodule_filepath, resource_kinds in api_group_resource_dict.items():
                with open(submodule_filepath, "w") as g:
                    # Write imports
                    for resource_kind in resource_kinds:
                        g.write(f"from {hidden_module_name} import {resource_kind}\n")

                    # Write __all__ variable
                    g.write(f"\n__all__ = [\n")
                    for resource_kind in resource_kinds:
                        g.write(f'    "{resource_kind}",\n')
                    g.write(f"]")

if __name__ == "__main__":
    main()
