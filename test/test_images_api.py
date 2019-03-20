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
from codefresh_client.api.images_api import ImagesApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.images_api.ImagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_images_add_from_external_source(self):
        """Test case for images_add_from_external_source

        Add from external source  # noqa: E501
        """
        pass

    def test_images_delete_metadata(self):
        """Test case for images_delete_metadata

        Delete metadata  # noqa: E501
        """
        pass

    def test_images_get(self):
        """Test case for images_get

        Get  # noqa: E501
        """
        pass

    def test_images_get_metadata(self):
        """Test case for images_get_metadata

        Get metadata  # noqa: E501
        """
        pass

    def test_images_get_tags(self):
        """Test case for images_get_tags

        Get tags  # noqa: E501
        """
        pass

    def test_images_list(self):
        """Test case for images_list

        List  # noqa: E501
        """
        pass

    def test_images_tag(self):
        """Test case for images_tag

        Tag  # noqa: E501
        """
        pass

    def test_images_untag(self):
        """Test case for images_untag

        Untag  # noqa: E501
        """
        pass

    def test_images_upsert_metadata(self):
        """Test case for images_upsert_metadata

        Upsert metadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()