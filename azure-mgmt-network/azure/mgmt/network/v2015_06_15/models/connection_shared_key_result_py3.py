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


class ConnectionSharedKeyResult(Model):
    """Response for CheckConnectionSharedKey Api servive call.

    :param value: The virtual network connection shared key value
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, value: str=None, **kwargs) -> None:
        super(ConnectionSharedKeyResult, self).__init__(**kwargs)
        self.value = value
