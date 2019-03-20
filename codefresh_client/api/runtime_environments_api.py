# coding: utf-8

"""
    Codefresh API

    Codefresh API openAPI 3.0 specification  # noqa: E501

    OpenAPI spec version: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from codefresh_client.api_client import ApiClient


class RuntimeEnvironmentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def on_prem_runtime_envs_list(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.on_prem_runtime_envs_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit:
        :param str offset:
        :param str account_ids:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.on_prem_runtime_envs_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.on_prem_runtime_envs_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def on_prem_runtime_envs_list_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.on_prem_runtime_envs_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit:
        :param str offset:
        :param str account_ids:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'offset', 'account_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method on_prem_runtime_envs_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'account_ids' in local_var_params:
            query_params.append(('accountIds', local_var_params['account_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/admin/runtime-environments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def on_prem_runtime_envs_plan_get(self, plan, name, **kwargs):  # noqa: E501
        """Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.on_prem_runtime_envs_plan_get(plan, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str plan: (required)
        :param str name: (required)
        :param str version:
        :param str extend:
        :param str history:
        :param str successors:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.on_prem_runtime_envs_plan_get_with_http_info(plan, name, **kwargs)  # noqa: E501
        else:
            (data) = self.on_prem_runtime_envs_plan_get_with_http_info(plan, name, **kwargs)  # noqa: E501
            return data

    def on_prem_runtime_envs_plan_get_with_http_info(self, plan, name, **kwargs):  # noqa: E501
        """Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.on_prem_runtime_envs_plan_get_with_http_info(plan, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str plan: (required)
        :param str name: (required)
        :param str version:
        :param str extend:
        :param str history:
        :param str successors:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['plan', 'name', 'version', 'extend', 'history', 'successors']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method on_prem_runtime_envs_plan_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'plan' is set
        if ('plan' not in local_var_params or
                local_var_params['plan'] is None):
            raise ValueError("Missing the required parameter `plan` when calling `on_prem_runtime_envs_plan_get`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `on_prem_runtime_envs_plan_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plan' in local_var_params:
            path_params['plan'] = local_var_params['plan']  # noqa: E501
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))  # noqa: E501
        if 'extend' in local_var_params:
            query_params.append(('extend', local_var_params['extend']))  # noqa: E501
        if 'history' in local_var_params:
            query_params.append(('history', local_var_params['history']))  # noqa: E501
        if 'successors' in local_var_params:
            query_params.append(('successors', local_var_params['successors']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/admin/runtime-environments/{plan}/{runtimeEnvironmentName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def runtime_envs_delete(self, name, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_delete(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str force:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.runtime_envs_delete_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.runtime_envs_delete_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def runtime_envs_delete_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_delete_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str force:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method runtime_envs_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `runtime_envs_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/runtime-environments/{runtimeEnvironmentName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def runtime_envs_get(self, name, **kwargs):  # noqa: E501
        """Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str version:
        :param str extend:
        :param str history:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.runtime_envs_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.runtime_envs_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def runtime_envs_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str version:
        :param str extend:
        :param str history:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'version', 'extend', 'history']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method runtime_envs_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `runtime_envs_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))  # noqa: E501
        if 'extend' in local_var_params:
            query_params.append(('extend', local_var_params['extend']))  # noqa: E501
        if 'history' in local_var_params:
            query_params.append(('history', local_var_params['history']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/runtime-environments/{runtimeEnvironmentName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def runtime_envs_list(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit:
        :param str offset:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.runtime_envs_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.runtime_envs_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def runtime_envs_list_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit:
        :param str offset:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method runtime_envs_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/runtime-environments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def runtime_envs_set_default(self, name, **kwargs):  # noqa: E501
        """Set default  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_set_default(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.runtime_envs_set_default_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.runtime_envs_set_default_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def runtime_envs_set_default_with_http_info(self, name, **kwargs):  # noqa: E501
        """Set default  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_set_default_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method runtime_envs_set_default" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `runtime_envs_set_default`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/runtime-environments/default/{runtimeEnvironmentName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def runtime_envs_update(self, name, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_update(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str extend:
        :param str description:
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.runtime_envs_update_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.runtime_envs_update_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def runtime_envs_update_with_http_info(self, name, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.runtime_envs_update_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str extend:
        :param str description:
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'extend', 'description', 'unknown_base_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method runtime_envs_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `runtime_envs_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'extend' in local_var_params:
            query_params.append(('extend', local_var_params['extend']))  # noqa: E501
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'unknown_base_type' in local_var_params:
            body_params = local_var_params['unknown_base_type']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/runtime-environments/{runtimeEnvironmentName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
