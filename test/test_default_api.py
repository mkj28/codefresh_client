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
from codefresh_client.api.default_api import DefaultApi  # noqa: E501
from codefresh_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = codefresh_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounts_account_id_user_id_resend_invite_post(self):
        """Test case for accounts_account_id_user_id_resend_invite_post

        """
        pass

    def test_admin_runtime_environments_account_modify_runtime_environment_name_delete(self):
        """Test case for admin_runtime_environments_account_modify_runtime_environment_name_delete

        """
        pass

    def test_admin_runtime_environments_account_modify_runtime_environment_name_put(self):
        """Test case for admin_runtime_environments_account_modify_runtime_environment_name_put

        """
        pass

    def test_registries_registry_id_default_patch(self):
        """Test case for registries_registry_id_default_patch

        """
        pass

    def test_registries_registry_id_patch(self):
        """Test case for registries_registry_id_patch

        """
        pass

    def test_user_onboarding_status_account_post(self):
        """Test case for user_onboarding_status_account_post

        """
        pass

    def test_user_onboarding_status_user_post(self):
        """Test case for user_onboarding_status_user_post

        """
        pass

    def test_user_post(self):
        """Test case for user_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
