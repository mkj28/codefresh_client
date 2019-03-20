# codefresh_client.RuntimeEnvironmentsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**on_prem_runtime_envs_list**](RuntimeEnvironmentsApi.md#on_prem_runtime_envs_list) | **GET** /admin/runtime-environments | List
[**on_prem_runtime_envs_plan_get**](RuntimeEnvironmentsApi.md#on_prem_runtime_envs_plan_get) | **GET** /admin/runtime-environments/{plan}/{runtimeEnvironmentName} | Get
[**runtime_envs_delete**](RuntimeEnvironmentsApi.md#runtime_envs_delete) | **DELETE** /runtime-environments/{runtimeEnvironmentName} | Delete
[**runtime_envs_get**](RuntimeEnvironmentsApi.md#runtime_envs_get) | **GET** /runtime-environments/{runtimeEnvironmentName} | Get
[**runtime_envs_list**](RuntimeEnvironmentsApi.md#runtime_envs_list) | **GET** /runtime-environments | List
[**runtime_envs_set_default**](RuntimeEnvironmentsApi.md#runtime_envs_set_default) | **PUT** /runtime-environments/default/{runtimeEnvironmentName} | Set default
[**runtime_envs_update**](RuntimeEnvironmentsApi.md#runtime_envs_update) | **PUT** /runtime-environments/{runtimeEnvironmentName} | Update


# **on_prem_runtime_envs_list**
> on_prem_runtime_envs_list(limit=limit, offset=offset, account_ids=account_ids)

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
api_instance = codefresh_client.RuntimeEnvironmentsApi(codefresh_client.ApiClient(configuration))
limit = 'limit_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
account_ids = 'account_ids_example' # str |  (optional)

try:
    # List
    api_instance.on_prem_runtime_envs_list(limit=limit, offset=offset, account_ids=account_ids)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->on_prem_runtime_envs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 
 **account_ids** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_prem_runtime_envs_plan_get**
> on_prem_runtime_envs_plan_get(plan, name, version=version, extend=extend, history=history, successors=successors)

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
api_instance = codefresh_client.RuntimeEnvironmentsApi(codefresh_client.ApiClient(configuration))
plan = 'plan_example' # str | 
name = 'name_example' # str | 
version = 'version_example' # str |  (optional)
extend = 'extend_example' # str |  (optional)
history = 'history_example' # str |  (optional)
successors = 'successors_example' # str |  (optional)

try:
    # Get
    api_instance.on_prem_runtime_envs_plan_get(plan, name, version=version, extend=extend, history=history, successors=successors)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->on_prem_runtime_envs_plan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **str**|  | 
 **name** | **str**|  | 
 **version** | **str**|  | [optional] 
 **extend** | **str**|  | [optional] 
 **history** | **str**|  | [optional] 
 **successors** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runtime_envs_delete**
> runtime_envs_delete(name, force=force)

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
api_instance = codefresh_client.RuntimeEnvironmentsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
force = 'force_example' # str |  (optional)

try:
    # Delete
    api_instance.runtime_envs_delete(name, force=force)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->runtime_envs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **force** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runtime_envs_get**
> runtime_envs_get(name, version=version, extend=extend, history=history)

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
api_instance = codefresh_client.RuntimeEnvironmentsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
version = 'version_example' # str |  (optional)
extend = 'extend_example' # str |  (optional)
history = 'history_example' # str |  (optional)

try:
    # Get
    api_instance.runtime_envs_get(name, version=version, extend=extend, history=history)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->runtime_envs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **version** | **str**|  | [optional] 
 **extend** | **str**|  | [optional] 
 **history** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runtime_envs_list**
> runtime_envs_list(limit=limit, offset=offset)

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
api_instance = codefresh_client.RuntimeEnvironmentsApi(codefresh_client.ApiClient(configuration))
limit = 'limit_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)

try:
    # List
    api_instance.runtime_envs_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->runtime_envs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runtime_envs_set_default**
> runtime_envs_set_default(name)

Set default

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
api_instance = codefresh_client.RuntimeEnvironmentsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Set default
    api_instance.runtime_envs_set_default(name)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->runtime_envs_set_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runtime_envs_update**
> runtime_envs_update(name, extend=extend, description=description, unknown_base_type=unknown_base_type)

Update

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
api_instance = codefresh_client.RuntimeEnvironmentsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
extend = 'extend_example' # str |  (optional)
description = 'description_example' # str |  (optional)
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Update
    api_instance.runtime_envs_update(name, extend=extend, description=description, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->runtime_envs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **extend** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

