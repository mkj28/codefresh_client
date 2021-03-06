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


class ReposApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def repos_create(self, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context: The git context name
        :param InlineObject31 inline_object31:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.repos_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def repos_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context: The git context name
        :param InlineObject31 inline_object31:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['context', 'inline_object31']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'context' in local_var_params:
            query_params.append(('context', local_var_params['context']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object31' in local_var_params:
            body_params = local_var_params['inline_object31']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/services', 'POST',
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

    def repos_delete(self, name, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_delete(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name (required)
        :param str context: Context
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_delete_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_delete_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def repos_delete_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_delete_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name (required)
        :param str context: Context
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `repos_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'context' in local_var_params:
            query_params.append(('context', local_var_params['context']))  # noqa: E501

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
            '/services/{name}', 'DELETE',
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

    def repos_get(self, name, **kwargs):  # noqa: E501
        """Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name (required)
        :param str context: Context
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def repos_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name (required)
        :param str context: Context
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `repos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'context' in local_var_params:
            query_params.append(('context', local_var_params['context']))  # noqa: E501

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
            '/services/{name}', 'GET',
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

    def repos_get_settings(self, repo_owner, repo_name, **kwargs):  # noqa: E501
        """Get settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_get_settings(repo_owner, repo_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_owner: name of owner of repository (required)
        :param str repo_name: repository name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_get_settings_with_http_info(repo_owner, repo_name, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_get_settings_with_http_info(repo_owner, repo_name, **kwargs)  # noqa: E501
            return data

    def repos_get_settings_with_http_info(self, repo_owner, repo_name, **kwargs):  # noqa: E501
        """Get settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_get_settings_with_http_info(repo_owner, repo_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_owner: name of owner of repository (required)
        :param str repo_name: repository name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['repo_owner', 'repo_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_get_settings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'repo_owner' is set
        if ('repo_owner' not in local_var_params or
                local_var_params['repo_owner'] is None):
            raise ValueError("Missing the required parameter `repo_owner` when calling `repos_get_settings`")  # noqa: E501
        # verify the required parameter 'repo_name' is set
        if ('repo_name' not in local_var_params or
                local_var_params['repo_name'] is None):
            raise ValueError("Missing the required parameter `repo_name` when calling `repos_get_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_owner' in local_var_params:
            path_params['repoOwner'] = local_var_params['repo_owner']  # noqa: E501
        if 'repo_name' in local_var_params:
            path_params['repoName'] = local_var_params['repo_name']  # noqa: E501

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
            '/repos/settings/{repoOwner}/{repoName}', 'GET',
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

    def repos_git_get_repo(self, owner, repo, **kwargs):  # noqa: E501
        """Get git repo  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_git_get_repo(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner (required)
        :param str repo: Repo (required)
        :param str context: Context
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_git_get_repo_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_git_get_repo_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def repos_git_get_repo_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """Get git repo  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_git_get_repo_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner (required)
        :param str repo: Repo (required)
        :param str context: Context
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['owner', 'repo', 'context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_git_get_repo" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in local_var_params or
                local_var_params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `repos_git_get_repo`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in local_var_params or
                local_var_params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repos_git_get_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501
        if 'repo' in local_var_params:
            path_params['repo'] = local_var_params['repo']  # noqa: E501

        query_params = []
        if 'context' in local_var_params:
            query_params.append(('context', local_var_params['context']))  # noqa: E501

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
            '/repos/{owner}/{repo}', 'GET',
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

    def repos_git_list(self, **kwargs):  # noqa: E501
        """List git repos (github, bitbucket, etc)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_git_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context: Context
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_git_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.repos_git_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def repos_git_list_with_http_info(self, **kwargs):  # noqa: E501
        """List git repos (github, bitbucket, etc)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_git_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context: Context
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_git_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'context' in local_var_params:
            query_params.append(('context', local_var_params['context']))  # noqa: E501

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
            '/repos', 'GET',
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

    def repos_list(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context: Context
        :param str thin: Thin
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.repos_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def repos_list_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context: Context
        :param str thin: Thin
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['context', 'thin']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'context' in local_var_params:
            query_params.append(('context', local_var_params['context']))  # noqa: E501
        if 'thin' in local_var_params:
            query_params.append(('thin', local_var_params['thin']))  # noqa: E501

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
            '/repos/existing', 'GET',
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
