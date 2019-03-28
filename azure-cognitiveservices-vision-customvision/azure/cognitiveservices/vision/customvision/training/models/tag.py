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


class Tag(Model):
    """Represents a Tag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Gets the Tag ID.
    :vartype id: str
    :param name: Required. Gets or sets the name of the tag.
    :type name: str
    :param description: Required. Gets or sets the description of the tag.
    :type description: str
    :param type: Required. Gets or sets the type of the tag. Possible values
     include: 'Regular', 'Negative'
    :type type: str or
     ~azure.cognitiveservices.vision.customvision.training.models.TagType
    :ivar image_count: Gets the number of images with this tag.
    :vartype image_count: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'description': {'required': True},
        'type': {'required': True},
        'image_count': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'image_count': {'key': 'imageCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(Tag, self).__init__(**kwargs)
        self.id = None
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.type = kwargs.get('type', None)
        self.image_count = None
