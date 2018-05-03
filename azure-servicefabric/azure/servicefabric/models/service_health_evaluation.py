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

from .health_evaluation import HealthEvaluation


class ServiceHealthEvaluation(HealthEvaluation):
    """Represents health evaluation for a service, containing information about
    the data and the algorithm used by health store to evaluate health. The
    evaluation is returned only when the aggregated health state is either
    Error or Warning.

    :param aggregated_health_state: The health state of a Service Fabric
     entity such as Cluster, Node, Application, Service, Partition, Replica
     etc. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error',
     'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param description: Description of the health evaluation, which represents
     a summary of the evaluation process.
    :type description: str
    :param kind: Constant filled by server.
    :type kind: str
    :param service_name: Name of the service whose health evaluation is
     described by this object.
    :type service_name: str
    :param unhealthy_evaluations: List of unhealthy evaluations that led to
     the current aggregated health state of the service. The types of the
     unhealthy evaluations can be PartitionsHealthEvaluation or
     EventHealthEvaluation.
    :type unhealthy_evaluations:
     list[~azure.servicefabric.models.HealthEvaluationWrapper]
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
    }

    def __init__(self, aggregated_health_state=None, description=None, service_name=None, unhealthy_evaluations=None):
        super(ServiceHealthEvaluation, self).__init__(aggregated_health_state=aggregated_health_state, description=description)
        self.service_name = service_name
        self.unhealthy_evaluations = unhealthy_evaluations
        self.kind = 'Service'
