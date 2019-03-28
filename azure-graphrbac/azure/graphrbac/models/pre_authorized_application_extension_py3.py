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


class PreAuthorizedApplicationExtension(Model):
    """Representation of an app PreAuthorizedApplicationExtension required by a
    pre authorized client app.

    :param conditions: The extension's conditions.
    :type conditions: list[str]
    """

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[str]'},
    }

    def __init__(self, *, conditions=None, **kwargs) -> None:
        super(PreAuthorizedApplicationExtension, self).__init__(**kwargs)
        self.conditions = conditions
