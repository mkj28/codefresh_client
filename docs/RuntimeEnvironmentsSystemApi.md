# codefresh_client.RuntimeEnvironmentsSystemApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**on_prem_runtime_envs_system_delete**](RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_delete) | **DELETE** /admin/runtime-environments/{runtimeEnvironmentName} | Delete sys re
[**on_prem_runtime_envs_system_get**](RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_get) | **GET** /admin/runtime-environments/{runtimeEnvironmentName} | Get sys re
[**on_prem_runtime_envs_system_update**](RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_update) | **PUT** /admin/runtime-environments/{runtimeEnvironmentName} | Update sys re


# **on_prem_runtime_envs_system_delete**
> on_prem_runtime_envs_system_delete(name, force=force)

Delete sys re

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
api_instance = codefresh_client.RuntimeEnvironmentsSystemApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
force = 'force_example' # str |  (optional)

try:
    # Delete sys re
    api_instance.on_prem_runtime_envs_system_delete(name, force=force)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsSystemApi->on_prem_runtime_envs_system_delete: %s\n" % e)
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

# **on_prem_runtime_envs_system_get**
> on_prem_runtime_envs_system_get(name, version=version, extend=extend, history=history, successors=successors)

Get sys re

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
api_instance = codefresh_client.RuntimeEnvironmentsSystemApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
version = 'version_example' # str |  (optional)
extend = 'extend_example' # str |  (optional)
history = 'history_example' # str |  (optional)
successors = 'successors_example' # str |  (optional)

try:
    # Get sys re
    api_instance.on_prem_runtime_envs_system_get(name, version=version, extend=extend, history=history, successors=successors)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsSystemApi->on_prem_runtime_envs_system_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **on_prem_runtime_envs_system_update**
> on_prem_runtime_envs_system_update(name, extend=extend, description=description, unknown_base_type=unknown_base_type)

Update sys re

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
api_instance = codefresh_client.RuntimeEnvironmentsSystemApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
extend = 'extend_example' # str |  (optional)
description = 'description_example' # str |  (optional)
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Update sys re
    api_instance.on_prem_runtime_envs_system_update(name, extend=extend, description=description, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsSystemApi->on_prem_runtime_envs_system_update: %s\n" % e)
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

