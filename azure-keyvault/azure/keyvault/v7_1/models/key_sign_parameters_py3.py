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


class KeySignParameters(Model):
    """The key operations parameters.

    All required parameters must be populated in order to send to Azure.

    :param algorithm: Required. The signing/verification algorithm identifier.
     For more information on possible algorithm types, see
     JsonWebKeySignatureAlgorithm. Possible values include: 'PS256', 'PS384',
     'PS512', 'RS256', 'RS384', 'RS512', 'RSNULL', 'ES256', 'ES384', 'ES512',
     'ES256K'
    :type algorithm: str or
     ~azure.keyvault.v7_1.models.JsonWebKeySignatureAlgorithm
    :param value: Required.
    :type value: bytes
    """

    _validation = {
        'algorithm': {'required': True, 'min_length': 1},
        'value': {'required': True},
    }

    _attribute_map = {
        'algorithm': {'key': 'alg', 'type': 'str'},
        'value': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, *, algorithm, value: bytes, **kwargs) -> None:
        super(KeySignParameters, self).__init__(**kwargs)
        self.algorithm = algorithm
        self.value = value
