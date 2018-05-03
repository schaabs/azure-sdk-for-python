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


class DatabaseAccountConnectionString(Model):
    """Connection string for the Cosmos DB account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar connection_string: Value of the connection string
    :vartype connection_string: str
    :ivar description: Description of the connection string
    :vartype description: str
    """

    _validation = {
        'connection_string': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'connection_string': {'key': 'connectionString', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self):
        super(DatabaseAccountConnectionString, self).__init__()
        self.connection_string = None
        self.description = None
