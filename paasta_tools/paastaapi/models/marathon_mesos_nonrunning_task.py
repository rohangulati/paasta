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


class MarathonMesosNonrunningTask(object):
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
        'deployed_timestamp': 'float',
        'hostname': 'str',
        'id': 'str',
        'state': 'str',
        'tail_lines': 'TaskTailLines'
    }

    attribute_map = {
        'deployed_timestamp': 'deployed_timestamp',
        'hostname': 'hostname',
        'id': 'id',
        'state': 'state',
        'tail_lines': 'tail_lines'
    }

    def __init__(self, deployed_timestamp=None, hostname=None, id=None, state=None, tail_lines=None, local_vars_configuration=None):  # noqa: E501
        """MarathonMesosNonrunningTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployed_timestamp = None
        self._hostname = None
        self._id = None
        self._state = None
        self._tail_lines = None
        self.discriminator = None

        if deployed_timestamp is not None:
            self.deployed_timestamp = deployed_timestamp
        if hostname is not None:
            self.hostname = hostname
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if tail_lines is not None:
            self.tail_lines = tail_lines

    @property
    def deployed_timestamp(self):
        """Gets the deployed_timestamp of this MarathonMesosNonrunningTask.  # noqa: E501

        The unix timestamp at which the task was deployed  # noqa: E501

        :return: The deployed_timestamp of this MarathonMesosNonrunningTask.  # noqa: E501
        :rtype: float
        """
        return self._deployed_timestamp

    @deployed_timestamp.setter
    def deployed_timestamp(self, deployed_timestamp):
        """Sets the deployed_timestamp of this MarathonMesosNonrunningTask.

        The unix timestamp at which the task was deployed  # noqa: E501

        :param deployed_timestamp: The deployed_timestamp of this MarathonMesosNonrunningTask.  # noqa: E501
        :type deployed_timestamp: float
        """

        self._deployed_timestamp = deployed_timestamp

    @property
    def hostname(self):
        """Gets the hostname of this MarathonMesosNonrunningTask.  # noqa: E501

        Name of the Mesos agent on which this task is running  # noqa: E501

        :return: The hostname of this MarathonMesosNonrunningTask.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this MarathonMesosNonrunningTask.

        Name of the Mesos agent on which this task is running  # noqa: E501

        :param hostname: The hostname of this MarathonMesosNonrunningTask.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this MarathonMesosNonrunningTask.  # noqa: E501

        The ID of the task in Mesos  # noqa: E501

        :return: The id of this MarathonMesosNonrunningTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MarathonMesosNonrunningTask.

        The ID of the task in Mesos  # noqa: E501

        :param id: The id of this MarathonMesosNonrunningTask.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this MarathonMesosNonrunningTask.  # noqa: E501

        The current state of the task  # noqa: E501

        :return: The state of this MarathonMesosNonrunningTask.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MarathonMesosNonrunningTask.

        The current state of the task  # noqa: E501

        :param state: The state of this MarathonMesosNonrunningTask.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def tail_lines(self):
        """Gets the tail_lines of this MarathonMesosNonrunningTask.  # noqa: E501


        :return: The tail_lines of this MarathonMesosNonrunningTask.  # noqa: E501
        :rtype: TaskTailLines
        """
        return self._tail_lines

    @tail_lines.setter
    def tail_lines(self, tail_lines):
        """Sets the tail_lines of this MarathonMesosNonrunningTask.


        :param tail_lines: The tail_lines of this MarathonMesosNonrunningTask.  # noqa: E501
        :type tail_lines: TaskTailLines
        """

        self._tail_lines = tail_lines

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
        if not isinstance(other, MarathonMesosNonrunningTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarathonMesosNonrunningTask):
            return True

        return self.to_dict() != other.to_dict()
