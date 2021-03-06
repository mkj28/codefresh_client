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


class KubernetesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def kubernetes_generate_image_pull_secret(self, namespace, selector, **kwargs):  # noqa: E501
        """Generate image pull secret  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kubernetes_generate_image_pull_secret(namespace, selector, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: Namespace (required)
        :param str selector: Selector (required)
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kubernetes_generate_image_pull_secret_with_http_info(namespace, selector, **kwargs)  # noqa: E501
        else:
            (data) = self.kubernetes_generate_image_pull_secret_with_http_info(namespace, selector, **kwargs)  # noqa: E501
            return data

    def kubernetes_generate_image_pull_secret_with_http_info(self, namespace, selector, **kwargs):  # noqa: E501
        """Generate image pull secret  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kubernetes_generate_image_pull_secret_with_http_info(namespace, selector, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: Namespace (required)
        :param str selector: Selector (required)
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['namespace', 'selector', 'unknown_base_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kubernetes_generate_image_pull_secret" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in local_var_params or
                local_var_params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `kubernetes_generate_image_pull_secret`")  # noqa: E501
        # verify the required parameter 'selector' is set
        if ('selector' not in local_var_params or
                local_var_params['selector'] is None):
            raise ValueError("Missing the required parameter `selector` when calling `kubernetes_generate_image_pull_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))  # noqa: E501
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
            '/kubernetes/secrets/imagePullSecret', 'POST',
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
