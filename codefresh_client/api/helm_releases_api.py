# coding: utf-8

"""
    Codefresh API

    Codefresh API openAPI 3.0 specification  # noqa: E501

    OpenAPI spec version: 0.0.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from codefresh_client.api_client import ApiClient


class HelmReleasesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def helm_releases_delete(self, release_name, selector, tiller_namespace, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_releases_delete(release_name, selector, tiller_namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str release_name: Release name (required)
        :param str selector: Selector (required)
        :param str tiller_namespace: Tiller namespace (required)
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_releases_delete_with_http_info(release_name, selector, tiller_namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_releases_delete_with_http_info(release_name, selector, tiller_namespace, **kwargs)  # noqa: E501
            return data

    def helm_releases_delete_with_http_info(self, release_name, selector, tiller_namespace, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_releases_delete_with_http_info(release_name, selector, tiller_namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str release_name: Release name (required)
        :param str selector: Selector (required)
        :param str tiller_namespace: Tiller namespace (required)
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['release_name', 'selector', 'tiller_namespace', 'unknown_base_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_releases_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'release_name' is set
        if ('release_name' not in local_var_params or
                local_var_params['release_name'] is None):
            raise ValueError("Missing the required parameter `release_name` when calling `helm_releases_delete`")  # noqa: E501
        # verify the required parameter 'selector' is set
        if ('selector' not in local_var_params or
                local_var_params['selector'] is None):
            raise ValueError("Missing the required parameter `selector` when calling `helm_releases_delete`")  # noqa: E501
        # verify the required parameter 'tiller_namespace' is set
        if ('tiller_namespace' not in local_var_params or
                local_var_params['tiller_namespace'] is None):
            raise ValueError("Missing the required parameter `tiller_namespace` when calling `helm_releases_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'release_name' in local_var_params:
            path_params['releaseName'] = local_var_params['release_name']  # noqa: E501

        query_params = []
        if 'selector' in local_var_params:
            query_params.append(('selector', local_var_params['selector']))  # noqa: E501
        if 'tiller_namespace' in local_var_params:
            query_params.append(('tillerNamespace', local_var_params['tiller_namespace']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'unknown_base_type' in local_var_params:
            body_params = local_var_params['unknown_base_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/kubernetes/releases/{releaseName}/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def helm_releases_test(self, release_name, **kwargs):  # noqa: E501
        """Test  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_releases_test(release_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str release_name: Release name (required)
        :param str selector: Selector
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_releases_test_with_http_info(release_name, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_releases_test_with_http_info(release_name, **kwargs)  # noqa: E501
            return data

    def helm_releases_test_with_http_info(self, release_name, **kwargs):  # noqa: E501
        """Test  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_releases_test_with_http_info(release_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str release_name: Release name (required)
        :param str selector: Selector
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['release_name', 'selector', 'unknown_base_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_releases_test" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'release_name' is set
        if ('release_name' not in local_var_params or
                local_var_params['release_name'] is None):
            raise ValueError("Missing the required parameter `release_name` when calling `helm_releases_test`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'release_name' in local_var_params:
            path_params['releaseName'] = local_var_params['release_name']  # noqa: E501

        query_params = []
        if 'selector' in local_var_params:
            query_params.append(('selector', local_var_params['selector']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'unknown_base_type' in local_var_params:
            body_params = local_var_params['unknown_base_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/kubernetes/releases/{releaseName}/test', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
