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


class ImageUrl(Model):
    """Image url.

    All required parameters must be populated in order to send to Azure.

    :param url: Required. Url of the image.
    :type url: str
    """

    _validation = {
        'url': {'required': True},
    }

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, *, url: str, **kwargs) -> None:
        super(ImageUrl, self).__init__(**kwargs)
        self.url = url
