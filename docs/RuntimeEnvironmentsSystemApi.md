# codefresh_client.RuntimeEnvironmentsSystemApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**on_prem_runtime_envs_system_delete**](RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_delete) | **DELETE** /admin/runtime-environments/{runtimeEnvironmentName} | Delete sys re
[**on_prem_runtime_envs_system_get**](RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_get) | **GET** /admin/runtime-environments/{runtimeEnvironmentName} | Get sys re
[**on_prem_runtime_envs_system_update**](RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_update) | **PUT** /admin/runtime-environments/{runtimeEnvironmentName} | Update sys re


# **on_prem_runtime_envs_system_delete**
> object on_prem_runtime_envs_system_delete(runtime_environment_name, force=force)

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
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name
force = 'force_example' # str | Force (optional)

try:
    # Delete sys re
    api_response = api_instance.on_prem_runtime_envs_system_delete(runtime_environment_name, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsSystemApi->on_prem_runtime_envs_system_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime_environment_name** | **str**| Runtime environment name | 
 **force** | **str**| Force | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_prem_runtime_envs_system_get**
> object on_prem_runtime_envs_system_get(runtime_environment_name, version=version, extend=extend, history=history, successors=successors)

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
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name
version = 'version_example' # str | Version (optional)
extend = 'extend_example' # str | Extend (optional)
history = 'history_example' # str | History (optional)
successors = 'successors_example' # str | Successors (optional)

try:
    # Get sys re
    api_response = api_instance.on_prem_runtime_envs_system_get(runtime_environment_name, version=version, extend=extend, history=history, successors=successors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsSystemApi->on_prem_runtime_envs_system_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime_environment_name** | **str**| Runtime environment name | 
 **version** | **str**| Version | [optional] 
 **extend** | **str**| Extend | [optional] 
 **history** | **str**| History | [optional] 
 **successors** | **str**| Successors | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_prem_runtime_envs_system_update**
> object on_prem_runtime_envs_system_update(runtime_environment_name, extend=extend, description=description, unknown_base_type=unknown_base_type)

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
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name
extend = 'extend_example' # str | Extend or not (optional)
description = 'description_example' # str | Description (optional)
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Update sys re
    api_response = api_instance.on_prem_runtime_envs_system_update(runtime_environment_name, extend=extend, description=description, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsSystemApi->on_prem_runtime_envs_system_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime_environment_name** | **str**| Runtime environment name | 
 **extend** | **str**| Extend or not | [optional] 
 **description** | **str**| Description | [optional] 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

