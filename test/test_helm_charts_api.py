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
from codefresh_client.api.helm_charts_api import HelmChartsApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestHelmChartsApi(unittest.TestCase):
    """HelmChartsApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.helm_charts_api.HelmChartsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_helm_charts_install(self):
        """Test case for helm_charts_install

        Install  # noqa: E501
        """
        pass

    def test_helm_charts_promote(self):
        """Test case for helm_charts_promote

        Promote  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
