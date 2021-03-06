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


class InstanceStatusTron(object):
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
        'action_command': 'str',
        'action_name': 'str',
        'action_raw_command': 'str',
        'action_start_time': 'str',
        'action_state': 'str',
        'action_stderr': 'str',
        'action_stdout': 'str',
        'job_name': 'str',
        'job_schedule': 'str',
        'job_status': 'str',
        'job_url': 'str'
    }

    attribute_map = {
        'action_command': 'action_command',
        'action_name': 'action_name',
        'action_raw_command': 'action_raw_command',
        'action_start_time': 'action_start_time',
        'action_state': 'action_state',
        'action_stderr': 'action_stderr',
        'action_stdout': 'action_stdout',
        'job_name': 'job_name',
        'job_schedule': 'job_schedule',
        'job_status': 'job_status',
        'job_url': 'job_url'
    }

    def __init__(self, action_command=None, action_name=None, action_raw_command=None, action_start_time=None, action_state=None, action_stderr=None, action_stdout=None, job_name=None, job_schedule=None, job_status=None, job_url=None, local_vars_configuration=None):  # noqa: E501
        """InstanceStatusTron - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action_command = None
        self._action_name = None
        self._action_raw_command = None
        self._action_start_time = None
        self._action_state = None
        self._action_stderr = None
        self._action_stdout = None
        self._job_name = None
        self._job_schedule = None
        self._job_status = None
        self._job_url = None
        self.discriminator = None

        if action_command is not None:
            self.action_command = action_command
        if action_name is not None:
            self.action_name = action_name
        if action_raw_command is not None:
            self.action_raw_command = action_raw_command
        if action_start_time is not None:
            self.action_start_time = action_start_time
        if action_state is not None:
            self.action_state = action_state
        if action_stderr is not None:
            self.action_stderr = action_stderr
        if action_stdout is not None:
            self.action_stdout = action_stdout
        self.job_name = job_name
        if job_schedule is not None:
            self.job_schedule = job_schedule
        if job_status is not None:
            self.job_status = job_status
        self.job_url = job_url

    @property
    def action_command(self):
        """Gets the action_command of this InstanceStatusTron.  # noqa: E501

        The command of the action  # noqa: E501

        :return: The action_command of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._action_command

    @action_command.setter
    def action_command(self, action_command):
        """Sets the action_command of this InstanceStatusTron.

        The command of the action  # noqa: E501

        :param action_command: The action_command of this InstanceStatusTron.  # noqa: E501
        :type action_command: str
        """

        self._action_command = action_command

    @property
    def action_name(self):
        """Gets the action_name of this InstanceStatusTron.  # noqa: E501

        The name of the action  # noqa: E501

        :return: The action_name of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this InstanceStatusTron.

        The name of the action  # noqa: E501

        :param action_name: The action_name of this InstanceStatusTron.  # noqa: E501
        :type action_name: str
        """

        self._action_name = action_name

    @property
    def action_raw_command(self):
        """Gets the action_raw_command of this InstanceStatusTron.  # noqa: E501

        The raw command of the action  # noqa: E501

        :return: The action_raw_command of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._action_raw_command

    @action_raw_command.setter
    def action_raw_command(self, action_raw_command):
        """Sets the action_raw_command of this InstanceStatusTron.

        The raw command of the action  # noqa: E501

        :param action_raw_command: The action_raw_command of this InstanceStatusTron.  # noqa: E501
        :type action_raw_command: str
        """

        self._action_raw_command = action_raw_command

    @property
    def action_start_time(self):
        """Gets the action_start_time of this InstanceStatusTron.  # noqa: E501

        The start time of the action  # noqa: E501

        :return: The action_start_time of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._action_start_time

    @action_start_time.setter
    def action_start_time(self, action_start_time):
        """Sets the action_start_time of this InstanceStatusTron.

        The start time of the action  # noqa: E501

        :param action_start_time: The action_start_time of this InstanceStatusTron.  # noqa: E501
        :type action_start_time: str
        """

        self._action_start_time = action_start_time

    @property
    def action_state(self):
        """Gets the action_state of this InstanceStatusTron.  # noqa: E501

        The state of the action  # noqa: E501

        :return: The action_state of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._action_state

    @action_state.setter
    def action_state(self, action_state):
        """Sets the action_state of this InstanceStatusTron.

        The state of the action  # noqa: E501

        :param action_state: The action_state of this InstanceStatusTron.  # noqa: E501
        :type action_state: str
        """

        self._action_state = action_state

    @property
    def action_stderr(self):
        """Gets the action_stderr of this InstanceStatusTron.  # noqa: E501

        The stderr command of the action  # noqa: E501

        :return: The action_stderr of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._action_stderr

    @action_stderr.setter
    def action_stderr(self, action_stderr):
        """Sets the action_stderr of this InstanceStatusTron.

        The stderr command of the action  # noqa: E501

        :param action_stderr: The action_stderr of this InstanceStatusTron.  # noqa: E501
        :type action_stderr: str
        """

        self._action_stderr = action_stderr

    @property
    def action_stdout(self):
        """Gets the action_stdout of this InstanceStatusTron.  # noqa: E501

        The stdout command of the action  # noqa: E501

        :return: The action_stdout of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._action_stdout

    @action_stdout.setter
    def action_stdout(self, action_stdout):
        """Sets the action_stdout of this InstanceStatusTron.

        The stdout command of the action  # noqa: E501

        :param action_stdout: The action_stdout of this InstanceStatusTron.  # noqa: E501
        :type action_stdout: str
        """

        self._action_stdout = action_stdout

    @property
    def job_name(self):
        """Gets the job_name of this InstanceStatusTron.  # noqa: E501

        The name of this job  # noqa: E501

        :return: The job_name of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this InstanceStatusTron.

        The name of this job  # noqa: E501

        :param job_name: The job_name of this InstanceStatusTron.  # noqa: E501
        :type job_name: str
        """
        if self.local_vars_configuration.client_side_validation and job_name is None:  # noqa: E501
            raise ValueError("Invalid value for `job_name`, must not be `None`")  # noqa: E501

        self._job_name = job_name

    @property
    def job_schedule(self):
        """Gets the job_schedule of this InstanceStatusTron.  # noqa: E501

        The job schedule of the job  # noqa: E501

        :return: The job_schedule of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._job_schedule

    @job_schedule.setter
    def job_schedule(self, job_schedule):
        """Sets the job_schedule of this InstanceStatusTron.

        The job schedule of the job  # noqa: E501

        :param job_schedule: The job_schedule of this InstanceStatusTron.  # noqa: E501
        :type job_schedule: str
        """

        self._job_schedule = job_schedule

    @property
    def job_status(self):
        """Gets the job_status of this InstanceStatusTron.  # noqa: E501

        The status of the job  # noqa: E501

        :return: The job_status of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this InstanceStatusTron.

        The status of the job  # noqa: E501

        :param job_status: The job_status of this InstanceStatusTron.  # noqa: E501
        :type job_status: str
        """

        self._job_status = job_status

    @property
    def job_url(self):
        """Gets the job_url of this InstanceStatusTron.  # noqa: E501

        The dashboard url of the job  # noqa: E501

        :return: The job_url of this InstanceStatusTron.  # noqa: E501
        :rtype: str
        """
        return self._job_url

    @job_url.setter
    def job_url(self, job_url):
        """Sets the job_url of this InstanceStatusTron.

        The dashboard url of the job  # noqa: E501

        :param job_url: The job_url of this InstanceStatusTron.  # noqa: E501
        :type job_url: str
        """
        if self.local_vars_configuration.client_side_validation and job_url is None:  # noqa: E501
            raise ValueError("Invalid value for `job_url`, must not be `None`")  # noqa: E501

        self._job_url = job_url

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
        if not isinstance(other, InstanceStatusTron):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceStatusTron):
            return True

        return self.to_dict() != other.to_dict()
