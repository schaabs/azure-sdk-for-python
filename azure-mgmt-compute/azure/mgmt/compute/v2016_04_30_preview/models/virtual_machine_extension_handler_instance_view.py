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


class VirtualMachineExtensionHandlerInstanceView(Model):
    """The instance view of a virtual machine extension handler.

    :param type: Specifies the type of the extension; an example is
     "CustomScriptExtension".
    :type type: str
    :param type_handler_version: Specifies the version of the script handler.
    :type type_handler_version: str
    :param status: The extension handler status.
    :type status:
     ~azure.mgmt.compute.v2016_04_30_preview.models.InstanceViewStatus
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'type_handler_version': {'key': 'typeHandlerVersion', 'type': 'str'},
        'status': {'key': 'status', 'type': 'InstanceViewStatus'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineExtensionHandlerInstanceView, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.type_handler_version = kwargs.get('type_handler_version', None)
        self.status = kwargs.get('status', None)
