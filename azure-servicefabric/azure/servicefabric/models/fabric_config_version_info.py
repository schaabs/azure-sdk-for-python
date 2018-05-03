# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FabricConfigVersionInfo(Model):
    """Information about a Service Fabric config version.

    :param config_version: The config version of Service Fabric.
    :type config_version: str
    """

    _attribute_map = {
        'config_version': {'key': 'ConfigVersion', 'type': 'str'},
    }

    def __init__(self, config_version=None):
        super(FabricConfigVersionInfo, self).__init__()
        self.config_version = config_version
