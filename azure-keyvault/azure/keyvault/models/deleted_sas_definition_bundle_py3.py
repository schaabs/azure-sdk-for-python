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

from .sas_definition_bundle import SasDefinitionBundle


class DeletedSasDefinitionBundle(SasDefinitionBundle):
    """A deleted SAS definition bundle consisting of its previous id, attributes
    and its tags, as well as information on when it will be purged.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The SAS definition id.
    :vartype id: str
    :ivar secret_id: Storage account SAS definition secret id.
    :vartype secret_id: str
    :ivar template_uri: The SAS definition token template signed with an
     arbitrary key.  Tokens created according to the SAS definition will have
     the same properties as the template.
    :vartype template_uri: str
    :ivar sas_type: The type of SAS token the SAS definition will create.
     Possible values include: 'account', 'service'
    :vartype sas_type: str or ~azure.keyvault.models.SasTokenType
    :ivar validity_period: The validity period of SAS tokens created according
     to the SAS definition.
    :vartype validity_period: str
    :ivar attributes: The SAS definition attributes.
    :vartype attributes: ~azure.keyvault.models.SasDefinitionAttributes
    :ivar tags: Application specific metadata in the form of key-value pairs
    :vartype tags: dict[str, str]
    :param recovery_id: The url of the recovery object, used to identify and
     recover the deleted SAS definition.
    :type recovery_id: str
    :ivar scheduled_purge_date: The time when the SAS definition is scheduled
     to be purged, in UTC
    :vartype scheduled_purge_date: datetime
    :ivar deleted_date: The time when the SAS definition was deleted, in UTC
    :vartype deleted_date: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'secret_id': {'readonly': True},
        'template_uri': {'readonly': True},
        'sas_type': {'readonly': True},
        'validity_period': {'readonly': True},
        'attributes': {'readonly': True},
        'tags': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'secret_id': {'key': 'sid', 'type': 'str'},
        'template_uri': {'key': 'templateUri', 'type': 'str'},
        'sas_type': {'key': 'sasType', 'type': 'str'},
        'validity_period': {'key': 'validityPeriod', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'SasDefinitionAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(self, *, recovery_id: str=None, **kwargs) -> None:
        super(DeletedSasDefinitionBundle, self).__init__(, **kwargs)
        self.recovery_id = recovery_id
        self.scheduled_purge_date = None
        self.deleted_date = None
