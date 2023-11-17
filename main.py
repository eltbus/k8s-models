from bs4 import BeautifulSoup, Tag
from dataclasses import dataclass
from typing import List, Optional, Iterator

def is_api_section(element):
    return element.get('id').endswith("-apis")

def is_definition_section(element):
    return element.get('id') == "definitions"

def is_deprecated_section(element):
    return element.get('id') == "old-api-versions"

def is_resource_container_section(element):
    return 'resource-container' in element.get('class', [])

def is_definition_container_section(element):
    return 'definition-container' in element.get('class', [])

def is_api_or_resource_or_definition_or_deprecated_section(element):
    """
    Used to ignore any other non-handled sections.
    """
    return (
        is_api_section(element)
        or is_definition_section(element)
        or is_deprecated_section(element)
        or is_resource_container_section(element)
        or is_definition_container_section(element)
    )

@dataclass
class Parameter: # Technically could be named Field
    name: str
    description: str

    @classmethod
    def from_tag(cls, tag: Tag):
        pass

@dataclass
class Resource:
    name: str
    group: str
    description: str
    parameters: Optional[List[Parameter]] = None

    @classmethod
    def from_tag(cls, tag: Tag):
        name_tag =  tag.find("h1")
        name = name_tag.get_text() if isinstance(name_tag, Tag) and name_tag is not None else ""

        group_class = name_tag.get("g") if isinstance(name_tag, Tag) and name_tag is not None else ""
        group = group_class if isinstance(group_class, str) else ""

        description_tag = tag.find("p")
        description = description_tag.get_text().replace("\n", " ") if isinstance(description_tag, Tag) and description_tag is not None else ""

        parameters = []

        while (next_element := tag.find_next_sibling(is_api_or_resource_or_definition_or_deprecated_section)) is not None:
            if not isinstance(next_element, Tag):
                break
            tag = next_element

            if is_resource_container_section(tag):
                parameters.append(Parameter.from_tag(tag))
                continue

            if is_definition_container_section(tag):
                name_tag =  tag.find("h2")
                name = name_tag.get_text() if name_tag is not None else ""
                print(f"\t - {name}")

            if is_api_section(tag) or is_definition_section(tag):
                break

            if is_deprecated_section(tag):
                break

        return cls(name=name, description=description, group=group)

@dataclass
class API:
    name: str
    description: str
    resources: Optional[List[Resource]] = None

    @classmethod
    def from_tag(cls, tag: Tag):
        name_tag =  tag.find("h1")
        name = name_tag.get_text() if name_tag is not None else ""

        description_tag = tag.find("p")
        description = description_tag.get_text().replace("\n", " ") if description_tag is not None else ""

        resources = []
        
        while (next_element := tag.find_next_sibling(is_api_or_resource_or_definition_or_deprecated_section)) is not None:
            if not isinstance(next_element, Tag):
                break
            tag = next_element

            if is_resource_container_section(tag):
                resources.append(Resource.from_tag(tag))
                continue

            if is_definition_container_section(tag):
                name_tag =  tag.find("h2")
                name = name_tag.get_text() if name_tag is not None else ""
                print(f"\t - {name}")

            if is_api_section(tag) or is_definition_section(tag):
                break

            if is_deprecated_section(tag):
                break

        return cls(name=name, description=description, resources=resources)

def gen_apis_from_kubernetes_docs(soup: BeautifulSoup) -> Iterator[API]:
    api_tags = soup.find_all("div", attrs={"id": lambda x: x and x.endswith("-apis")})
    apis = map(lambda x: API.from_tag(x), api_tags)
    for api in apis:
        yield api

if __name__ == "__main__":
    with open("v1.28.html", "r") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    print(next(gen_apis_from_kubernetes_docs(soup)))
