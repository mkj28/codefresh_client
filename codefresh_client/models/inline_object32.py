# coding: utf-8

"""
    Codefresh API

    Codefresh API openAPI 3.0 specification  # noqa: E501

    OpenAPI spec version: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineObject32(object):
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
        'tags': 'list[str]',
        'name': 'str',
        'users': 'list[str]'
    }

    attribute_map = {
        'tags': 'tags',
        'name': 'name',
        'users': 'users'
    }

    def __init__(self, tags=None, name=None, users=None):  # noqa: E501
        """InlineObject32 - a model defined in OpenAPI"""  # noqa: E501

        self._tags = None
        self._name = None
        self._users = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if name is not None:
            self.name = name
        if users is not None:
            self.users = users

    @property
    def tags(self):
        """Gets the tags of this InlineObject32.  # noqa: E501


        :return: The tags of this InlineObject32.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject32.


        :param tags: The tags of this InlineObject32.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def name(self):
        """Gets the name of this InlineObject32.  # noqa: E501


        :return: The name of this InlineObject32.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject32.


        :param name: The name of this InlineObject32.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def users(self):
        """Gets the users of this InlineObject32.  # noqa: E501


        :return: The users of this InlineObject32.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this InlineObject32.


        :param users: The users of this InlineObject32.  # noqa: E501
        :type: list[str]
        """

        self._users = users

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
        if not isinstance(other, InlineObject32):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other