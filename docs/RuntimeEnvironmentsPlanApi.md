# codefresh_client.RuntimeEnvironmentsPlanApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**on_prem_runtime_envs_plan_delete**](RuntimeEnvironmentsPlanApi.md#on_prem_runtime_envs_plan_delete) | **DELETE** /admin/runtime-environments/{plan}/{runtimeEnvironmentName} | Delete
[**on_prem_runtime_envs_plan_set_default**](RuntimeEnvironmentsPlanApi.md#on_prem_runtime_envs_plan_set_default) | **PUT** /admin/runtime-environments/default/{plan}/{runtimeEnvironmentName} | Set default
[**on_prem_runtime_envs_plan_update**](RuntimeEnvironmentsPlanApi.md#on_prem_runtime_envs_plan_update) | **PUT** /admin/runtime-environments/{plan}/{runtimeEnvironmentName} | Update


# **on_prem_runtime_envs_plan_delete**
> on_prem_runtime_envs_plan_delete(plan, name, force=force)

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
api_instance = codefresh_client.RuntimeEnvironmentsPlanApi(codefresh_client.ApiClient(configuration))
plan = 'plan_example' # str | 
name = 'name_example' # str | 
force = 'force_example' # str |  (optional)

try:
    # Delete
    api_instance.on_prem_runtime_envs_plan_delete(plan, name, force=force)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsPlanApi->on_prem_runtime_envs_plan_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **str**|  | 
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

# **on_prem_runtime_envs_plan_set_default**
> on_prem_runtime_envs_plan_set_default(plan, name)

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
api_instance = codefresh_client.RuntimeEnvironmentsPlanApi(codefresh_client.ApiClient(configuration))
plan = 'plan_example' # str | 
name = 'name_example' # str | 

try:
    # Set default
    api_instance.on_prem_runtime_envs_plan_set_default(plan, name)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsPlanApi->on_prem_runtime_envs_plan_set_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_prem_runtime_envs_plan_update**
> on_prem_runtime_envs_plan_update(plan, name, extend=extend, description=description, unknown_base_type=unknown_base_type)

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
api_instance = codefresh_client.RuntimeEnvironmentsPlanApi(codefresh_client.ApiClient(configuration))
plan = 'plan_example' # str | 
name = 'name_example' # str | 
extend = 'extend_example' # str |  (optional)
description = 'description_example' # str |  (optional)
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Update
    api_instance.on_prem_runtime_envs_plan_update(plan, name, extend=extend, description=description, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsPlanApi->on_prem_runtime_envs_plan_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **str**|  | 
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

