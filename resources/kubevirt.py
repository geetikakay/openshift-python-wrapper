from .resource import NamespacedResource


class KubeVirt(NamespacedResource):
    api_group = NamespacedResource.ApiGroup.KUBEVIRT_IO
