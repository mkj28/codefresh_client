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


class InlineObject3(object):
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
        'rules': 'list[str]'
    }

    attribute_map = {
        'tags': 'tags',
        'rules': 'rules'
    }

    def __init__(self, tags=None, rules=None):  # noqa: E501
        """InlineObject3 - a model defined in OpenAPI"""  # noqa: E501

        self._tags = None
        self._rules = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if rules is not None:
            self.rules = rules

    @property
    def tags(self):
        """Gets the tags of this InlineObject3.  # noqa: E501


        :return: The tags of this InlineObject3.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject3.


        :param tags: The tags of this InlineObject3.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def rules(self):
        """Gets the rules of this InlineObject3.  # noqa: E501


        :return: The rules of this InlineObject3.  # noqa: E501
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this InlineObject3.


        :param rules: The rules of this InlineObject3.  # noqa: E501
        :type: list[str]
        """

        self._rules = rules

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
        if not isinstance(other, InlineObject3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
