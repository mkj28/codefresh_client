# codefresh_client.RuntimeEnvironmentsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**on_prem_runtime_envs_list**](RuntimeEnvironmentsApi.md#on_prem_runtime_envs_list) | **GET** /admin/runtime-environments | List
[**on_prem_runtime_envs_plan_get**](RuntimeEnvironmentsApi.md#on_prem_runtime_envs_plan_get) | **GET** /admin/runtime-environments/{plan}/{runtimeEnvironmentName} | Get


# **on_prem_runtime_envs_list**
> object on_prem_runtime_envs_list(limit=limit, offset=offset, account_ids=account_ids)

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
limit = 'limit_example' # str | Limit (optional)
offset = 'offset_example' # str | Offset (optional)
account_ids = 'account_ids_example' # str | Account ids (optional)

try:
    # List
    api_response = api_instance.on_prem_runtime_envs_list(limit=limit, offset=offset, account_ids=account_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->on_prem_runtime_envs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Limit | [optional] 
 **offset** | **str**| Offset | [optional] 
 **account_ids** | **str**| Account ids | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_prem_runtime_envs_plan_get**
> object on_prem_runtime_envs_plan_get(plan, runtime_environment_name, version=version, extend=extend, history=history, successors=successors)

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
plan = 'plan_example' # str | Plan
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name
version = 'version_example' # str | Version (optional)
extend = 'extend_example' # str | Extend (optional)
history = 'history_example' # str | History (optional)
successors = 'successors_example' # str | Successors (optional)

try:
    # Get
    api_response = api_instance.on_prem_runtime_envs_plan_get(plan, runtime_environment_name, version=version, extend=extend, history=history, successors=successors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsApi->on_prem_runtime_envs_plan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **str**| Plan | 
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

