from pydantic import Field

from k8s_models.models import KubeModel


class ObjectReference(KubeModel):
    apiVersion: str = Field(default="v1", description=r""" API version of the referent. """)
    fieldPath: str = Field(default=None, description=r""" If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. """)
    kind: str = Field(default="ObjectReference", description=r""" Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """)
    name: str = Field(default=None, description=r""" Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """)
    namespace: str = Field(default=None, description=r""" Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ """)
    resourceVersion: str = Field(default=None, description=r""" Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency """)
    uid: str = Field(default=None, description=r""" UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids """)
