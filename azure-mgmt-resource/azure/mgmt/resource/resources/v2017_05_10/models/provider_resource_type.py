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


class ProviderResourceType(Model):
    """Resource type managed by the resource provider.

    :param resource_type: The resource type.
    :type resource_type: str
    :param locations: The collection of locations where this resource type can
     be created.
    :type locations: list[str]
    :param aliases: The aliases that are supported by this resource type.
    :type aliases:
     list[~azure.mgmt.resource.resources.v2017_05_10.models.AliasType]
    :param api_versions: The API version.
    :type api_versions: list[str]
    :param properties: The properties.
    :type properties: dict[str, str]
    """

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'aliases': {'key': 'aliases', 'type': '[AliasType]'},
        'api_versions': {'key': 'apiVersions', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, resource_type=None, locations=None, aliases=None, api_versions=None, properties=None):
        super(ProviderResourceType, self).__init__()
        self.resource_type = resource_type
        self.locations = locations
        self.aliases = aliases
        self.api_versions = api_versions
        self.properties = properties
