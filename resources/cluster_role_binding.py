# -*- coding: utf-8 -*-

from .resource import Resource


class ClusterRoleBinding(Resource):
    """
    ClusterRoleBinding object.
    """

    api_group = Resource.ApiGroup.RBAC_AUTHORIZATION_K8S_IO
