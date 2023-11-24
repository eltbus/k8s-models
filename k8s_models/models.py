from pydantic import BaseModel

from yaml import safe_dump

class KubeModel(BaseModel):

    def model_to_yaml(self):
        model_data = self.model_dump(by_alias=True, exclude_none=True)
        return safe_dump(
            data=model_data,
            sort_keys=False,
            default_flow_style=False,
            indent=2,
            allow_unicode=True,
            explicit_start=True
        )