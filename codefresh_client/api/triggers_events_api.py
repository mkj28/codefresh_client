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


class TriggersEventsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def triggers_events_create(self, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_events_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str public:
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.triggers_events_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.triggers_events_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def triggers_events_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_events_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str public:
        :param UNKNOWN_BASE_TYPE unknown_base_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['public', 'unknown_base_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method triggers_events_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'public' in local_var_params:
            query_params.append(('public', local_var_params['public']))  # noqa: E501

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
            '/hermes/events', 'POST',
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

    def triggers_events_delete(self, event, context, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_events_delete(event, context, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event: (required)
        :param str context: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.triggers_events_delete_with_http_info(event, context, **kwargs)  # noqa: E501
        else:
            (data) = self.triggers_events_delete_with_http_info(event, context, **kwargs)  # noqa: E501
            return data

    def triggers_events_delete_with_http_info(self, event, context, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_events_delete_with_http_info(event, context, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event: (required)
        :param str context: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['event', 'context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method triggers_events_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'event' is set
        if ('event' not in local_var_params or
                local_var_params['event'] is None):
            raise ValueError("Missing the required parameter `event` when calling `triggers_events_delete`")  # noqa: E501
        # verify the required parameter 'context' is set
        if ('context' not in local_var_params or
                local_var_params['context'] is None):
            raise ValueError("Missing the required parameter `context` when calling `triggers_events_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event' in local_var_params:
            path_params['event'] = local_var_params['event']  # noqa: E501
        if 'context' in local_var_params:
            path_params['context'] = local_var_params['context']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/hermes/events/{event}/{context}', 'DELETE',
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

    def triggers_events_get(self, event, **kwargs):  # noqa: E501
        """Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_events_get(event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.triggers_events_get_with_http_info(event, **kwargs)  # noqa: E501
        else:
            (data) = self.triggers_events_get_with_http_info(event, **kwargs)  # noqa: E501
            return data

    def triggers_events_get_with_http_info(self, event, **kwargs):  # noqa: E501
        """Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_events_get_with_http_info(event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['event']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method triggers_events_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'event' is set
        if ('event' not in local_var_params or
                local_var_params['event'] is None):
            raise ValueError("Missing the required parameter `event` when calling `triggers_events_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event' in local_var_params:
            path_params['event'] = local_var_params['event']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/hermes/events/{event}', 'GET',
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

    def triggers_events_list(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_events_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type:
        :param str kind:
        :param str filter:
        :param str public:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.triggers_events_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.triggers_events_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def triggers_events_list_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_events_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type:
        :param str kind:
        :param str filter:
        :param str public:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['type', 'kind', 'filter', 'public']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method triggers_events_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'public' in local_var_params:
            query_params.append(('public', local_var_params['public']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/hermes/events', 'GET',
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