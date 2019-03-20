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
from codefresh_client.api.helm_boards_api import HelmBoardsApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestHelmBoardsApi(unittest.TestCase):
    """HelmBoardsApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.helm_boards_api.HelmBoardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_helm_boards_create(self):
        """Test case for helm_boards_create

        Create  # noqa: E501
        """
        pass

    def test_helm_boards_delete(self):
        """Test case for helm_boards_delete

        Delete  # noqa: E501
        """
        pass

    def test_helm_boards_delete_all(self):
        """Test case for helm_boards_delete_all

        Delete all  # noqa: E501
        """
        pass

    def test_helm_boards_get(self):
        """Test case for helm_boards_get

        Get  # noqa: E501
        """
        pass

    def test_helm_boards_get_by_name(self):
        """Test case for helm_boards_get_by_name

        Get by name  # noqa: E501
        """
        pass

    def test_helm_boards_list(self):
        """Test case for helm_boards_list

        List  # noqa: E501
        """
        pass

    def test_helm_boards_patch(self):
        """Test case for helm_boards_patch

        Patch  # noqa: E501
        """
        pass

    def test_helm_boards_update(self):
        """Test case for helm_boards_update

        Update  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()