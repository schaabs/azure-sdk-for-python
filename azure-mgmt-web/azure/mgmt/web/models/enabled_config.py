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


class EnabledConfig(Model):
    """Enabled configuration.

    :param enabled: True if configuration is enabled, false if it is disabled
     and null if configuration is not set.
    :type enabled: bool
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    def __init__(self, enabled=None):
        super(EnabledConfig, self).__init__()
        self.enabled = enabled
