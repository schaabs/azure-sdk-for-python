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


class Sku(Model):
    """SKU parameters supplied to the create namespace operation.

    :param name: Name of this SKU. Possible values include: 'Basic',
     'Standard'
    :type name: str or ~azure.mgmt.eventhub.models.SkuName
    :param tier: The billing tier of this particular SKU. Possible values
     include: 'Basic', 'Standard'
    :type tier: str or ~azure.mgmt.eventhub.models.SkuTier
    :param capacity: The Event Hubs throughput units, vaule should be 0 to 20
     throughput units.
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
        'capacity': {'maximum': 20, 'minimum': 0},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, name, tier=None, capacity=None):
        super(Sku, self).__init__()
        self.name = name
        self.tier = tier
        self.capacity = capacity
