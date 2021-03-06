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
from codefresh_client.api.runtime_environments_api import RuntimeEnvironmentsApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestRuntimeEnvironmentsApi(unittest.TestCase):
    """RuntimeEnvironmentsApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.runtime_environments_api.RuntimeEnvironmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_on_prem_runtime_envs_list(self):
        """Test case for on_prem_runtime_envs_list

        List  # noqa: E501
        """
        pass

    def test_on_prem_runtime_envs_plan_get(self):
        """Test case for on_prem_runtime_envs_plan_get

        Get  # noqa: E501
        """
        pass

    def test_runtime_envs_delete(self):
        """Test case for runtime_envs_delete

        Delete  # noqa: E501
        """
        pass

    def test_runtime_envs_get(self):
        """Test case for runtime_envs_get

        Get  # noqa: E501
        """
        pass

    def test_runtime_envs_list(self):
        """Test case for runtime_envs_list

        List  # noqa: E501
        """
        pass

    def test_runtime_envs_set_default(self):
        """Test case for runtime_envs_set_default

        Set default  # noqa: E501
        """
        pass

    def test_runtime_envs_update(self):
        """Test case for runtime_envs_update

        Update  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
