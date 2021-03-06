# coding: utf-8

"""
    Codefresh API

    Codefresh API openAPI 3.0 specification  # noqa: E501

    OpenAPI spec version: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import codefresh_client
from codefresh_client.api.runtime_environments__account_api import RuntimeEnvironmentsAccountApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestRuntimeEnvironmentsAccountApi(unittest.TestCase):
    """RuntimeEnvironmentsAccountApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.runtime_environments__account_api.RuntimeEnvironmentsAccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_on_prem_runtime_envs_account_list(self):
        """Test case for on_prem_runtime_envs_account_list

        Get by account  # noqa: E501
        """
        pass

    def test_on_prem_runtime_envs_account_set_default(self):
        """Test case for on_prem_runtime_envs_account_set_default

        Set default for account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
