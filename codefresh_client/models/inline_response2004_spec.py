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


class InlineResponse2004Spec(object):
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
        'variables': 'list[PipelinesnameSpecVariables]'
    }

    attribute_map = {
        'variables': 'variables'
    }

    def __init__(self, variables=None):  # noqa: E501
        """InlineResponse2004Spec - a model defined in OpenAPI"""  # noqa: E501

        self._variables = None
        self.discriminator = None

        if variables is not None:
            self.variables = variables

    @property
    def variables(self):
        """Gets the variables of this InlineResponse2004Spec.  # noqa: E501


        :return: The variables of this InlineResponse2004Spec.  # noqa: E501
        :rtype: list[PipelinesnameSpecVariables]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this InlineResponse2004Spec.


        :param variables: The variables of this InlineResponse2004Spec.  # noqa: E501
        :type: list[PipelinesnameSpecVariables]
        """

        self._variables = variables

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
        if not isinstance(other, InlineResponse2004Spec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
