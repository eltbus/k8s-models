from pydantic import BaseModel, Field

from k8s_models.definitions.meta.label_selector import LabelSelector
from k8s_models.metadata.core.pod_template_spec import PodTemplateSpec
from k8s_models.definitions.apps.daemon_set_update_strategy import DaemonSetUpdateStrategy


class DaemonSetSpec(BaseModel):
    minReadySeconds: int = Field(default=None, description=r""" The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready). """)
    revisionHistoryLimit: int = Field(default=None, description=r""" The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. """)
    selector: LabelSelector = Field(default=None, description=r""" A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """)
    template: PodTemplateSpec = Field(default=None, description=r""" An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """)
    updateStrategy: DaemonSetUpdateStrategy = Field(default=None, description=r""" An update strategy to replace existing DaemonSet pods with new pods. """)
