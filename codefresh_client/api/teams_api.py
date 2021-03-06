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


class TeamsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def teams_add_user(self, team_id, user_id, **kwargs):  # noqa: E501
        """Add user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_add_user(team_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: The id of the team (required)
        :param str user_id: The user id for assign (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.teams_add_user_with_http_info(team_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.teams_add_user_with_http_info(team_id, user_id, **kwargs)  # noqa: E501
            return data

    def teams_add_user_with_http_info(self, team_id, user_id, **kwargs):  # noqa: E501
        """Add user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_add_user_with_http_info(team_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: The id of the team (required)
        :param str user_id: The user id for assign (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method teams_add_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `teams_add_user`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in local_var_params or
                local_var_params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `teams_add_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['teamId'] = local_var_params['team_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/team/{teamId}/{userId}/assignUserToTeam', 'PUT',
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

    def teams_create(self, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InlineObject32 inline_object32:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.teams_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.teams_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def teams_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InlineObject32 inline_object32:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['inline_object32']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method teams_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object32' in local_var_params:
            body_params = local_var_params['inline_object32']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/team', 'POST',
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

    def teams_list(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.teams_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.teams_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def teams_list_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method teams_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/team', 'GET',
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

    def teams_list_by_user(self, user_id, **kwargs):  # noqa: E501
        """List by user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_list_by_user(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.teams_list_by_user_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.teams_list_by_user_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def teams_list_by_user_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List by user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_list_by_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: User id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method teams_list_by_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in local_var_params or
                local_var_params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `teams_list_by_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/team/{userId}/findTeamsByUser', 'GET',
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

    def teams_remove_user(self, team_id, user_id, **kwargs):  # noqa: E501
        """Remove user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_remove_user(team_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: The id of the team (required)
        :param str user_id: The user id for assign (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.teams_remove_user_with_http_info(team_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.teams_remove_user_with_http_info(team_id, user_id, **kwargs)  # noqa: E501
            return data

    def teams_remove_user_with_http_info(self, team_id, user_id, **kwargs):  # noqa: E501
        """Remove user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_remove_user_with_http_info(team_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: The id of the team (required)
        :param str user_id: The user id for assign (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team_id', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method teams_remove_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in local_var_params or
                local_var_params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `teams_remove_user`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in local_var_params or
                local_var_params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `teams_remove_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in local_var_params:
            path_params['teamId'] = local_var_params['team_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/team/{teamId}/{userId}/deleteUserFromTeam', 'PUT',
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

    def teams_synchronize_client_with_group(self, name, type, **kwargs):  # noqa: E501
        """Synchronize client with group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_synchronize_client_with_group(name, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name (required)
        :param str type: Type (required)
        :param str access_token: Access token
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.teams_synchronize_client_with_group_with_http_info(name, type, **kwargs)  # noqa: E501
        else:
            (data) = self.teams_synchronize_client_with_group_with_http_info(name, type, **kwargs)  # noqa: E501
            return data

    def teams_synchronize_client_with_group_with_http_info(self, name, type, **kwargs):  # noqa: E501
        """Synchronize client with group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.teams_synchronize_client_with_group_with_http_info(name, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name (required)
        :param str type: Type (required)
        :param str access_token: Access token
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'type', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method teams_synchronize_client_with_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `teams_synchronize_client_with_group`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `teams_synchronize_client_with_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']  # noqa: E501

        query_params = []
        if 'access_token' in local_var_params:
            query_params.append(('access_token', local_var_params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/team/group/synchronize/name/{name}/type/{type}', 'GET',
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
