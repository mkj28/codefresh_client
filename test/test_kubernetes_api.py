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
from codefresh_client.api.kubernetes_api import KubernetesApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestKubernetesApi(unittest.TestCase):
    """KubernetesApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.kubernetes_api.KubernetesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_kubernetes_generate_image_pull_secret(self):
        """Test case for kubernetes_generate_image_pull_secret

        Generate image pull secret  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
