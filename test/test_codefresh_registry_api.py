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
from codefresh_client.api.codefresh_registry_api import CodefreshRegistryApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestCodefreshRegistryApi(unittest.TestCase):
    """CodefreshRegistryApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.codefresh_registry_api.CodefreshRegistryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_codefresh_registry_generate_cfcr_token(self):
        """Test case for codefresh_registry_generate_cfcr_token

        Generate cfcr token  # noqa: E501
        """
        pass

    def test_registries_create(self):
        """Test case for registries_create

        Create  # noqa: E501
        """
        pass

    def test_registries_delete(self):
        """Test case for registries_delete

        Delete  # noqa: E501
        """
        pass

    def test_registries_list(self):
        """Test case for registries_list

        List registries  # noqa: E501
        """
        pass

    def test_registries_test(self):
        """Test case for registries_test

        Test  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()