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


class SubscriptionOperationListResult(Model):
    """A list of pending subscription operations.

    :param value: A list of pending SubscriptionOperations
    :type value: list[~azure.mgmt.subscription.models.SubscriptionOperation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SubscriptionOperation]'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionOperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
