# codefresh_client.RuntimeEnvironmentsAccountApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**on_prem_runtime_envs_account_delete**](RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_delete) | **DELETE** /admin/runtime-environments/account/modify/{runtimeEnvironmentName} | Delete for account
[**on_prem_runtime_envs_account_list**](RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_list) | **GET** /admin/runtime-environments/account/{account} | Get by account
[**on_prem_runtime_envs_account_modify**](RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_modify) | **PUT** /admin/runtime-environments/account/modify/{runtimeEnvironmentName} | Add to account
[**on_prem_runtime_envs_account_set_default**](RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_set_default) | **PUT** /admin/runtime-environments/account/default/{account}/{runtimeEnvironmentName} | Set default for account


# **on_prem_runtime_envs_account_delete**
> object on_prem_runtime_envs_account_delete(runtime_environment_name)

Delete for account

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
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name

try:
    # Delete for account
    api_response = api_instance.on_prem_runtime_envs_account_delete(runtime_environment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsAccountApi->on_prem_runtime_envs_account_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime_environment_name** | **str**| Runtime environment name | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_prem_runtime_envs_account_list**
> object on_prem_runtime_envs_account_list(account, limit=limit, offset=offset, account_ids=account_ids)

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
account = 'account_example' # str | Account
limit = 'limit_example' # str | Limit (optional)
offset = 'offset_example' # str | Offset (optional)
account_ids = 'account_ids_example' # str | Account ids (optional)

try:
    # Get by account
    api_response = api_instance.on_prem_runtime_envs_account_list(account, limit=limit, offset=offset, account_ids=account_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsAccountApi->on_prem_runtime_envs_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Account | 
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

# **on_prem_runtime_envs_account_modify**
> object on_prem_runtime_envs_account_modify(runtime_environment_name)

Add to account

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
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name

try:
    # Add to account
    api_response = api_instance.on_prem_runtime_envs_account_modify(runtime_environment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsAccountApi->on_prem_runtime_envs_account_modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime_environment_name** | **str**| Runtime environment name | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_prem_runtime_envs_account_set_default**
> object on_prem_runtime_envs_account_set_default(account, runtime_environment_name)

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
account = 'account_example' # str | Account
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name

try:
    # Set default for account
    api_response = api_instance.on_prem_runtime_envs_account_set_default(account, runtime_environment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnvironmentsAccountApi->on_prem_runtime_envs_account_set_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Account | 
 **runtime_environment_name** | **str**| Runtime environment name | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

