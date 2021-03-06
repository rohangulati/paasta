# coding: utf-8

"""
    Paasta API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from paasta_tools.paastaapi.configuration import Configuration


class InstanceStatusKubernetes(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'app_count': 'int',
        'app_id': 'str',
        'autoscaling_status': 'InstanceStatusKubernetesAutoscalingStatus',
        'backoff_seconds': 'int',
        'bounce_method': 'str',
        'create_timestamp': 'float',
        'deploy_status': 'str',
        'deploy_status_message': 'str',
        'desired_state': 'str',
        'error_message': 'str',
        'expected_instance_count': 'int',
        'namespace': 'str',
        'pods': 'list[KubernetesPod]',
        'replicasets': 'list[KubernetesReplicaSet]',
        'running_instance_count': 'int',
        'smartstack': 'SmartstackStatus',
        'envoy': 'EnvoyStatus'
    }

    attribute_map = {
        'app_count': 'app_count',
        'app_id': 'app_id',
        'autoscaling_status': 'autoscaling_status',
        'backoff_seconds': 'backoff_seconds',
        'bounce_method': 'bounce_method',
        'create_timestamp': 'create_timestamp',
        'deploy_status': 'deploy_status',
        'deploy_status_message': 'deploy_status_message',
        'desired_state': 'desired_state',
        'error_message': 'error_message',
        'expected_instance_count': 'expected_instance_count',
        'namespace': 'namespace',
        'pods': 'pods',
        'replicasets': 'replicasets',
        'running_instance_count': 'running_instance_count',
        'smartstack': 'smartstack',
        'envoy': 'envoy'
    }

    def __init__(self, app_count=None, app_id=None, autoscaling_status=None, backoff_seconds=None, bounce_method=None, create_timestamp=None, deploy_status=None, deploy_status_message=None, desired_state=None, error_message=None, expected_instance_count=None, namespace=None, pods=None, replicasets=None, running_instance_count=None, smartstack=None, envoy=None, local_vars_configuration=None):  # noqa: E501
        """InstanceStatusKubernetes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_count = None
        self._app_id = None
        self._autoscaling_status = None
        self._backoff_seconds = None
        self._bounce_method = None
        self._create_timestamp = None
        self._deploy_status = None
        self._deploy_status_message = None
        self._desired_state = None
        self._error_message = None
        self._expected_instance_count = None
        self._namespace = None
        self._pods = None
        self._replicasets = None
        self._running_instance_count = None
        self._smartstack = None
        self._envoy = None
        self.discriminator = None

        self.app_count = app_count
        if app_id is not None:
            self.app_id = app_id
        if autoscaling_status is not None:
            self.autoscaling_status = autoscaling_status
        if backoff_seconds is not None:
            self.backoff_seconds = backoff_seconds
        self.bounce_method = bounce_method
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if deploy_status is not None:
            self.deploy_status = deploy_status
        if deploy_status_message is not None:
            self.deploy_status_message = deploy_status_message
        self.desired_state = desired_state
        if error_message is not None:
            self.error_message = error_message
        if expected_instance_count is not None:
            self.expected_instance_count = expected_instance_count
        if namespace is not None:
            self.namespace = namespace
        if pods is not None:
            self.pods = pods
        if replicasets is not None:
            self.replicasets = replicasets
        if running_instance_count is not None:
            self.running_instance_count = running_instance_count
        if smartstack is not None:
            self.smartstack = smartstack
        if envoy is not None:
            self.envoy = envoy

    @property
    def app_count(self):
        """Gets the app_count of this InstanceStatusKubernetes.  # noqa: E501

        The number of different running versions of the same service (0 for stopped, 1 for running and 1+ for bouncing)  # noqa: E501

        :return: The app_count of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: int
        """
        return self._app_count

    @app_count.setter
    def app_count(self, app_count):
        """Sets the app_count of this InstanceStatusKubernetes.

        The number of different running versions of the same service (0 for stopped, 1 for running and 1+ for bouncing)  # noqa: E501

        :param app_count: The app_count of this InstanceStatusKubernetes.  # noqa: E501
        :type app_count: int
        """
        if self.local_vars_configuration.client_side_validation and app_count is None:  # noqa: E501
            raise ValueError("Invalid value for `app_count`, must not be `None`")  # noqa: E501

        self._app_count = app_count

    @property
    def app_id(self):
        """Gets the app_id of this InstanceStatusKubernetes.  # noqa: E501

        ID of the desired version of a service instance  # noqa: E501

        :return: The app_id of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this InstanceStatusKubernetes.

        ID of the desired version of a service instance  # noqa: E501

        :param app_id: The app_id of this InstanceStatusKubernetes.  # noqa: E501
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def autoscaling_status(self):
        """Gets the autoscaling_status of this InstanceStatusKubernetes.  # noqa: E501


        :return: The autoscaling_status of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: InstanceStatusKubernetesAutoscalingStatus
        """
        return self._autoscaling_status

    @autoscaling_status.setter
    def autoscaling_status(self, autoscaling_status):
        """Sets the autoscaling_status of this InstanceStatusKubernetes.


        :param autoscaling_status: The autoscaling_status of this InstanceStatusKubernetes.  # noqa: E501
        :type autoscaling_status: InstanceStatusKubernetesAutoscalingStatus
        """

        self._autoscaling_status = autoscaling_status

    @property
    def backoff_seconds(self):
        """Gets the backoff_seconds of this InstanceStatusKubernetes.  # noqa: E501

        backoff in seconds before launching the next task  # noqa: E501

        :return: The backoff_seconds of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: int
        """
        return self._backoff_seconds

    @backoff_seconds.setter
    def backoff_seconds(self, backoff_seconds):
        """Sets the backoff_seconds of this InstanceStatusKubernetes.

        backoff in seconds before launching the next task  # noqa: E501

        :param backoff_seconds: The backoff_seconds of this InstanceStatusKubernetes.  # noqa: E501
        :type backoff_seconds: int
        """

        self._backoff_seconds = backoff_seconds

    @property
    def bounce_method(self):
        """Gets the bounce_method of this InstanceStatusKubernetes.  # noqa: E501

        Method to transit between new and old versions of a service  # noqa: E501

        :return: The bounce_method of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._bounce_method

    @bounce_method.setter
    def bounce_method(self, bounce_method):
        """Sets the bounce_method of this InstanceStatusKubernetes.

        Method to transit between new and old versions of a service  # noqa: E501

        :param bounce_method: The bounce_method of this InstanceStatusKubernetes.  # noqa: E501
        :type bounce_method: str
        """
        if self.local_vars_configuration.client_side_validation and bounce_method is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_method`, must not be `None`")  # noqa: E501
        allowed_values = ["brutal", "upthendown", "downthenup", "crossover"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and bounce_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `bounce_method` ({0}), must be one of {1}"  # noqa: E501
                .format(bounce_method, allowed_values)
            )

        self._bounce_method = bounce_method

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this InstanceStatusKubernetes.  # noqa: E501

        Unix timestamp when this app was created  # noqa: E501

        :return: The create_timestamp of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: float
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this InstanceStatusKubernetes.

        Unix timestamp when this app was created  # noqa: E501

        :param create_timestamp: The create_timestamp of this InstanceStatusKubernetes.  # noqa: E501
        :type create_timestamp: float
        """

        self._create_timestamp = create_timestamp

    @property
    def deploy_status(self):
        """Gets the deploy_status of this InstanceStatusKubernetes.  # noqa: E501

        Deploy status of a Kubernetes service  # noqa: E501

        :return: The deploy_status of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._deploy_status

    @deploy_status.setter
    def deploy_status(self, deploy_status):
        """Sets the deploy_status of this InstanceStatusKubernetes.

        Deploy status of a Kubernetes service  # noqa: E501

        :param deploy_status: The deploy_status of this InstanceStatusKubernetes.  # noqa: E501
        :type deploy_status: str
        """
        allowed_values = ["Running", "Deploying", "Stopped", "Delayed", "Waiting", "NotRunning"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deploy_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deploy_status` ({0}), must be one of {1}"  # noqa: E501
                .format(deploy_status, allowed_values)
            )

        self._deploy_status = deploy_status

    @property
    def deploy_status_message(self):
        """Gets the deploy_status_message of this InstanceStatusKubernetes.  # noqa: E501

        Reason for the deploy status  # noqa: E501

        :return: The deploy_status_message of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._deploy_status_message

    @deploy_status_message.setter
    def deploy_status_message(self, deploy_status_message):
        """Sets the deploy_status_message of this InstanceStatusKubernetes.

        Reason for the deploy status  # noqa: E501

        :param deploy_status_message: The deploy_status_message of this InstanceStatusKubernetes.  # noqa: E501
        :type deploy_status_message: str
        """

        self._deploy_status_message = deploy_status_message

    @property
    def desired_state(self):
        """Gets the desired_state of this InstanceStatusKubernetes.  # noqa: E501

        Desired state of a service, for Kubernetes  # noqa: E501

        :return: The desired_state of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        """Sets the desired_state of this InstanceStatusKubernetes.

        Desired state of a service, for Kubernetes  # noqa: E501

        :param desired_state: The desired_state of this InstanceStatusKubernetes.  # noqa: E501
        :type desired_state: str
        """
        if self.local_vars_configuration.client_side_validation and desired_state is None:  # noqa: E501
            raise ValueError("Invalid value for `desired_state`, must not be `None`")  # noqa: E501
        allowed_values = ["start", "stop"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and desired_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `desired_state` ({0}), must be one of {1}"  # noqa: E501
                .format(desired_state, allowed_values)
            )

        self._desired_state = desired_state

    @property
    def error_message(self):
        """Gets the error_message of this InstanceStatusKubernetes.  # noqa: E501

        Error message when a kubernetes object (Deployment/Statefulset) cannot be found  # noqa: E501

        :return: The error_message of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this InstanceStatusKubernetes.

        Error message when a kubernetes object (Deployment/Statefulset) cannot be found  # noqa: E501

        :param error_message: The error_message of this InstanceStatusKubernetes.  # noqa: E501
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def expected_instance_count(self):
        """Gets the expected_instance_count of this InstanceStatusKubernetes.  # noqa: E501

        The number of desired instances of the service  # noqa: E501

        :return: The expected_instance_count of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: int
        """
        return self._expected_instance_count

    @expected_instance_count.setter
    def expected_instance_count(self, expected_instance_count):
        """Sets the expected_instance_count of this InstanceStatusKubernetes.

        The number of desired instances of the service  # noqa: E501

        :param expected_instance_count: The expected_instance_count of this InstanceStatusKubernetes.  # noqa: E501
        :type expected_instance_count: int
        """

        self._expected_instance_count = expected_instance_count

    @property
    def namespace(self):
        """Gets the namespace of this InstanceStatusKubernetes.  # noqa: E501

        The namespace this app is running  # noqa: E501

        :return: The namespace of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this InstanceStatusKubernetes.

        The namespace this app is running  # noqa: E501

        :param namespace: The namespace of this InstanceStatusKubernetes.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def pods(self):
        """Gets the pods of this InstanceStatusKubernetes.  # noqa: E501

        Pods associated to this app  # noqa: E501

        :return: The pods of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: list[KubernetesPod]
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        """Sets the pods of this InstanceStatusKubernetes.

        Pods associated to this app  # noqa: E501

        :param pods: The pods of this InstanceStatusKubernetes.  # noqa: E501
        :type pods: list[KubernetesPod]
        """

        self._pods = pods

    @property
    def replicasets(self):
        """Gets the replicasets of this InstanceStatusKubernetes.  # noqa: E501

        ReplicaSets associated to this app  # noqa: E501

        :return: The replicasets of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: list[KubernetesReplicaSet]
        """
        return self._replicasets

    @replicasets.setter
    def replicasets(self, replicasets):
        """Sets the replicasets of this InstanceStatusKubernetes.

        ReplicaSets associated to this app  # noqa: E501

        :param replicasets: The replicasets of this InstanceStatusKubernetes.  # noqa: E501
        :type replicasets: list[KubernetesReplicaSet]
        """

        self._replicasets = replicasets

    @property
    def running_instance_count(self):
        """Gets the running_instance_count of this InstanceStatusKubernetes.  # noqa: E501

        The number of actual running instances of the service  # noqa: E501

        :return: The running_instance_count of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: int
        """
        return self._running_instance_count

    @running_instance_count.setter
    def running_instance_count(self, running_instance_count):
        """Sets the running_instance_count of this InstanceStatusKubernetes.

        The number of actual running instances of the service  # noqa: E501

        :param running_instance_count: The running_instance_count of this InstanceStatusKubernetes.  # noqa: E501
        :type running_instance_count: int
        """

        self._running_instance_count = running_instance_count

    @property
    def smartstack(self):
        """Gets the smartstack of this InstanceStatusKubernetes.  # noqa: E501


        :return: The smartstack of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: SmartstackStatus
        """
        return self._smartstack

    @smartstack.setter
    def smartstack(self, smartstack):
        """Sets the smartstack of this InstanceStatusKubernetes.


        :param smartstack: The smartstack of this InstanceStatusKubernetes.  # noqa: E501
        :type smartstack: SmartstackStatus
        """

        self._smartstack = smartstack

    @property
    def envoy(self):
        """Gets the envoy of this InstanceStatusKubernetes.  # noqa: E501


        :return: The envoy of this InstanceStatusKubernetes.  # noqa: E501
        :rtype: EnvoyStatus
        """
        return self._envoy

    @envoy.setter
    def envoy(self, envoy):
        """Sets the envoy of this InstanceStatusKubernetes.


        :param envoy: The envoy of this InstanceStatusKubernetes.  # noqa: E501
        :type envoy: EnvoyStatus
        """

        self._envoy = envoy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceStatusKubernetes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceStatusKubernetes):
            return True

        return self.to_dict() != other.to_dict()
