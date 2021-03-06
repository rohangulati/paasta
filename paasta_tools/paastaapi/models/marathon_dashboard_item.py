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


class MarathonDashboardItem(object):
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
        'instance': 'str',
        'service': 'str',
        'shard_url': 'str'
    }

    attribute_map = {
        'instance': 'instance',
        'service': 'service',
        'shard_url': 'shard_url'
    }

    def __init__(self, instance=None, service=None, shard_url=None, local_vars_configuration=None):  # noqa: E501
        """MarathonDashboardItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instance = None
        self._service = None
        self._shard_url = None
        self.discriminator = None

        if instance is not None:
            self.instance = instance
        if service is not None:
            self.service = service
        if shard_url is not None:
            self.shard_url = shard_url

    @property
    def instance(self):
        """Gets the instance of this MarathonDashboardItem.  # noqa: E501

        Instance name  # noqa: E501

        :return: The instance of this MarathonDashboardItem.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this MarathonDashboardItem.

        Instance name  # noqa: E501

        :param instance: The instance of this MarathonDashboardItem.  # noqa: E501
        :type instance: str
        """

        self._instance = instance

    @property
    def service(self):
        """Gets the service of this MarathonDashboardItem.  # noqa: E501

        Service name  # noqa: E501

        :return: The service of this MarathonDashboardItem.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this MarathonDashboardItem.

        Service name  # noqa: E501

        :param service: The service of this MarathonDashboardItem.  # noqa: E501
        :type service: str
        """

        self._service = service

    @property
    def shard_url(self):
        """Gets the shard_url of this MarathonDashboardItem.  # noqa: E501

        Marathon Shard URL  # noqa: E501

        :return: The shard_url of this MarathonDashboardItem.  # noqa: E501
        :rtype: str
        """
        return self._shard_url

    @shard_url.setter
    def shard_url(self, shard_url):
        """Sets the shard_url of this MarathonDashboardItem.

        Marathon Shard URL  # noqa: E501

        :param shard_url: The shard_url of this MarathonDashboardItem.  # noqa: E501
        :type shard_url: str
        """

        self._shard_url = shard_url

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
        if not isinstance(other, MarathonDashboardItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarathonDashboardItem):
            return True

        return self.to_dict() != other.to_dict()
