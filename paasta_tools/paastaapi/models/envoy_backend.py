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


class EnvoyBackend(object):
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
        'address': 'str',
        'eds_health_status': 'str',
        'has_associated_task': 'bool',
        'hostname': 'str',
        'port_value': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'address': 'address',
        'eds_health_status': 'eds_health_status',
        'has_associated_task': 'has_associated_task',
        'hostname': 'hostname',
        'port_value': 'port_value',
        'weight': 'weight'
    }

    def __init__(self, address=None, eds_health_status=None, has_associated_task=None, hostname=None, port_value=None, weight=None, local_vars_configuration=None):  # noqa: E501
        """EnvoyBackend - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._eds_health_status = None
        self._has_associated_task = None
        self._hostname = None
        self._port_value = None
        self._weight = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if eds_health_status is not None:
            self.eds_health_status = eds_health_status
        if has_associated_task is not None:
            self.has_associated_task = has_associated_task
        if hostname is not None:
            self.hostname = hostname
        if port_value is not None:
            self.port_value = port_value
        if weight is not None:
            self.weight = weight

    @property
    def address(self):
        """Gets the address of this EnvoyBackend.  # noqa: E501

        Address of the host on which the backend is running  # noqa: E501

        :return: The address of this EnvoyBackend.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this EnvoyBackend.

        Address of the host on which the backend is running  # noqa: E501

        :param address: The address of this EnvoyBackend.  # noqa: E501
        :type address: str
        """

        self._address = address

    @property
    def eds_health_status(self):
        """Gets the eds_health_status of this EnvoyBackend.  # noqa: E501

        Status of the backend in Envoy as reported by the EDS  # noqa: E501

        :return: The eds_health_status of this EnvoyBackend.  # noqa: E501
        :rtype: str
        """
        return self._eds_health_status

    @eds_health_status.setter
    def eds_health_status(self, eds_health_status):
        """Sets the eds_health_status of this EnvoyBackend.

        Status of the backend in Envoy as reported by the EDS  # noqa: E501

        :param eds_health_status: The eds_health_status of this EnvoyBackend.  # noqa: E501
        :type eds_health_status: str
        """

        self._eds_health_status = eds_health_status

    @property
    def has_associated_task(self):
        """Gets the has_associated_task of this EnvoyBackend.  # noqa: E501

        Whether this backend has an associated task running  # noqa: E501

        :return: The has_associated_task of this EnvoyBackend.  # noqa: E501
        :rtype: bool
        """
        return self._has_associated_task

    @has_associated_task.setter
    def has_associated_task(self, has_associated_task):
        """Sets the has_associated_task of this EnvoyBackend.

        Whether this backend has an associated task running  # noqa: E501

        :param has_associated_task: The has_associated_task of this EnvoyBackend.  # noqa: E501
        :type has_associated_task: bool
        """

        self._has_associated_task = has_associated_task

    @property
    def hostname(self):
        """Gets the hostname of this EnvoyBackend.  # noqa: E501

        Name of the host on which the backend is running  # noqa: E501

        :return: The hostname of this EnvoyBackend.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this EnvoyBackend.

        Name of the host on which the backend is running  # noqa: E501

        :param hostname: The hostname of this EnvoyBackend.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def port_value(self):
        """Gets the port_value of this EnvoyBackend.  # noqa: E501

        Port number on which the backend responds  # noqa: E501

        :return: The port_value of this EnvoyBackend.  # noqa: E501
        :rtype: int
        """
        return self._port_value

    @port_value.setter
    def port_value(self, port_value):
        """Sets the port_value of this EnvoyBackend.

        Port number on which the backend responds  # noqa: E501

        :param port_value: The port_value of this EnvoyBackend.  # noqa: E501
        :type port_value: int
        """

        self._port_value = port_value

    @property
    def weight(self):
        """Gets the weight of this EnvoyBackend.  # noqa: E501

        The weight of this backend in the cluster  # noqa: E501

        :return: The weight of this EnvoyBackend.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this EnvoyBackend.

        The weight of this backend in the cluster  # noqa: E501

        :param weight: The weight of this EnvoyBackend.  # noqa: E501
        :type weight: int
        """

        self._weight = weight

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
        if not isinstance(other, EnvoyBackend):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvoyBackend):
            return True

        return self.to_dict() != other.to_dict()
