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


class PolicyDefinition(Model):
    """The policy definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param policy_type: The type of policy definition. Possible values are
     NotSpecified, BuiltIn, and Custom. Possible values include:
     'NotSpecified', 'BuiltIn', 'Custom'
    :type policy_type: str or
     ~azure.mgmt.resource.policy.v2016_12_01.models.PolicyType
    :param mode: The policy definition mode. Possible values are NotSpecified,
     Indexed, and All. Possible values include: 'NotSpecified', 'Indexed',
     'All'
    :type mode: str or
     ~azure.mgmt.resource.policy.v2016_12_01.models.PolicyMode
    :param display_name: The display name of the policy definition.
    :type display_name: str
    :param description: The policy definition description.
    :type description: str
    :param policy_rule: The policy rule.
    :type policy_rule: object
    :param metadata: The policy definition metadata.
    :type metadata: object
    :param parameters: Required if a parameter is used in policy rule.
    :type parameters: object
    :ivar id: The ID of the policy definition.
    :vartype id: str
    :ivar name: The name of the policy definition.
    :vartype name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'policy_rule': {'key': 'properties.policyRule', 'type': 'object'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, policy_type=None, mode=None, display_name=None, description=None, policy_rule=None, metadata=None, parameters=None):
        super(PolicyDefinition, self).__init__()
        self.policy_type = policy_type
        self.mode = mode
        self.display_name = display_name
        self.description = description
        self.policy_rule = policy_rule
        self.metadata = metadata
        self.parameters = parameters
        self.id = None
        self.name = None
