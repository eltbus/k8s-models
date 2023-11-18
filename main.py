from __future__ import annotations

from pathlib import Path
from typing import List, Iterator

from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel, Field

def is_apis_div(element) -> bool:
    return element.name == 'div' and element.get('id', '').endswith("-apis")

def is_definition_div(element) -> bool:
    return element.name == 'div' and element.get('id') == "definitions"

def is_deprecated_div(element) -> bool:
    return element.name == 'div' and element.get('id') == "old-api-versions"

def is_resource_container_div(element) -> bool:
    return element.name == 'div' and 'resource-container' in element.get('class', [])

"definition-container"
def is_params_table(element) -> bool:
    return element.name == 'table' and 'col-md-8' not in element.get('class', [])

def is_inline_definition_container_div(element) -> bool:
    return element.name == 'div' and 'inline-definitions-container' in element.get('class', [])

def is_inline_definition_h3(element) -> bool:
    return element.name == 'h3' and 'inline-definition' in element.get('class', [])

def is_definition_container_div(element) -> bool:
    return element.name == 'div' and 'definition-container' in element.get('class', [])

def is_api_div(element) -> bool:
    return (
        is_apis_div(element)
        or is_definition_div(element)
        or is_deprecated_div(element)
    )

def is_resource_div(element) -> bool:
    return (
        is_resource_container_div(element)
        or is_inline_definition_container_div(element)
        or is_definition_container_div(element)
    )

def is_handled_div(element) -> bool:
    return (
        is_api_div(element)
        or is_resource_div(element)
    )

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

class Parameter(BaseModel):
    name: str
    kind: str
    description: str

    @classmethod
    def from_tr_tag(cls, tag: Tag) -> Parameter:
        if isinstance(tag, Tag):
            col_tags = tag.find_all('td')
            name_tag = col_tags[0].find('code')
            name = name_tag.get_text() if isinstance(name_tag, Tag) and name_tag is not None else ""
            kind_tag = col_tags[0].find('i')
            kind = kind_tag.get_text() if isinstance(kind_tag, Tag) and kind_tag is not None else ""
            description = col_tags[1].get_text().strip()
        return cls(name=name, kind=kind, description=description)

class Resource(BaseModel):
    kind: str
    group: str
    parameters: List[Parameter] = Field(default_factory=list)

    @classmethod
    def from_resource_container_tag(cls, tag: Tag) -> Resource:
        kind_tag =  tag.find('span', class_='k')
        kind = kind_tag.get_text() if isinstance(kind_tag, Tag) and kind_tag is not None else ""

        group_tag =  tag.find('span', class_='g')
        group = group_tag.get_text() if isinstance(group_tag, Tag) and group_tag is not None else ""

        parameters = []
        table_tag = tag.find(is_params_table)
        if isinstance(table_tag, Tag):
            tbody_tag = table_tag.find("tbody")
            if isinstance(tbody_tag, Tag):
                for row_tag in tbody_tag.find_all("tr"):
                    parameters.append(Parameter.from_tr_tag(row_tag))
        return cls(kind=kind, group=group, parameters=parameters)

    @classmethod
    def from_inline_definition_container_tag(cls, tag: Tag) -> Resource:
        kind_group_tag =  tag.find(is_inline_definition_h3)
        kind, _, group = kind_group_tag.get_text().split(" ") if isinstance(kind_group_tag, Tag) and kind_group_tag is not None else ""
        table_tag = tag.find("tbody")
        parameters = []
        if isinstance(table_tag, Tag):
            for row_tag in table_tag.find_all("tr"):
                parameters.append(Parameter.from_tr_tag(row_tag))
        return cls(kind=kind, group=group, parameters=parameters)

class API(BaseModel):
    name: str
    description: str
    resources: List = Field(default_factory=list)

    @classmethod
    def from_api_tag(cls, tag: Tag) -> API:
        name_tag =  tag.find("h1")
        name = name_tag.get_text() if name_tag is not None else ""

        description_tag = tag.find("p")
        description = description_tag.get_text().replace("\n", " ") if description_tag is not None else ""

        resources = []
        
        while (next_element := tag.find_next_sibling(is_handled_div)) is not None:
            if not isinstance(next_element, Tag):
                break
            tag = next_element

            if is_resource_container_div(tag):
                resources.append(Resource.from_resource_container_tag(tag))

                for inline_definition_container_tag in tag.find_all(is_inline_definition_container_div):
                    result = Resource.from_inline_definition_container_tag(inline_definition_container_tag)
                    resources.append(result)
                continue

            if is_definition_container_div(tag):
                name_tag =  tag.find("h2")
                name = name_tag.get_text() if name_tag is not None else ""
                print(f"\t - {name}")

            if is_api_div(tag) or is_definition_div(tag):
                break

            if is_deprecated_div(tag):
                break

        return cls(name=name, description=description, resources=resources)

def gen_apis_from_kubernetes_docs(soup: BeautifulSoup) -> Iterator[API]:
    api_tags = soup.find_all("div", attrs={"id": lambda x: x and x.endswith("-apis")})
    apis = map(lambda x: API.from_api_tag(x), api_tags)
    for api in apis:
        yield api

def gen_definitions_from_kubernetes_docs(soup: BeautifulSoup) -> Iterator[Resource]:
    definition_tags = soup.find_all(is_definition_container_div)
    definitions = map(lambda x: Resource.from_resource_container_tag(x), definition_tags)
    for definition in definitions:
        yield definition

def gen_resources_from_kubernetes_docs(soup: BeautifulSoup) -> Iterator[Resource]:
    for api in gen_apis_from_kubernetes_docs(soup):
        for resource in api.resources:
            yield resource

def main():
    with open("v1.28.html", "r") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    # for api in gen_apis_from_kubernetes_docs(soup):
    #     print(api.name)
    #     for resource in api.resources:
    #         print(f"\t - {resource.kind}")
    #         for param in resource.parameters:
    #             print(f"\t\t - {param.name}: {param.description[:20]}...")
    #     print("=" * 120)
    for definition in gen_definitions_from_kubernetes_docs(soup):
        print(f"{definition.kind}")
        for param in definition.parameters:
            print(f"\t- {param.name}")

if __name__ == "__main__":
    root = Path(__file__).parent / "k8s_py"
    main()
