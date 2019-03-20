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
> repos_create(context=context, inline_object31=inline_object31)

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
    api_instance.repos_create(context=context, inline_object31=inline_object31)
except ApiException as e:
    print("Exception when calling ReposApi->repos_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| The git context name | [optional] 
 **inline_object31** | [**InlineObject31**](InlineObject31.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete**
> repos_delete(name, context=context)

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
name = 'name_example' # str | 
context = 'context_example' # str |  (optional)

try:
    # Delete
    api_instance.repos_delete(name, context=context)
except ApiException as e:
    print("Exception when calling ReposApi->repos_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **context** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get**
> repos_get(name, context=context)

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
name = 'name_example' # str | 
context = 'context_example' # str |  (optional)

try:
    # Get
    api_instance.repos_get(name, context=context)
except ApiException as e:
    print("Exception when calling ReposApi->repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **context** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_settings**
> repos_get_settings(repo_owner, repo_name)

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
    api_instance.repos_get_settings(repo_owner, repo_name)
except ApiException as e:
    print("Exception when calling ReposApi->repos_get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_owner** | **str**| name of owner of repository | 
 **repo_name** | **str**| repository name | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_git_get_repo**
> repos_git_get_repo(owner, repo, context=context)

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
owner = 'owner_example' # str | 
repo = 'repo_example' # str | 
context = 'context_example' # str |  (optional)

try:
    # Get git repo
    api_instance.repos_git_get_repo(owner, repo, context=context)
except ApiException as e:
    print("Exception when calling ReposApi->repos_git_get_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repo** | **str**|  | 
 **context** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_git_list**
> repos_git_list(context=context)

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
context = 'context_example' # str |  (optional)

try:
    # List git repos (github, bitbucket, etc)
    api_instance.repos_git_list(context=context)
except ApiException as e:
    print("Exception when calling ReposApi->repos_git_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list**
> repos_list(context=context, thin=thin)

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
context = 'context_example' # str |  (optional)
thin = 'thin_example' # str |  (optional)

try:
    # List
    api_instance.repos_list(context=context, thin=thin)
except ApiException as e:
    print("Exception when calling ReposApi->repos_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  | [optional] 
 **thin** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

