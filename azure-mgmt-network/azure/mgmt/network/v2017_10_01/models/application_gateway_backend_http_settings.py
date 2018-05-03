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

from .sub_resource import SubResource


class ApplicationGatewayBackendHttpSettings(SubResource):
    """Backend address pool settings of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param port: Port
    :type port: int
    :param protocol: Protocol. Possible values include: 'Http', 'Https'
    :type protocol: str or
     ~azure.mgmt.network.v2017_10_01.models.ApplicationGatewayProtocol
    :param cookie_based_affinity: Cookie based affinity. Possible values
     include: 'Enabled', 'Disabled'
    :type cookie_based_affinity: str or
     ~azure.mgmt.network.v2017_10_01.models.ApplicationGatewayCookieBasedAffinity
    :param request_timeout: Request timeout in seconds. Application Gateway
     will fail the request if response is not received within RequestTimeout.
     Acceptable values are from 1 second to 86400 seconds.
    :type request_timeout: int
    :param probe: Probe resource of an application gateway.
    :type probe: ~azure.mgmt.network.v2017_10_01.models.SubResource
    :param authentication_certificates: Array of references to application
     gateway authentication certificates.
    :type authentication_certificates:
     list[~azure.mgmt.network.v2017_10_01.models.SubResource]
    :param connection_draining: Connection draining of the backend http
     settings resource.
    :type connection_draining:
     ~azure.mgmt.network.v2017_10_01.models.ApplicationGatewayConnectionDraining
    :param host_name: Host header to be sent to the backend servers.
    :type host_name: str
    :param pick_host_name_from_backend_address: Whether to pick host header
     should be picked from the host name of the backend server. Default value
     is false.
    :type pick_host_name_from_backend_address: bool
    :param affinity_cookie_name: Cookie name to use for the affinity cookie.
    :type affinity_cookie_name: str
    :param probe_enabled: Whether the probe is enabled. Default value is
     false.
    :type probe_enabled: bool
    :param path: Path which should be used as a prefix for all HTTP requests.
     Null means no path will be prefixed. Default value is null.
    :type path: str
    :param provisioning_state: Provisioning state of the backend http settings
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'port': {'key': 'properties.port', 'type': 'int'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'cookie_based_affinity': {'key': 'properties.cookieBasedAffinity', 'type': 'str'},
        'request_timeout': {'key': 'properties.requestTimeout', 'type': 'int'},
        'probe': {'key': 'properties.probe', 'type': 'SubResource'},
        'authentication_certificates': {'key': 'properties.authenticationCertificates', 'type': '[SubResource]'},
        'connection_draining': {'key': 'properties.connectionDraining', 'type': 'ApplicationGatewayConnectionDraining'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'pick_host_name_from_backend_address': {'key': 'properties.pickHostNameFromBackendAddress', 'type': 'bool'},
        'affinity_cookie_name': {'key': 'properties.affinityCookieName', 'type': 'str'},
        'probe_enabled': {'key': 'properties.probeEnabled', 'type': 'bool'},
        'path': {'key': 'properties.path', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayBackendHttpSettings, self).__init__(**kwargs)
        self.port = kwargs.get('port', None)
        self.protocol = kwargs.get('protocol', None)
        self.cookie_based_affinity = kwargs.get('cookie_based_affinity', None)
        self.request_timeout = kwargs.get('request_timeout', None)
        self.probe = kwargs.get('probe', None)
        self.authentication_certificates = kwargs.get('authentication_certificates', None)
        self.connection_draining = kwargs.get('connection_draining', None)
        self.host_name = kwargs.get('host_name', None)
        self.pick_host_name_from_backend_address = kwargs.get('pick_host_name_from_backend_address', None)
        self.affinity_cookie_name = kwargs.get('affinity_cookie_name', None)
        self.probe_enabled = kwargs.get('probe_enabled', None)
        self.path = kwargs.get('path', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
        self.type = kwargs.get('type', None)
