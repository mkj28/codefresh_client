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
from codefresh_client.api.builds_api import BuildsApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestBuildsApi(unittest.TestCase):
    """BuildsApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.builds_api.BuildsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_workflows_get(self):
        """Test case for workflows_get

        Get  # noqa: E501
        """
        pass

    def test_workflows_list(self):
        """Test case for workflows_list

        List  # noqa: E501
        """
        pass

    def test_workflows_restart(self):
        """Test case for workflows_restart

        Restart  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
