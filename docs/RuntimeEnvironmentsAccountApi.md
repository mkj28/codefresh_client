# codefresh_client.RuntimeEnvironmentsAccountApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**on_prem_runtime_envs_account_list**](RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_list) | **GET** /admin/runtime-environments/account/{account} | Get by account
[**on_prem_runtime_envs_account_set_default**](RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_set_default) | **PUT** /admin/runtime-environments/account/default/{account}/{runtimeEnvironmentName} | Set default for account


# **on_prem_runtime_envs_account_list**
> on_prem_runtime_envs_account_list(account, limit=limit, offset=offset, account_ids=account_ids)

Get by account

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
api_instance = codefresh_client.RuntimeEnvironmentsAccountApi(codefresh_client.ApiClient(configuration))
account = 'account_example' # str | 
limit = 'limit_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
account_ids = 'account_ids_example' # str |  (optional)

try:
    # Get by account
    api_instance.on_prem_runtime_envs_account_list(account, limit=limit, offset=offset, account_ids=account_ids)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsAccountApi->on_prem_runtime_envs_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 
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

# **on_prem_runtime_envs_account_set_default**
> on_prem_runtime_envs_account_set_default(account, name)

Set default for account

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
api_instance = codefresh_client.RuntimeEnvironmentsAccountApi(codefresh_client.ApiClient(configuration))
account = 'account_example' # str | 
name = 'name_example' # str | 

try:
    # Set default for account
    api_instance.on_prem_runtime_envs_account_set_default(account, name)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsAccountApi->on_prem_runtime_envs_account_set_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

