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


class KeyItem(Model):
    """The key item containing key metadata.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param kid: Key identifier.
    :type kid: str
    :param attributes: The key management attributes.
    :type attributes: ~azure.keyvault.v7_1.models.KeyAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    :ivar managed: True if the key's lifetime is managed by key vault. If this
     is a key backing a certificate, then managed will be true.
    :vartype managed: bool
    """

    _validation = {
        'managed': {'readonly': True},
    }

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed': {'key': 'managed', 'type': 'bool'},
    }

    def __init__(self, *, kid: str=None, attributes=None, tags=None, **kwargs) -> None:
        super(KeyItem, self).__init__(**kwargs)
        self.kid = kid
        self.attributes = attributes
        self.tags = tags
        self.managed = None
