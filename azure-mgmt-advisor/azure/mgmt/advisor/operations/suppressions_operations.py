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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class SuppressionsOperations(object):
    """SuppressionsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: The version of the API to be used with the client request. Constant value: "2017-04-19".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2017-04-19"

        self.config = config

    def get(
            self, resource_uri, recommendation_id, name, custom_headers=None, raw=False, **operation_config):
        """Obtains the details of a suppression.

        :param resource_uri: The fully qualified Azure Resource Manager
         identifier of the resource to which the recommendation applies.
        :type resource_uri: str
        :param recommendation_id: The recommendation ID.
        :type recommendation_id: str
        :param name: The name of the suppression.
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SuppressionContract or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.advisor.models.SuppressionContract or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = '/{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name}'
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str'),
            'recommendationId': self._serialize.url("recommendation_id", recommendation_id, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SuppressionContract', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create(
            self, resource_uri, recommendation_id, name, suppression_id=None, ttl=None, custom_headers=None, raw=False, **operation_config):
        """Enables the snoozed or dismissed attribute of a recommendation. The
        snoozed or dismissed attribute is referred to as a suppression. Use
        this API to create or update the snoozed or dismissed status of a
        recommendation.

        :param resource_uri: The fully qualified Azure Resource Manager
         identifier of the resource to which the recommendation applies.
        :type resource_uri: str
        :param recommendation_id: The recommendation ID.
        :type recommendation_id: str
        :param name: The name of the suppression.
        :type name: str
        :param suppression_id: The GUID of the suppression.
        :type suppression_id: str
        :param ttl: The duration for which the suppression is valid.
        :type ttl: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SuppressionContract or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.advisor.models.SuppressionContract or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        suppression_contract = models.SuppressionContract(suppression_id=suppression_id, ttl=ttl)

        # Construct URL
        url = '/{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name}'
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str'),
            'recommendationId': self._serialize.url("recommendation_id", recommendation_id, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(suppression_contract, 'SuppressionContract')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SuppressionContract', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete(
            self, resource_uri, recommendation_id, name, custom_headers=None, raw=False, **operation_config):
        """Enables the activation of a snoozed or dismissed recommendation. The
        snoozed or dismissed attribute of a recommendation is referred to as a
        suppression.

        :param resource_uri: The fully qualified Azure Resource Manager
         identifier of the resource to which the recommendation applies.
        :type resource_uri: str
        :param recommendation_id: The recommendation ID.
        :type recommendation_id: str
        :param name: The name of the suppression.
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = '/{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name}'
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str'),
            'recommendationId': self._serialize.url("recommendation_id", recommendation_id, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [204]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def list(
            self, top=None, skip_token=None, custom_headers=None, raw=False, **operation_config):
        """Retrieves the list of snoozed or dismissed suppressions for a
        subscription. The snoozed or dismissed attribute of a recommendation is
        referred to as a suppression.

        :param top: The number of suppressions per page if a paged version of
         this API is being used.
        :type top: int
        :param skip_token: The page-continuation token to use with a paged
         version of this API.
        :type skip_token: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of SuppressionContract
        :rtype:
         ~azure.mgmt.advisor.models.SuppressionContractPaged[~azure.mgmt.advisor.models.SuppressionContract]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/providers/Microsoft.Advisor/suppressions'
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if skip_token is not None:
                    query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.SuppressionContractPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.SuppressionContractPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
