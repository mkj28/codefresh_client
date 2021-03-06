# codefresh_client.ReposApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repos_create**](ReposApi.md#repos_create) | **POST** /services | Create
[**repos_delete**](ReposApi.md#repos_delete) | **DELETE** /services/{name} | Delete
[**repos_get**](ReposApi.md#repos_get) | **GET** /services/{name} | Get
[**repos_get_settings**](ReposApi.md#repos_get_settings) | **GET** /repos/settings/{repoOwner}/{repoName} | Get settings
[**repos_git_get_repo**](ReposApi.md#repos_git_get_repo) | **GET** /repos/{owner}/{repo} | Get git repo
[**repos_git_list**](ReposApi.md#repos_git_list) | **GET** /repos | List git repos (github, bitbucket, etc)
[**repos_list**](ReposApi.md#repos_list) | **GET** /repos/existing | List


# **repos_create**
> object repos_create(context=context, inline_object31=inline_object31)

Create

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.ReposApi(codefresh_client.ApiClient(configuration))
context = 'context_example' # str | The git context name (optional)
inline_object31 = codefresh_client.InlineObject31() # InlineObject31 |  (optional)

try:
    # Create
    api_response = api_instance.repos_create(context=context, inline_object31=inline_object31)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->repos_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| The git context name | [optional] 
 **inline_object31** | [**InlineObject31**](InlineObject31.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete**
> object repos_delete(name, context=context)

Delete

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.ReposApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | Name
context = 'context_example' # str | Context (optional)

try:
    # Delete
    api_response = api_instance.repos_delete(name, context=context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->repos_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 
 **context** | **str**| Context | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get**
> object repos_get(name, context=context)

Get

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.ReposApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | Name
context = 'context_example' # str | Context (optional)

try:
    # Get
    api_response = api_instance.repos_get(name, context=context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 
 **context** | **str**| Context | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_settings**
> object repos_get_settings(repo_owner, repo_name)

Get settings

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.ReposApi(codefresh_client.ApiClient(configuration))
repo_owner = 'repo_owner_example' # str | name of owner of repository
repo_name = 'repo_name_example' # str | repository name

try:
    # Get settings
    api_response = api_instance.repos_get_settings(repo_owner, repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->repos_get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_owner** | **str**| name of owner of repository | 
 **repo_name** | **str**| repository name | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_git_get_repo**
> object repos_git_get_repo(owner, repo, context=context)

Get git repo

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.ReposApi(codefresh_client.ApiClient(configuration))
owner = 'owner_example' # str | Owner
repo = 'repo_example' # str | Repo
context = 'context_example' # str | Context (optional)

try:
    # Get git repo
    api_response = api_instance.repos_git_get_repo(owner, repo, context=context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->repos_git_get_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Owner | 
 **repo** | **str**| Repo | 
 **context** | **str**| Context | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_git_list**
> object repos_git_list(context=context)

List git repos (github, bitbucket, etc)

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.ReposApi(codefresh_client.ApiClient(configuration))
context = 'context_example' # str | Context (optional)

try:
    # List git repos (github, bitbucket, etc)
    api_response = api_instance.repos_git_list(context=context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->repos_git_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| Context | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list**
> object repos_list(context=context, thin=thin)

List

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.ReposApi(codefresh_client.ApiClient(configuration))
context = 'context_example' # str | Context (optional)
thin = 'thin_example' # str | Thin (optional)

try:
    # List
    api_response = api_instance.repos_list(context=context, thin=thin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->repos_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| Context | [optional] 
 **thin** | **str**| Thin | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

