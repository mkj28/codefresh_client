# coding: utf-8

"""
    Codefresh API

    Codefresh API openAPI 3.0 specification  # noqa: E501

    OpenAPI spec version: 0.0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineObject8(object):
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
        'account': 'list[str]',
        'provider': 'AdminaccountsaddpendinguserProvider',
        'user_name': 'str'
    }

    attribute_map = {
        'account': 'account',
        'provider': 'provider',
        'user_name': 'userName'
    }

    def __init__(self, account=None, provider=None, user_name=None):  # noqa: E501
        """InlineObject8 - a model defined in OpenAPI"""  # noqa: E501

        self._account = None
        self._provider = None
        self._user_name = None
        self.discriminator = None

        if account is not None:
            self.account = account
        self.provider = provider
        self.user_name = user_name

    @property
    def account(self):
        """Gets the account of this InlineObject8.  # noqa: E501


        :return: The account of this InlineObject8.  # noqa: E501
        :rtype: list[str]
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this InlineObject8.


        :param account: The account of this InlineObject8.  # noqa: E501
        :type: list[str]
        """

        self._account = account

    @property
    def provider(self):
        """Gets the provider of this InlineObject8.  # noqa: E501


        :return: The provider of this InlineObject8.  # noqa: E501
        :rtype: AdminaccountsaddpendinguserProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this InlineObject8.


        :param provider: The provider of this InlineObject8.  # noqa: E501
        :type: AdminaccountsaddpendinguserProvider
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def user_name(self):
        """Gets the user_name of this InlineObject8.  # noqa: E501


        :return: The user_name of this InlineObject8.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this InlineObject8.


        :param user_name: The user_name of this InlineObject8.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

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
        if not isinstance(other, InlineObject8):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
